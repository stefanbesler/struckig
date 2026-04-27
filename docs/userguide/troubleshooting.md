# Troubleshooting

Common issues when integrating Struckig in PLC projects.

## `TrajectoryState.Error` right after start

Likely causes:

- negative or zero limits where positive limits are required
- inconsistent vector size for configured DoFs
- impossible target state for active constraints

What to check:

- all `Max*` limits are sensible and positive
- each array has exactly `dofs` entries
- current and target state values are in consistent units
- inspect `ErrorCode()` in addition to `ErrorMessage()`

## `Zero limits conflict` errors

Likely causes:

- one or more axes use zero acceleration or jerk limits while target states still require constrained motion
- synchronization forces coupling with another DoF that cannot satisfy zero-limit constraints

What to check:

- avoid mixing zero limits with aggressive target velocity/acceleration requests
- test with `SynchronizationType.None` to isolate per-axis feasibility
- reintroduce synchronization after each axis is individually valid

## Motion looks too slow or too fast

Likely causes:

- `cycletime` does not match actual task period
- unit mismatch (`mm` vs `m`, `deg` vs `rad`)

What to check:

- task period in TwinCAT and `cycletime` are equal
- velocity, acceleration, jerk are scaled to your position unit

## Never reaches `Idle`

Likely causes:

- target is overwritten each cycle by other logic
- external sequence logic modifies `Current*` continuously

What to check:

- write targets at state boundaries, not continuously
- avoid changing `CurrentPosition/Velocity/Acceleration` during active segments unless intentional
- verify whether target velocity or target acceleration is intentionally non-zero

## Axis movement is jerky

Likely causes:

- jerk limits too high for mechanics
- output updates are not applied every cycle
- drive interpolation mode mismatch

What to check:

- reduce `MaxJerk` and test again
- ensure cyclic setpoint mapping runs unconditionally
- validate axis mode and interpolation settings
- consider `DiscretizationType.Discrete` for cycle-aligned durations

## Unexpected path shape in multi-axis motion

Likely causes:

- synchronization mode does not match path intent
- constraints differ strongly between axes

What to check:

- try `SynchronizationType.Phase` for geometric path consistency
- align relative limits between axes where possible
- avoid partial per-DoF overrides unless required

## Validation passes, but runtime still errors

Likely causes:

- parameters changed between `ValidateInput` and `otg()` call
- external logic writes NaN or invalid numbers during runtime

What to check:

- keep setpoint update and `otg()` call in the same deterministic code region
- guard external writes and sanitize values
- log parameter snapshots on transition edges

## Diagnostic workflow

1. log `State` and `ErrorMessage()` when errors occur
2. log current and target vectors at segment entry
3. verify cycle time, units, and limit ranges
4. reduce complexity to a 1-axis move, then scale back up
