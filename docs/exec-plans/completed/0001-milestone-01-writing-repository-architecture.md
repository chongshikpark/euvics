# Completed execution plan 0001 — Milestone 1 writing repository architecture

## Status

Completed on 2026-07-28, subject to the project-owner review noted below.

## Objective

Implement the repository and LaTeX document architecture defined by
`docs/document_writing_milestones_20260727/milestone_01_writing_repository_architecture.md`
without rewriting technical content.

## Assumptions and boundaries

- The current `euvics` repository is the separate writing repository described by the roadmap.
- The imported PDFs are historical references, not authoritative technical results.
- Existing technical prose was preserved except for bounded terminology and heading corrections required by repository conventions.
- Physics conclusions, safety claims, costs, schedules, institutional commitments, and release decisions were not approved or introduced by this work.

## Executed plan

1. Inventoried the original TeX sources, PDFs, image, existing build artifacts, and installed LaTeX tools.
2. Calculated SHA-256 checksums for the imported material.
3. Copied the two original TeX sources, layout image, and historical PDFs to `archive/original_20260727/`.
4. Recorded the checksums in `archive/original_20260727/SHA256SUMS` and made the archived source artifacts read-only.
5. Split the Proposal and Conceptual Design Report into independent `main.tex` entry points and named section files.
6. Added audience-neutral shared preamble, terminology, symbols, requirements, and generated-output locations.
7. Replaced technically inappropriate generic headings in the laser and controls sections with subsystem-specific headings.
8. Established `latexmk` builds, BibTeX policy, deterministic-build environment settings, build-directory output, cleaning, archive verification, and unresolved-reference checks.
9. Expanded `.gitignore` for LaTeX auxiliary and build files.
10. Added repository documentation, a decision log, and chapter, figure, and baseline-change review checklists.
11. Built both documents independently, inspected warnings, verified archive integrity, checked repeated-build PDF hashes, and ran `git diff --check`.

## Changed and added paths

- `AGENTS.md`
- `.gitignore`
- `README.md`
- `Makefile`
- `latexmkrc`
- `archive/original_20260727/`
- `bibliography/references.bib`
- `proposal/main.tex`
- `proposal/sections/`
- `cdr/main.tex`
- `cdr/sections/`
- `cdr/appendices/`
- `shared/`
- `reviews/`

The original working material under `papers/` was not deleted or overwritten.

## Verification performed

- `make check`: passed.
- Independent Proposal build: passed; output `build/proposal/main.pdf`.
- Independent CDR build: passed; output `build/cdr/main.pdf`.
- Archive SHA-256 verification: all five archived artifacts passed.
- Missing-file, undefined-citation, and unresolved-reference log checks: passed.
- Repeated build PDF checksums: identical for each document.
- `git diff --check`: passed.

## Known warnings

The imported formatting setup produces the following non-fatal warnings in both documents:

- `sectsty` reports that `\underbar` and `\underline` have changed.
- Computer Modern lacks the requested 13 pt bold font, so LaTeX substitutes 12 pt.

These warnings are documented in the repository `README.md`. Typography and package modernization were deferred because they can change layout and pagination.

## Remaining TBDs and review needs

- `TBD` — project owner: review and approve the root `AGENTS.md`, including the completed-plan archival rule added after Milestone 1 execution.
- `TBD` — project owner: approve the initial shared requirements baseline during Milestone 2.
- Existing generic technical claims require evidence and scientific review in later milestones; Milestone 1 did not validate them.
