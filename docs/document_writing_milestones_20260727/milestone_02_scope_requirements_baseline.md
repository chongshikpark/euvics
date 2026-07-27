# Milestone 2 — Scope, Terminology, and Requirements Baseline

## Objective

Define what EUVICS is being proposed, which operating cases the documents cover, which statements are requirements versus goals or predictions, and which conventions control every calculation and table.

## Work breakdown

### 2.1 Define audiences and document purposes

For the proposal, identify the target sponsor or decision-maker, page or format constraints, evaluation criteria, requested funding period, and expected decision. For the CDR, define the design-review audience, maturity level, configuration baseline, and required technical depth.

Until an actual call or template exists, mark sponsor-specific sections as placeholders rather than inventing requirements.

### 2.2 Define the project scope

State the system boundary: electron source, injector, linac or energy-setting system, beam transport, laser, synchronization, interaction region, EUV extraction and optics, diagnostics, detector/electronics, controls, facilities, shielding, and data analysis. Mark excluded systems and interfaces owned by others.

### 2.3 Establish reference operating cases

Create reviewed parameter sets for:

- The nominal 3 MeV kinetic-energy and 800 nm laser case
- A 6.7 nm target case
- A 13.5 nm target case
- Any staging or reduced-power commissioning case

Each parameter must have a status: requirement, design target, assumed input, pyEUVICS prediction, external reference, or `TBD`.

### 2.4 Build the requirements hierarchy

Assign stable identifiers to top-level and subsystem requirements. Suggested groups include:

- Source wavelength, bandwidth, flux, brilliance, stability, polarization, repetition rate, and availability
- Electron energy, charge, emittance, spread, timing, and pointing
- Laser wavelength, energy, duration, waist, `a0`, bandwidth, polarization, timing, and stability
- Interaction geometry and overlap
- EUV transport, acceptance, and diagnostics
- Radiation protection, interlocks, maintainability, utilities, and facility interfaces

For each requirement, capture rationale, verification method, owner, status, source, and affected subsystems.

### 2.5 Normalize terminology and notation

Create a glossary and symbol list. Define kinetic versus total electron energy, head-on collision angle, observation angle, waist convention, RMS versus FWHM widths, peak versus average power, spectral peak versus centroid, and all bandwidth definitions.

## Deliverables

```text
shared/terminology.tex
shared/symbols.tex
shared/requirements.tex
shared/reference_cases.tex
tables/requirements_matrix.csv
tables/reference_parameters.csv
reviews/open_decisions.md
docs/document_scope.md
```

## Completion criteria

- Proposal audience, CDR audience, and submission constraints are documented or explicitly `TBD`.
- Every reference parameter has units, status, owner, and provenance.
- Requirements, goals, assumptions, and predictions are visibly distinct.
- The 3 MeV quantity is explicitly identified as kinetic energy wherever applicable.
- Angle, bandwidth, waist, pulse-duration, and polarization conventions are frozen.
- The proposal and CDR import the same approved parameter macros or tables.
- Open design decisions have owners and resolution criteria.

## Codex tasks

Use Codex to extract candidate requirements from source notes, identify ambiguous wording, check unit consistency, and generate traceability tables. Require human approval before changing requirement values or status.

