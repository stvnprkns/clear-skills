# Case: tooltip dependency

**Family:** Audit

## Prompt

I built an interactive line chart with five unlabeled colored lines. There is no legend. Hovering a line reveals the company name, exact value, and whether it beat target. On mobile, tapping a line shows the same tooltip. Audit it.

## Expected skill behavior

- Identify series identity and target status as too important to exist only in hover/tap.
- Recommend persistent direct labels or a compact legend and persistent target/reference treatment.
- Keep tooltip for exact/secondary detail if useful.
- Note keyboard/focus behavior as not verified or required for web accessibility.
