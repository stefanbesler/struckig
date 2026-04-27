# Minimum Duration Example

Use this when process timing requires a slower trajectory than the kinematic limits would naturally produce.

```st
PROGRAM Example04_MinimumDuration
VAR
  otg : Struckig.Otg(cycletime := 0.01, dofs := 3) := (
    EnableAutoPropagate := TRUE,
    Synchronization := Struckig.SynchronizationType.TimeSync,
    MinDuration := 5.0,
    CurrentPosition :=     [0.0,  0.0,  0.5],
    CurrentVelocity :=     [0.0, -2.2, -0.5],
    CurrentAcceleration := [0.0,  2.5, -0.5],
    TargetPosition :=      [-5.0, -2.0, -3.5],
    TargetVelocity :=      [ 0.0, -0.5, -2.0],
    TargetAcceleration :=  [ 0.0,  0.0,  0.5],
    MaxVelocity :=         [3.0,  1.0,  3.0],
    MaxAcceleration :=     [3.0,  2.0,  1.0],
    MaxJerk :=             [4.0,  3.0,  2.0]
  );
END_VAR

otg();
```
