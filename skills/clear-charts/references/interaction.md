# Interaction

Interaction should expose additional understanding, not merely make a static chart feel sophisticated.

## Interaction earns itself when it enables

- detail on demand;
- comparison of subsets;
- exploration across a large domain;
- brushing/linking between related views;
- manipulation of a model or scenario;
- focus on dense overlapping data;
- navigation through meaningful hierarchy;
- responsive disclosure on constrained screens.

If the same understanding can be delivered clearly in the initial state, prefer the simpler static behavior.

## Initial state must stand on its own

Before interaction, the reader should know:

- what the chart represents;
- primary units and axes;
- major series/categories;
- the main insight or analytical affordance;
- what is interactive when interaction is central.

Do not make users “scrub for meaning.”

## Tooltips

Tooltips are secondary detail.

Good tooltip content:

- exact value where the plot emphasizes pattern;
- date/category reminder;
- secondary measures;
- sample size or metadata;
- concise explanation for an unusual point.

Bad tooltip dependency:

- series identity available only on hover;
- primary value available only on hover when exact value is critical;
- key benchmark hidden until hover;
- important caveat hidden in tooltip.

Tooltips should appear on keyboard focus as well as pointer hover when implemented on the web.

## Filtering

Use filters when users have a genuine subset-selection task.

Avoid filters that force users to reconstruct a comparison serially. If users need to compare A vs B, showing both simultaneously is often better than making them select A, remember it, then select B.

Preserve context after filtering when users need to understand what was removed.

## Highlighting / selection

Selection should create hierarchy without making unselected data disappear unnecessarily.

Useful pattern:

- selected: strong emphasis;
- related/context: muted but visible;
- unrelated: reduced prominence;
- labels/details: update near the selection.

Avoid complete disappearance unless filtering, rather than focus, is the user's explicit action.

## Zoom and pan

Use when the domain genuinely exceeds the available resolution, such as long time series or dense spatial plots.

Requirements:

- clear reset/home affordance;
- preserve orientation/context;
- do not make users zoom merely to read the basic chart;
- support keyboard or alternative controls where required.

## Brushing and linked views

Linked views are useful when a selection in one representation reveals a relationship in another.

The connection must be visually obvious. Avoid silent changes elsewhere on the screen with no selected-state cue.

## Animation

Animation should explain change, preserve object identity, or reveal causality.

Use for:

- transition between related states;
- reordering/filtering where object continuity helps;
- step-through explanation;
- simulation where motion is the phenomenon.

Avoid:

- animating every chart on load;
- long easing before users can read values;
- looping decoration;
- motion as the only cue for state change.

Respect reduced-motion preferences in interactive web implementations.

## Responsive behavior

Do not only shrink a desktop chart.

On narrow screens consider:

- fewer direct labels with priority preserved;
- shorter text;
- changed aspect ratio;
- horizontal scrolling only when preserving scale is better than compression;
- small multiples stacked vertically;
- key annotations moved to a readable region;
- explicit static values replacing hover-only detail.

Never remove the primary insight just because the screen is smaller.

## Accessibility

For interactive charts:

- all interactive elements must be reachable without a pointer;
- focus must be visible;
- interaction must not depend on color alone;
- hover behaviors need focus/touch equivalents;
- provide a text summary and/or accessible data alternative when the graphic cannot communicate equivalent information to assistive technology;
- announce meaningful selection/filter changes when appropriate to the implementation.

## Anti-pattern: gratuitous controls

Sliders, dropdowns, toggles, tabs, and playback controls create work. Add a control only when the user has a meaningful question that the control helps answer.

A static small-multiple comparison often beats a clever interactive selector because simultaneous visibility reduces memory load.
