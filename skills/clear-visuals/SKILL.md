---
name: clear-visuals
description: >-
  Umbrella information-design orchestration for choosing among charts, tables, diagrams, dashboards, explainers, and specialized quantitative visualizations, coordinating multi-domain creation or review, and consolidating findings without duplicated rules. Use when the representation is undecided, an artifact crosses multiple visual-information domains, or the user requests a holistic visual audit.
---

# Clear Visuals

Choose the representation that reduces the reader's work without distorting meaning. Route domain decisions to their owner, then consolidate around the user's question rather than merging lint lists.

This skill owns representation-level orchestration, cross-domain conflicts, review priority, and final consolidation. It does not duplicate chart, table, diagram, dashboard, explainer, or specialized-form rules.

## Quick Reference

| Need | Read |
| --- | --- |
| Route a question to one or more domain owners | [routing.md](references/routing.md) |
| Create a representation brief before implementation | [representation-brief.md](references/representation-brief.md) |
| Resolve cross-domain conflicts and consolidate review | [consolidated-review.md](references/consolidated-review.md) |

## Domain Owners

| Domain | Owner | Primary decision |
| --- | --- | --- |
| Quantitative charts | `clear-charts` | encoding, scale, chart interaction |
| Exact/dense comparison | `clear-tables` | row/column structure, retrieval, scanability |
| Systems and relationships | `clear-diagrams` | topology, boundaries, traceability |
| Multi-view environments | `clear-dashboards` | KPI hierarchy, controls, cross-view state |
| Narrative explanations | `clear-explainers` | sequence, progressive reveal, simulation |
| Specialized quantitative forms | `clear-dataviz` | complexity justification and validation |

## Operating Sequence

1. State the reader, decision/informational purpose, material questions, constraints, and evidence.
2. Split the artifact into primary and secondary cognitive tasks.
3. Route each task to one owner; use multiple owners only when decisions truly cross domains.
4. Ask owners for candidate, rejection condition, tradeoff, and preserved decisions—not exhaustive findings.
5. Resolve conflicts by the primary user task, integrity, accessibility, and system constraints.
6. Consolidate root causes across domains; remove duplicates and implementation preferences.
7. Verify the whole artifact's reading order, responsive behavior, states, and handoffs.
8. Report one representation decision and a prioritized cross-domain review.

## Core Principles

1. **Choose the question before the medium.** “Make it visual” does not require a chart.
2. **Assign one owner per rule.** Secondary skills report effects; they do not redefine the rule.
3. **Use the fewest domains needed.** More skill context can dilute judgment.
4. **Primary task breaks ties.** Exact retrieval favors tables; pattern perception charts; topology diagrams; recurring multi-view action dashboards; mental-model sequence explainers.
5. **Integrity outranks cohesion.** Do not preserve visual consistency when it creates a misleading scale, mixed grain, false boundary, or hidden caveat.
6. **Cohesion outranks local perfection after integrity.** A locally ideal component can be wrong if it breaks cross-view identity, order, or interaction.
7. **Consolidate root causes.** One broken information hierarchy may create chart, table, and layout symptoms; report it once.
8. **Preserve the visual system when defensible.** Do not replace libraries, notation, or style merely because another implementation is preferred.
9. **Separate observed from inferred.** Rendered behavior, source semantics, data validity, and accessibility require different evidence.
10. **Allow `Clear`.** A holistic review does not need a finding from every domain.

## Common Mistakes

| Mistake | Corrective question |
| --- | --- |
| Loading every domain skill | Which decisions actually cross ownership boundaries? |
| Calling every visual a chart | Is the task pattern, lookup, topology, monitoring, or explanation? |
| Merging all findings | Which root cause explains several symptoms? |
| Letting local rules conflict | Which choice supports the primary task without integrity loss? |
| Recommending a new stack | What user-facing failure requires it? |
| One finding per domain | Is there real evidence, or are we filling a taxonomy? |

## Reporting

Use [consolidated-review.md](references/consolidated-review.md). Domain review contracts are inputs; this skill owns the final order, deduplication, and verdict.
