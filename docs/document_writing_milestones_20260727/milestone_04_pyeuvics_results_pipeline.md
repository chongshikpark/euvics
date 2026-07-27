# Milestone 4 — Reproducible pyEUVICS Results Pipeline

## Objective

Connect the writing repository to versioned pyEUVICS calculations so that document tables, figures, and numerical statements can be regenerated and audited instead of copied manually from notebooks or terminal output.

## Work breakdown

### 4.1 Freeze the calculation interface

Record the pyEUVICS release or commit used for each document baseline. Store configuration files for the nominal, 6.7 nm, and 13.5 nm cases. A configuration must include units, energy convention, collision and observation angles, model type, `a0`, polarization, harmonic, recoil choice, acceptance, and random seed when applicable.

### 4.2 Define result provenance

Each exported result bundle should contain:

- Input configuration and schema version
- pyEUVICS version or commit
- Python and dependency versions
- Calculation timestamp
- Model assumptions and warnings
- Random seed and sample count
- Source-data checksums
- Machine-readable results with full precision

### 4.3 Generate LaTeX-safe values

Write a small export tool that converts reviewed result bundles into `shared/generated/pyeuvics_results.tex`. Use named macros for important baseline values and generate complete tables where appropriate. Control significant figures and units in one formatting layer without changing stored numerical precision.

### 4.4 Generate figures reproducibly

Generate spectra, angle scans, `a0` scans, yield budgets, throughput, detector response, and uncertainty figures from configuration-driven scripts. Every figure should have a companion metadata file or manifest identifying inputs and code provenance.

### 4.5 Validate document results

Add automated checks for missing macros, nonfinite values, unit mismatches, stale generated files, inconsistent reference cases, and divergence from pyEUVICS benchmark tolerances. Compare key values with analytical limits and CAIN only under matched assumptions.

### 4.6 Separate notebooks from publication artifacts

Jupyter notebooks may explore and explain calculations, but publication figures and tables must be reproducible through noninteractive scripts. Do not rely on notebook cell order or hidden state.

## Deliverables

```text
configurations/pyeuvics/nominal_3MeV_800nm.yaml
configurations/pyeuvics/target_6p7nm.yaml
configurations/pyeuvics/target_13p5nm.yaml
scripts/run_pyeuvics_cases.py
scripts/export_latex_results.py
scripts/generate_figures.py
shared/generated/pyeuvics_results.tex
data/manifests/pyeuvics_results.json
data/derived/
figures/generated/
reviews/numerical_validation.md
```

## Completion criteria

- One documented command regenerates all pyEUVICS-derived macros, tables, and figures.
- The proposal and CDR use generated values rather than separately typed copies.
- Result bundles preserve configuration, units, version, assumptions, and warnings.
- Nominal, 6.7 nm, and 13.5 nm cases pass agreed reference checks.
- Generated LaTeX compiles without manual editing.
- Figure axes, legends, and captions state units and necessary model assumptions.
- Stale or uncommitted generated results are detectable before release.

## Codex tasks

Use Codex to implement exporters, connect macros to the documents, compare generated artifacts, and diagnose reproducibility failures. Ask it to report the originating configuration for every number it edits.

