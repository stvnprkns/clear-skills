# Case: stale data remains green

**Family:** Audit

## Prompt

A warehouse dashboard shows “Healthy” in green because the latest stored value is within target. The ingestion job failed 19 hours ago; normal freshness is 15 minutes. Audit it.

## Expected skill behavior

- Treat freshness as part of status integrity.
- Replace or qualify healthy state with stale/unknown and recovery context.
- Show last successful update and affected scope.
- Do not display zero or retain green as if current.
