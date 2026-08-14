---
name: clear-charts
description: >-
  Information-design judgment for choosing, creating, auditing, and improving quantitative charts and plots. Use for bar charts, line charts, scatterplots, distributions, time series, rankings, comparisons, part-to-whole charts, axes, scales, legends, labels, annotations, chart color, uncertainty, tooltips, and interactive charts. Triggers on chart, graph, plot, time series, trend, comparison, distribution, axis, scale, legend, tooltip, data visualization, chart review, chart audit, make this chart clearer.
---

# Clear Charts

A chart succeeds when the relationship that matters becomes easier to see, compare, and understand without distorting the data.

Optimize for understanding before novelty, decoration, or density. Determine what the reader needs to understand before selecting or improving a chart type. Do not preserve a requested representation merely because it already exists.

When reviewing, prioritize the smallest number of changes that would produce the largest improvement. A Clear review is a design critique, not a list of every technically possible refinement.

`clear-tables` owns exact-value retrieval and dense tabular comparison. `clear-diagrams` owns processes, systems, and non-quantitative relationships. `clear-dashboards` owns multi-view information environments. `clear-explainers` owns narrative and explanatory interaction. `clear-visuals` owns cross-domain representation choice and consolidated review when those skills are available.

## Quick Reference

| Category | Use when | Reference |
| --- | --- | --- |
| Chart selection | Decide whether to chart and which visual form fits the question | [chart-selection.md](references/chart-selection.md) |
| Encoding & comparison | Position, length, area, grouping, ranking, small multiples | [encoding-and-comparison.md](references/encoding-and-comparison.md) |
| Scales & axes | Baselines, domains, ticks, log scales, normalization, dual axes | [scales-and-axes.md](references/scales-and-axes.md) |
| Labels & annotation | Direct labels, legends, titles, callouts, values, reference lines | [labels-and-annotation.md](references/labels-and-annotation.md) |
| Color | Categorical, sequential, diverging, emphasis, accessibility | [color.md](references/color.md) |
| Uncertainty & missingness | Estimates, intervals, incomplete observations, interpolation | [uncertainty-and-missing-data.md](references/uncertainty-and-missing-data.md) |
| Interaction | Tooltips, filtering, brushing, zoom, selection, responsive behavior | [interaction.md](references/interaction.md) |
| Review output | Priorities, Keep/Rethink, verification, verdict | [review-output.md](references/review-output.md) |

## Core Principles

### 1. Start With the Question

State the relationship the reader needs to understand before choosing the chart.

Useful formulations include:

- How has this changed over time?
- Which category is largest or smallest?
- How far are actuals from a target or reference?
- What does the distribution look like?
- Are two variables related?
- Which items changed the most?
- How does composition differ between groups?

If the chart cannot be tied to a meaningful question, do not optimize its styling yet.

### 2. Choose the Representation From the Relationship

Choose the form that makes the required comparison easiest. Do not choose a visualization because it is visually interesting or convenient in the current charting library.

If a simpler representation communicates the relationship equally well, prefer the simpler one. If exact lookup is the primary task, prefer a table. If the information is fundamentally about steps or dependencies rather than quantities, prefer a diagram.

### 3. Make the Important Comparison Explicit

Readers should not perform arithmetic the design can perform for them.

When the important fact is a difference, delta, ranking, threshold, target, or change in slope, expose that relationship directly through ordering, reference marks, derived values, or annotation.

Do not force repeated eye travel between a legend, axis, and marks to reconstruct the intended comparison.

### 4. Prefer More Accurate Encodings When Precision Matters

For precise quantitative comparison, prefer common position and aligned length before area, angle, volume, or color intensity.

Less precise encodings can be appropriate when the task is to perceive an overall pattern, density, or composition. Do not use them merely for visual variety.

### 5. Treat Scales as Part of the Argument

A scale determines how magnitude is perceived.

Use domains and baselines appropriate to the visual encoding and intended comparison. Make non-obvious transformations such as logarithmic scales, indexing, normalization, or truncated domains explicit.

Never increase visual drama by exaggerating differences.

### 6. Label the Data, Not the Interface

Place identifying information close to the marks it explains when doing so reduces lookup effort.

Prefer direct labels over detached legends when the chart remains legible. Use units consistently. Titles and subtitles should add meaning or context rather than repeat the chart type.

The primary message must not depend on a tooltip.

### 7. Annotate Significance, Not Everything

Use annotations to explain why a point, change, threshold, range, or event matters. Annotation creates hierarchy; it should not become a second dataset layered over the first.

If the chart’s primary insight exists only in prose outside the visualization, consider moving the essential context closer to the relevant marks.

### 8. Use Color as Meaning and Emphasis

Color should encode a meaningful category, ordered value, divergence, state, or emphasis.

Do not assign a different saturated hue to every category when identity is already obvious through position or labels. De-emphasize context so the important series can dominate.

Never rely on color alone to communicate information.

### 9. Represent Missingness and Uncertainty Honestly

Do not silently convert missing observations to zero or connect gaps as though values were observed.

Distinguish zero, unavailable, estimated, incomplete, and suppressed values when the distinction affects interpretation. When uncertainty could change the conclusion, represent it at an appropriate level.

### 10. Interaction Must Earn Its Complexity

Use interaction when it enables meaningful exploration, comparison, detail, or manipulation that would otherwise be difficult to provide.

If removing an interaction leaves comprehension unchanged, remove it. Essential information must remain available without hover, and interactive states should be keyboard/focus accessible when the medium supports interaction.

### 11. Reduce Before Adding

When a chart feels unclear, first look for what can disappear.

Grid lines, borders, legends, redundant labels, repeated units, decorative marks, unnecessary series, and container chrome all compete for attention. Remove only what does not help orientation, comparison, or interpretation.

### 12. Preserve What Already Works

A review is not a redesign exercise.

Explicitly protect strong decisions. Recommend replacing the representation only when the current form creates a meaningful comprehension, integrity, or task-fit problem.

## Common Mistakes

| Mistake | Better approach |
| --- | --- |
| Choosing a chart before defining the question | Identify the relationship the reader must understand first |
| Using the requested chart type as an immutable constraint | Treat it as a starting hypothesis unless the user explicitly requires it |
| Giving every series equal prominence | Establish primary data and contextual data |
| Asking readers to mentally calculate the key difference | Encode, derive, sort, or annotate the difference |
| Using a detached legend for a few easily labeled series | Direct-label when space and collision allow |
| Using saturated color simply because categories differ | Use color only when it carries meaning or hierarchy |
| Hiding essential values or identity in hover | Make the primary information persistent |
| Truncating or transforming a scale without disclosure | Make the transformation explicit and justify it |
| Treating missing as zero | Encode missingness separately |
| Connecting across a missing interval as observed continuity | Break or style the connection to reveal uncertainty/missingness |
| Adding interaction that reveals nothing new | Remove the interaction |
| Styling a fundamentally mismatched chart | Recommend a better representation before polishing |
| Reporting every minor issue | Prioritize the highest-leverage changes |
| Redesigning strong decisions | Include a Keep section and leave them intact |

## Reporting

For a standalone chart audit, use [review-output.md](references/review-output.md). The review is complete only when the highest-impact findings, deliberately preserved decisions, verification status, and verdict are reported.

When `clear-visuals` orchestrates a future cross-domain review, its consolidated reporting rules take precedence while `clear-charts` remains the source of truth for chart-specific judgment.
