# Chart Construction and Coordinate Systems

Chart craft is reliable when every visual layer shares an explicit geometry and state model. Alignment that merely looks close at one width is not a finished implementation.

## Decision contract

### Principle

Define the plot rectangle, domain, range, and accessor once. Derive axes, labels, marks, guides, hit targets, annotations, and selected states from that same contract.

### Constraint

Reject an implementation when elements that imply the same coordinate use different layout systems or independent arithmetic. Common failures include:

- weekday labels distributed with CSS `justify-content: space-between` while SVG points use `i / (n - 1)`;
- labels centered in equal-width cells while points use interval endpoints;
- an overlay or cursor measured against the container while marks use an inset plot rectangle;
- repeated sparklines with slightly different inner padding;
- responsive CSS resizing the visible plot without updating the pointer-to-domain calculation.

Do not repair these failures with per-label margins, `translateX`, or magic offsets. Those corrections usually fail at another width, label length, or data count.

### Pattern

Write down one coordinate contract before styling:

```text
domain: [Mon, Tue, Wed, Thu, Fri]
plot: { x, y, width, height }
x(day): band center inside plot, or point position across plot
y(value): shared quantitative scale inside plot
selectedDay: one domain value, not a pixel
```

Then use the same `x(day)` for:

- visible day labels and ticks;
- every spark point;
- vertical day guides;
- hover/focus hit regions;
- selected-day cursor and ring;
- expanded detail aligned beneath the same column.

Use band centers, `x + (i + 0.5) * width / n`, when each label names an interval/cell. Use point positions, `x + i * width / (n - 1)`, when labels and marks represent endpoints including both plot edges. Choose deliberately; do not mix them.

Commit to one model in the implementation contract when the artifact provides enough evidence. Do not carry `band centers OR endpoints` into the final recommendation merely to sound flexible.

| Evidence | Choose | Why |
| --- | --- | --- |
| Mon–Fri are five observed points and the line begins/ends on Mon/Fri | endpoint positions, `i / 4` | labels identify the same observations as the plotted points |
| Each weekday owns an equal-width cell/bin, such as daily totals occupying intervals | band centers, `(i + 0.5) / 5` | the mark represents the cell rather than its boundary |
| Evidence is insufficient | state the missing semantic/layout evidence and make the choice provisional | arbitrary certainty is worse than an explicit verification need |

Hit regions may use midpoint boundaries around endpoint-positioned marks. That does not convert the visible marks or labels into band-center geometry.

### Escape condition

Independent geometry is valid when views do not claim alignment—for example, separate cards whose only task is individual shape inspection. If readers must compare values at the same day or category, shared geometry is required.

## Plot box before chart box

The chart container is not automatically the plot rectangle. Titles, y labels, legends, direct labels, and padding consume space.

Keep these explicit:

- outer component bounds;
- plot insets;
- drawable plot bounds;
- overflow reserved for endpoint/direct labels;
- hit region bounds.

Pointer inversion must use the drawable plot bounds, not the outer card. Clamp only after converting through the correct range.

## Persistent axis versus interactive detail

A chart should remain oriented before hover or focus.

Persist the minimum scale needed to answer:

- what the horizontal positions mean;
- what direction and rough range the vertical dimension uses;
- which series or state is visible.

Interaction may add exact values, provenance, or a linked readout. It should not be the first moment the reader learns that the points represent Monday through Friday or that the vertical range is 50–100%.

Compact axis prose such as “Mon–Fri across · 50–100% up” can supplement a small chart, but it does not repair marks that fail to align with the visible day positions.

## Synchronized selection across repeated charts

When rows share a time/category domain and the task is cross-row comparison, prefer one selected domain value across the group.

### Pattern

- Keep `selectedDay` as the source of truth.
- Map pointer position to a day through the shared inverse scale.
- Let hovering the persistent axis or any plot update the same selection.
- Let Left/Right (or domain-appropriate keys) step the selection.
- Show the selected day persistently near the axis or linked values.
- Update every row from the same domain value.
- Preserve context: unselected lines and points remain visible unless filtering is the stated action.

### Constraint

Reject synchronized interaction when rows use different domains or when a shared selection implies false comparability. Do not silently snap missing row values to zero; show missing/unavailable state.

## Marks and state hierarchy

Point markers are useful when they expose observation cadence, provide selection targets, or distinguish measured values from interpolation. They are not mandatory decoration.

For a short five-day sparkline, a reliable hierarchy is:

1. line carries trend;
2. small persistent points establish the five observations when cadence matters;
3. latest point may receive restrained emphasis when recency is decision-relevant;
4. selected point receives a ring or shape change plus linked text;
5. faint day guides appear only when they materially improve cross-row tracing.

Reject “dot every point” when the domain is dense, markers obscure crossings, or the axis already makes cadence unambiguous. Reject a strong Friday treatment when Friday is not actually privileged by the decision.

## Interaction craft

- High-frequency scrubbing should respond immediately; do not add bouncy or staged animation.
- If transitions help preserve identity when data changes, animate only the changing mark properties and keep duration short.
- Never use motion as the only selected-state cue.
- Keep the cursor, active ring, axis label, and linked readout optically aligned.
- Expand hit regions without changing the visible data coordinate.
- Verify pointer, keyboard, and touch behavior separately.

## Verification checklist

Inspect the rendered result rather than trusting source arithmetic.

- first, middle, and last positions align at wide and narrow widths;
- labels and marks still align with long/localized labels;
- all repeated plots share the same drawable x range;
- pointer at plot edges resolves to the first/last domain value;
- keyboard stepping updates the same state as pointer scrubbing;
- selected state remains legible without color and without motion;
- missing values do not create false points or connections;
- dense data does not inherit a short-domain marker pattern mechanically.

Report implementation evidence as a contract: named plot bounds, shared scale/accessor, selected domain state, supported input modes, and rendered sizes checked. “Adjusted spacing” is not sufficient evidence for a coordinate fix.
