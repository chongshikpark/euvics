# Authoritative EUVICS physics narrative — completed

## Scope

Created a citable project-level explanation of EUVICS and inverse Compton
scattering for the Proposal and CDR. The Proposal remains concise; the CDR
carries explicit conventions, equations, assumptions, subsystem interfaces,
and the boundary to pyEUVICS.

This task did not approve numerical requirements, validation outcomes,
publication, or the CDR layout figure. It did not change the public-content
allowlist or the website repository.

## Authoritative inputs

- Existing EUVICS candidate baseline, bibliography, claim ledger, and literature
  notes.
- pyEUVICS 0.5.0 publication contract and allowlisted science documentation at
  locked commit `6193ab3e2be39fc74d40cd7ed1f9cece993b9ecd`.
- Existing primary-source records for Sun and Wu (2011), Krafft et al. (2005),
  and Hartemann and Wu (2013).

## Completed work

- [x] Added five locked pyEUVICS 0.5.0 bibliography records for conventions,
      exact equations, model scope, instrumentation, and validation status;
      added matching source-inventory entries.
- [x] Expanded the Proposal with an accessible definition of EUVICS, the
      two-Doppler-shift explanation, limiting head-on/on-axis scaling, the
      physical source chain, output dependencies, and the pyEUVICS role and
      limitations.
- [x] Expanded the CDR with kinetic and total energy definitions, gamma and beta,
      collision and observation angles, the exact coplanar recoil-aware energy
      equation, the Thomson limit, distinct linear/nonlinear regimes, beam-width
      conventions, output dependencies, subsystem interfaces, and validation
      boundaries.
- [x] Enabled the verified CDR bibliography and kept both bibliographies
      readable with long locked-source records.
- [x] Added claim-ledger entries CLM-021 through CLM-028 for the material new
      project, physics, model, and validation statements.
- [x] Left `publication/public-content-v1.json` unchanged with an empty
      allowlist.

## Verification evidence

- `make check` passed on 2026-08-03: publication validation reported zero
  approved files; all 12 publication-contract tests passed; all five archive
  checksums passed; Proposal and CDR LaTeX/BibTeX builds passed; and the
  undefined citation/reference/missing-file scan passed.
- Final logs contain no overfull/underfull boxes, undefined citations or
  references, duplicate labels, LaTeX errors, or package errors. Only the
  pre-existing `sectsty` compatibility and 13-to-12 pt font-substitution
  warnings documented in `README.md` remain.
- At the unchanged local pyEUVICS checkout, focused verification passed:
  `./bin/python -m pytest tests/physics/test_kinematics.py
  tests/physics/test_nonlinear.py` — 11 tests passed. The locked publication
  commit and local checkout have no differences in the cited publication
  manifest, science, instrumentation, or validation documentation.
- Poppler rendered all six Proposal pages and all seven CDR pages at 130 DPI.
  Every page was visually inspected; equations, citations, headings, margins,
  page numbers, and the existing layout figure render legibly without clipping
  or overlap.
- Proposal PDF SHA-256:
  `ce88c4ec2b2cd4408c899aaf65ea89cdcaf71a8e380cd30b656d1a237ebe1ba8`.
- CDR PDF SHA-256:
  `6e46cc529096a5a25b2bb9b4fac1a489dbf99c42f0dafbb8e8247eb89f9207c1`.
- `git diff --check` passed; the publication-manifest diff is empty.

## Unresolved scientific and approval questions

- The 3 MeV kinetic-energy and 800 nm values remain nominal assumed inputs with
  project-owner approval pending; 6.7 nm and 13.5 nm remain candidate targets.
- Application requirements and accelerator, laser, interaction-region, optics,
  detector, timing, acceptance, cost, safety, and verification allocations
  remain TBD with their existing owners or decision questions.
- The 6.7 nm CAIN comparison remains a known disagreement with incomplete
  provenance; no empirical correction is justified. The 13.5 nm case remains
  provisional. Synthetic detector calibration remains workflow evidence only.
- The CDR subsystem chapters remain heading-only and require reviewed technical
  content. The page-2 layout figure remains restricted until distribution
  permission is resolved or an approved replacement is supplied.
- Both documents require scientific and project-owner review. Neither document
  is approved for public website assembly by this task.
