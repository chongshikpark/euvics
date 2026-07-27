# Milestone 3 — Evidence, Bibliography, and Claim Traceability

## Objective

Build a reliable evidence base for the physics, accelerator, laser, EUV application, diagnostic, safety, cost, and technology-readiness claims in both documents.

## Work breakdown

### 3.1 Create a source plan

List the evidence needed for every major section. Prefer primary and authoritative sources: peer-reviewed papers, standards, manufacturer calibration documents, facility design reports, validated simulation documentation, and original experimental records.

### 3.2 Establish the bibliography

- Use stable citation keys and one shared bibliography database.
- Record DOI, URL, access date where relevant, report number, edition, and page or section notes.
- Deduplicate entries and preserve capitalization in titles and acronyms.
- Never create a citation from memory alone; verify it against the source.

### 3.3 Create a claim ledger

For each material claim, record the document location, claim text or summary, evidence type, citation or calculation artifact, confidence, reviewer, and status. Include quantitative performance claims, comparisons with other EUV technologies, technology-readiness claims, component capabilities, cost assumptions, and safety statements.

### 3.4 Build the literature synthesis

Prepare short reviewed notes on:

- ICS and nonlinear ICS kinematics
- Compact accelerator-based photon sources
- EUV source requirements and application context
- Superconducting RF photoinjectors and low-energy linacs
- High-power ultrafast laser systems and synchronization
- Interaction-region design and beam overlap
- EUV optics, gratings, photodiodes, and electronics
- Radiation safety and shielding methodology
- CAIN and other relevant simulation tools

The notes should distinguish directly supported facts from EUVICS design inferences.

### 3.5 Citation and permission review

Track the license or permission status of reused figures and tables. Prefer original redrawn diagrams based on cited sources. Do not copy copyrighted visuals merely because they are accessible online.

## Deliverables

```text
bibliography/references.bib
bibliography/source_inventory.md
reviews/claim_ledger.csv
reviews/missing_evidence.md
notes/literature/
figures/permissions.md
```

## Completion criteria

- Every material externally verifiable claim has a citation or documented calculation artifact.
- All bibliography records have been checked against their sources.
- Comparative statements define a comparable metric and operating condition.
- Source notes distinguish quotation, paraphrase, and project inference.
- Figure and table reuse has documented permission or an original replacement plan.
- Compilation produces no undefined citations.
- No placeholder or fabricated bibliography entries remain.

## Codex tasks

Ask Codex to map claims to already supplied sources, summarize sources within copyright limits, flag unsupported statements, normalize BibTeX entries, and check citation coverage. Human reviewers should decide whether the evidence is scientifically sufficient.

