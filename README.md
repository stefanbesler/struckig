!! *WARNING: THIS IS NOT READY TO USE YET* !!

<div align="center">
  <h1 align="center">(ST)Ruckig</h1>
  <h3 align="center">
    Online Trajectory Generation. Real-time. Jerk-constrained. Time-optimal<br/>
    "Full" port from C++ to Structured Text, TwinCAT 3.
  </h3>
</div>

<p align="center">
  <a href="https://github.com/stefanbesler/ruckig/actions">
    <img src="https://github.com/stefanbesler/ruckig/workflows/CI/badge.svg" alt="CI">
  </a>
  <a href="https://github.com/stefanbesler/ruckig/issues">
    <img src="https://img.shields.io/github/issues/stefanbesler/ruckig.svg" alt="Issues">
  </a>
  <a href="https://github.com/stefanbesler/ruckig/releases">
    <img src="https://img.shields.io/github/v/release/stefanbesler/ruckig.svg?include_prereleases&sort=semver" alt="Releases">
  </a>

  <a href="https://github.com/stefanbesler/ruckig/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="MIT">
  </a>
</p>

This repository aims to port [pantor/ruckig](https://github.com/pantor/ruckig) to Structured Text to bring open-source powered Online
Trajectory Generation to TwinCAT 3. Please note, that while this port aims to be a full port, it will probably never reach the performance 
of the original C++ code for the following reasons. 
- the original code uses templates and C++17 features to reduce load during runtime. 
- the codesys compiler , in contrast to C++ compilers, does not come with a lot of compile time optimizations. Even simple loop unwrapping optimizations are not performed - probably to make debugging easier (?)
- while some optimizations could be done by hand, I would rather have the port as close to the original as possible, only changing the architecture where it is required, because of limitiations of the programming language of the port.

If you are looking for best possible performance of Ruckig, I suggest you look into making pantor/ruckig a TwinCAT C++ module. However,
if you would like to use a library that is implemented in a IEC 61131-3 conform language, this port of pantor/ruckig might be for you.

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
    - [ ] otg-benchmark.cpp - implement test to check for regressions and test overall performance on codesys compiler 
    - [x] run unit tests to find more issues that sneaked in while porting
- [ ] The original code is rather functional, which TwinCAT ST doesn't benefit from a lot, rewrite to OOP where needed
- [ ] Refactor (coding conventions)
- [ ] Code cleanup and optimize performance, some parts have to be change to be faster in twincat, we do not have the power of a cpp compiler
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

The source code and usage documentation of this library is (will be) hosted on [https://stefanbesler.github.io/struckig/](https://stefanbesler.github.io/struckig/). Kudos again to [@Zeugwerk](https://github.com/Zeugwerk) for letting me beta test their TwinCAT documentation generation, which is still in alpha phase.

# Example: Create time-based profile for 1 axis

This examples shows how to create a single-axis trajectory from point A=0mm to point B=100mm.
The initial state assumes that the trajectory is in stillstand and target velocity and acceleration is set to
0. The `MinDuration` parameter is set to `10s`. Please not that `MaxVelocity`, `MaxAcceleration` and `MaxJerk` would
allow for a shorter travel time, but  if `MinDuration` together with Synchronization = SynchronizationType.TimeSync is set,
the `MinDuration` parameter is considered instead.

```
PROGRAM Example05_1DoFs_MinDuration
VAR
  ruckig : Struckig.Ruckig(0.001);
  input : Struckig.InputParameter(1) := (
    Synchronization := SynchronizationType.TimeSync, // Set to TimeSync, otherwise MinDuration is ignored
    MinDuration :=         10.0, // if MinDuration is set to a value > 0 it is considered in trajectory calculation
    MaxVelocity :=         [ 2000.0 ],
    MaxAcceleration :=     [ 20000.0 ],
    MaxJerk :=             [ 800000.0 ],
    CurrentPosition :=     [ 0 ],
    CurrentVelocity :=     [ 0 ],
    CurrentAcceleration := [ 0 ],
    TargetPosition :=      [ 100 ],
    TargetVelocity :=      [ 0.0 ],
    TargetAcceleration :=  [ 0.0 ]
  );
  output : Struckig.OutputParameter;
END_VAR

// =====================================================================================================================

state := ruckig.update(input, output);

// Update the current values, these should be send to a drive as well
// so that it can follow the trajectory.
input.CurrentPosition := output.NewPosition;
input.CurrentVelocity := output.NewVelocity;
input.CurrentAcceleration := output.NewAcceleration;

moving := state = TrajectoryState.Busy;
```

![image](https://user-images.githubusercontent.com/11271989/129452181-57d28187-cafb-44be-b1ad-f73a5ed80556.png)



# Example: Create a two-step profile for 1 axis

The following (advanced) examples shows how to use (st)ruckig to calculate a 2-step positioning profile for a single axis.
 - The first step moves the axis from a start position (47mm) to a target position (18mm) with a *high* velocity and an end-velocity of -50mm/s.
 - From that point the profile is *switched* such that the axis continues to moves "slowly" (speed: 50mm/s) to its final destination (9mm) 
   where the axis stops moving.
```

PROGRAM Example02_PositionProfile_2Steps
VAR
  ruckig : Ruckig(0.001);
  input_step1 : InputParameter(1) := (synchronizationType := SynchronizationTypeEnum.none,
                                      max_velocity :=         [ 1200.0 ],
                                      max_acceleration :=     [ 25000.0 ],
                                      max_jerk :=             [ 25000.0 / 0.008 ], // ~ s-time = 8ms
                                      current_position :=     [ 47.0 ],
                                      current_velocity :=     [ 0.0 ],
                                      current_acceleration := [ 0.0 ],
                                      target_position :=      [ 18.0 ],
                                      target_velocity :=      [ -50.0 ],
                                      target_acceleration :=  [ 0.0 ]);
  input_step2 : InputParameter(1) := (max_velocity :=         [ 50.0 ], // limit velocity to end-velocity of first step
                                      target_position :=      [ 9.0 ],
                                      target_velocity :=      [ 0.0 ],
                                      target_acceleration :=  [ 0.0 ]);
  input : REFERENCE TO InputParameter REF= input_step1;                                    
  output : OutputParameter;    
  run : BOOL;
  switched : BOOL;
END_VAR

// =====================================================================================================================

IF run
THEN
  ruckig.update(input, output);
  
  // switch to second profile
  IF NOT ruckig.isBusy() AND_THEN NOT switched
  THEN
    switched := TRUE;
    input.max_velocity := input_step2.max_velocity;    
    input.target_position := input_step2.target_position;
    input.target_velocity := input_step2.target_velocity;    
    input.target_acceleration := input_step2.target_acceleration;
  END_IF
  
  input.current_position := output.new_position;
  input.current_velocity := output.new_velocity;
  input.current_acceleration := output.new_acceleration;
END_IF
```

![image](https://user-images.githubusercontent.com/11271989/126785368-205a491b-0acb-4a52-8b90-a6e3f1283a18.png)

