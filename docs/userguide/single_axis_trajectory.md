# Single axis trajectory

This example shows how to calculate a single axis with some kinematics and a minimum duration constraint

```
  otg : Struckig.Otg(cycletime:=0.001, dofs:=1) := (
          EnableAutoPropagate := TRUE,
          Synchronization := SynchronizationType.TimeSync, // one axis -> no synchronistation is required
          MinDuration := 10.0, // if MinDuration is set to a value > 0 it is considered in trajectory calculation
          MaxVelocity := [ 2000.0 ],
          MaxAcceleration := [ 20000.0 ],
          MaxJerk := [ 800000.0 ],
          CurrentPosition := [ 0 ],
          CurrentVelocity := [ 0 ],
          CurrentAcceleration := [ 0 ],
          TargetPosition := [ 100 ],
          TargetVelocity := [ 0.0, 0.0, 0.0 ],
          TargetAcceleration := [ 0.0, 0.0, 0.0 ]
  );
```

<div class="gallery">
  <div class="gallery-item">
    <figure>
      <img src="../images/single_axis_trajectory.png" alt="Visualization overview"/>
    </figure>
  </div>
</div>