# Controls and States

## Principle

Make scope, state, and recovery visible. Controls should change a meaningful question, not expose every available query parameter.

## Use when

- time, entity, segment, or scenario selection is essential;
- drilldown preserves overview context;
- saved views support recurring roles;
- alerts or actions have accountable workflows.

## Reject when

- default state is meaningless until several filters are set;
- filter chips do not reveal full scope;
- changing one control resets another silently;
- loading, empty, no-results, stale, partial, and error states look alike;
- auto-refresh destroys focus or comparison.

## Prefer instead

Provide a decision-useful default, visible active scope, clear reset, stable URLs where useful, and state-specific recovery. Preserve the prior trustworthy view during refresh when possible and label its age.

## Escape conditions

- Complex analyst tools may expose many controls when users understand their model; group by question and support presets.
- Auto-refresh is valid for monitoring when changes are calm, announced appropriately, and do not steal focus.
- An empty state may be positive (“no incidents”) only when successful retrieval is verified.

## Audit signals

- “0” displayed after fetch failure;
- current month compared to complete months;
- stale data retains green status;
- mobile hides filter scope;
- destructive action lacks affected-scope confirmation.
