# Milestone 1 — Writing Repository and Document Architecture

## Objective

Create a separate, version-controlled LaTeX repository in which the EUVICS Proposal and Conceptual Design Report can evolve independently while sharing verified terminology, parameters, citations, figures, and pyEUVICS outputs.

## Work breakdown

### 1.1 Import and preserve the originals

- Copy the two current `.tex` sources and `img/ics-layout.png` into an `archive/original_20260727/` directory.
- Record checksums and do not edit the archived copies.
- Ignore auxiliary LaTeX build files such as `.aux`, `.log`, `.out`, `.toc`, `.synctex.gz`, and local build directories.
- Preserve the existing PDFs only as historical references, not authoritative results.

### 1.2 Split the documents into maintainable files

Create separate `proposal/main.tex` and `cdr/main.tex` entry points. Move chapters or sections into clearly named files. Keep shared material limited to preamble definitions, symbols, terminology, reviewed requirements, and generated numerical macros.

Replace the repeated generic subsection pattern where it is technically inappropriate. For example, laser, controls, cost, and safety sections should use subsystem-specific engineering headings rather than “Accelerator Physics Design.”

### 1.3 Establish the build system

- Use `latexmk` or an equivalent noninteractive build command.
- Choose one bibliography system and document it; `biblatex`/Biber or BibTeX are acceptable if applied consistently.
- Provide commands to build each document, build both, clean generated files, and run checks.
- Make outputs deterministic where LaTeX permits and write them to a build directory.
- Confirm missing references, citations, or figures cause visible warnings in continuous integration.

### 1.4 Define repository rules for Codex

Create a root `AGENTS.md` covering scientific conventions, citation requirements, source-data immutability, generated files, LaTeX style, build verification, and the rule that Codex must not invent references, costs, performance numbers, partners, approvals, or experimental results.

### 1.5 Add planning and review infrastructure

Provide issue templates or Markdown checklists for chapter drafting, technical review, figure review, and baseline changes. Use a decision log for changes that affect both documents.

## Deliverables

```text
AGENTS.md
README.md
.gitignore
Makefile
latexmkrc
archive/original_20260727/
proposal/main.tex
proposal/sections/
cdr/main.tex
cdr/sections/
cdr/appendices/
shared/preamble.tex
shared/terminology.tex
shared/symbols.tex
reviews/decision_log.md
reviews/chapter_checklist.md
```

## Completion criteria

- Both imported documents compile from their new entry points.
- Original sources and image are archived without modification.
- Auxiliary build files are excluded from version control.
- A clean-checkout build procedure is documented and verified.
- The proposal and CDR can be built independently.
- Shared files do not contain audience-specific prose.
- Root Codex instructions are reviewed by the project owner.

## Codex tasks

Ask Codex to inventory the originals, propose the file split, patch one structural change at a time, compile after each change, and report warnings. Do not ask it to rewrite technical content during this milestone.

