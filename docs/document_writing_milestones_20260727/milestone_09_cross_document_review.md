# Milestone 9 — Cross-Document Technical Review

## Objective

Verify that the proposal and CDR tell a consistent, technically defensible story while retaining their different levels of detail and decision purposes.

## Work breakdown

### 9.1 Automated consistency review

Check shared parameter macros, units, acronyms, symbols, requirement identifiers, figure references, bibliography entries, filenames, and links. Fail the release check when the proposal and CDR use different baseline values without an explicit explanation.

### 9.2 Scientific review

Review ICS equations, approximation domains, electron-energy convention, geometry, nonlinear treatment, spectral definitions, yield, acceptance, uncertainty, and CAIN comparison. Trace all important numbers to generated pyEUVICS results or external evidence.

### 9.3 Engineering review

Review subsystem requirements, margins, interfaces, selected concepts, alternatives, failure states, diagnostics, controls, utilities, maintainability, safety, and verification plans.

### 9.4 Programmatic review

Cross-check objectives, work packages, staffing assumptions, schedule, costs, risks, R&D tasks, decision gates, and outcomes. Confirm that the proposal does not promise more than the CDR supports.

### 9.5 Editorial and accessibility review

Review structure, narrative flow, terminology, grammar, equation formatting, significant figures, table readability, figure resolution, color accessibility, captions, PDF bookmarks, alt-text strategy where supported, and print quality.

### 9.6 Comment resolution

Assign every review comment an identifier, severity, owner, disposition, evidence, and closure approval. Preserve rejected comments and rationale. Changes to baselined numbers require a decision-log entry and regenerated artifacts.

## Suggested review gates

```text
30% review  — structure, scope, requirements, evidence plan
60% review  — complete technical content with known gaps
90% review  — verified numbers, figures, cost, schedule, risk, and citations
final review — resolved comments and reproducible release candidate
```

## Deliverables

```text
reviews/30_percent/
reviews/60_percent/
reviews/90_percent/
reviews/final/
reviews/consistency_report.md
reviews/claim_ledger.csv
reviews/comment_register.csv
reviews/baseline_change_log.md
reviews/release_readiness.md
```

## Completion criteria

- Proposal and CDR reference-case values agree with generated pyEUVICS artifacts.
- All requirements, units, acronyms, symbols, citations, figures, and cross-references resolve.
- Material claims have evidence and an approved confidence status.
- Cost, schedule, risk, work-package, and R&D identifiers are consistent across documents.
- No unresolved critical review comments remain.
- Remaining lower-severity open items are visible with owners and due dates.
- PDF visual inspection finds no clipped tables, unreadable figures, blank pages, or broken bookmarks.
- The proposal remains concise and decision-oriented; the CDR remains complete and traceable.

## Codex tasks

Ask Codex to run mechanical checks, compare shared facts, produce contradiction lists, trace claims, and apply approved comment resolutions. Do not ask it to close technical review comments without reviewer evidence.

