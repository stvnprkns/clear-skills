# Scales and Axes

## Decision contract

### Principle

A domain is part of the claim. Judge it by the mark's encoding and the reader's comparison, not by a universal zero rule.

### Use when

- use zero for bars and areas whose length/filled extent encodes magnitude from a baseline;
- use a narrower line/dot domain when position and change are the task, variation would otherwise disappear, and the domain is explicit;
- use log scale for multiplicative change across orders of magnitude when zero/negative values are absent and the audience can interpret it;
- use indexing when relative change from a meaningful common origin is primary.

### Reject when

- a cropped bar makes small differences look like large quantities;
- domains are tuned independently to manufacture correlation;
- normalization hides totals that change the decision;
- a free scale in small multiples invites level comparison;
- transformation is undisclosed or semantically invalid.

### Prefer instead

Use dot plots for close category values, aligned panels for unlike units, companion totals for normalized composition, and annotated overview/detail rather than an axis break.

### Escape conditions

Keep a narrow sensor/process-control line domain when deviations around tolerance are the operational question. Keep independent panel domains when only shape matters, but label the choice and do not invite magnitude comparison.

Scales are not neutral plumbing. They define the visual relationship between data values and marks.

## Baseline rules by encoding

### Bars and columns

Quantitative bar length normally requires a zero baseline because viewers interpret the full length as magnitude.

If a non-zero baseline is essential to show a narrow interval, switch to a position-based mark such as a dot/range rather than truncating bars.

### Lines and dots

A zero baseline is not automatically required because position, not filled length, carries the value. A narrower domain can be legitimate when it reveals meaningful variation.

But:

- disclose the domain through visible ticks or annotation;
- avoid a crop chosen solely to manufacture drama;
- include meaningful reference values when they change interpretation.

### Area

Because filled area visually implies magnitude from a baseline, baseline choice matters similarly to bars. Avoid arbitrary cropped baselines for filled area.

## Domain selection

Choose the domain from the analytical question, not from the desire to fill the plotting rectangle.

Consider:

- zero when magnitude from zero matters;
- meaningful thresholds or reference ranges;
- all comparable panels when cross-panel magnitude matters;
- enough headroom for labels and context without flattening variation unnecessarily.

Do not silently use different y-domains across small multiples when users are expected to compare magnitudes.

## Log scales

Use logarithmic scales when multiplicative change or orders of magnitude are genuinely the structure of interest.

Requirements:

- label the scale as logarithmic or make tick progression unmistakable;
- use meaningful powers/multiples for ticks;
- do not place zero on a standard log scale;
- avoid log transformation simply to fit extreme values if users will interpret equal visual distance as equal absolute difference.

If the audience is unlikely to understand the transformation, consider annotation, a second view, or an alternative scale.

## Indexed and normalized views

Indexing (for example, setting each series to 100 at a start date) can make relative growth easy to compare but removes absolute level.

Use when relative change is the question. Preserve or expose original magnitude elsewhere when it matters.

100% normalization is appropriate for composition share but hides total size. Do not use it when absolute totals are part of the decision.

## Dual axes

Dual axes can imply a relationship because two independently scaled shapes share one space.

Before using them, test alternatives:

- two aligned panels sharing x;
- index both series to a common baseline;
- show one metric as annotation/reference;
- normalize if relative change is truly the question.

If dual axes remain necessary:

- map each series to its axis unmistakably;
- avoid decorative domain tuning that makes shapes appear more correlated;
- avoid same-style marks that make axis ownership ambiguous;
- document units next to each series/axis.

## Axis direction

Use familiar direction unless the domain has a meaningful convention. Higher values normally go upward/rightward.

Reversed axes are acceptable for domains with established meaning (for example, rank where 1 is best) but should be obvious.

## Tick density

Ticks exist to support estimation and orientation.

Prefer:

- a small set of interpretable values;
- natural intervals;
- labels that fit without rotation when possible;
- more context where exact estimation matters;
- fewer ticks where labels or direct values already provide orientation.

Avoid:

- every possible date/category label;
- arbitrary decimal precision;
- rotated text as the default escape hatch for overcrowding;
- dense gridlines that overpower data.

## Units

Make units available where readers need them.

Patterns:

- append a unit to tick labels when short and unambiguous;
- state the unit in subtitle/axis context if repetition would be noisy;
- repeat currency/percent context in tooltips or selected values where the axis is no longer in the reader's immediate focus;
- distinguish percentage points from percent change.

Do not mix units on one scale.

## Number precision

Show no more precision than the data quality or task supports.

- Remove meaningless trailing decimals.
- Use consistent precision within a comparison.
- Do not round values so aggressively that meaningful differences disappear.
- Avoid pseudo-precision for estimates.

## Gridlines

Gridlines support value estimation and shared orientation. They are not inherently “chart junk.”

Keep when they help readers compare values across distance. Reduce contrast rather than delete them by reflex.

Remove/reduce when:

- direct value labels make them redundant;
- only one reference line matters;
- dense gridlines compete with the marks.

## Scale breaks

Treat axis breaks as a last resort. They make distance discontinuous and are easy to misread.

Prefer faceting, a log scale (when semantically valid), separate detail view, or annotation of the outlier. If a break is unavoidable, make the discontinuity visually explicit.
