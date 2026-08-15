---
name: clear-dashboards
description: >-
  Information-design judgment for choosing, structuring, auditing, and improving multi-view dashboards and operational decision environments. Use for KPI dashboards, analytics dashboards, monitoring consoles, scorecards, executive dashboards, filters, drilldowns, dashboard layout, metric hierarchy, cross-view coordination, alerting, freshness, empty/loading/error states, and responsive dashboard review.
---

# Clear Dashboards

A dashboard is a recurring decision environment, not a collage of charts. It succeeds when readers can detect material state, understand why it matters, and move into diagnosis or action without reconstructing context.

Use `clear-charts` for chart-level encoding, `clear-tables` for exact retrieval, and `clear-diagrams` for topology. This skill owns the hierarchy and relationships among views, controls, metrics, and states.

## Quick Reference

| Need | Read |
| --- | --- |
| Define audience, decisions, cadence, and KPI environment | [decision-environment.md](references/decision-environment.md) |
| Build hierarchy and relationships across views | [view-composition.md](references/view-composition.md) |
| Design controls, drilldowns, freshness, and system states | [controls-and-states.md](references/controls-and-states.md) |
| Report a standalone audit | [review-output.md](references/review-output.md) |

## Operating Sequence

1. State reader, recurring decision, cadence, scope, and consequence of delay/error.
2. Separate monitor, diagnose, decide, and act tasks.
3. Define KPI semantics, thresholds, freshness, comparison basis, and ownership.
4. Build a default hierarchy: state → exception → explanation → detail/action.
5. Give every view a job and every control a real analytical question.
6. Coordinate filters, selections, time ranges, units, and identities explicitly.
7. Verify loading, stale, empty, error, partial, filtered, narrow, and accessible states.
8. Report systemic root causes before chart-level craft.

## Core Principles

1. **One dashboard, one decision environment.** Do not merge executive status, analyst exploration, and frontline work queues without explicit modes.
2. **Lead with material state, not metric inventory.** A KPI earns prominence by consequence and actionability, not availability.
3. **Context completes the number.** Current value needs target, baseline, trend, freshness, and denominator only to the degree they change interpretation.
4. **Overview and diagnosis are different layers.** The default should reveal whether attention is needed; detail should explain where and why.
5. **Cross-view interaction must be legible.** Readers must know which views changed, what remains filtered, and how to reset.
6. **Alerts require ownership and action.** Red decoration without threshold semantics or response path is noise.
7. **Freshness is a data dimension.** Stale, partial, delayed, unavailable, and zero are not interchangeable.
8. **Responsive design reprioritizes tasks.** Do not shrink a desktop wall or silently remove the context needed for mobile decisions.
9. **Avoid KPI theater.** More tiles, colors, real-time motion, and decimals do not create operational value.
10. **Preserve a quiet dashboard.** If stable state, exceptions, and drilldown already work, do not add explanatory clutter.

## Common Mistakes

| Mistake | Corrective question |
| --- | --- |
| Equal-size KPI grid | Which state changes action first? |
| One global filter for unrelated views | Which semantic scope does it actually control? |
| Green/red without thresholds | What policy or consequence defines the state? |
| Current number without basis | Compared with what period, target, or population? |
| Every view interactive | What secondary task does each interaction unlock? |
| Desktop compressed onto mobile | Which mobile decision has priority? |
| Empty chart interpreted as zero | Is the system empty, filtered, stale, or failed? |
| Fixing chart cosmetics first | Is the dashboard's hierarchy itself wrong? |

## Reporting

Use [review-output.md](references/review-output.md). Consolidate repeated chart symptoms into dashboard-level causes.
