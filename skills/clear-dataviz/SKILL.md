---
name: clear-dataviz
description: >-
  Expert judgment for choosing, creating, auditing, and validating specialized or unconventional quantitative visualizations beyond standard chart grammar. Use for Sankey and alluvial diagrams, chord diagrams, parallel coordinates, streamgraphs, horizon graphs, ridgeline plots, hexbin and density maps, ternary plots, contour and surface plots, networks with quantitative encodings, uncertainty ensembles, multivariate glyphs, novel data visualization, and deciding whether an advanced form earns its complexity.
---

# Clear Dataviz

Use a specialized form only when it exposes a decision-relevant structure that a standard chart, table, or diagram cannot expose as directly. Novelty carries a comprehension and validation burden.

`clear-charts` owns standard quantitative grammar. `clear-diagrams` owns non-quantitative topology. This skill owns specialized quantitative forms and the evidence required to justify them.

## Quick Reference

| Need | Read |
| --- | --- |
| Test whether a specialized form earns itself | [complexity-test.md](references/complexity-test.md) |
| Choose among specialized form families | [specialized-forms.md](references/specialized-forms.md) |
| Validate transformations, perception, and fallbacks | [validation-and-fallbacks.md](references/validation-and-fallbacks.md) |
| Report a standalone audit | [review-output.md](references/review-output.md) |

## Operating Sequence

1. State the reader, decision, perceptual task, and why standard forms appear insufficient.
2. Establish a standard-form baseline.
3. Name the additional structure the specialized form reveals and the decoding cost it adds.
4. Validate transformation, conservation, aggregation, topology, scale, and occlusion.
5. Provide orientation, labels, examples, interaction, or a fallback proportional to unfamiliarity.
6. Test representative and adversarial data, narrow layout, color loss, and noninteractive output.
7. Prefer the baseline unless the specialized form wins materially.
8. Report both the gain and the cost.

## Core Principles

1. **Require an incremental question.** “Looks more sophisticated” is not a task.
2. **Compare against a strong baseline.** A bad bar chart is not evidence that a chord diagram is better.
3. **Expose the transformation.** Binning, smoothing, normalization, stacking, projection, and layout algorithms affect the claim.
4. **Match form to topology and quantity.** A Sankey requires meaningful flow and conserved width; a ternary plot requires three-part composition; contours require an interpretable field.
5. **Protect orientation.** Specialized encodings need a clear entry point, units, reading instructions, and stable identity.
6. **Design for approximate versus precise tasks explicitly.** Density or topology overview may justify weaker exact lookup; provide secondary detail when needed.
7. **Test edge cases.** Sparse data, zeros, negatives, missing links, extreme values, tied ranks, and small screens often break novel forms silently.
8. **Do not disguise uncertainty as texture.** Simulation and ensemble forms must explain what varies and why.
9. **Provide an exit.** When the form cannot travel to print, mobile, assistive reading, or low-literacy audiences, provide a truthful fallback.
10. **Preserve an advanced form that earns itself.** Unfamiliarity alone is not a defect for expert audiences with a real specialized task.

## Common Mistakes

| Mistake | Corrective question |
| --- | --- |
| Novel form before baseline | What does it reveal that the best standard form cannot? |
| Sankey without conservation | What quantity flows, and where is loss/gain encoded? |
| Chord for exact pair lookup | Would a matrix make the pairwise comparison easier? |
| Smoothed density as raw data | Which transformation produced the shape? |
| Beautiful network hairball | Is topology overview or path lookup the task? |
| Interaction as explanation | What survives in the default/static state? |
| Rejecting expert notation | Does the intended audience already read it fluently? |

## Reporting

Use [review-output.md](references/review-output.md). Always state the standard baseline, incremental gain, decoding cost, and validation boundary.
