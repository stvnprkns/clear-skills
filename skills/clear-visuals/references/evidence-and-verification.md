# Evidence and Verification

Use this contract for any Clear output that claims to be accessible, perceptually effective, readable, usable, or evidence-based. A polished artifact is not proof of those claims.

## Evidence ladder

Name the basis for consequential recommendations:

| Basis | Appropriate use | Do not claim |
| --- | --- | --- |
| Normative standard | Testable conformance requirements such as WCAG | That conformance proves comprehension or usability |
| Peer-reviewed empirical research | Directional perceptual or interaction evidence under comparable conditions | A universal threshold beyond the study conditions |
| Representative-user evidence | Task success for the actual audience, device, environment, and consequence | General validity outside the tested sample and conditions |
| Expert heuristic | Candidate improvement or diagnostic hypothesis | Scientific validation |
| Project convention | Cohesion and implementation consistency | Accessibility or perceptual superiority |

When sources conflict, prefer the requirement that applies to the delivery context. Otherwise expose the conflict, audience, task, and uncertainty rather than averaging incompatible guidance.

## Web accessibility baseline

Treat WCAG 2.2 Level A and AA as the default verification baseline for web output unless the project names another legal or organizational target. Test the rendered artifact, not just its source.

| Concern | Minimum check | Evidence boundary |
| --- | --- | --- |
| Text alternatives | Meaningful raster images get context-specific `alt`; decorative or redundant images get empty `alt`; complex charts and diagrams get a concise name plus an adjacent or linked structured description of the essential information. | A filename, title repetition, or exhaustive narration of every mark is not an equivalent. |
| Programmatic structure | Use native headings, lists, tables, controls, labels, and landmarks. Give inline SVG a usable name and role when it conveys meaning; hide it when nearby text already provides the equivalent. | ARIA does not repair incorrect reading order or inaccessible custom behavior. |
| Data tables | Associate headers and cells with native table markup; use `scope` for straightforward row/column relationships and explicit `id`/`headers` associations when relationships are irregular or multi-level. | Visual alignment alone does not expose table relationships. |
| Keyboard and focus | Every meaningful action works without a pointer; focus order follows the task; focus is visible and not obscured; drag-only actions have an endpoint-based alternative. | A control being focusable does not prove that its state or result is understandable. |
| Color and contrast | Do not use color as the only carrier of meaning. Verify WCAG contrast against actual foreground/background pairs: normally 4.5:1 for text, 3:1 for large text, and 3:1 for meaningful UI boundaries and graphical objects where required. | Palette names, isolated swatches, or simulated color blindness do not establish contrast or comprehension. |
| Resize, reflow, and spacing | Check text at 200% resize; reflow at the WCAG 320-CSS-pixel equivalent; and the WCAG text-spacing override without clipped, overlapping, hidden, or unusable content. | Passing one responsive breakpoint is not a reflow test. |
| Target size | Verify WCAG 2.2 AA target size: normally at least 24 by 24 CSS px or a documented exception with sufficient separation. Treat 44 by 44 CSS px as the enhanced AAA target, not an invented universal minimum. | Visible icon size and interactive hit area are different measurements. |
| Motion and updates | Respect reduced-motion preferences, make nonessential motion suppressible, keep important meaning available without animation, and announce material updates without flooding assistive technology. | A CSS media query alone does not prove that every motion path or update is covered. |

Primary accessibility basis: [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [WAI complex images](https://www.w3.org/WAI/tutorials/images/complex/), [WAI alt decision tree](https://www.w3.org/WAI/tutorials/images/decision-tree/), and [WAI tables tutorial](https://www.w3.org/WAI/tutorials/tables/).

## Perception and legibility

- Prefer encodings supported by the required task. For precision-critical quantitative comparison, position on a common scale is generally more accurately judged than angle, area, volume, or color; do not turn that ordering into a ban on lower-precision encodings when the task is overview, topology, or approximate composition.
- Keep comparison anchors simultaneously visible when exact comparison matters. Serial reveal and visual disruption add memory and change-detection costs.
- Evaluate text, color, strokes, hit areas, and labels in their rendered size, density, background, device, zoom, and viewing context. An isolated token sheet is insufficient.
- Do not assert a universal minimum chart-label size, line length, card gap, or dashboard density. CSS pixels do not guarantee a fixed physical visual angle. Use applicable standards, product constraints, and representative-user evidence.

Primary empirical basis: Cleveland & McGill, [Graphical Perception (1984)](https://doi.org/10.1080/01621459.1984.10478080); Heer & Bostock, [Crowdsourcing Graphical Perception (2010)](https://doi.org/10.1145/1753326.1753357); Rensink, O'Regan & Clark, [To See or Not to See (1997)](https://doi.org/10.1111/1467-9280.00020). Apply findings only to materially comparable tasks and conditions.

## Representative-user verification

Use user testing when readability, density, unfamiliar notation, target comfort, or task visibility depends on audience and context rather than a normative threshold.

1. Define the actual task, decision, consequence of error, device, viewport, input mode, viewing distance/environment, and required precision.
2. Recruit representative readers, including relevant disability and domain-expertise ranges; record who was not represented.
3. Test realistic data and important states: default, dense/long, empty, loading, stale/error, selected, narrow, zoomed, keyboard, and reduced motion as applicable.
4. Record task completion, substantive errors, time/effort, recovery, and confidence. Ask comprehension questions; preference alone is not evidence of understanding.
5. Compare against the current or simplest credible baseline. Change one consequential variable when causal attribution matters.
6. Report sample, conditions, protocol, results, failures, and limits. Do not convert a small directional test into a universal design law.

## Verification stack

Use the cheapest layer that can answer the claim, but do not stop before the relevant layer:

1. **Static inspection:** structure, labels, data/scale contracts, alt strategy, and obvious state coverage.
2. **Automated checks:** parsing, missing names, contrast calculations, duplicate IDs, and supported accessibility tooling. Treat results as signals, not proof.
3. **Rendered checks:** representative viewport, zoom, text spacing, color/contrast, clipping, overlap, focus, and pointer targets.
4. **Interaction checks:** keyboard order/operation, state announcements, non-hover access, reset/recovery, reduced motion, and touch behavior.
5. **Assistive-technology checks:** at least one relevant browser/screen-reader pairing for consequential web output; include table, control, update, and long-description navigation.
6. **User evidence:** representative task testing when the claim concerns comprehension, discoverability, efficiency, or comfort.

For HTML available on disk, run `python3 skills/clear-visuals/scripts/check_web_accessibility.py path/to/page.html` early. It catches only a bounded set of structural failures and always requires the rendered, interaction, assistive-technology, and user-evidence layers appropriate to the claim.

## Claim language

Use `meets [named criterion] in tested states` only when measured. Use `consistent with [source or principle]` for evidence-informed judgment. Use `passed representative-user task test under [conditions]` for observed usability. Otherwise say `not verified`.

Never write “scientifically optimized,” “fully accessible,” “visibility tested,” or “best practice compliant” without naming the source, protocol, states, results, and boundary.
