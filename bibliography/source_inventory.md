# Source inventory

Last verification date: 2026-07-29. Bibliography keys refer to `references.bib`.

| Key | Evidence area | Source type | Verification point | Intended use | Limits |
|---|---|---|---|---|---|
| `SunWu2011ComptonSource` | ICS kinematics and source modeling | Peer-reviewed primary/modeling paper | APS DOI and Duke publication record | Dependence of spectrum and yield on electron, laser, geometry, and collimation inputs | Gamma-ray cases; equations and assumptions must be checked before transfer to EUV parameters |
| `KrafftEtAl2005NonlinearThomson` | Nonlinear Thomson scattering | Peer-reviewed theory paper | APS DOI and PubMed record | Pulsed-laser treatment and general geometry | Classical/Thomson regime; not a substitute for recoil treatment |
| `HartemannWu2013Brightness` | Nonlinear Compton broadening | Peer-reviewed theory paper | APS DOI and accepted manuscript | Ponderomotive broadening and optimization dependencies | No EUVICS performance inference without matched inputs |
| `ArnoldTeichert2011SRFPhotoinjectors` | SRF photoinjectors | Peer-reviewed review | APS journal record | Technology classes, implementation issues, reported experiments | Review-era state; does not select an EUVICS injector |
| `PetrushinaEtAl2020SRFGun` | SRF photoinjector experiment | Peer-reviewed primary experiment | APS DOI/journal record | Example measured CW SRF-gun performance | Facility-specific; performance cannot be assigned to EUVICS |
| `CiovatiEtAl2018LowEnergySRFLinac` | Low-energy SRF linac | Peer-reviewed design paper | APS/OSTI DOI and report number | Example subsystem design methodology and interfaces | Different application and operating point; no cost/performance transfer |
| `FilippettoEtAl2022UED` | Lasers, synchronization, diagnostics | Peer-reviewed review | APS DOI and review contents | Laser-to-RF synchronization, time stamping, electron diagnostics | UED context; EUVICS tolerances remain TBD |
| `VanDenBoogaardEtAl2012EUVMirror` | EUV optics | Peer-reviewed primary experiment | Optica DOI/publisher record | Example 13.5 nm multilayer-grating measurement and spectral filtering | Sample- and geometry-specific result |
| `NISTEUVDetectorCalibration` | EUV radiometry | Authoritative metrology service | NIST page, accessed 2026-07-29 | Traceable detector/instrument calibration context | Service range is not a detector specification for EUVICS |
| `IAEA2010SSG8` | Accelerator radiation safety | Authoritative safety guide | IAEA publication record | Safety-program and engineered-control methodology | Local law, dose criteria, shielding design, and applicability require qualified review |
| `YokoyaCAINManual` | CAIN simulation | Author-issued software manual | CERN-hosted manual identifying KEK distribution | Inputs, capabilities, and version reporting | No CAIN agreement claim; EUVICS version/configuration is TBD |
| `pyEUVICSConventions050` | EUVICS model conventions | Approved pyEUVICS 0.5.0 science documentation | Public-content allowlist at locked commit `6193ab3e...` | Kinetic-energy, collision-angle, observation-angle, wavelength, and default-model conventions | Documents implemented package conventions; scientific approval of an EUVICS design configuration remains separate |
| `pyEUVICSEquations050` | Exact linear ICS kinematics | Approved pyEUVICS 0.5.0 science documentation and tested implementation | Equation and recoil denominator checked against the locked documentation and `kinematics.py` tests | Exact coplanar linear Compton relation and Thomson limit | Free-electron, single-photon, coplanar model; nonlinear effects are separate |
| `pyEUVICSModels050` | Nonlinear, spectrum, yield, and workflow models | Approved pyEUVICS 0.5.0 science/workflow documentation | Public-content allowlist at locked commit `6193ab3e...` | Model scope, beam-width conventions, dependencies, provenance, and limitations | Approximate models do not constitute facility validation; harmonic locations are not relative yields |
| `pyEUVICSInstrumentation050` | Optical transport and detector response | Approved pyEUVICS 0.5.0 instrumentation documentation | Public-content allowlist at locked commit `6193ab3e...` | Staged throughput, incidence-angle conventions, and photodiode interpretation | Requires configuration-specific efficiency/responsivity provenance; nondispersive detection does not measure wavelength directly |
| `pyEUVICSValidation050` | Reference-campaign validation status | Approved pyEUVICS 0.5.0 validation documentation | Public-content allowlist at locked commit `6193ab3e...` | Preserve CAIN disagreement, 13.5 nm provisional status, and synthetic-calibration boundary | Numerical target matching is not independent experimental validation |

## Source gaps

The current inventory does not establish EUVICS-specific performance, component specifications, technology readiness, costs, schedule, partners, approvals, application requirements, or safety acceptance. Those require project artifacts or additional authoritative sources listed in `reviews/missing_evidence.md`.

## Section source plan

| Document area | Evidence required before review-ready claims | Current coverage | Next action |
|---|---|---|---|
| Need and application context | Sponsor requirements and primary application metrics | General NIST metrology context only | Close `ME-001` |
| ICS physics and performance | Governing theory plus versioned EUVICS calculations | General theory/modeling sources present | Close `ME-002`; execute M4 |
| Comparison with other sources | Matched primary measurements and normalized definitions | None; inherited comparison removed | Close `ME-003` |
| Injector | Selected design artifacts and applicable component/experimental evidence | Review and external example present | Close `ME-004` |
| Linac and transport | Lattice, RF, cryogenic, errors, losses, interfaces, verification | External methodology example present | Close `ME-005` |
| Laser and synchronization | Architecture, measured pulse/timing capability, calibration | General review present | Close `ME-006` |
| Interaction region | Geometry, overlap/acceptance model, diagnostics, uncertainties | General theory and diagnostics context present | Close `ME-002` and `ME-006` |
| EUV optics and diagnostics | Selected-component data, optical/radiometric budgets, calibrations | General optics experiment and NIST service present | Close `ME-007` |
| Controls and data | Architecture, interface control, provenance and verification artifacts | No project evidence | Close `ME-006` and define controls artifacts |
| Safety and shielding | Local requirements, source terms, qualified calculations and review | IAEA methodology present | Close `ME-009` |
| Cost, schedule, readiness, and partners | Controlled project records and approvals | None; unsupported prose removed | Close `ME-010` through `ME-012` |
| CAIN comparison | Versioned matched input/output package | Manual only | Close `ME-008` |
