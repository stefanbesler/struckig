<div align="center">
  <h1 align="center">(ST)Ruckig</h1>
  <h3 align="center">
    Instantaneous Motion Generation for Robots and Machines.<br>
    Port of ruckig to Structured Text, TwinCAT 3.
  </h3>
</div>

<p align="center">
  <a href="https://github.com/stefanbesler/struckig/actions">
    <img src="https://github.com/stefanbesler/struckig/actions/workflows/build.yml/badge.svg" alt="Build/Test">
  </a>
  <a href="https://stefanbesler.github.io/struckig/struckig/Constants.html">
    <img src="https://github.com/stefanbesler/struckig/actions/workflows/documentation.yml/badge.svg" alt="Documentation">
  </a>  
  <a href="https://github.com/stefanbesler/struckig/issues">
    <img src="https://img.shields.io/github/issues/stefanbesler/struckig.svg" alt="Issues">
  </a>
  <a href="https://github.com/stefanbesler/struckig/releases">
    <img src="https://img.shields.io/github/v/release/stefanbesler/ruckig.svg?include_prereleases&sort=semver" alt="Releases">
  </a>

  <a href="https://github.com/stefanbesler/struckig/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="MIT">
  </a>
</p>

This repository ports [pantor/ruckig](https://github.com/pantor/ruckig) to Structured Text to bring open-source powered Online-Trajectory-Generation to TwinCAT 3.
I am developing and maintaining this port in my spare time and have no interest in making this a commercial product. So, only the Community Version is ported
and pro features are not available.
Anyway, if you want to motivate, donate a coffee and star this repository.

<p align="center">
  <a href="https://www.paypal.com/donate?hosted_button_id=PWRUSMDGJNQ2A"><img alt="Donate" src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" /></a>
</p>

# Porting progress

The original project, `ruckig` is a submodule of this repository. The commit-hash reflects the commits that are ported already - I try to keep up with changes that are done in `ruckig`.

- [x] Crude initial port of source code
- [x] Check source code for obvious copy & paste errors that may have occured during the port
- [x] Manual testing
- [x] Initial commit
- [x] Implement unit tests with TcUnit-Runner or use TcUnit-Wrapper to put aside this dependency
    - [x] KnownExamples (otg-test.cpp)
    - [x] SecondaryFeatures (otg-test.cpp)
    - [x] Randomized trajectories (~otg-test.cpp) implemented python script that generates radomized Unittests to compare the cpp implementaion with the port
    - [x] otg-benchmark.cpp - implement test to check for regressions and test overall performance on codesys compiler 
    - [x] run unit tests to find more issues that sneaked in while porting
- [x] The original code is rather functional, which TwinCAT ST doesn't benefit from a lot, rewrite to OOP where needed
- [x] Refactor (coding conventions)
- [x] Code cleanup and optimize performance, some parts have to be change to be faster in twincat, we do not have the power of a cpp compiler
- [x] CI - using [Zeugwerk](http://zeugwerk.at) tool chain paired with GitHub actions for continuous integration
- [x] Examples
  - [x] Position.cpp
- [ ] Documentation - gh-pages generated from CI

# Unittests

This project uses [TcUnit](http://www.tcunit.org/) for unittesting. Since the library is a standalone PLC project, unittests are implemented in a different solution (subfolder `./Struckig_unittest`) than the library. In order to execute the unittests the `Struckig` library has to be [saved and installed](https://infosys.beckhoff.com/english.php?content=../content/1033/tc3_plc_intro/4189307403.html&id=) and `TcUnit.library` has to be [downloaded](https://github.com/tcunit/TcUnit/releases) and [installed](https://infosys.beckhoff.com/english.php?content=../content/1033/tc3_plc_intro/4189333259.html&id=).

Please note, that not all unittests from the [original](https://www.github.com/pantor/ruckig) source code are ported yet, but only the `KnownExamples` and `SecondaryFeatures` tests.

# Continuous integration

Continuous integration has not really arrived in Operational technology (OT) -- yet. Some colleguages from work are making good progress in implementing buildtools and preparing a CI/CD environment for TwinCAT that will be publically available. Luckily, they agreed with me to let me try their tools as an
alpha/beta tester with this project. For more information on this topic, please contact [Zeugwerk](mailto:info@zeugwerk.at); In the meantime I
thank [@Zeugwerk](https://github.com/Zeugwerk) for letting me use their build environment in this early development stage of their DevOps tools.

# Documentation

The source code and usage documentation of this library is hosted on [https://stefanbesler.github.io/struckig/](https://stefanbesler.github.io/struckig/). Kudos again to [@Zeugwerk](https://github.com/Zeugwerk) for letting me beta test their TwinCAT documentation generation, which is still in alpha phase.

# Example: Create time-based profile for 1 axis

This examples shows how to create a single-axis trajectory from point A=0mm to point B=100mm.
The initial state assumes that the trajectory is in stillstand and target velocity and acceleration is set to
0. The `MinDuration` parameter is set to `10s`. Please not that `MaxVelocity`, `MaxAcceleration` and `MaxJerk` would
allow for a shorter travel time, but  if `MinDuration` together with Synchronization = SynchronizationType.TimeSync is set,
the `MinDuration` parameter is considered instead.

```
PROGRAM Example
VAR
  otg : Struckig.Ruckig(deltaTime:=0.001, dofs:=1) := (
    Synchronization := SynchronizationType.TimeSync, // Set to TimeSync, otherwise MinDuration is ignored
    MinDuration :=         10.0, // if MinDuration is set to a value > 0 it is considered in trajectory calculation
    MaxVelocity :=         [ 2000.0 ],
    MaxAcceleration :=     [ 20000.0 ],
    MaxJerk :=             [ 800000.0 ],
    CurrentPosition :=     [ 0.0 ],
    CurrentVelocity :=     [ 0.0 ],
    CurrentAcceleration := [ 0.0 ],
    TargetPosition :=      [ 100.0 ],
    TargetVelocity :=      [ 0.0 ],
    TargetAcceleration :=  [ 0.0 ]
  );
END_VAR

// =====================================================================================================================

otg();

// Update the current values, these should be send to a drive as well
// so that it can follow the trajectory.
otg.CurrentPosition := otg.NewPosition;
otg.CurrentVelocity := otg.NewVelocity;
otg.CurrentAcceleration := otg.NewAcceleration;
```

![image](https://user-images.githubusercontent.com/11271989/129452181-57d28187-cafb-44be-b1ad-f73a5ed80556.png)
