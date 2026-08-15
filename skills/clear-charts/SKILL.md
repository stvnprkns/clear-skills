---
name: clear-charts
description: >-
  Expert information-design judgment for choosing, creating, auditing, and rethinking quantitative charts under ambiguity. Use for charts, graphs, plots, time series, rankings, comparisons, distributions, dashboards, axes, scales, legends, labels, annotations, color, uncertainty, tooltips, responsive charts, chart review, or when the requested chart may be the wrong representation.
---

# Clear Charts

A chart is a decision interface. Optimize the comparison a reader must make, not the form requested or the statistically most interesting pattern.

Do not begin with chart type. Establish the decision, reader, question, perceptual task, and evidence needed. Treat the requested form as a hypothesis. When several forms are defensible, compare what each makes easy, what it hides, and what would make it fail.

Prioritize comprehension and integrity before polish. Recommend the smallest intervention that fixes the root problem. Preserve a strong chart explicitly; criticism is not the default outcome.

`clear-tables` owns exact-value retrieval and dense tables. `clear-diagrams` owns processes and non-quantitative relationships. `clear-dashboards` owns multi-view environments. `clear-explainers` owns narrative sequencing and explanatory interaction. Use those skills when available; do not copy their rules here.

## Quick Reference

| Need | Read |
| --- | --- |
| Frame the decision and actual question | [choosing-the-question.md](references/choosing-the-question.md) |
| Challenge the requested form | [rethink-the-chart.md](references/rethink-the-chart.md) |
| Choose among plausible chart families | [chart-selection.md](references/chart-selection.md) |
| Resolve overlay, small multiple, ranking, and encoding tradeoffs | [encoding-and-comparison.md](references/encoding-and-comparison.md) |
| Build axes, marks, overlays, and linked states from one coordinate contract | [chart-construction.md](references/chart-construction.md) |
| Judge baselines, domains, normalization, and dual axes | [scales-and-axes.md](references/scales-and-axes.md) |
| Decide what to label or annotate | [labels-and-annotation.md](references/labels-and-annotation.md) |
| Use color for identity, order, state, or emphasis | [color.md](references/color.md) |
| Handle estimates, missingness, and incomplete periods | [uncertainty-and-missing-data.md](references/uncertainty-and-missing-data.md) |
| Decide whether interaction earns its cost | [interaction.md](references/interaction.md) |
| Audit nonvisual access and input modes | [accessibility.md](references/accessibility.md) |
| Trace empirical findings to rules and escape conditions | [research-foundations.md](references/research-foundations.md) |
| Report a concise, evidence-backed review | [review-output.md](references/review-output.md) |

## Operating Sequence

1. **Frame** — State the decision, reader, actual question, and required perceptual task. Separate them from the requested form.
2. **Generate** — Name two or three plausible representations, including a table or no chart when credible.
3. **Trade off** — For each candidate, state what becomes easy, what becomes hard, and its rejection condition.
4. **Choose** — Select the representation whose primary encoding matches the task. Decision relevance outranks visual or statistical novelty.
5. **Inspect** — Use rendered evidence. Trace labels, marks, overlays, and pointer/focus states back to their scale and plot bounds when alignment or interaction is involved. When a supported chart specification is available, run `scripts/inspect-chart.py`; treat its output as evidence, never a verdict.
6. **Intervene** — Fix the smallest number of root causes. Prefer one shared coordinate/state contract over local pixel corrections. Do not redesign sound choices.
7. **Verify** — Check the rendered default, important states, narrow layout, non-hover access, and data/scale claims when available.
8. **Report** — Use the review contract. Distinguish observed, inferred, and unverified claims.

## Core Principles

### 1. Optimize the perceptual task

Translate the question into an operation the eye must perform: lookup, rank, compare magnitude, compare change, trace a path, find a threshold crossing, assess distribution, judge association, or inspect composition. A chart that contains the data but obscures that operation is not task-fit.

### 2. Make alternatives compete

Do not jump from problem to favorite chart. For ambiguous cases, compare candidates explicitly. Prefer overlay for same-position comparison, small multiples for individual shape and identity, indexed views for relative change, and ranked deltas for endpoint change—but only when their rejection conditions do not apply.

### 3. Show decision-relevant structure

The most statistically unusual feature is not automatically the most useful one. Emphasize it only when it could change a decision, interpretation, or next action. Preserve material caveats even when they are not the headline.

### 4. Make the important comparison explicit

Do not make readers perform arithmetic or serial memory work the design can perform. Encode deltas, ranks, thresholds, references, or uncertainty directly when they are the question.

### 5. Make geometry share one source of truth

Every element that claims to occupy the same data coordinate—axis label, tick, point, guide, hover target, annotation, or selection cursor—must derive from the same domain, plot bounds, and scale function. CSS distribution and chart-scale math are not interchangeable. Fix the coordinate contract before nudging individual marks.

### 6. Treat scales and omission as arguments

Domains, baselines, normalization, aggregation, missingness, filtering, and partial periods all shape the claim. Reject choices that manufacture drama or erase material context. A zero baseline is normally required for bar length; it is not a universal rule for position-based charts.

### 7. Spend attention deliberately

Color, annotation, line weight, and interaction allocate attention. Highlight only when the focal series is decision-relevant and the remaining context stays sufficient to interpret it. Equal prominence is not neutrality when one relationship matters more.

### 8. Keep primary meaning persistent

Hover, selection, and animation may add detail but must not contain the only series identity, value needed for the decision, benchmark, caveat, or instruction.

### 9. Preserve valid complexity

Gridlines, multiple colors, interaction, and non-zero domains can be correct. Keep them when they support the task, identity across views, precision, or accessible exploration. Rules are evidence prompts, not automatic verdicts.

### 10. Know when to do nothing

If representation, integrity, hierarchy, labeling, and access already support the question, say so. Do not invent a quota of improvements. A review may conclude `Clear` with only verification notes.

## Common Mistakes

| Mistake | Corrective question |
| --- | --- |
| Accepting the requested form | What is the actual decision and perceptual task? |
| Naming one plausible chart immediately | What credible alternative exposes the comparison better? |
| Applying a rule mechanically | What is the rule's escape condition here? |
| Treating statistical interest as importance | Would this feature change a decision or explanation? |
| Hiding context to strengthen emphasis | What comparison or base rate disappears? |
| Fixing label/point drift with offsets | Which domain, range, inset, and scale should both use? |
| Giving each repeated chart its own hover state | Is the reader comparing one shared domain value across rows? |
| Listing every imperfection | Which one to three root changes materially improve understanding? |
| Inferring runtime behavior from source | Which rendered states remain unverified? |
| Treating detector output as truth | Does the surfaced evidence matter in this context? |
| Redesigning an already strong chart | What concrete task or integrity failure justifies change? |

## Reporting

Use [review-output.md](references/review-output.md). A complete audit names the actual question, gives a verdict, reports only high-leverage findings, protects working decisions, and states verification limits.
