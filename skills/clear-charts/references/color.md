# Color

Color is a channel for meaning and attention. Treat it as scarce.

## First question: what job is color doing?

Color may encode:

- category identity;
- ordered magnitude;
- divergence around a meaningful midpoint;
- status/state;
- focal emphasis;
- uncertainty/forecast distinction;
- selection in an interactive chart.

If it is doing none of these, consider a neutral color.

## Categorical color

Use distinct hues for categories when readers need category identity across space or views.

Constraints:

- keep the number of simultaneously important hues limited;
- reuse category colors consistently across related charts;
- do not assign hues randomly if categories have established semantic associations that matter;
- avoid adjacent colors that are hard to distinguish;
- provide another cue when color carries essential identity.

If categories are already directly labeled and position separates them, they may not need different hues.

## Sequential color

Use a sequential lightness/chroma progression for ordered values that move from low to high.

Rules:

- the perceptual order should match the data order;
- use sufficient contrast between meaningful steps;
- do not use a rainbow palette for a single ordered measure;
- distinguish “no data” from the lowest value.

## Diverging color

Use diverging color when there is a meaningful center such as:

- zero;
- target;
- historical average;
- neutral response;
- break-even.

Center the color scale on the meaningful value, not automatically the midpoint of observed min/max.

If there is no meaningful center, use sequential rather than diverging color.

## Emphasis

A highly effective default for explanatory charts:

- focal data: one strong emphasis color;
- context: neutral gray or restrained same-hue variants;
- annotation/reference: enough contrast to support the focal relationship without becoming another focal series.

Do not highlight five things equally and call it hierarchy.

## Gray is functional

Neutral gray is useful for:

- contextual series;
- axes;
- gridlines;
- non-data structure;
- categories that should recede.

Use multiple neutral strengths if needed; not every non-data element needs identical gray.

## Color alone is insufficient

When color communicates essential meaning, pair it with at least one of:

- direct text label;
- shape;
- line style;
- pattern;
- position;
- icon/symbol;
- explicit selected-state treatment.

This is especially important for red/green distinctions and dense categorical palettes.

## Contrast

Ensure information-critical marks remain distinguishable from their adjacent background and from each other. Thin lines and small marks generally need stronger contrast than large filled areas.

For web artifacts, respect applicable accessibility requirements for text and graphical objects. If visible labels already expose the same values/identity, they can reduce reliance on subtle graphical boundaries, but do not use this as an excuse for barely visible marks.

## Semantic color

Reserve established semantic colors when the meaning is actually present.

Examples:

- red for destructive/negative/critical when the product system uses that convention;
- green for positive/success when culturally and contextually appropriate;
- warning amber for warning state.

Do not turn all below-average values red if “below average” is not actually bad.

## Brand color

Brand is not a data encoding.

Use brand colors where they support identity and hierarchy, but do not force every category into a brand palette if it reduces discriminability or creates false semantics.

## Backgrounds

Avoid tinted plotting backgrounds unless the tint carries meaning (for example, acceptable range). A neutral background gives color encodings more room to work.

If using dark mode, re-evaluate:

- gridline prominence;
- chroma/saturation;
- text contrast;
- thin line visibility;
- adjacent categorical distinctions.

Do not mechanically invert a light palette.

## Forecast / uncertainty color

Do not use a completely unrelated hue for forecast if the viewer should understand it as the same measure continuing under a different certainty level.

Prefer continuity of identity plus a secondary cue such as:

- reduced opacity;
- dashed line;
- shaded interval;
- boundary annotation.

## Anti-patterns

- rainbow palette for ordered values;
- every bar a different saturated hue without a reason;
- using red/green as the only distinction;
- “no data” sharing the same color as zero;
- multiple unrelated meanings assigned to one hue in the same view;
- subtle low-contrast gray for information users must perceive;
- changing category colors between adjacent charts without a reason.
