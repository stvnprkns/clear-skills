# Scan and Density

## Principle

Use visual rhythm to expose row identity, comparison columns, groups, and exceptions. Density is a task decision, not a style preference.

## Use when

- expert users scan many rows repeatedly;
- several values must remain visible together;
- sorting or grouping creates meaningful runs;
- small inline encodings reduce arithmetic without replacing exact values.

## Reject when

- zebra stripes, borders, badges, and bold text all compete;
- padding forces useful rows below the fold without improving targeting;
- compression makes wrapped rows or click targets ambiguous;
- conditional color creates a false heatmap or value judgment;
- every cell is emphasized.

## Prefer instead

- Use whitespace for ordinary row separation and stronger rules for groups/totals.
- Right-align comparable numbers and use tabular numerals where supported.
- Keep precision consistent within a column.
- Place units in headers when stable.
- Use in-cell bars only when magnitude comparison is frequent; retain exact labels.
- Pin one identity column and only the decision-critical context.

## Escape conditions

- Zebra striping can help very wide tables where tracking across distance is difficult.
- Dense rows are appropriate for trained, frequent users; offer a density preference when audiences differ.
- Multiple status colors can be justified when states are stable, actionable, and redundantly labeled.

## Examples

A financial reconciliation table may legitimately use compact rows, gridlines, parentheses, and tabular numerals because exact cross-column checking is the task. Turning each row into a spacious card would be a regression.

## Audit signals

- decimal points do not align;
- row height changes unpredictably;
- totals are mistaken for records;
- long labels truncate the differentiating suffix;
- colored pills dominate quantitative values;
- frozen region leaves too little viewport for data.
