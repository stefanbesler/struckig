# FAQ

## Do I need to call `otg()` every cycle?

Yes. Struckig is designed for cyclic execution. Skipping calls leads to discontinuous setpoints and poor motion quality.

## Should I always use `EnableAutoPropagate := TRUE`?

For normal online use, yes. It is the default workflow and keeps `Current*` aligned with generated `New*` values.

Use manual propagation only when you explicitly need custom stepping behavior.

## Why do I get `TrajectoryState.Error`?

Most errors are input-related:

- invalid values (NaN or negative limits)
- target kinematics outside configured constraints
- zero-limit conflicts in constrained/synchronized cases

Check both `ErrorCode()` and `ErrorMessage()`.

## What is the best synchronization mode?

- `TimeSync` for shared arrival time
- `Phase` for coordinated path progression
- `None` for independent axis timing

There is no universal best mode. Select based on machine behavior.

## Why does `ValidateInput` pass but runtime still fails?

Inputs may change between validation and execution, or external logic may write invalid values later in the cycle. Keep validation and `otg()` close in deterministic code.

## Can I mix control interfaces per axis?

Yes, with `PerDofControlInterface`. Do this only when required, since mixed-interface trajectories are harder to reason about during maintenance.

## Does `MinDuration` always extend the move?

No. It only affects trajectories that would otherwise finish earlier than the specified minimum.

## Why does motion feel rough near limits?

Usually jerk or acceleration is too high for the mechanical system. Reduce `MaxJerk` first, then reevaluate `MaxAcceleration`.

## Should I use `Continuous` or `Discrete` discretization?

For PLC cycle-oriented control, `Discrete` is often easier to integrate and reason about. `Continuous` can be useful when strict cycle quantization is not required.
