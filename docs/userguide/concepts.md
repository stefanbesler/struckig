# Concepts

This page summarizes the core motion concepts used by Struckig.

## Online trajectory generation

Struckig computes a valid next motion state every PLC cycle from:

- current position, velocity, acceleration
- target position, velocity, acceleration
- kinematic limits (velocity, acceleration, jerk)

The function block is called cyclically and produces updated values (`New*` outputs, plus propagated `Current*` when enabled).

## Control interfaces

Struckig supports different control interfaces depending on the machine behavior you need:

- `Position`: full state-to-state motion planning
- `Velocity`: velocity-profile-centric behavior, useful for controlled stopping or drive-level velocity control loops

In most point-to-point applications, start with `Position`.

Important behavior:

- In `Velocity` interface, position limits are not the primary driver of trajectory generation.
- `Velocity` interface is well suited for controlled stop logic and velocity-profile transitions.

## Synchronization modes

For multi-axis trajectories, synchronization mode defines how axes coordinate:

- `TimeSync`: all axes finish together in time
- `TimeIfNecessarySync`: synchronize only when needed for target kinematics
- `Phase`: all axes evolve with coordinated phase progression
- `None`: each DoF is calculated independently

`Phase` is often preferred for XY path-following motion.

## Motion order

- Third-order (jerk-limited): set `MaxJerk`
- Second-order (acceleration-limited): leave jerk unconstrained

Jerk-limited motion is typically smoother for mechanics and process quality.

## Discretization

Struckig supports two discretization modes:

- `Continuous`: trajectory duration can take any value
- `Discrete`: synchronized duration is aligned to task-cycle multiples

For PLC command generation, `Discrete` often gives more predictable setpoint handover at cycle boundaries.

## Propagation model

With `EnableAutoPropagate := TRUE`, each cycle automatically uses the newly generated state as the next cycle's current state. This is the default online operation mode.

Set it to `FALSE` only when you need manual propagation control for offline or custom stepping scenarios.

Manual propagation is done with `PassOutputToInput()`.

## Enabled DoFs and per-DoF overrides

Struckig supports per-axis control for complex machines:

- `Enabled[i]` lets you disable specific DoFs in a calculation cycle
- `PerDofControlInterface[i]` can override global control interface
- `PerDofSynchronization[i]` can override global synchronization mode

If a per-DoF override is set to `Undefined`, the global setting is used.

## States and error codes

At runtime, use both state and error methods:

- `State`: `Busy`, `Idle`, or `Error`
- `ErrorCode()`: machine-readable failure category
- `ErrorMessage()`: human-readable reason

Frequent error classes include invalid input values and zero-limits conflicts.

## Units and consistency

Struckig is unit-agnostic, but units must remain consistent per axis:

- position: `mm`, `deg`, or similar
- velocity: position unit per second
- acceleration: position unit per second squared
- jerk: position unit per second cubed

Mixing inconsistent units is one of the most common causes of unstable behavior.
