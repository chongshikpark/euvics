# EUVICS documents

This repository contains two independently buildable LaTeX documents:

- `proposal/main.tex`: the concise, decision-oriented EUVICS Proposal;
- `cdr/main.tex`: the technical-baseline Conceptual Design Report (CDR).

Shared files are limited to presentation setup, terminology, symbols, reviewed requirements, bibliography data, and reproducibly generated results. Audience-specific prose belongs under the corresponding document directory.

## Prerequisites

Install a TeX distribution providing `latexmk`, `pdflatex`, and BibTeX. The repository uses BibTeX consistently; verified entries belong in `bibliography/references.bib`.

## Build and checks

Run commands from the repository root:

```sh
make proposal       # build/proposal/main.pdf
make cdr            # build/cdr/main.pdf
make all            # both documents
make check          # archive checksums, builds, and unresolved-reference checks
make clean          # remove generated LaTeX output
```

Build artifacts are written below `build/` and ignored by Git. `SOURCE_DATE_EPOCH` is set by the Makefile to reduce avoidable PDF metadata variation and may be overridden by a release process.

## Source and archive policy

The imported 2026-07-27 sources, image, and historical PDFs are preserved in `archive/original_20260727/`. They are read-only historical references. Verify them with `make verify-archive`; do not edit them or treat the PDFs as authoritative results.

The original working copies remain in `papers/` during Milestone 1 to avoid deleting user material. New edits belong in `proposal/`, `cdr/`, or the bounded shared directories.

## Repository layout

- `proposal/sections/`: proposal-specific sections.
- `cdr/sections/` and `cdr/appendices/`: CDR-specific material.
- `shared/`: audience-neutral LaTeX setup, terminology, symbols, reviewed requirements, and generated macros.
- `bibliography/`: verified BibTeX records.
- `reviews/`: review checklists and cross-document decisions.
- `archive/`: immutable imported material and checksums.

All scientific, citation, generated-result, and review rules in `AGENTS.md` apply. Missing facts remain explicit `TBD`s with an owner or question; they must not be filled speculatively.

## Known build warnings

The imported preamble uses `sectsty` and requests a 13 pt bold Computer Modern font in a 10 pt article. Current TeX Live reports package-command compatibility warnings and substitutes the available 12 pt bold font. These warnings do not indicate missing content or unresolved references. Typography/package modernization is deferred to an approved bounded change because it can alter pagination and appearance.
