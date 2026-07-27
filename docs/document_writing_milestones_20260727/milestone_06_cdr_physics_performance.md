# Milestone 6 — CDR Physics and Source-Performance Chapters

## Objective

Create the scientific core of the Conceptual Design Report: traceable requirements, explicit ICS equations and conventions, reference cases, performance predictions, sensitivity, uncertainty, and validation status.

## Proposed CDR chapters for this milestone

1. Executive summary and design status
2. Mission, applications, scope, and top-level requirements
3. System concept and reference configurations
4. Inverse Compton scattering physics
5. Linear, recoil, nonlinear, polarization, and harmonic models
6. Beam overlap, photon yield, spectrum, bandwidth, and angular acceptance
7. EUV power, brilliance definitions, and performance budgets
8. Sensitivity and uncertainty analysis
9. pyEUVICS methodology and software provenance
10. Analytical, legacy-script, CAIN, and experimental validation status

## Work breakdown

### 6.1 Write the requirements-to-physics chain

Explain how application-level wavelength, bandwidth, flux, stability, and availability goals flow down to electron, laser, interaction, optical, and diagnostic requirements. Every performance table should identify whether it is a requirement, target, prediction, or measured result.

### 6.2 Document equations and domains

Present the exact definitions and governing equations used by pyEUVICS. State approximation domains, recoil treatment, nonlinear effective-mass convention, polarization factors, harmonic interpretation, and conditions not modeled.

### 6.3 Establish reference cases

Provide complete input and result tables for the nominal 3 MeV/800 nm case and reviewed 6.7 nm and 13.5 nm cases. Show the quantitative difference between interpreting 3 MeV as kinetic versus total electron energy as a convention-control example.

### 6.4 Add realistic performance budgets

Include energy spread, emittance, divergence, laser bandwidth, pointing, timing, spatial overlap, aperture, and optical/detector effects where implemented and validated. Avoid quoting brilliance until its definition and normalization are explicit.

### 6.5 Present validation honestly

Compare with analytical limits, legacy scripts, CAIN, published cases, and measurements under matched assumptions. Discuss residual discrepancies and model limits rather than applying undocumented correction factors.

## Deliverables

```text
cdr/sections/executive_summary.tex
cdr/sections/mission_requirements.tex
cdr/sections/system_concept.tex
cdr/sections/ics_physics.tex
cdr/sections/source_performance.tex
cdr/sections/sensitivity_uncertainty.tex
cdr/sections/model_validation.tex
cdr/appendices/equations.tex
cdr/appendices/reference_cases.tex
tables/performance_budget.csv
reviews/physics_review_checklist.md
```

## Completion criteria

- All symbols and conventions match pyEUVICS and the shared terminology files.
- Each equation defines its variables, units, assumptions, and applicability.
- Reference case tables regenerate from versioned configurations.
- Performance budgets identify dominant uncertainties and acceptance assumptions.
- Kinetic versus total energy cannot be confused.
- CAIN comparisons use matched geometry, aperture, polarization, harmonic, and statistic definitions.
- Known discrepancies and unimplemented physics are explicit.
- A qualified reviewer can reproduce key calculations from the documented inputs.

## Codex tasks

Use Codex to turn verified equation notes and generated tables into structured prose, check symbol consistency, trace every number to a macro or source, and produce review questions. Require a physics expert to approve equations and conclusions.

