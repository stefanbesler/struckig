# Stop Trajectory Example

This pattern starts with a position trajectory and switches to velocity-interface stopping after a runtime condition.

```st
PROGRAM Example03_StopTrajectory
VAR
  otg : Struckig.Otg(cycletime := 0.01, dofs := 3) := (
    EnableAutoPropagate := TRUE,
    CurrentPosition :=     [0.0,  0.0,  0.5],
    CurrentVelocity :=     [0.0, -2.2, -0.5],
    CurrentAcceleration := [0.0,  2.5, -0.5],
    TargetPosition :=      [5.0, -2.0, -3.5],
    TargetVelocity :=      [0.0, -0.5, -2.0],
    TargetAcceleration :=  [0.0,  0.0,  0.5],
    MaxVelocity :=         [3.0,  1.0,  3.0],
    MaxAcceleration :=     [3.0,  2.0,  1.0],
    MaxJerk :=             [4.0,  3.0,  2.0]
  );
  elapsed : LREAL;
  onStopTrajectory : BOOL;
END_VAR

elapsed := elapsed + 0.01;

IF elapsed >= 1.0 AND_THEN NOT onStopTrajectory THEN
  onStopTrajectory := TRUE;
  otg.ControlInterface := Struckig.ControlInterfaceType.Velocity;
  otg.Synchronization := Struckig.SynchronizationType.None;
  otg.TargetVelocity := [0.0, 0.0, 0.0];
  otg.TargetAcceleration := [0.0, 0.0, 0.0];
  otg.MaxJerk := [12.0, 10.0, 8.0];
END_IF

otg();
```
