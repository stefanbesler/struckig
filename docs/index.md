---
toc_rel: userguide/toc.yml
toc_href: userguide/
_tocRel: userguide/toc.yml
_tocHref: userguide/
_disableToc: false
---

# Struckig

Struckig is the Structured Text port of [Ruckig](https://docs.ruckig.com), bringing online trajectory generation to TwinCAT 3 and other IEC 61131-3 environments.

It computes jerk-limited, acceleration-limited, and velocity-limited trajectories in real time, cycle by cycle, from your current kinematic state to a target state.

> [!IMPORTANT]
> Struckig ports the open-source Ruckig Community feature set. Ruckig Pro features are not part of this project.

## Start Here

- New to Struckig: go to [Installation](userguide/installation.md) and then [Single Axis Trajectory](userguide/single_axis_trajectory.md).
- Learn the model first: read [Concepts](userguide/concepts.md).
- Check applicability boundaries: [Feature Scope](userguide/feature_scope.md).
- Building machine logic with state machines and segments: read [Examples](userguide/examples_structured_text.md).
- Integrating with cyclic PLC execution: read [Cycle Integration](userguide/cycle_integration.md).
- Using multi-axis coordination: read [Synchronized Trajectory](userguide/synchronized_trajectory.md).
- If behavior is off: check [Troubleshooting](userguide/troubleshooting.md).
- Common questions: [FAQ](userguide/faq.md).

## Why Struckig

- Online trajectory generation directly in PLC code.
- Deterministic cycle-by-cycle updates based on your task cycle time.
- Same algorithmic core and terminology as Ruckig where applicable.
- Native Structured Text API with arrays and TwinCAT-friendly integration.

## Licensing

Struckig is dual-licensed.

- Open-source usage is available under [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html).
- If your project cannot comply with GPL requirements, contact [stefan@besler.me](mailto:stefan@besler.me) for a commercial license.

