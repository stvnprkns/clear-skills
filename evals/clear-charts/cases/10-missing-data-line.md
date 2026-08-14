# Case: missing observations

**Family:** Audit

## Prompt

A sensor line chart has no readings for six hours because the device was offline. The chart library automatically connects the point before the outage to the point after it with a normal solid line. Audit it.

## Expected skill behavior

- Flag implied observed continuity.
- Recommend a gap or explicitly styled estimated connection only if interpolation is justified.
- Make the outage/missingness discoverable when it matters.
- Do not replace the missing period with zero.
