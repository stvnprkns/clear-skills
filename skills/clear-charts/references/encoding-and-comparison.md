# Encoding and Comparison

The visual encoding determines what the eye can compare easily. Put the most important quantitative relationship in the strongest available channel.

## Encoding hierarchy for precise comparison

As a practical default when accuracy matters:

1. position on a common aligned scale;
2. length from a common baseline;
3. position on unaligned scales / slope;
4. angle or direction;
5. area;
6. volume;
7. color lightness/saturation.

This is not a universal scoring table. The rule is: **use the most perceptually direct encoding that fits the task and preserves the data's structure.**

## Common baseline

A common baseline dramatically reduces comparison effort.

### Strong uses

- bars sharing zero;
- dots sharing one axis;
- aligned small multiples sharing a scale;
- reference-line comparisons where all values are judged against the same target.

### Warning signs

- interior stacked segments that require comparing floating lengths;
- independent mini-charts with different unannounced scales;
- bubbles that require comparing area across distant positions;
- multiple donut charts used for close percentage comparisons.

## Sort to reveal the question

Default order should communicate structure.

Use:

- descending/ascending order for ranking;
- chronological order for time;
- meaningful domain order for ordinal stages;
- a consistent order across small multiples when cross-panel comparison matters.

Do not alphabetize categories by default when magnitude is the story.

Preserve conventional or semantic order when re-sorting would destroy meaning: weekdays, lifecycle stages, survey scales, age bands, geographic paths.

## Derive the comparison when that is the question

If the reader needs a delta, percent change, variance to target, or rank movement, consider encoding that derived quantity directly rather than expecting subtraction from raw marks.

Patterns:

- actual vs target → actual mark + reference target or variance view;
- before vs after → endpoints connected by slope/dumbbell;
- many time series, question is “who moved most?” → calculate change and rank it;
- current vs previous period → highlight delta near the current value while retaining enough raw context to avoid hiding scale.

Do not derive a metric whose definition materially changes the interpretation without labeling it.

## Small multiples

### Decision framework: many time series

| Candidate | Use when | Reject when | Cost accepted |
| --- | --- | --- | --- |
| Overlay | precise same-x comparison or crossings matter; few series remain distinguishable | identity tracing, occlusion, or color decoding dominates | individual shapes compete |
| Highlighted overlay | one series is focal and context defines whether it is unusual | highlight predetermines an open-ended discovery task or hides materially different peers | context is less individually readable |
| Small multiples | individual shape and identity matter; shared axes preserve level comparison | panel count defeats scanning or free scales would hide magnitude | same-x comparison requires eye travel |
| Indexed overlay | relative growth from a meaningful common origin matters | starting values or absolute exposure change the decision | absolute magnitude is suppressed |
| Ranked delta | endpoints and prioritization matter more than path | reversals, timing, or volatility explain the decision | intermediate trajectory moves secondary |

For eight series, do not choose by count alone. Ask whether the reader must trace identity, compare at the same date, compare overall shape, or rank change.

Keep scales shared when magnitude comparison across panels matters. Use free scales only when shape is explicitly the task, disclose them prominently, and reject them if level is decision-relevant. Keep ordering and visual grammar stable across panels.

### Highlighting without distortion

Use emphasis when the focal series is selected by the reader, named by the decision, or justified by a stated threshold. Preserve enough context to judge whether it is representative.

Reject emphasis when it:

- implies importance only because a series was preselected;
- mutes a peer that would reverse the conclusion;
- uses a strong hue to suggest good/bad without that semantic basis;
- turns an exploratory question into a predetermined story.

Escape condition: coordinated views may keep one identity color across all panels even when no series is globally “most important”; consistency, not rhetorical emphasis, is doing the work.

## Layering

Layer marks only when the relationship between layers is meaningful.

Good:

- observations + target/reference;
- points + interval;
- actual + forecast with a clear boundary;
- historical context in neutral tone + focal series in emphasis color.

Bad:

- several unrelated metrics on one plot because they share dates;
- line + bar + area simply to create richness;
- reference bands so numerous that the data becomes secondary.

## Size and area

When size encodes value, encode by **area**, not radius or diameter. Even with correct area scaling, expect lower precision than position/length.

Use size primarily for pattern or salience, not exact ranking among similar values.

If small values disappear, do not “fix” them with a nonlinear size mapping without clearly understanding how the transformation changes perception.

## Line weight and mark size

Visual weight should reflect hierarchy, not value unless weight/size is the explicit encoding.

- focal series may be thicker or more opaque;
- contextual series should recede;
- avoid thick lines that obscure crossings or local variation;
- point markers should not cover meaningful nearby values.

## Overplotting

When many observations collide:

Consider:

- transparency;
- smaller marks;
- jitter for categorical axes;
- hex/bin density;
- contours;
- faceting;
- sampling only when analytically defensible and disclosed.

Do not solve overplotting by simply adding random color.

## Composition

When showing part-to-whole:

- verify parts actually sum to the whole represented;
- distinguish absolute composition from proportional composition;
- order stacked components consistently;
- put the most important comparable segment on a baseline when possible;
- avoid too many thin segments.

If each segment needs accurate cross-category comparison, unstack it.

## Reference values

Reference lines and bands are powerful when they encode a meaningful comparison such as:

- target;
- budget;
- zero;
- median/benchmark;
- historical range;
- acceptable threshold.

Label the meaning directly. A reference line with no explanation is chart furniture.

## Anti-pattern: visual equality for unequal importance

If one relationship is the reason the chart exists, do not render every series, label, gridline, and annotation with equal contrast.

Create hierarchy through:

- position/order;
- opacity;
- neutral vs emphasis color;
- annotation;
- line weight;
- selective labels.

The goal is not to hide context. It is to keep context from competing with the answer.
