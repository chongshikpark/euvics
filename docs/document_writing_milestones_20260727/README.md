# EUVICS Proposal and Conceptual Design Report Writing Roadmap

This roadmap covers development of two related LaTeX documents in a separate writing repository:

- **EUVICS Proposal** — a concise, persuasive case for support, centered on need, novelty, objectives, feasibility, work plan, resources, schedule, cost, risk, and expected impact.
- **EUVICS Conceptual Design Report (CDR)** — a traceable engineering and scientific baseline describing requirements, physics, subsystem designs, interfaces, performance budgets, safety, commissioning, cost, schedule, risks, and remaining R&D.

The existing `conceptual_design_report.tex` is primarily a section skeleton. `EUVICS Proposal.tex` contains an early generic narrative. Both documents need quantified requirements, cited evidence, verified pyEUVICS results, consistent terminology, and a reproducible build process.

## Milestone index

| Milestone | Theme | Primary outcome |
|---|---|---|
| [1](milestone_01_writing_repository_architecture.md) | Writing repository and document architecture | Clean, reproducible two-document LaTeX project |
| [2](milestone_02_scope_requirements_baseline.md) | Scope, terminology, and requirements baseline | Approved scientific and engineering baseline |
| [3](milestone_03_evidence_bibliography_claims.md) | Evidence, bibliography, and claims | Traceable sources for technical statements |
| [4](milestone_04_pyeuvics_results_pipeline.md) | pyEUVICS results pipeline | Reproducible tables and figures linked to code provenance |
| [5](milestone_05_proposal_draft.md) | EUVICS Proposal | Complete decision-oriented proposal draft |
| [6](milestone_06_cdr_physics_performance.md) | CDR physics and performance | Verified source-physics and performance chapters |
| [7](milestone_07_cdr_subsystem_design.md) | CDR subsystem design | Engineering descriptions and interface baselines |
| [8](milestone_08_integration_cost_schedule_risk.md) | Integration, safety, cost, schedule, and risk | Credible implementation and R&D plan |
| [9](milestone_09_cross_document_review.md) | Cross-document technical review | Consistent, evidence-backed proposal and CDR |
| [10](milestone_10_publication_release.md) | Publication and release | Reproducible review or submission packages |

## Recommended sequence

```text
M1  Repository and document architecture
 └─ M2  Scope, conventions, and requirements
     ├─ M3  Evidence and bibliography
     └─ M4  Reproducible pyEUVICS results
         ├─ M5  Proposal draft
         └─ M6  CDR physics and performance
             └─ M7  CDR subsystem design
                 └─ M8  Integration, cost, schedule, risk, and R&D
                     └─ M9  Cross-document review
                         └─ M10  Publication and release
```

Milestones 3 and 4 can proceed in parallel after the baseline is frozen. Drafting the proposal and CDR can overlap, but shared numerical claims must come from the same reviewed baseline.

## Suggested writing repository

```text
euvics-documents/
├── AGENTS.md
├── README.md
├── Makefile
├── latexmkrc
├── proposal/
│   ├── main.tex
│   └── sections/
├── cdr/
│   ├── main.tex
│   ├── sections/
│   └── appendices/
├── shared/
│   ├── preamble.tex
│   ├── terminology.tex
│   ├── symbols.tex
│   ├── requirements.tex
│   └── generated/
│       └── pyeuvics_results.tex
├── bibliography/
│   └── references.bib
├── configurations/
│   └── pyeuvics/
├── data/
│   ├── manifests/
│   └── derived/
├── figures/
│   ├── source/
│   └── generated/
├── tables/
├── scripts/
├── reviews/
└── releases/
```

Share definitions, requirements, reviewed parameter values, citations, and generated results. Do not share long prose passages automatically: the proposal and CDR have different audiences and purposes.

## Shared scientific conventions

- Electron energy is explicitly identified as kinetic or total energy; accelerator beam energy defaults to kinetic energy.
- Collision angle is measured between electron and laser propagation vectors: `0°` is co-propagating and `180°` is head-on.
- Observation angle is measured from the electron propagation direction.
- Linear, exact-recoil, nonlinear, polarization, harmonic, aperture, and bandwidth assumptions are stated with every result.
- Use standard SI units internally and display laboratory units explicitly.
- Use **extreme ultraviolet (EUV)** consistently rather than “extreme ultra-violet,” unless quoting a source.
- No numerical performance, cost, schedule, safety, or readiness claim is inserted without a source, calculation artifact, or explicit `TBD` owner.

## Codex collaboration

Copy [separate_repo_AGENTS.md](separate_repo_AGENTS.md) to the root of the new repository as `AGENTS.md`, then adapt paths and build commands. Give Codex bounded tasks such as one subsection, one table, one figure pipeline, or one review checklist at a time. Require it to preserve citations and distinguish verified facts from proposed design targets.

## Definition of done

The writing program is complete when both documents build cleanly from a fresh checkout; shared parameters and figures are reproducible; every material claim is traceable; unresolved decisions are visible; cross-document consistency checks pass; and review-ready PDFs are archived with their source, inputs, and provenance.

