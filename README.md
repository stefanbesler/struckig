<div align="center">
  <img src="docs/images/struckig-logo-readme.svg" alt="Struckig logo" width="260">
  <h3 align="center">
    Instantaneous Motion Generation for Robots and Machines.<br>
    Port of ruckig to Structured Text, TwinCAT 3.
  </h3>
</div>

<p align="center">
  <a href="https://github.com/stefanbesler/struckig/actions">
    <img src="https://github.com/stefanbesler/struckig/actions/workflows/build.yml/badge.svg" alt="Build/Test">
  </a>
  <a href="https://stefanbesler.github.io/struckig/Struckig/Constants.html">
    <img src="https://github.com/stefanbesler/struckig/actions/workflows/documentation.yml/badge.svg" alt="Documentation">
  </a>  
  <a href="https://github.com/stefanbesler/struckig/issues">
    <img src="https://img.shields.io/github/issues/stefanbesler/Struckig.svg" alt="Issues">
  </a>
  <a href="https://github.com/stefanbesler/struckig/releases">
    <img src="https://img.shields.io/github/v/release/stefanbesler/struckig.svg?include_prereleases&sort=semver" alt="Releases">
  </a>
  <a href="https://www.gnu.org/licenses/gpl-3.0.en.html">
    <img src="https://img.shields.io/badge/license-GPLv3-green.svg" alt="GPLv3">
  </a>
</p>

Struckig ports [pantor/ruckig](https://github.com/pantor/ruckig) to Structured Text and brings open-source online trajectory generation to TwinCAT 3.
It targets deterministic PLC task loops and multi-axis synchronization in machine control scenarios.

Only the Community Version of Ruckig is ported and pro features are not available.
Struckig is dual licensed:

- GPLv3 for open-source usage
- commercial custom license for closed-source usage (contact [stefan@besler.me](mailto:stefan@besler.me))

## Documentation

- Full docs: [stefanbesler.github.io/struckig](https://stefanbesler.github.io/struckig/)
- Installation guide: [User guide installation](https://stefanbesler.github.io/struckig/userguide/installation.html)
- API reference: [API Reference](https://stefanbesler.github.io/struckig/api/Struckig.html)

## Installation

1. Download the latest release from [Releases](https://github.com/stefanbesler/struckig/releases).
2. Add the library to your TwinCAT project.
3. Instantiate `Struckig.Otg` and call `otg()` once per PLC cycle.

For screenshots and TwinCAT step-by-step instructions, use the [installation docs](https://stefanbesler.github.io/struckig/userguide/installation.html).

## Quick example (single axis)

```st
PROGRAM Example
VAR
  otg : Struckig.Otg(cycletime:=0.001, dofs:=1) := (
    EnableAutoPropagate := TRUE,
    Synchronization := SynchronizationType.TimeSync,
    MinDuration := 10.0,
    MaxVelocity := [2000.0],
    MaxAcceleration := [20000.0],
    MaxJerk := [800000.0],
    CurrentPosition := [0.0],
    CurrentVelocity := [0.0],
    CurrentAcceleration := [0.0],
    TargetPosition := [100.0],
    TargetVelocity := [0.0],
    TargetAcceleration := [0.0]
  );
END_VAR

otg();
```

Map `otg.NewPosition`, `otg.NewVelocity`, and optionally `otg.NewAcceleration` to your axis interface each cycle.

## Extra features

- While the port stays close to upstream, additional behavior can be enabled via feature flags on `Otg` or globally in library parameters.

| Flag | Description |
|------|-------------|
| `SmoothBrake` | In ruckig, reducing `MaxVelocity` below the current velocity triggers a brake ramp to `velocity = 0` before transitioning to the new limit. Enable this flag to bypass that behavior and switch to the new `MaxVelocity` immediately. |

## Development

- CI uses [zkbuild](https://github.com/Zeugwerk/zkbuild-action)
- Docs generation uses [zkdoc](https://github.com/Zeugwerk/zkdoc-action)
- Unit tests can be run with [TcUnit](http://www.tcunit.org/) via `test\Struckig\Struckig_unittest.sln`
