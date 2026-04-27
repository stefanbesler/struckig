# Velocity Interface Example

Use this when your application is primarily velocity driven, such as controlled deceleration behavior.

```st
PROGRAM Example02_Velocity
VAR
  otg : Struckig.Otg(cycletime := 0.01, dofs := 3) := (
    EnableAutoPropagate := TRUE,
    ControlInterface := Struckig.ControlInterfaceType.Velocity,
    CurrentPosition :=     [0.0,  0.0,  0.5],
    CurrentVelocity :=     [3.0, -2.2, -0.5],
    CurrentAcceleration := [0.0,  2.5, -0.5],
    TargetVelocity :=      [0.0, -0.5, -1.5],
    TargetAcceleration :=  [0.0,  0.0,  0.5],
    MaxAcceleration :=     [3.0,  2.0,  1.0],
    MaxJerk :=             [6.0,  6.0,  4.0]
  );
END_VAR

otg();
```
