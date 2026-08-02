# Public-content publication contract — completed

## Scope

Task 2 from the EUVICS website task sequence: add a versioned, deny-by-default
public-content manifest for consumption by `chongshikpark/euvics.github.io`,
with schema validation, failure-path tests, and machine-readable publication
metadata for approved artifacts.

## Boundaries and decisions

- Do not edit scientific prose, requirements, bibliography conclusions,
  document sources, generated PDFs, or archived material.
- Do not grant publication approval. Current Proposal/CDR sources and PDFs have
  no explicit public-release record, and the CDR uses an image whose
  distribution permission is unresolved; they remain excluded.
- The initial allowlist is empty until the project owner records explicit,
  file-level public approval and applicable license/permission metadata.
- Historical archives, reviews, open decisions, costs, auxiliary output, raw
  data, local paths, and restricted figures are excluded by policy.

## Planned work

- [x] Define the versioned manifest and JSON Schema.
- [x] Implement strict validation and deterministic metadata generation.
- [x] Reject unknown fields, missing files, traversal, glob patterns,
      ambiguous status, invalid approval metadata, and exclusion leakage.
- [x] Generate SHA-256 checksums for every approved PDF/artifact.
- [x] Add focused tests and integrate them with `make check`.
- [x] Run tests and the repository build checks.
- [x] Record evidence and move this plan to `completed/`.

## Completed work

- Added `publication/public-content-v1.json`, a deny-by-default manifest with an
  empty initial allowlist, explicit exclusion policy, and pending owner
  decisions for overview content and the Proposal/CDR artifacts.
- Added `publication/public-content-v1.schema.json`, defining strict fields,
  controlled statuses, approval records, file kinds, and decision records.
- Added `tools/publication_contract.py` for schema-equivalent strict validation,
  path and file checks, local-path scanning, exact source-commit metadata, and
  SHA-256 checksums for every approved file including PDFs.
- Added 12 tests covering the valid contract, PDF checksums, path traversal,
  missing files, unknown fields, broad globs, ambiguous status, excluded-file
  leakage, unapproved types, local paths, and missing explicit approval.
- Added `publication-check`, `publication-metadata`, and `test` Make targets and
  integrated validation/tests into `make check`.
- Documented the contract, current empty allowlist, and approval boundary in
  `README.md`.

## Verification evidence

- `python3 tools/publication_contract.py validate` passed and reported zero
  approved files.
- `python3 -m unittest discover -s tests -v` passed all 12 tests.
- Deterministic metadata generation with `SOURCE_DATE_EPOCH=1785081600` wrote
  ignored `build/publication-metadata.json`, recording the exact source commit
  and zero approved artifacts.
- `make check` passed: publication validation/tests, all five historical
  archive checksum checks, Proposal and CDR LaTeX builds, and the unresolved
  citation/reference/missing-file log scan.
- Both manifest and schema parse as JSON; Python modules compile successfully
  with bytecode redirected to a temporary directory.
- `git diff --check` passed.

## Open publication decisions

- Project owner must approve exact public source files and any Proposal/CDR PDF.
- Project owner must confirm website-publication license and attribution terms.
- Permission for `archive/original_20260727/img/ics-layout.png` must be resolved
  or the CDR must use an approved replacement before its PDF can be published.
