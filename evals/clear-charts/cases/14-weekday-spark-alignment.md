# Case: weekday spark alignment and shared scrub

**Family:** Create / Audit

## Prompt

Audit and improve a project list containing one five-day sparkline per row. A persistent header reads Mon Tue Wed Thu Fri above the spark column and a note says “Mon→Fri across · 50–100% up.” The day labels use a CSS flex row with `justify-between`; spark points use `i / (n - 1)` inside an SVG plot with left/right insets. The dots visibly drift away from the label centers. Each row currently owns its own hover day. The proposed fix is to nudge the labels, add a faint vertical column for every day, draw a dot at every observation, emphasize Friday, and synchronize all rows to one active day.

Readers need to compare project utilization on the same weekday and trace a project across the workweek. The implementation must work at desktop and narrow widths, with pointer and keyboard input.

## Expected skill behavior

- Identify the root cause as competing coordinate systems, not generic spacing or SVG imprecision.
- Define one explicit plot rectangle and one weekday x accessor used by header labels, spark points, guides, hit regions, active cursor/ring, and expanded detail.
- Choose endpoint positions `i / 4` for this artifact because Mon–Fri are the five observed points and the plotted line begins/ends on those observations. Explain that band centers would apply if weekdays represented equal-width intervals/cells; do not leave the implementation contract as an unresolved choice or prescribe magic offsets.
- Recommend one selected weekday domain value shared across rows because same-day cross-project comparison is the stated task; include Left/Right keyboard stepping and pointer mapping through the same plot bounds.
- Keep weekday orientation persistent at rest and preserve the 50–100% vertical context without implying that prose alone fixes alignment.
- Treat vertical guides, dots on every point, and Friday emphasis as conditional craft choices: keep only those that improve tracing, observation cadence, or a decision-relevant latest state.
- Require rendered verification at first/middle/last positions, desktop/narrow widths, and missing-value states.
- Produce an implementation-ready coordinate/state contract rather than only saying “align the dots” or “tighten the chart.”
