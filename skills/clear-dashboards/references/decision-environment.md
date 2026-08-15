# Decision Environment

## Principle

Define the recurring decision, cadence, and escalation path before selecting metrics or views.

## Use when

- users monitor state repeatedly;
- exceptions trigger diagnosis or action;
- several measures jointly define health;
- different roles need related but not identical context.

## Reject when

- the page is a one-time explanation better served by a report/explainer;
- metrics have no owner, threshold, comparison, or action;
- audiences have incompatible decisions but share one undifferentiated default;
- “real time” is requested without a latency-sensitive response.

## Prefer instead

Write a dashboard contract: audience, decisions, cadence, entities, time basis, freshness promise, threshold source, actions, and failure cost. Remove measures that cannot influence any of those.

## Escape conditions

- Exploratory analytics may not have fixed actions; define the supported question families and starting overview instead.
- Executive dashboards can prioritize shared orientation over direct action, but claims still need scope and comparison.
- A single KPI can be the dashboard when it fully determines the operational decision.

## Audit signals

- tiles mirror database fields;
- status colors lack policy semantics;
- several time windows appear without coordination;
- metric definitions change between views;
- users export data to answer the dashboard's supposed primary question.
