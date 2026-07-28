# EUVICS document scope baseline

Baseline revision: `M2-candidate-20260728`  
Approval status: `TBD — project-owner approval pending`

## Document purposes and audiences

### Proposal

The Proposal is intended to support a funding or project-authorization decision. It should state the need, novelty, objectives, feasibility, work plan, resources, cost, risk, and expected impact concisely. Sponsor-specific wording remains a placeholder until an authoritative call or template is supplied.

| Item | Baseline |
|---|---|
| Target sponsor or decision-maker | `TBD — owner: project owner; provide the authoritative call or decision context.` |
| Page and format constraints | `TBD — owner: project owner; provide the call/template.` |
| Evaluation criteria | `TBD — owner: project owner; provide the authoritative criteria.` |
| Requested funding period | `TBD — owner: project owner and cost/schedule owners.` |
| Requested funding amount | `TBD — owner: project owner and cost owner.` |
| Expected decision | `TBD — owner: project owner; identify funding, authorization, review, or other decision.` |

### Conceptual Design Report

The Conceptual Design Report (CDR) is the traceable scientific and engineering baseline for conceptual design review. It must document requirements, assumptions, governing equations, subsystem concepts, interfaces, predicted performance, verification, safety, cost, schedule, risk, and remaining research and development.

| Item | Baseline |
|---|---|
| Design-review audience | `TBD — owner: project owner; identify scientific, engineering, safety, facility, and sponsor reviewers.` |
| Maturity level | Conceptual design; subsystem maturity and technology readiness are `TBD` and must not be inferred. |
| Configuration baseline | `M2-candidate-20260728`; numerical approval pending. |
| Required technical depth | Sufficient to trace each approved requirement to rationale, allocation, analysis/model, interface, and verification method; detailed acceptance criteria remain `TBD` until requirements are approved. |

## System boundary

The candidate EUVICS system boundary includes the following functions and their internal interfaces:

1. electron source and photocathode drive;
2. injector;
3. linac or other energy-setting system;
4. electron-beam transport, focusing, steering, and dump;
5. incident laser source, transport, focusing, and polarization control;
6. electron–laser synchronization and timing distribution;
7. interaction region, vacuum, alignment, and overlap control;
8. extreme ultraviolet extraction, collection, transport, filtering, and optics;
9. electron, laser, extreme ultraviolet, radiation, and machine-protection diagnostics;
10. detectors, readout electronics, timing, triggering, and acquisition;
11. supervisory controls, interlocks, machine protection, and data systems;
12. required utilities, cryogenics, radio-frequency power, cooling, vacuum services, and facility interfaces;
13. radiation protection, shielding interfaces, access control, and safety systems; and
14. physics analysis, calibration, uncertainty evaluation, simulation provenance, and data archiving.

This list defines scope for interface and requirements capture; it does not assert a selected subsystem technology or approved performance.

## Exclusions and externally owned interfaces

No excluded systems or externally owned interfaces are approved. `TBD — owner: project owner` must identify host-facility scope, user/end-station scope, utility tie-in ownership, conventional construction, shielding ownership, source/application optics ownership, data infrastructure, and regulatory responsibilities. Until resolved, these are boundary decisions rather than exclusions.

## Reference operating cases

All documents use the same candidate cases in `shared/reference_cases.tex` and `tables/reference_parameters.csv`:

- nominal case: electron kinetic energy of 3 MeV and incident laser wavelength of 800 nm, both roadmap-sourced assumed inputs;
- 6.7 nm case: 6.7 nm output wavelength is a roadmap-specified candidate design target; all parameters needed to realize or predict it are `TBD`;
- 13.5 nm case: 13.5 nm output wavelength is a roadmap-specified candidate design target; all parameters needed to realize or predict it are `TBD`; and
- commissioning case: configuration and reduced-power/staging parameters are `TBD`.

The 3 MeV quantity is kinetic energy, not total energy. No output wavelength, flux, brilliance, bandwidth, power, or agreement with another code or experiment is implied by the nominal inputs.

## Classification and approval rules

- **Requirement:** an approved, verifiable statement using “shall,” with an owner and source.
- **Design target:** proposed performance for design optimization; not contractually or technically approved as a requirement.
- **Assumed input:** value imposed for a calculation; not a prediction.
- **pyEUVICS prediction:** result produced by a versioned configuration/result artifact with provenance.
- **External reference:** value or claim directly attributed to an authoritative citation.
- **Measurement:** result tied to identified data, calibration, uncertainty, and conditions.
- **TBD:** missing information with a named owner or resolution question.

Candidate statements in `tables/requirements_matrix.csv` are not requirements until their status is changed through project-owner approval and the decision log.

## Controlled scientific conventions

- Electron kinetic energy is `K_e`; total energy is `E_e = K_e + m_e c^2`. Tables may not use unlabeled “electron energy.”
- Collision angle is between electron and laser propagation vectors: 0 degrees is co-propagating and 180 degrees is head-on.
- Observation angle is measured from the electron propagation direction.
- Laser waist `w_0` is the 1/e² intensity radius unless an alternative is explicitly labeled.
- Every spatial, temporal, angular, energy, and spectral width states RMS or FWHM. For a Gaussian, `FWHM = 2 sqrt(2 ln 2) sigma`.
- Peak and average power are separately named, with the averaging interval or pulse train stated for average power.
- Spectral peak and centroid are separately defined and reported with the calculation/integration domain.
- Bandwidth states the spectral variable, RMS/FWHM convention, normalization, domain, and angular/spectral acceptance.
- Polarization states basis, propagation direction, handedness convention where applicable, and representation (Jones, Stokes, or degree of polarization).
- Every calculated result states model regime, recoil treatment, nonlinear parameter/model, polarization treatment, harmonic, aperture/acceptance, bandwidth convention, and provenance.
