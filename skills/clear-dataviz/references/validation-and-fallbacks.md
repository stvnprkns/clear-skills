# Validation and Fallbacks

## Principle

Validate the data transformation and rendered perception separately. Source correctness does not prove visual correctness.

## Use when

- layout or aggregation is algorithmic;
- interaction changes scale, subset, or topology;
- the form uses animation, simulation, projection, or interpolation;
- a fallback is required for accessibility, print, export, or mobile.

## Reject when

- totals before and after transformation cannot be reconciled;
- ordering or random seed changes the apparent conclusion materially;
- labels/paths collide in representative data;
- fallback omits a caveat or changes the primary comparison;
- noninteractive output is unintelligible.

## Prefer instead

Test known fixtures, conservation checks, missing/extreme values, stable ordering, repeated seeds, resize states, grayscale/non-color cues, keyboard focus, reduced motion, print/export, and a baseline representation.

## Escape conditions

- Stochastic layouts may vary visually when measured conclusions remain stable; document the invariant.
- A simplified fallback can omit exploratory detail if it preserves the primary claim and links to accessible data.
- Expert-only tools may require training, but still need truthful transformations and recoverable interaction.

## Audit signals

- layout changes on refresh with no semantic reason;
- hover changes geometry rather than emphasis;
- aggregate totals drift after filtering;
- screenshot cannot communicate the primary meaning;
- accessible summary describes form but not relationship.
