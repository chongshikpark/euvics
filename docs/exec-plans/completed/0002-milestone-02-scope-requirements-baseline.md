# Completed execution plan 0002 — Milestone 2 scope and requirements baseline

## Status

Repository implementation completed on 2026-07-28. Numerical requirements,
reference-case approval, sponsor constraints, system exclusions, and responsible
owner assignments remain pending project-owner and applicable specialist review.

## Objective

Implement the scope, terminology, reference-case, and candidate requirements
baseline defined by
`docs/document_writing_milestones_20260727/milestone_02_scope_requirements_baseline.md`
without inventing sponsor constraints, design values, sources, or approvals.

## Assumptions and boundaries

- The milestone roadmap is the only repository source for the nominal 3 MeV
  kinetic-energy input, 800 nm incident-laser input, and 6.7 nm and 13.5 nm
  candidate target cases.
- Generic prose inherited from the original Proposal is not an approved source
  of requirements or numerical values.
- Reporting conventions may be controlled by the candidate baseline, but physics
  conclusions and numerical requirement approval require human review.
- Role-based owners identify who must resolve each question; they do not assert
  that a named individual or institutional commitment exists.

## Executed plan

1. Read Milestone 2 and inventoried shared files, document structure, existing
   terminology, candidate requirement language, and available numerical inputs.
2. Confirmed that no authoritative sponsor call, parameter source, subsystem
   allocation, or approved numerical requirements are present in the repository.
3. Defined Proposal and CDR purposes, audiences, maturity, submission constraints,
   system boundary, exclusions, and external interfaces, using owner-assigned
   `TBD`s where decisions are missing.
4. Established explicit classifications for requirements, design targets, assumed
   inputs, pyEUVICS predictions, external references, measurements, and `TBD`s.
5. Froze reporting conventions for kinetic/total electron energy, collision and
   observation angles, laser waist, RMS/FWHM widths, power, spectral peak/centroid,
   bandwidth, and polarization.
6. Created shared reference-case macros for 3 MeV kinetic energy, 800 nm incident
   laser wavelength, and 6.7 nm and 13.5 nm candidate targets, all marked as
   approval pending and not predictions or measurements.
7. Created a 32-row reference-parameter register with units, status, approval
   state, owner, provenance, and notes for nominal, 6.7 nm, 13.5 nm, and
   commissioning cases.
8. Created a 41-row candidate requirements hierarchy with stable system and
   subsystem identifiers, rationale, verification placeholder, owner, approval
   status, provenance, and affected subsystems.
9. Added nine owner-assigned open decisions with explicit resolution criteria and
   added three proposed cross-document decisions to the decision log.
10. Imported the same terminology, symbols, requirements revision, and reference
    cases into both LaTeX entry points through the shared preamble.
11. Validated CSV structure, identifiers, required metadata, archive integrity,
    LaTeX builds, unresolved references, and patch whitespace.

## Changed and added paths

- `README.md`
- `shared/preamble.tex`
- `shared/terminology.tex`
- `shared/symbols.tex`
- `shared/requirements.tex`
- `shared/reference_cases.tex`
- `tables/requirements_matrix.csv`
- `tables/reference_parameters.csv`
- `reviews/decision_log.md`
- `reviews/open_decisions.md`
- `docs/document_scope.md`

## Verification performed

- `make check`: passed for archive integrity and both independent document builds.
- Undefined citations, unresolved references, and missing-file checks: passed.
- CSV parsing: passed for 41 requirement rows/13 columns and 32 reference rows/10 columns.
- Stable-ID uniqueness and required metadata checks: passed.
- Both LaTeX logs show imports of `shared/requirements.tex` and
  `shared/reference_cases.tex`.
- `git diff --check`: passed.

## Known warnings

The inherited `sectsty` compatibility and 13 pt Computer Modern font-substitution
warnings remain unchanged from Milestone 1. No new warnings were introduced.

## Remaining TBDs and review needs

- `OD-001` through `OD-009` in `reviews/open_decisions.md` require resolution.
- Project-owner approval is required before candidate statements become requirements.
- Scientific review is required for reference-case and convention approval.
- Qualified/responsible owners must be assigned for safety, cost, schedule,
  facility-interface, and subsystem requirements.
- The commissioning case and complete nominal, 6.7 nm, and 13.5 nm parameter sets
  remain `TBD` pending versioned configurations and review.
