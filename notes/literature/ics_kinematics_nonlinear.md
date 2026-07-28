# ICS and nonlinear ICS kinematics

## Sources reviewed

- `SunWu2011ComptonSource` — peer-reviewed analytical and Monte Carlo treatment.
- `KrafftEtAl2005NonlinearThomson` — peer-reviewed classical nonlinear treatment for pulsed lasers and general geometries.
- `HartemannWu2013Brightness` — peer-reviewed analysis of nonlinear ponderomotive broadening and brightness optimization.

## Supported paraphrase

Compton-source spectra and angular distributions depend on electron and laser
parameters, collision/observation geometry, polarization treatment, collimation,
and the selected recoil/nonlinear model. Pulsed high-intensity fields can introduce
nonlinear spectral structure or broadening.

## EUVICS inference and limits

These sources justify tracking the dependencies; they do not predict EUVICS
output. A project inference requires a versioned pyEUVICS configuration with
explicit energy, angle, waist, width, polarization, recoil, harmonic, and
acceptance conventions. Classical Thomson and recoil-aware Compton results must
not be mixed without a documented approximation check.

Quotation status: no quotation used.
