#!/usr/bin/env python3
"""Validate the deny-by-default EUVICS publication manifest and emit metadata."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath
from typing import Any

ROOT_FIELDS = {
    "$schema", "schema_version", "contract_id", "repository", "default_policy",
    "allowlist", "exclusions", "publication_decisions",
}
REPOSITORY_FIELDS = {"url", "source_commit_policy"}
ENTRY_REQUIRED = {
    "path", "kind", "title", "version", "publication_status", "approval",
    "license", "attribution", "known_limitations",
}
ENTRY_FIELDS = ENTRY_REQUIRED | {"document_date"}
APPROVAL_FIELDS = {"status", "approved_by", "approved_on"}
EXCLUSION_FIELDS = {"path_prefix", "category", "reason"}
DECISION_FIELDS = {"subject", "status", "owner", "decision_needed"}
KINDS = {"markdown", "latex-source", "bibliography", "metadata", "pdf", "image", "data"}
EXTENSIONS = {
    "markdown": {".md"}, "latex-source": {".tex"}, "bibliography": {".bib"},
    "metadata": {".json", ".csv"}, "pdf": {".pdf"},
    "image": {".png", ".jpg", ".jpeg", ".svg"}, "data": {".csv", ".json"},
}
PUBLICATION_STATUSES = {"public-draft", "released"}
DECISION_STATUSES = {"approval-pending", "blocked-permission"}
GLOB_CHARS = set("*?[]{}")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")
LOCAL_PATH_RE = re.compile(r"(?:/Users/|/home/[^/\s]+/|[A-Za-z]:\\\\)")


class ContractError(ValueError):
    """A publication contract is invalid or unsafe."""


def _object(value: Any, name: str, fields: set[str], required: set[str] | None = None) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ContractError(f"{name} must be an object")
    unknown = set(value) - fields
    missing = (required if required is not None else fields) - set(value)
    if unknown:
        raise ContractError(f"{name} has unknown fields: {sorted(unknown)}")
    if missing:
        raise ContractError(f"{name} is missing fields: {sorted(missing)}")
    return value


def _text(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ContractError(f"{name} must be a non-empty string")
    return value


def _safe_path(value: Any, name: str, *, prefix: bool = False) -> str:
    path = _text(value, name)
    if any(char in path for char in GLOB_CHARS):
        raise ContractError(f"{name} must not contain glob syntax: {path}")
    pure = PurePosixPath(path)
    if pure.is_absolute() or ".." in pure.parts or "." in pure.parts or "\\" in path:
        raise ContractError(f"{name} is not a safe repository-relative path: {path}")
    if prefix and path.endswith("//"):
        raise ContractError(f"{name} has an invalid prefix: {path}")
    return path


def _date(value: Any, name: str) -> str:
    text = _text(value, name)
    if not DATE_RE.fullmatch(text):
        raise ContractError(f"{name} must use YYYY-MM-DD")
    try:
        dt.date.fromisoformat(text)
    except ValueError as exc:
        raise ContractError(f"{name} is not a valid date") from exc
    return text


def _under_prefix(path: str, prefix: str) -> bool:
    normalized = prefix.rstrip("/")
    return path == normalized or path.startswith(normalized + "/")


def load_manifest(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ContractError(f"cannot read manifest {path}: {exc}") from exc
    return _object(value, "manifest", ROOT_FIELDS)


def validate_manifest(manifest_path: Path, repository_root: Path) -> dict[str, Any]:
    manifest = load_manifest(manifest_path)
    if manifest["$schema"] != "public-content-v1.schema.json":
        raise ContractError("manifest must reference public-content-v1.schema.json")
    if manifest["schema_version"] != "1.0" or manifest["contract_id"] != "euvics-public-content-v1":
        raise ContractError("unsupported publication contract identity or version")
    if manifest["default_policy"] != "excluded":
        raise ContractError("default_policy must be excluded")

    repository = _object(manifest["repository"], "repository", REPOSITORY_FIELDS)
    if repository != {
        "url": "https://github.com/chongshikpark/euvics",
        "source_commit_policy": "locked-by-consuming-website",
    }:
        raise ContractError("repository identity or source-commit policy is invalid")

    exclusions = manifest["exclusions"]
    if not isinstance(exclusions, list):
        raise ContractError("exclusions must be an array")
    exclusion_prefixes: list[str] = []
    for index, raw in enumerate(exclusions):
        item = _object(raw, f"exclusions[{index}]", EXCLUSION_FIELDS)
        prefix = _safe_path(item["path_prefix"], f"exclusions[{index}].path_prefix", prefix=True)
        _text(item["category"], f"exclusions[{index}].category")
        _text(item["reason"], f"exclusions[{index}].reason")
        exclusion_prefixes.append(prefix)

    allowlist = manifest["allowlist"]
    if not isinstance(allowlist, list):
        raise ContractError("allowlist must be an array")
    seen: set[str] = set()
    root = repository_root.resolve()
    for index, raw in enumerate(allowlist):
        item = _object(raw, f"allowlist[{index}]", ENTRY_FIELDS, ENTRY_REQUIRED)
        path = _safe_path(item["path"], f"allowlist[{index}].path")
        if path in seen:
            raise ContractError(f"duplicate allowlist path: {path}")
        seen.add(path)
        if any(_under_prefix(path, prefix) for prefix in exclusion_prefixes):
            raise ContractError(f"allowlisted path is covered by an exclusion: {path}")
        resolved = (root / path).resolve()
        if root not in resolved.parents or not resolved.is_file():
            raise ContractError(f"allowlisted file is missing or outside repository: {path}")
        kind = item["kind"]
        if kind not in KINDS or resolved.suffix.lower() not in EXTENSIONS[kind]:
            raise ContractError(f"unapproved file type for {path}: {kind}")
        for field in ("title", "version", "license", "attribution"):
            _text(item[field], f"allowlist[{index}].{field}")
        if item["publication_status"] not in PUBLICATION_STATUSES:
            raise ContractError(f"ambiguous publication status for {path}")
        approval = _object(item["approval"], f"allowlist[{index}].approval", APPROVAL_FIELDS)
        if approval["status"] != "approved":
            raise ContractError(f"allowlist entry lacks explicit approval: {path}")
        _text(approval["approved_by"], f"allowlist[{index}].approval.approved_by")
        _date(approval["approved_on"], f"allowlist[{index}].approval.approved_on")
        if "document_date" in item:
            _date(item["document_date"], f"allowlist[{index}].document_date")
        limits = item["known_limitations"]
        if not isinstance(limits, list) or any(not isinstance(v, str) or not v.strip() for v in limits):
            raise ContractError(f"known_limitations must be an array of non-empty strings: {path}")
        if resolved.suffix.lower() in {".md", ".tex", ".bib", ".csv", ".json", ".svg"}:
            try:
                content = resolved.read_text(encoding="utf-8")
            except UnicodeDecodeError as exc:
                raise ContractError(f"allowlisted text file is not UTF-8: {path}") from exc
            if LOCAL_PATH_RE.search(content):
                raise ContractError(f"allowlisted file contains an absolute local path: {path}")

    decisions = manifest["publication_decisions"]
    if not isinstance(decisions, list):
        raise ContractError("publication_decisions must be an array")
    for index, raw in enumerate(decisions):
        item = _object(raw, f"publication_decisions[{index}]", DECISION_FIELDS)
        for field in ("subject", "owner", "decision_needed"):
            _text(item[field], f"publication_decisions[{index}].{field}")
        if item["status"] not in DECISION_STATUSES:
            raise ContractError(f"publication_decisions[{index}] has ambiguous status")
    return manifest


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def generate_metadata(manifest: dict[str, Any], root: Path, commit: str, timestamp: str) -> dict[str, Any]:
    if not COMMIT_RE.fullmatch(commit):
        raise ContractError("source commit must be a full lowercase 40-character Git SHA")
    try:
        normalized_time = dt.datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ContractError("build timestamp must be ISO 8601") from exc
    if normalized_time.tzinfo is None:
        raise ContractError("build timestamp must include a timezone")
    artifacts = []
    for entry in manifest["allowlist"]:
        item = {key: entry[key] for key in (
            "path", "kind", "title", "version", "publication_status", "approval",
            "license", "attribution", "known_limitations",
        )}
        if "document_date" in entry:
            item["document_date"] = entry["document_date"]
        item["sha256"] = _sha256(root / entry["path"])
        artifacts.append(item)
    return {
        "metadata_version": "1.0",
        "contract_id": manifest["contract_id"],
        "source_repository": manifest["repository"]["url"],
        "source_commit": commit,
        "build_timestamp": normalized_time.astimezone(dt.timezone.utc).isoformat().replace("+00:00", "Z"),
        "artifacts": artifacts,
        "publication_decisions": manifest["publication_decisions"],
    }


def _current_commit(root: Path) -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=root, text=True, stderr=subprocess.DEVNULL
    ).strip()


def _timestamp_from_environment() -> str:
    epoch = os.environ.get("SOURCE_DATE_EPOCH")
    if epoch is None:
        raise ContractError("SOURCE_DATE_EPOCH is required for deterministic metadata")
    try:
        instant = dt.datetime.fromtimestamp(int(epoch), tz=dt.timezone.utc)
    except (ValueError, OverflowError) as exc:
        raise ContractError("SOURCE_DATE_EPOCH must be a valid integer timestamp") from exc
    return instant.isoformat().replace("+00:00", "Z")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("validate", "metadata"))
    parser.add_argument("--manifest", type=Path, default=Path("publication/public-content-v1.json"))
    parser.add_argument("--repository-root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, default=Path("build/publication-metadata.json"))
    args = parser.parse_args(argv)
    try:
        manifest = validate_manifest(args.manifest, args.repository_root)
        if args.command == "metadata":
            metadata = generate_metadata(
                manifest, args.repository_root, _current_commit(args.repository_root), _timestamp_from_environment()
            )
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            print(f"wrote {args.output} ({len(metadata['artifacts'])} approved artifacts)")
        else:
            print(f"valid publication manifest: {len(manifest['allowlist'])} approved files")
    except (ContractError, OSError, subprocess.SubprocessError) as exc:
        print(f"publication contract error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
