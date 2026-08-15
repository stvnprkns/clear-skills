# Accessibility

## Principle

Provide equivalent access to the chart's purpose, structure, key relationships, and available actions. Do not treat alt text as a substitute for an unusable interaction or an inaccessible data structure.

## Use when

- creating or auditing web, app, document, or presentation charts;
- color, hover, animation, dragging, or dense visual comparison carries meaning;
- the chart updates after filtering or selection;
- the audience or publication standard requires nonvisual access.

## Reject when

Reject implementations where:

- essential identity or status uses color alone;
- the only values or caveats exist on pointer hover;
- keyboard users cannot reach or operate meaningful controls;
- focus order follows SVG/DOM accidents rather than reading order;
- a generic image label repeats the title but omits the chart's takeaway;
- auto-updating content interrupts reading without control.

## Prefer instead

- Give the figure a concise title and purpose.
- Provide a nearby summary of the key relationship, not every mark.
- Offer underlying data in an accessible table or structured equivalent when exact values matter.
- Pair color with labels, position, shape, stroke, or pattern.
- Expose tooltip content on keyboard focus and keep primary meaning persistent.
- Make filters and legend controls native, named, focus-visible, and operable without dragging.
- Announce meaningful updates without flooding a live region.
- Respect reduced motion and avoid animation as the sole explanation of change.

## Escape conditions

- Do not duplicate a full data table when it creates noise and exact retrieval is irrelevant; a concise summary may be sufficient.
- Do not add patterns to every categorical chart when direct labels already provide equivalent identity.
- Canvas can be appropriate when performance requires it, but provide a semantic companion and operable controls.
- Not every decorative gridline or mark needs individual exposure to assistive technology.

## Examples

**Five interactive lines:** Persist series names at line ends or in a compact legend. Keep exact values in focusable tooltips and provide the data table if lookup matters.

**Static report chart:** Use a figure label, descriptive title, concise relationship summary, source/note, and accessible document reading order. Do not narrate every coordinate.

## Audit signals

- “hover to see” instruction with no focus behavior;
- red/green-only state;
- unlabeled chart controls;
- SVG marks receiving hundreds of meaningless tab stops;
- mobile tap targets overlap dense marks;
- responsive layout clips labels or removes the only legend;
- screenshot/PDF lacks adjacent text equivalent;
- accessibility claim is based on source inspection without runtime verification.
