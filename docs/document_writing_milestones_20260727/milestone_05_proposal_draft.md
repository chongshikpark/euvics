# Milestone 5 — EUVICS Proposal Draft

## Objective

Transform the current generic proposal into a concise, evidence-backed request for support that explains the need, proposed innovation, credible technical path, resources, risks, schedule, cost, and measurable outcomes.

The proposal should not read like a shortened CDR. It should help a reviewer decide whether EUVICS is valuable, feasible, differentiated, and ready for the requested next phase.

## Proposed structure

1. Title page and document control
2. Executive summary
3. Need and opportunity
4. Project objectives and measurable success criteria
5. EUVICS concept and distinguishing features
6. Baseline performance and evidence
7. Technical approach and work packages
8. pyEUVICS development and validation role
9. Team, facilities, and required partnerships
10. Schedule, milestones, and decision gates
11. Budget summary and basis
12. Technical, programmatic, and cost risks
13. Expected scientific, industrial, and workforce impact
14. References and concise appendices

Adapt this structure to the actual sponsor template when available.

## Work breakdown

### 5.1 Replace generic claims

Rewrite broad statements about brightness, stability, efficiency, cost, maintenance, and applications using quantified goals or cited evidence. If no defensible number exists, describe the intended investigation rather than claiming a result.

### 5.2 Define the funding ask

State what phase is being proposed, what will be delivered, what facilities and staff are required, what decision follows, and what work is explicitly outside scope. Link funds to work packages and completion evidence.

### 5.3 Present the technical concept

Use a clear system diagram and a short explanation of the electron beam, laser, ICS interaction, EUV transport, diagnostics, and controls. Include only the equations needed to establish feasibility; move detailed derivations to the CDR.

### 5.4 Present verified performance

Use the reviewed requirements baseline and generated pyEUVICS tables. Separate design targets from predictions, CAIN comparisons, and measured values. Explain the status of the 6.7 nm comparison and 13.5 nm target without implying validation that has not occurred.

### 5.5 Build work packages and decision gates

For each work package, define objective, tasks, responsible role, inputs, deliverables, schedule, dependencies, acceptance criteria, and risk-reduction value. Include explicit prototype, simulation, design-review, and validation gates.

### 5.6 Prepare budget and risk summaries

Use documented estimating assumptions and uncertainty ranges. Do not invent vendor quotations or institutional commitments. Link major risks to mitigation work and contingency.

## Deliverables

```text
proposal/main.tex
proposal/sections/executive_summary.tex
proposal/sections/need_and_opportunity.tex
proposal/sections/objectives.tex
proposal/sections/concept.tex
proposal/sections/performance.tex
proposal/sections/work_plan.tex
proposal/sections/team_facilities.tex
proposal/sections/schedule_budget.tex
proposal/sections/risks_impact.tex
reviews/proposal_compliance_matrix.md
reviews/proposal_open_items.md
```

## Completion criteria

- The first page states the need, EUVICS concept, differentiator, requested work, and expected outcome.
- Every objective has a measurable completion criterion.
- Design targets, calculations, references, and measurements are clearly distinguished.
- Work packages map to schedule, cost, risk reduction, and deliverables.
- Unsupported superlatives and generic filler are removed.
- Sponsor requirements are satisfied or visibly awaiting input.
- The proposal compiles cleanly and meets the applicable length and format constraints.
- A reviewer can understand the funding decision without reading the full CDR.

## Codex tasks

Give Codex one section with its audience, word budget, required evidence, and approved facts. Ask it to produce a claim ledger with the draft and to flag missing inputs instead of filling them speculatively.

