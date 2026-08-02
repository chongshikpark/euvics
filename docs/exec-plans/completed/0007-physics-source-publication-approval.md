# Physics-source publication approval — completed

## Scope

Prepared and executed the narrow, auditable approval and allowlist change for
the authoritative physics narrative created in Task 1. No website lock, PDF,
figure, cost source, archive, or internal record was published.

## Completed work

- [x] Identified the smallest sufficient source set and exact SHA-256 values.
- [x] Reviewed selected files for sensitive information, local paths,
      credentials, costs/personnel details, image-permission dependencies, and
      unsupported claims.
- [x] Recorded scientific-review and project-owner approval by Chong Shik Park,
      Ph.D., dated 2026-08-03, for the exact source hashes.
- [x] Recorded `physics-overview-v1`, `public-draft`, MIT License, attribution,
      and file-specific known limitations.
- [x] Allowlisted exactly two CDR LaTeX sections and the verified bibliography.
- [x] Preserved every exclusion and both remaining PDF publication decisions;
      removed only the resolved website-overview approval decision.
- [x] Committed the approved source and manifest at immutable commit
      `f142bd188892f9518a956989ebaf7a42b6930f33`.
- [x] Prepared the exact website lock handoff without updating the website.

## Verification evidence

- `make check` passed: publication validation reported three approved files;
  all 12 publication-contract tests passed; all archive checksums passed; both
  documents built; and the unresolved citation/reference scan passed.
- `make publication-metadata` passed and emitted three artifacts with the exact
  source hashes, approval metadata, limitations, and source commit
  `f142bd188892f9518a956989ebaf7a42b6930f33`.
- Sensitive-information and local-path scans returned no findings for the three
  selected source files. No selected file references an image.
- `git diff --check` passed before the immutable publication commit.

## Approved public-draft inputs

- `cdr/sections/introduction.tex` — SHA-256
  `b1e362f6e89c6d79f6840c75c15995960911d8f08043d5baf39530491f3f4c76`.
- `cdr/sections/source_overview.tex` — SHA-256
  `988b309fadf0cb5b2a8114575c77acac101218014c44e757fd2548b77c7658ab`.
- `bibliography/references.bib` — SHA-256
  `c859403aad7ff42b8f0ae963231ae16146329452e43fad7ba794760602be56d9`.

## Remaining exclusions

Proposal and CDR PDFs, `cdr/main.tex`, the permission-unresolved layout figure,
cost material, internal reviews, execution plans, archives, historical working
copies, and all other unlisted files remain excluded. The website must update
its EUVICS source lock separately to the immutable handoff commit before it can
consume these sources.
