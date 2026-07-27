# Milestone 8 — Integration, Safety, Cost, Schedule, Risk, and R&D Plan

## Objective

Complete the project-level design information needed to judge whether EUVICS can be built, operated, verified, and advanced from conceptual design through commissioning within credible resources and constraints.

## Work breakdown

### 8.1 System integration

Describe installation sequence, alignment, coordinate control, vacuum segmentation, timing distribution, controls architecture, utilities, access, maintainability, configuration control, and interfaces with the host facility.

### 8.2 Safety and regulatory basis

Create a conceptual safety section covering radiation sources and shielding methodology, high voltage, RF, laser safety, cryogens, oxygen deficiency, vacuum, electrical hazards, interlocks, access control, and operating authorization. Use qualified safety calculations and applicable institutional or national requirements; do not let generic prose substitute for expert analysis.

### 8.3 Commissioning and verification

Define staged commissioning from component acceptance through injector, linac, laser, synchronization, first interaction, EUV detection, and performance demonstration. Identify diagnostics, prerequisites, hold points, acceptance criteria, and recovery paths.

### 8.4 Work breakdown and schedule

Build a work-breakdown structure linking design, procurement, fabrication, integration, commissioning, pyEUVICS validation, and documentation. Identify dependencies, long-lead items, critical-path assumptions, decision gates, and schedule uncertainty.

### 8.5 Cost estimate

State estimate date, currency, price basis, scope, exclusions, labor assumptions, procurement assumptions, escalation, contingency method, uncertainty range, and source for each major cost element. Separate base estimate, contingency, and management reserve where appropriate.

### 8.6 Risk and opportunity register

Cover physics performance, injector/linac, laser, synchronization, overlap, optical damage, detector sensitivity, radiation safety, procurement, schedule, cost, staffing, facility, and integration risks. Record probability, consequence, trigger, mitigation, owner, residual risk, and retirement evidence.

### 8.7 R&D and prototype plan

Convert “R&D required” statements into bounded tasks with hypotheses, prototype or test activity, required resources, quantitative exit criteria, schedule, and the design decision enabled by the result.

## Deliverables

```text
cdr/sections/system_integration.tex
cdr/sections/safety.tex
cdr/sections/commissioning.tex
cdr/sections/project_execution.tex
cdr/sections/cost_estimate.tex
cdr/sections/risk_and_rd.tex
proposal/sections/work_plan.tex
proposal/sections/schedule_budget.tex
proposal/sections/risks_impact.tex
tables/work_breakdown_structure.csv
tables/integrated_schedule.csv
tables/cost_estimate.csv
tables/risk_register.csv
tables/rd_plan.csv
```

## Completion criteria

- Integration interfaces and installation assumptions are explicit.
- Safety hazards, responsible experts, analysis needs, and authorization path are identified.
- Commissioning stages have prerequisites and measurable completion criteria.
- Schedule tasks connect to deliverables, dependencies, decision gates, and cost elements.
- Cost values have a basis, date, currency, uncertainty, and owner—or remain clearly `TBD`.
- Risks have owners, mitigations, triggers, and residual assessments.
- Each R&D task retires a named risk or enables a design decision.
- Proposal summaries agree with the detailed CDR tables.

## Codex tasks

Use Codex to normalize registers, cross-check schedule/cost/work-package identifiers, identify missing links, and draft summaries from approved tables. Human project, safety, and cost owners must approve substantive values and conclusions.

