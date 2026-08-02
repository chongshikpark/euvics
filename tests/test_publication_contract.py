from __future__ import annotations

import copy
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from publication_contract import ContractError, generate_metadata, validate_manifest


class PublicationContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "docs").mkdir()
        (self.root / "docs" / "overview.md").write_text("# Approved overview\n", encoding="utf-8")
        self.manifest = {
            "$schema": "public-content-v1.schema.json",
            "schema_version": "1.0",
            "contract_id": "euvics-public-content-v1",
            "repository": {
                "url": "https://github.com/chongshikpark/euvics",
                "source_commit_policy": "locked-by-consuming-website",
            },
            "default_policy": "excluded",
            "allowlist": [self.entry()],
            "exclusions": [{
                "path_prefix": "reviews/", "category": "internal-review",
                "reason": "Not public.",
            }],
            "publication_decisions": [],
        }

    def tearDown(self) -> None:
        self.temp.cleanup()

    @staticmethod
    def entry() -> dict[str, object]:
        return {
            "path": "docs/overview.md", "kind": "markdown", "title": "Overview",
            "version": "1", "publication_status": "public-draft",
            "approval": {"status": "approved", "approved_by": "project-owner", "approved_on": "2026-08-02"},
            "license": "MIT", "attribution": "EUVICS project",
            "known_limitations": ["Draft overview; no performance claims."],
        }

    def write(self, manifest: dict | None = None) -> Path:
        path = self.root / "manifest.json"
        path.write_text(json.dumps(self.manifest if manifest is None else manifest), encoding="utf-8")
        return path

    def assert_invalid(self, mutate, message: str) -> None:
        manifest = copy.deepcopy(self.manifest)
        mutate(manifest)
        with self.assertRaisesRegex(ContractError, message):
            validate_manifest(self.write(manifest), self.root)

    def test_repository_manifest_is_valid_and_deny_by_default(self) -> None:
        manifest = validate_manifest(ROOT / "publication/public-content-v1.json", ROOT)
        self.assertEqual(manifest["default_policy"], "excluded")
        self.assertEqual(
            [entry["path"] for entry in manifest["allowlist"]],
            [
                "cdr/sections/introduction.tex",
                "cdr/sections/source_overview.tex",
                "bibliography/references.bib",
            ],
        )
        self.assertTrue(
            all(entry["approval"]["status"] == "approved" for entry in manifest["allowlist"])
        )
        self.assertTrue(
            all(entry["publication_status"] == "public-draft" for entry in manifest["allowlist"])
        )

    def test_valid_entry_and_metadata_checksum(self) -> None:
        manifest = validate_manifest(self.write(), self.root)
        metadata = generate_metadata(manifest, self.root, "a" * 40, "2026-08-02T00:00:00Z")
        expected = hashlib.sha256((self.root / "docs/overview.md").read_bytes()).hexdigest()
        self.assertEqual(metadata["artifacts"][0]["sha256"], expected)
        self.assertEqual(metadata["source_commit"], "a" * 40)

    def test_approved_pdf_receives_sha256_checksum(self) -> None:
        (self.root / "build").mkdir()
        pdf = self.root / "build" / "proposal.pdf"
        pdf.write_bytes(b"%PDF-1.4\napproved fixture\n")
        entry = self.entry()
        entry.update(path="build/proposal.pdf", kind="pdf", title="EUVICS Proposal")
        self.manifest["allowlist"] = [entry]
        manifest = validate_manifest(self.write(), self.root)
        metadata = generate_metadata(manifest, self.root, "b" * 40, "2026-08-02T00:00:00Z")
        self.assertEqual(metadata["artifacts"][0]["sha256"], hashlib.sha256(pdf.read_bytes()).hexdigest())

    def test_rejects_path_traversal(self) -> None:
        self.assert_invalid(lambda m: m["allowlist"][0].update(path="../secret.md"), "safe repository-relative")

    def test_rejects_missing_file(self) -> None:
        self.assert_invalid(lambda m: m["allowlist"][0].update(path="docs/missing.md"), "missing or outside")

    def test_rejects_unknown_field(self) -> None:
        self.assert_invalid(lambda m: m["allowlist"][0].update(unreviewed=True), "unknown fields")

    def test_rejects_broad_glob(self) -> None:
        self.assert_invalid(lambda m: m["allowlist"][0].update(path="docs/*.md"), "glob syntax")

    def test_rejects_ambiguous_publication_status(self) -> None:
        self.assert_invalid(lambda m: m["allowlist"][0].update(publication_status="approved-ish"), "ambiguous publication status")

    def test_rejects_excluded_file_leakage(self) -> None:
        (self.root / "reviews").mkdir()
        (self.root / "reviews" / "open.md").write_text("internal", encoding="utf-8")
        self.assert_invalid(lambda m: m["allowlist"][0].update(path="reviews/open.md"), "covered by an exclusion")

    def test_rejects_unapproved_file_type(self) -> None:
        (self.root / "docs" / "run.exe").write_bytes(b"binary")
        self.assert_invalid(
            lambda m: m["allowlist"][0].update(path="docs/run.exe", kind="markdown"),
            "unapproved file type",
        )

    def test_rejects_local_absolute_path(self) -> None:
        (self.root / "docs" / "overview.md").write_text("use /Users/example/private/data", encoding="utf-8")
        with self.assertRaisesRegex(ContractError, "absolute local path"):
            validate_manifest(self.write(), self.root)

    def test_rejects_missing_explicit_approval(self) -> None:
        self.assert_invalid(
            lambda m: m["allowlist"][0]["approval"].update(status="pending"),
            "lacks explicit approval",
        )


if __name__ == "__main__":
    unittest.main()
