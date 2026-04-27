# Feature Scope

This page clarifies which concepts are relevant for Struckig users and how to interpret them in PLC projects.

## What Struckig focuses on

Struckig is centered on real-time, cycle-based trajectory generation in Structured Text:

- point-to-point motion from current state to target state
- velocity, acceleration, and jerk constrained planning
- single-axis and multi-axis synchronization strategies
- deterministic cyclic integration through `Struckig.Otg`

## What to expect in this user guide

This guide emphasizes:

- practical setup and commissioning
- integration patterns in PLC cycle logic
- troubleshooting with `State`, `ErrorCode()`, and `ErrorMessage()`
- code snippets that are directly usable in Structured Text

## Scope notes for advanced topics

Some concepts in broader Ruckig material are not central for this Struckig user guide:

- offline-only workflows that bypass cyclic PLC update patterns
- features that depend on APIs not commonly used in day-to-day PLC control loops

When in doubt, follow the examples in `Examples` and `Cycle Integration` first, then expand.

## Community baseline

The terminology and behavior are aligned with the open-source Ruckig community model where applicable. Struckig exposes this in an IEC 61131-3 Structured Text form for PLC usage.

## Struckig-specific features

Struckig is not only a passive port. It can introduce PLC-focused features that are not part of upstream Ruckig when they provide clear value for industrial applications.

One planned example is `SmoothBrake`:

- purpose: provide a smoother, safer braking behavior profile for machine-integrated stop scenarios
- status model: introduced as an opt-in extension, not silently changing default trajectory behavior
- compatibility goal: keep default behavior aligned with the known Ruckig baseline

## Feature flags and rollout model

Struckig-specific features are intended to be exposed via feature flags:

- default: off, to preserve predictable baseline behavior
- opt-in: enabled explicitly at project level
- migration-friendly: allows validating advanced behavior per machine before broad rollout

This model lets teams adopt new behavior incrementally while keeping deterministic, auditable motion behavior in production.

## Practical recommendation

For maintainable projects, keep application code structured in layers:

1. motion planning (`Struckig.Otg` inputs and outputs)
2. sequence logic (state machine decisions)
3. drive interface mapping (setpoint transfer)
4. safety and limit supervision

This separation makes tuning, debugging, and audits much easier.
