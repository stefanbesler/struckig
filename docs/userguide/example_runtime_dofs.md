# Runtime-Selected DoFs Example

This setup is useful for machine variants where active axis count differs between deployments.

```st
PROGRAM Example05_RuntimeDofs
VAR CONSTANT
  ActiveDofs : UINT := 6; // runtime-selected size in this project variant
END_VAR
VAR
  otg : Struckig.Otg(cycletime := 0.01, dofs := ActiveDofs) := (
    EnableAutoPropagate := TRUE,
    CurrentPosition :=     [0.0,  -0.1, 0.12, 0.0,  0.3, 0.05],
    CurrentVelocity :=     [0.0,   0.0, 0.2,  0.0,  0.0, 0.0],
    CurrentAcceleration := [0.0,   0.0, 0.0,  0.0,  0.0, 0.0],
    TargetPosition :=      [1.0,   0.5, 0.5,  0.0, -0.1, 0.2],
    TargetVelocity :=      [0.0,   0.0, 0.0,  0.0,  0.0, 0.0],
    TargetAcceleration :=  [0.0,   0.0, 0.0,  0.0,  0.0, 0.0],
    MaxVelocity :=         [1.2,   1.2, 1.2,  0.6,  0.6, 0.6],
    MaxAcceleration :=     [4.0,   4.0, 4.0,  1.5,  1.5, 1.5],
    MaxJerk :=             [10.0, 10.0, 10.0, 4.0,  4.0, 4.0]
  );
END_VAR

otg();
```
