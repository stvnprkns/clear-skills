# Uncertainty and Missing Data

A chart should communicate not only observed values but also the limits of what those values mean when uncertainty or missingness could affect the conclusion.

## Distinguish states that are not equivalent

Do not collapse these into one visual state:

- observed zero;
- missing / unavailable;
- not applicable;
- suppressed for privacy/sample size;
- estimated;
- provisional;
- forecast;
- incomplete current period.

Use text, gaps, patterns, opacity, line style, or explicit notes as appropriate.

## Missing time-series observations

Do not automatically connect observed points across a missing interval as though the path were measured.

Options:

- break the line;
- use a visibly different interpolation segment when an estimate is analytically justified;
- annotate the data gap;
- show markers only at observed points when gaps are central to interpretation.

Never fill missing with zero unless zero is the documented value.

## Incomplete periods

Current week/month/quarter values are often lower simply because the period is unfinished.

If comparing incomplete to complete periods:

- mark the period as partial;
- compare like-for-like elapsed windows where possible;
- project only when a projection model is defensible and clearly labeled;
- avoid presenting partial totals as a decline without context.

## Confidence and credible intervals

When interval uncertainty materially affects comparison, show it.

Common forms:

- error bars;
- interval bands;
- point + interval (often clearer than a bar);
- distribution/ensemble when shape matters.

Do not imply that overlapping intervals automatically prove “no difference” or non-overlap automatically proves a specific statistical claim unless the analytic method supports it.

## Forecasts

Separate observed history from forecast without destroying series identity.

Useful cues:

- boundary line/annotation at forecast start;
- same base hue with dashed continuation;
- interval fan/band;
- lighter or differentiated future region.

Label forecast horizon and uncertainty assumptions when they are decision-relevant.

## Estimates and modeled values

If points are estimates rather than direct observations, consider whether users need:

- uncertainty intervals;
- sample size;
- methodology note;
- model vs observed distinction.

Do not add statistical decoration when uncertainty is negligible for the task or would distract from a simple operational use case.

## Aggregation hides variation

Means, medians, totals, and rates can hide distribution and subgroup differences.

When variation changes the interpretation, supplement or replace an aggregate with:

- distribution plot;
- range/interval;
- small multiples by relevant subgroup;
- raw points (when count and privacy allow).

## Outliers

Do not silently remove outliers to make the chart cleaner.

If excluding them:

- use a defensible analytical reason;
- document the rule;
- make sure the exclusion does not reverse the conclusion.

If an outlier compresses the rest of the chart, consider faceting, log scale, detail inset, annotation, or a position-based alternative before an axis break.

## Denominators and sample size

Rates and percentages can look stable even when based on very different denominators.

Expose sample size when it changes trust or interpretation, especially for:

- small groups;
- survey estimates;
- low-volume conversion rates;
- rolling metrics with changing exposure.

## Missingness itself may be data

If missing values cluster by time, geography, customer type, or process stage, hiding them can erase a meaningful pattern.

When missingness is analytically relevant, visualize or report it explicitly rather than treating it only as a rendering problem.
