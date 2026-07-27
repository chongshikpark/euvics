# Milestone 7 — CDR Subsystem Design Chapters

## Objective

Document a coherent conceptual design for each EUVICS subsystem, including requirements, selected concept, alternatives, interfaces, predicted performance, diagnostics, controls, technical risks, and remaining R&D.

## Proposed subsystem chapters

1. Electron source and superconducting RF photoinjector
2. Superconducting RF linac or energy-control system
3. Electron-beam transport, focusing, and dump
4. Incident laser and pulse delivery
5. Synchronization and timing
6. Interaction region and beam-overlap diagnostics
7. EUV extraction, optics, filtering, and spectral diagnostics
8. Detector and electronics chain
9. Controls, data acquisition, and machine protection
10. Cryogenics, RF, vacuum, utilities, and facility interfaces

## Standard subsystem template

Each chapter should use a consistent structure:

- Purpose and scope
- Allocated requirements
- Interface inputs and outputs
- Selected conceptual design
- Key parameters and performance budget
- Alternatives considered and selection rationale
- Diagnostics, controls, and calibration
- Operating modes and failure states
- Safety and maintainability considerations
- Verification plan
- Open decisions, risks, and required R&D

### 7.1 Replace vague subsystem descriptions

The current drafts use broad statements such as “high power,” “high brightness,” “precise timing,” and “advanced controls.” Replace these with allocated targets, rationale, uncertainty, and verification method—or label them `TBD`.

### 7.2 Define interfaces

Create interface-control tables for electron-to-interaction, laser-to-interaction, interaction-to-EUV optics, detector-to-electronics, and subsystem-to-controls boundaries. Capture coordinate frames, timing references, apertures, vacuum interfaces, power, cooling, data, interlocks, and ownership.

### 7.3 Document design alternatives

For major choices, record alternatives, evaluation criteria, assumptions, evidence, selected baseline, and deferred decisions. Conceptual design maturity does not require false precision; it requires clear decisions and visible uncertainty.

### 7.4 Add verification paths

Map each allocated requirement to analysis, simulation, inspection, component test, subsystem test, or integrated commissioning measurement.

## Deliverables

```text
cdr/sections/electron_injector.tex
cdr/sections/rf_linac.tex
cdr/sections/beam_transport.tex
cdr/sections/laser_system.tex
cdr/sections/timing_synchronization.tex
cdr/sections/interaction_region.tex
cdr/sections/euv_optics_diagnostics.tex
cdr/sections/detector_electronics.tex
cdr/sections/controls_daq.tex
cdr/sections/utilities_facilities.tex
tables/subsystem_parameters/
tables/interface_control.csv
tables/verification_matrix.csv
reviews/subsystem_open_items.md
```

## Completion criteria

- Every subsystem requirement traces to a top-level requirement.
- Interface quantities have units, coordinate or timing conventions, owners, and status.
- Parameter tables distinguish selected values, ranges, margins, and `TBD`s.
- Alternatives and selection rationale are documented for major architecture choices.
- Diagnostics and verification methods are sufficient to test allocated requirements.
- Remaining R&D has a reason, deliverable, and decision criterion.
- Figures are legible, original or licensed, and consistent with the parameter baseline.
- Cross-subsystem contradictions are entered in the decision log.

## Codex tasks

Ask Codex to apply the common subsystem template, detect vague or inconsistent requirements, compare interface tables, and maintain open-item lists. Do not let it infer component specifications or supplier capabilities without verified sources.

