<div align="center">
  <h1 align="center">Struckig</h1>
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

This repository ports [pantor/ruckig](https://github.com/pantor/ruckig) to Structured Text to bring open-source powered Online-Trajectory-Generation to TwinCAT 3.
Only the Community Version of Ruckig is ported and pro features are not available. **Struckig itself is dual licenced, you can use the source code provided here accordingly to GPLv3. If you want to use this commercially and not disclose your own source code, Struckig is also available with a custom licence**. In the latter case, contact [me](mailto:stefan@besler.me).

# Porting progress and learnings

This project started on June 14, 2021 and I am happy to say that after 3 years of working on this project, it finally catched up to the HEAD of the C++ counterpart on May 15, 2024.

In hindsight, the hardest parts of the port were

- Porting mathematical functions from C++ to Structured Text such that the same accuracy is achieved: Functions like `cbrt` are not available in Structured Text out-of-the-box and the functionality had to be ported in a way that calculation have the exact same value in the port as C++ compilers do it. 
- Exception handling: While C++ allows control over how div0 exceptions are handled, this is not possible in Structured Text. While `ruckig` can just ignore div0 exceptions and then throw away calculations yielding NaN durations, this is not possible in Structured Text. This means that every calculation, which might produce a div0 exception have to be handled.

The original project, `ruckig` is a submodule of this repository and the hashes in "ported" commits reflect the state of the port. Future commits in the will be continuously ported over to Struckig when time sees fit.


# Continuous integration & Documentation

This project is using [zkbuild](https://github.com/Zeugwerk/zkbuild-action) for continuous integration and [zkdoc](https://github.com/Zeugwerk/zkdoc-action) for generating the [documentation](https://stefanbesler.github.io/Struckig/).
To run the tests manually, get a copy of [TcUnit](http://www.tcunit.org/) and activate the testing solution *test\Struckig\Struckig_unittest.sln*



# Example: Create time-based profile for 1 axis

This examples shows how to create a single-axis trajectory from point A=0mm to point B=100mm.
The initial state assumes that the trajectory is in stillstand and target velocity and acceleration is set to
0. The `MinDuration` parameter is set to `10s`. Please not that `MaxVelocity`, `MaxAcceleration` and `MaxJerk` would
allow for a shorter travel time, but  if `MinDuration` together with Synchronization = SynchronizationType.TimeSync is set,
the `MinDuration` parameter is considered instead.

If you only want to have a acceleration-constrained trajectory, you can also omit the `MaxJerk` 
as well as the CurrentAcceleration and TargetAcceleration value.

```
PROGRAM Example
VAR
  otg : Struckig.Otg(cycletime:=0.001, dofs:=1) := (
    EnableAutoPropagate := TRUE, //< Automatically copies the new trajectory state to the current trajectory state with every otg() call
    Synchronization :=     SynchronizationType.TimeSync, //< Set to TimeSync, otherwise MinDuration is ignored
    MinDuration :=         10.0, //< if MinDuration > 0 and Synchronization is set to TimeSync this sets the duration of the trajectory (if the other limitations would yields a shorter duration)
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
// axis.SetTargetPosition(otg.NewPosition[0]); send the new position to your axis, which should be in a cyclic position mode
// axis.SetVelocityOffset(otg.NewVelocity[0]); send the new velocity to your axis, e.g. with a velocity feedforward
// axis.SetTorqueOffset( accelerationTorqueFactor * otg.NewAcceleration[0]) send the new acceleration to your acces, e.g. with a current feedforward
```

![image](https://user-images.githubusercontent.com/11271989/129452181-57d28187-cafb-44be-b1ad-f73a5ed80556.png)

Note: Struckig supports motions with multiple degree of freedoms with the Otg function block. If you need to use only 1 degree of freedom you can also
utilize the specialized function block `Otg1`. The latter function block uses single variables instead of arrays, which simplifies the usage a bit.


# Examples

For more advanced examples, we created full applications, including a visualization. The source code of these examples can be found in the links below

- [Flying Saw](https://github.com/Zeugwerk/FlyingSaw-Example): Struckig is used to match speed with a conveyor, which is moving at a constant speed
- [Gear Synchronization][()](https://github.com/Zeugwerk/GearSim-Example): Struckig is used to thread-in and thread-out with one gear to another gear, which rotates at constant speed
- [XY Table](https://github.com/stefanbesler/XyTable-Example): This demo shows of phase-synchronization of two axes



