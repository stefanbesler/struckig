# Cycle Integration

This guide focuses on how to integrate Struckig into a PLC task loop safely and predictably.

## Recommended loop structure

Use a stable three-part cycle:

1. update targets and limits at well-defined step boundaries
2. call `otg()` exactly once per PLC cycle
3. map outputs to axis setpoints and handle state/errors

```st
// 1) Update targets on sequence events (not shown here)

// 2) Cyclic update
otg();

// 3) Output mapping and safety checks
IF otg.State = Struckig.TrajectoryState.Error THEN
  Abort(otg.ErrorMessage());
ELSE
  axisX.SetInterpolatedPosition(THIS^, otg.CurrentPosition[0]);
  axisY.SetInterpolatedPosition(THIS^, otg.CurrentPosition[1]);
  axisX.SetInterpolatedVelocity(THIS^, otg.CurrentVelocity[0]);
  axisY.SetInterpolatedVelocity(THIS^, otg.CurrentVelocity[1]);
END_IF
```

## Task cycle time

- Set `cycletime` to the real PLC task period in seconds.
- If task time changes dynamically, update `CycleTime` before running `otg()`.
- Keep jitter low in motion tasks to avoid setpoint quality degradation.

## State handling

Typical state flow:

- `Busy`: trajectory is active
- `Idle`: target reached within internal checks
- `Error`: invalid input or infeasible constraints

Use transitions on `Idle` to trigger the next machine step.

Important nuance:

- `Idle` means final target state is reached.
- If target velocity or acceleration is non-zero, physical movement can still be expected in downstream drive behavior even when the trajectory state is complete for the requested target.

## Target update timing

Do:

- write complete target vectors atomically at step entry
- reset current state only when starting a new independent segment

Avoid:

- partial per-element target updates across multiple cycles
- changing hard limits continuously unless this is a deliberate feature

## Input validation flow

Before applying new targets from external logic, validate input:

```st
IF NOT otg.ValidateInput(
  checkCurrentStateWithinLimits := FALSE,
  checkTargetStateWithinLimits := TRUE
) THEN
  Abort(otg.ErrorMessage());
END_IF
```

This catches invalid values earlier and gives better diagnostics than handling errors only after `otg()`.

## Multi-axis notes

- Keep all axis constraints in realistic mechanical range.
- Use `Phase` synchronization for coordinated path execution.
- Use `TimeSync` for simultaneous arrivals with less strict geometric coupling.
- Use `None` when independent axis completion is preferred, for example emergency deceleration behavior.

## Per-DoF runtime control

You can mix interfaces or synchronization modes per axis:

```st
otg.ControlInterface := Struckig.ControlInterfaceType.Position;
otg.PerDofControlInterface[1] := Struckig.ControlInterfaceType.Velocity;

otg.Synchronization := Struckig.SynchronizationType.TimeSync;
otg.PerDofSynchronization[2] := Struckig.SynchronizationType.None;
```

Use this carefully, as mixed policies can change trajectory shape and duration in non-obvious ways.

## Integration checklist

- `cycletime` matches task period
- consistent units across all vectors
- one `otg()` call per cycle
- explicit `Error` handling path
- axis outputs mapped every cycle
- `ValidateInput` is used at setpoint handover boundaries
