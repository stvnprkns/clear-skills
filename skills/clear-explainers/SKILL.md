---
name: clear-explainers
description: >-
  Information-design judgment for choosing, sequencing, creating, auditing, and improving narrative, interactive, and causal explanations. Use for scrollytelling, step-by-step explainers, annotated stories, simulations, model explanations, causal narratives, progressive reveal, before-and-after explanations, onboarding explanations, educational interactives, and explanatory visual review.
---

# Clear Explainers

An explainer succeeds when readers build the intended mental model in a sequence they can follow, test, and retain without losing evidence or confusing narrative order with causality.

Use `clear-charts` for quantitative encodings and `clear-diagrams` for topology. This skill owns explanatory sequence, progressive reveal, narrative claims, and explanatory interaction.

## Quick Reference

| Need | Read |
| --- | --- |
| Define the mental-model change and narrative spine | [explanatory-arc.md](references/explanatory-arc.md) |
| Decide what to reveal, persist, compare, or repeat | [progressive-reveal.md](references/progressive-reveal.md) |
| Design simulation and explanatory interaction | [simulation-and-interaction.md](references/simulation-and-interaction.md) |
| Verify access, motion, comprehension, and evidence claims | [evidence-and-verification.md](../clear-visuals/references/evidence-and-verification.md) |
| Report a standalone audit | [review-output.md](references/review-output.md) |

## Operating Sequence

1. State the audience's starting model, target model, decision/use, and likely misconception.
2. Write the causal or conceptual spine as claims with evidence and dependencies.
3. Choose scenes so each adds one necessary relationship without erasing needed context.
4. Decide what stays persistent, what changes, and what readers control.
5. Separate observed evidence, interpretation, mechanism, and uncertainty.
6. Provide orientation, pacing, reversibility, and a meaningful static/default state.
7. Apply the suite evidence contract. Verify reduced motion, keyboard, narrow and zoomed layout, restart, deep-link, interrupted reading, meaningful sequence, and a nonanimated equivalent. Use representative-user tasks before claiming that the intended model was understood.
8. Report where the mental model breaks, not every decorative issue.

## Core Principles

1. **Teach a model, not a slideshow.** Every scene must change or test what the reader understands.
2. **Sequence by dependency.** Introduce concepts before consequences that rely on them; do not use chronology when causal structure is the real need.
3. **Persist comparison anchors.** Progressive reveal should reduce load, not force memory of vanished values or states.
4. **Separate evidence from narration.** Annotation may guide attention but cannot turn correlation, order, or animation into proof of cause.
5. **Let interaction answer a question.** A control should expose sensitivity, mechanism, counterfactual, or detail—not merely produce motion.
6. **Constrain simulations honestly.** Declare inputs, assumptions, valid ranges, outputs, and what the model omits.
7. **Respect reader control.** Support pause, back, replay, reduced motion, and recovery from interruption when the sequence matters.
8. **Reveal complexity at the right time.** Do not hide material caveats until after a persuasive claim.
9. **Keep orientation visible.** Readers should know where they are, what changed, and what remains constant.
10. **Preserve a strong static explanation.** Interaction and animation are not upgrades when a compact annotated view already teaches the model.

## Common Mistakes

| Mistake | Corrective question |
| --- | --- |
| Scene count as progress | What new relationship is learned here? |
| Clearing the canvas each step | Which anchors must persist for comparison? |
| Animation implies cause | What evidence supports the mechanism? |
| Slider without model contract | What assumption and output does it change? |
| Caveat at the end | Could it reverse an earlier conclusion? |
| Scroll locks user control | Can readers pause, reverse, or skip safely? |
| Narrating every mark | Which claim needs guidance? |
| Adding interaction to strong prose/chart | What understanding becomes possible only through interaction? |

## Reporting

Use [review-output.md](references/review-output.md). Prioritize broken mental-model transitions, unsupported claims, and lost comparison anchors.
