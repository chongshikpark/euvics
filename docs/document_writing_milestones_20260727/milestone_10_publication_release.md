# Milestone 10 — Publication, Reproducible Build, and Release

## Objective

Create review, submission, and archival packages that reproduce the approved EUVICS Proposal and Conceptual Design Report from tagged source and preserve the evidence behind every released version.

## Work breakdown

### 10.1 Release build

Build both documents from a clean checkout using the documented toolchain. Regenerate approved pyEUVICS tables and figures from frozen result bundles or verify their hashes. Capture compiler, bibliography tool, package, and pyEUVICS versions.

### 10.2 Quality gates

Require successful LaTeX compilation, no undefined citations or references, no missing figures, approved numerical consistency, completed visual inspection, resolved review comments, and verified metadata before release.

Warnings should be classified; do not suppress warnings broadly merely to make the build appear clean.

### 10.3 Submission package

Prepare the sponsor-required proposal files, ensuring page size, margins, fonts, page count, file size, accessibility, naming, and supplemental-material rules are satisfied. Keep confidential budget or partner information in controlled files when required.

### 10.4 CDR review package

Prepare the CDR PDF, source archive, appendices, requirements matrix, interface tables, validation report, cost/schedule/risk summaries, and review-comment disposition record appropriate to the review audience.

### 10.5 Archival package

Archive tagged source, generated PDFs, bibliography, configurations, result manifests, figure manifests, checksums, license and permission records, release notes, and build instructions. Restricted data should be represented by checksums and access notes rather than redistributed.

### 10.6 Versioning and change control

Use clear document versions and baselines. After release, corrections and design changes must update the change log and identify affected requirements, calculations, figures, costs, schedules, and conclusions.

## Deliverables

```text
releases/proposal_vX.Y/
releases/cdr_vX.Y/
releases/manifest.json
releases/checksums.sha256
CHANGELOG.md
BUILDING.md
reviews/final/release_checklist.md
reviews/final/comment_disposition.pdf
```

## Completion criteria

- Both PDFs build from a clean tagged checkout using documented commands.
- Released PDFs match recorded checksums.
- All included generated results trace to reviewed pyEUVICS configurations and provenance.
- Proposal submission requirements are verified item by item.
- CDR review materials include the required technical and programmatic appendices.
- Bibliography, figure permissions, authorship, affiliations, acknowledgments, and distribution markings are approved.
- Restricted information is handled according to the applicable policy.
- Release notes identify scientific limitations, unresolved design decisions, and validation coverage.
- A new contributor can reproduce the public portion of the release without undocumented local files.

## Codex tasks

Use Codex to run the release checklist, reproduce builds, compare hashes, inspect logs, check the archive manifest, and draft release notes from approved change records. Final submission and distribution require explicit project-owner approval.

