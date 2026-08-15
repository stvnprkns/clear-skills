# Case: transaction trace or architecture map

**Family:** Create / Ambiguity

## Prompt

Design one diagram for incident responders investigating delayed checkout. They must trace the order of synchronous calls and asynchronous retries for one transaction, know which trust boundary each service occupies, and understand which components are shared with unrelated workflows. A stakeholder asks for a complete architecture diagram with numbered arrows.

## Expected skill behavior

- Identify transaction sequence as the primary incident task and use a sequence/trace view with trust boundaries.
- Preserve shared-component architecture context secondarily without forcing unrelated topology into the primary path.
- Distinguish synchronous calls, queued work, retry, timeout, and observed versus inferred events.
- State the cost of narrowing to one transaction and provide a route to the broader architecture map.
- Do not invent concrete services, events, timeout values, or retry counts as facts; use labeled placeholders until logs/specifications supply them.
