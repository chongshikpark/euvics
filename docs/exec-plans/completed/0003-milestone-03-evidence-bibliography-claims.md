# Completed execution plan 0003 — Milestone 3 evidence, bibliography, and claims

## Status

Repository implementation completed on 2026-07-29. Scientific sufficiency,
project-specific evidence, figure-release permission, and owner approvals remain
open as recorded in the review files.

## Objective

Implement the evidence, shared bibliography, claim traceability, literature notes,
and permission review defined by
`docs/document_writing_milestones_20260727/milestone_03_evidence_bibliography_claims.md`
without fabricating sources or transferring external performance to EUVICS.

## Assumptions and boundaries

- Primary publisher pages, issuing-body pages, author-issued documentation, and
  DOI records were used to verify bibliography entries.
- External facilities and experiments provide context or methods only; their
  performance, cost, and readiness were not assigned to EUVICS.
- The CDR remains a section skeleton, so its only current material evidence issue
  is the permission status of the archived layout image.
- Human reviewers determine scientific sufficiency and source applicability.

## Executed plan

1. Read Milestone 3 and inventoried active claims, bibliography hooks, source
   gaps, and the current figure.
2. Identified unsupported comparative, performance, readiness, and cost language
   inherited from the original Proposal.
3. Verified eleven primary or authoritative records covering Compton modeling,
   nonlinear scattering, SRF photoinjectors and linacs, ultrafast synchronization,
   EUV optics and metrology, radiation safety, and CAIN.
4. Added a shared BibTeX database with stable keys, DOI/URL/report metadata where
   verified, access dates for online sources, and applicability notes.
5. Added a source inventory and section-by-section evidence acquisition plan.
6. Rewrote active Proposal claims to cite suitable evidence, state project-baseline
   provenance, or expose an owner-assigned evidence gap.
7. Removed unsupported claims of superior brightness/control, application
   essentiality, excellent stability/efficiency, robustness/scalability, and an
   existing detailed cost basis.
8. Created a 20-row claim ledger covering supported current claims, project
   baseline statements, approval-pending inputs, figure permission, and removed
   unsupported inherited claims.
9. Created twelve missing-evidence actions with owners and closure criteria.
10. Wrote nine literature synthesis notes that distinguish supported paraphrase
    from EUVICS inference and use no direct quotations or copied visuals.
11. Added a figure permission register and an original-replacement plan for the
    archived layout image.
12. Enabled the Proposal bibliography and compiled until citations resolved.

## Changed and added paths

- `bibliography/references.bib`
- `bibliography/source_inventory.md`
- `proposal/main.tex`
- `proposal/sections/`
- `reviews/claim_ledger.csv`
- `reviews/missing_evidence.md`
- `notes/literature/`
- `figures/permissions.md`

## Verification performed

- `make check`: passed for archive integrity and both document builds.
- BibTeX: no missing database entries or record warnings.
- Final Proposal and CDR logs: no undefined citations or references.
- Claim ledger: 20 rows, unique IDs, and complete fields.
- Active-document unsupported-superlative/comparison scan: passed.
- New overfull-box scan after rephrasing: passed.
- `git diff --check`: passed.

## Known warnings

Only the inherited Milestone 1 warning classes remain: `sectsty` command-change
warnings and 13 pt Computer Modern bold-font substitution. No new citation,
reference, missing-file, bibliography, or layout-overflow warnings remain.

## Remaining TBDs and review needs

- `ME-001` through `ME-012` require project evidence and assigned/qualified review.
- All EUVICS numerical performance remains pending M4 versioned calculations.
- Scientific reviewers must approve the adequacy and applicability of physics,
  accelerator, laser, optics, and diagnostic sources.
- A qualified safety reviewer must approve applicable regulation, source terms,
  shielding, controls, and verification; IAEA guidance is not project approval.
- The layout image remains internal-only pending authorship and distribution-rights
  confirmation or replacement by an approved original diagram.
- Cost, schedule, readiness, partner, approval, and institutional claims remain
  unsupported and absent from active prose.
