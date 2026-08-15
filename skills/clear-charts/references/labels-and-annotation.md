# Labels and Annotation

## Decision contract

### Principle

Label what readers must identify; annotate what changes interpretation or action. Do not turn the chart into prose.

### Use when

- direct labels remove repeated legend lookup;
- a threshold, event, caveat, or supported insight changes the decision;
- exact values are few and central;
- a partial period, forecast boundary, or denominator prevents misreading.

### Reject when

- every point is labeled despite pattern being primary;
- annotation states a claim the data does not establish;
- a dashboard narrates ordinary variation and competes with monitoring;
- detached prose makes the eye search for the referenced mark;
- the label merely repeats an axis or chart type.

### Prefer instead

Use selective endpoints, collision-managed direct labels, one labeled reference, or a concise subtitle that defines metric and comparison. Put secondary exact values in accessible detail.

### Escape conditions

Keep a compact legend when direct labels collide, series recur across coordinated views, or labels would obscure the data. Keep gridlines instead of dense value labels when across-distance estimation is the task.

Text is part of the visualization. It should reduce translation between what the reader sees and what the data means.

## Direct labels first when practical

Prefer placing a series/category name near the relevant mark when this avoids repeated eye travel to a legend.

Strong candidates:

- a few line-series endpoints;
- key scatterplot points;
- bars with category names already adjacent;
- a focal range or threshold;
- selected small multiples.

Keep a legend when direct labels would collide, produce long leader lines, or overwhelm the plot.

## Essential information cannot live only in hover

Tooltips are good for detail-on-demand, not for the primary identity or conclusion.

Persistent chart should usually expose:

- what the chart measures;
- units;
- primary categories/series;
- important reference/target;
- the central comparison or insight when the chart is explanatory.

## Titles

A title can be **descriptive** or **assertive**.

Descriptive title:

> Monthly active users by plan, Jan–Jul 2026

Use when the visualization is exploratory or the audience should draw its own conclusion.

Assertive title:

> Enterprise adoption accelerated after the March launch

Use when the chart supports a specific communicated insight and the statement is directly defensible from the data.

Do not overclaim causality when the chart only shows correlation or temporal coincidence.

## Subtitle / deck

Use a subtitle to supply context that changes interpretation:

- population/denominator;
- time range;
- unit definition;
- adjustment (inflation-adjusted, indexed, seasonally adjusted);
- comparison baseline;
- important filtering.

Do not repeat the title in different words.

## Value labels

Use value labels selectively.

Good uses:

- endpoint values;
- a few important peaks/troughs;
- bars when exact values matter and labels remain scannable;
- before/after endpoints;
- small charts where labels can replace an axis cleanly.

Avoid labeling every point when it creates texture instead of information.

## Annotation

Annotations should answer “why does this matter?” or “what happened here?”

Good annotation types:

- event tied to an inflection;
- threshold meaning;
- outlier explanation;
- methodological change;
- forecast boundary;
- data caveat at the relevant region;
- callout of the comparison the audience might otherwise miss.

### Annotation hierarchy

1. Primary insight annotation.
2. Context necessary to interpret it.
3. Secondary detail only if it does not compete.

A chart with ten equal-weight callouts has no annotation hierarchy.

## Reference line labels

Always identify what a non-obvious reference means. Prefer direct text such as:

- Target 95%
- 2025 average
- Break-even
- National median

Do not make the reader infer a dashed line from a legend unless the layout makes direct labeling impossible.

## Legends

A legend is a decoding device. Minimize the distance and effort required to use it.

If a legend is necessary:

- order items to match visual order when possible;
- use the same label wording everywhere;
- keep symbols/line styles faithful to the plot;
- do not hide categories in a scrolling legend unless the chart supports exploration and the hidden state is obvious.

## Text orientation

Prefer horizontal text. Rotated labels impose reading cost and often indicate that the representation or spacing needs reconsideration.

Before rotating labels:

- shorten labels;
- increase width;
- use horizontal bars;
- show fewer axis ticks;
- wrap where sensible;
- use small multiples.

## Number formatting

Formatting is part of comprehension.

- Use separators appropriate to locale.
- Keep comparable values at comparable precision.
- Use compact suffixes (`k`, `M`, `B`) only when the audience understands them and the lost precision is acceptable.
- Put the minus sign where it is easy to perceive.
- Distinguish `12%` from `+12%` and `+12 pp` correctly.

## Sources and notes

For published/editorial charts, include source and methodology notes when they affect trust or interpretation. For product charts, source provenance may be implicit in the product context, but calculation definitions should still be discoverable.

## Anti-pattern: separate explanatory card

Do not put critical interpretation in a detached card if a concise annotation can live adjacent to the relevant visual element. Spatial proximity is part of the explanation.

Use a separate narrative region when explanation is too long to coexist with the plot or when the chart is one step in a larger story.
