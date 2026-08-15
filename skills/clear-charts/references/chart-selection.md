# Chart Selection

Choose a representation from the reader's task and the structure of the data, not from a chart-type menu.

## First decision: should this be a chart?

### Prefer a chart when the reader needs to perceive

- pattern or trend;
- relative magnitude;
- ranking;
- distribution or outliers;
- relationship or correlation;
- change or deviation;
- composition;
- many values at a glance.

### Prefer a table when the reader primarily needs

- exact values;
- lookup by row/column;
- several measures per item;
- identifiers or long text labels;
- comparison across dimensions that do not share one dominant visual question.

A chart may supplement a table, but do not chart data merely because the user used the word “visualize.”

### Prefer a diagram when the reader primarily needs

- sequence;
- dependency;
- system structure;
- ownership or hierarchy;
- cause-and-effect logic that is not encoded as quantitative measurements.

## Translate the question into a relationship

| Reader question | Relationship | Strong starting forms |
| --- | --- | --- |
| How did one or a few measures change over time? | Change over time | Line, step line, area when accumulation is meaningful |
| Which categories are larger? | Magnitude / ranking | Sorted bar, dot plot |
| How far is each item from a baseline or target? | Deviation | Diverging bar, dot + reference, bullet chart |
| How much did items change between two moments? | Before/after | Slope, dumbbell, arrow/range plot, ranked delta |
| What is the distribution? | Distribution | Histogram, strip/dot, box plot, violin when shape matters |
| Are two measures related? | Correlation | Scatterplot; add trend only when analytically justified |
| How do groups differ across the same categories? | Comparison | Grouped dot/bar, small multiples |
| How does a whole break into parts? | Composition | Stacked bar, 100% stacked bar; pie/donut only for very small simple sets |
| How does composition change over time? | Composition + time | 100% stacked area/bar, small multiples; use carefully when interior categories need comparison |
| Which items account for most of a total? | Concentration / cumulative contribution | Ranked bars + cumulative line only if cumulative share is itself useful |
| Where are values located geographically? | Spatial | Map only when geography is analytically relevant; otherwise rank or plot values directly |

These are starting points, not automatic mappings.

## Rules that prevent common wrong turns

### Time series is not automatically a line chart

Use a line when the *path* through time matters. If the real question is “which changed most between start and end,” a slope/dumbbell/ranked delta view may be clearer than showing every intermediate point.

Use small multiples instead of many overlaid lines when individual trajectory matters but overlap makes comparison difficult.

### Bars are for magnitude from a baseline

Bars make length the quantitative signal. They are strong for category comparisons and ranking. When the baseline is not meaningful or zero would consume most of the chart, a dot plot may show close values with less visual distortion pressure.

### Pie/donut is a narrow tool

Use only when:

- the parts form a meaningful whole;
- there are few segments;
- approximate part-to-whole perception is enough;
- no precise cross-category ranking is required.

Reject when there are many slices, similar slices that require precise comparison, multiple pies that readers must compare, or values do not form a whole.

### Stacked bars optimize different comparisons

A stacked bar is good for total + composition. Only the segment attached to the common baseline is easy to compare precisely across categories. If comparison of every segment matters, use grouped bars, dots, or small multiples instead.

100% stacked bars are for composition share, not absolute magnitude. If total size matters, do not normalize it away without a second representation or explicit total.

### Area charts imply magnitude and continuity

Use filled area when the area from baseline carries meaning, often for totals over time. Avoid overlapping opaque areas for multiple independent series. Do not use area solely because it looks more substantial than a line.

### Scatterplots are for paired quantitative variables

Do not connect points unless sequence/path is meaningful. Use size as a third quantitative variable sparingly; area is harder to compare than position. Use shape or faceting for categories when color alone would overload the plot.

### Bubble charts trade precision for compact multivariable pattern

Use when approximate magnitude and spatial pattern are enough. Reject when users need accurate size comparison or when many bubbles overlap.

### Dual-axis charts require a strong reason

Before using two quantitative axes, ask whether indexing, faceting, normalization, or separate aligned charts can make the comparison without inviting false visual correlation. If dual axes are unavoidable, make axis-series mapping unmistakable and avoid manipulating domains to create matching shapes.

### Maps require a geographic question

Geographic data does not automatically require a map. Use a map when location, adjacency, region, route, or spatial pattern is part of the question. If users just need to know which state/region is highest, a sorted chart is usually easier to compare.

## Selection sequence

1. **Question** — Write the sentence the chart must make easier to answer.
2. **Data semantics** — Identify quantitative, temporal, ordinal, nominal, and geographic fields by meaning, not storage type.
3. **Comparison** — Identify what the eye must compare: common baseline, endpoints, slopes, distribution, position, composition, or path.
4. **Candidate forms** — Generate 2–3 plausible representations, including a table when relevant.
5. **Reject** — Remove forms that hide the primary comparison or introduce unnecessary decoding.
6. **Choose** — Use the simplest form that preserves the needed information.
7. **Test** — Ask whether the important answer is visible without hover or mental arithmetic.

## Ambiguous selection decisions

### Close values: bars, dots, or a narrowed line domain?

| Choose | When | Reject when |
| --- | --- | --- |
| Zero-based bars | magnitude relative to absence is meaningful | the narrow difference is the only task and zero makes it unreadable |
| Dot plot | close category values need position-based comparison | the filled magnitude from zero is itself meaningful |
| Narrow-domain line | change or deviation around a stable level is the task, domain is disclosed, and continuity matters | readers may infer the cropped vertical distance as absolute magnitude |

Do not crop a bar baseline to expose close values. Do not force a zero domain on every line or dot chart. If both absolute level and close deviation matter, pair an overview with a focused view or annotate the difference explicitly.

### Thirty categories: reveal structure before reducing count

1. Determine whether the task is full ranking, lookup, distribution, top contributors, or exception handling.
2. Preserve all categories when individual actionability matters; use a sorted scrollable list or table with stable labels.
3. Group only by real domain structure. An “Other” bucket is acceptable for composition but not when tail items need action.
4. Filter when users arrive with a target in mind; do not require serial filtering for comparison.
5. Replace the chart with a distribution plus labeled exceptions when the question is about typicality, not every category.

### Explain or explore?

Use a persistent annotation when a supported insight must be noticed for the decision. Use exploration when different readers legitimately pursue different questions. A dashboard can do both: the default state establishes the monitoring question and material exception; controls support diagnosis.

Reject annotation that converts a tentative pattern into a conclusion. Reject exploration that makes readers hunt for the basic state of the system.

## Rethink threshold

Recommend a different representation when at least one is true:

- the current chart visually encodes the wrong relationship;
- users cannot make the intended comparison reliably;
- the chart removes information essential to the question;
- the chart materially exaggerates or suppresses differences;
- the primary task is exact lookup and the visualization makes lookup harder;
- complexity exists mainly because of the chosen chart type.

Do **not** recommend replacement merely because another chart is fashionable, slightly cleaner, or personally preferred.
