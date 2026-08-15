# Notation and Boundaries

## Principle

Use the smallest visual vocabulary that distinguishes every relationship relevant to the question.

## Use when

- node shape distinguishes stable semantic types;
- boundary style identifies ownership, trust, deployment, or scope;
- edge style distinguishes synchronous/asynchronous, allowed/prohibited, current/proposed, or certain/uncertain relationships;
- labels name domain terms more efficiently than icons.

## Reject when

- one color/shape carries several unrelated meanings;
- standard icons are used without labels for an unfamiliar audience;
- dashed lines ambiguously mean optional, future, async, or unknown;
- current and proposed architecture appear equally factual;
- a legend contains more vocabulary than the diagram's question needs.
- unprovided service names, events, timeouts, retry counts, or boundary assignments are rendered as actual system facts;
- an `observed` label appears without a trace, log, specification, or other named evidence source.

## Prefer instead

Declare notation locally. Label boundary meaning. Keep current/proposed or observed/inferred layers visually distinct. Use stable IDs or terms across related views. Mark omitted scope and material unknowns.

When designing from incomplete information, produce a schema rather than a fictional incident: use placeholders such as `[checkout service]`, `[observed timeout if present]`, and `[retry policy from telemetry/config]`. Concrete illustrative paths must be labeled `Example only` and kept separate from the asserted system view.

## Escape conditions

- Use established UML, BPMN, circuit, or cloud notation for an audience fluent in it; do not translate away useful precision.
- Color alone may be decorative if no information depends on it.
- An intentionally schematic map need not preserve physical distance if topology is clearly stated.

## Audit signals

- ambiguous arrowheads;
- unlabeled external actor or system boundary;
- future-state component presented as deployed;
- error/alternate paths missing from a supposedly operational flow;
- icon similarity masks different node types;
- legend lookup dominates tracing.
