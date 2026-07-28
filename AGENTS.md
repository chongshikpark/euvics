# AGENTS.md — EUVICS Writing Repository

## Purpose

This repository contains the EUVICS Proposal and Conceptual Design Report. Treat both as scientific and engineering documents: clarity, evidence, reproducibility, and traceability are more important than producing large amounts of prose quickly.

## Document roles

- The proposal is concise and decision-oriented. It explains need, novelty, objectives, feasibility, work plan, resources, cost, risk, and impact.
- The CDR is the technical baseline. It documents requirements, assumptions, equations, subsystem designs, interfaces, performance, verification, safety, cost, schedule, risk, and remaining R&D.
- Share approved facts, definitions, references, and generated results. Do not force identical prose into both documents.

## Scientific conventions

- State whether electron energy is kinetic or total. Accelerator beam energy defaults to kinetic energy only when the field is explicitly named accordingly.
- Define collision angle between electron and laser propagation vectors: `0°` is co-propagating and `180°` is head-on.
- Define observation angle relative to electron propagation.
- State units and width conventions, including RMS versus FWHM and laser-waist definitions.
- State linear/exact, recoil, nonlinear, polarization, harmonic, aperture, and bandwidth assumptions with each result.
- Use “extreme ultraviolet (EUV)” consistently.

## Sources and claims

- Never invent citations, quotations, performance results, costs, schedules, partners, approvals, standards, component specifications, or experimental measurements.
- Cite primary or authoritative sources where practical.
- Trace numerical claims to a citation, approved table, or versioned calculation artifact.
- Mark missing information as `TBD` with an owner or question; do not fill gaps speculatively.
- Distinguish requirement, design target, assumption, calculation, simulation reference, and measurement.
- Do not reproduce copyrighted figures without permission. Prefer original diagrams with citations.

## pyEUVICS results

- Use versioned configuration and result files; do not copy terminal or notebook numbers manually into prose.
- Generate LaTeX macros, tables, and publication figures through documented scripts.
- Preserve pyEUVICS version, configuration, units, warnings, seed, sample count, and input checksums.
- Do not edit generated result files by hand.
- Do not claim agreement with CAIN or experiment unless definitions, geometry, acceptance, binning, and uncertainties are matched.

## File handling

- Preserve archived originals and raw data as read-only references.
- Edit source files, not compiled PDFs or auxiliary LaTeX output.
- Keep build artifacts out of source directories when possible.
- Do not delete or overwrite user material unless explicitly requested.
- Keep confidential or restricted information out of distributable examples and archives.

## Writing style

- Prefer precise, direct technical prose.
- Define acronyms on first use and use terminology consistently.
- Avoid unsupported superlatives and vague adjectives such as “high,” “advanced,” “efficient,” or “low cost”; quantify or qualify them.
- Keep equations, tables, and figures close to the text that interprets them.
- Captions should explain what is shown, relevant conditions, and the conclusion the reader may draw.
- Use consistent significant figures and do not imply more precision than the inputs support.

## Working method

1. Inspect the applicable requirements, sources, generated results, and nearby prose before editing.
2. State assumptions and unresolved questions.
3. Make bounded changes to one section, table, figure, or review task at a time.
4. Compile the affected document and inspect warnings.
5. Check citations, references, units, terminology, and cross-document consistency.
6. Summarize changed files, verification performed, and remaining `TBD`s.
7. After completing a milestone execution, save its completed execution plan under
   `docs/exec-plans/completed/`. Use a sequential zero-padded numeric prefix and a
   concise description, for example `0001-milestone-01-repository-architecture.md`.

## Review boundaries

- Codex may draft, restructure, check, and apply approved revisions.
- Physics conclusions require scientific review.
- Safety claims and shielding calculations require qualified safety review.
- Costs and schedules require approval by their responsible owners.
- Authorship, institutional commitments, licensing, submission, and public release require project-owner approval.

## Definition of done for an edit

- The requested content is complete within its stated scope.
- Claims and numerical values are traceable.
- Units, symbols, and terminology are consistent.
- LaTeX builds without new errors or unresolved references.
- Generated artifacts are reproducible and not hand-edited.
- Open questions and review needs remain visible.
