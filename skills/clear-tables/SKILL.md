---
name: clear-tables
description: >-
  Information-design judgment for choosing, creating, auditing, and improving tables used for exact retrieval, dense comparison, ranking, and multi-attribute decisions. Use for data tables, comparison tables, matrices, leaderboards, schedules, financial tables, wide or responsive tables, sorting, filtering, pagination, frozen columns, inline visualization, column alignment, row density, and table accessibility.
---

# Clear Tables

A table succeeds when readers can find the right row, understand the schema, compare the relevant values, and act without decoding avoidable structure.

Start from the retrieval or comparison task. Do not turn a table into a chart merely because it is dense, or preserve a grid when the actual task is pattern perception.

`clear-charts` owns visual pattern and quantitative encoding. `clear-dashboards` owns tables inside multi-view environments. `clear-visuals` owns cross-domain routing and consolidation when available.

## Quick Reference

| Need | Read |
| --- | --- |
| Decide whether a table is primary and orient its schema | [selection-and-structure.md](references/selection-and-structure.md) |
| Tune ordering, hierarchy, density, and inline encodings | [scan-and-density.md](references/scan-and-density.md) |
| Design sorting, filtering, responsive behavior, and access | [interaction-and-accessibility.md](references/interaction-and-accessibility.md) |
| Verify access, density, target size, and evidence claims | [evidence-and-verification.md](../clear-visuals/references/evidence-and-verification.md) |
| Report a standalone audit | [review-output.md](references/review-output.md) |

## Operating Sequence

1. State the reader, decision, lookup key, comparison direction, and required precision.
2. Decide whether the primary task is retrieval, comparison, pattern perception, or editing.
3. Choose row grain and column semantics; reject mixed grains and ambiguous derived fields.
4. Order rows and columns around the dominant task, not source-system order.
5. Establish hierarchy with alignment, whitespace, rules, typography, and restrained state color.
6. Add sorting, filtering, freezing, expansion, or pagination only for real tasks.
7. Apply the suite evidence contract. Verify native header relationships, representative, empty, long-label, narrow, zoomed, text-spacing, keyboard, target-size, and assistive states.
8. Report the smallest set of changes that improves retrieval or decision quality.

In review, consolidate all symptoms of one semantic defect. Mixed row grain plus its sorting and styling consequences is one finding, not a quota of adjacent findings.

## Core Principles

1. **One row, one declared entity.** If rows mix vendors, contracts, and subtotals without explicit hierarchy, comparisons become untrustworthy.
2. **Optimize the dominant comparison direction.** Put items in rows for scanning many entities; put alternatives in columns when a small set must be compared attribute by attribute.
3. **Put identity and decisions first.** Keep the lookup key and decision-critical state visible; move provenance and secondary metadata later or into detail.
4. **Sort by the question.** Preserve semantic order when it carries meaning; otherwise rank by the measure driving action. Alphabetical is for known-item lookup, not a neutral default.
5. **Align by data type.** Left-align text, align comparable numbers on place/decimal, use consistent units and precision, and distinguish percent from percentage-point change.
6. **Use density intentionally.** Dense tables can be excellent for expert scanning. Reject spacious card grids when they reduce simultaneous comparison; reject compression when rows become inseparable or targets unusable.
7. **Make hierarchy survive color loss.** Use grouping, indentation, labels, position, weight, and rules; reserve color for state or restrained emphasis.
8. **Keep derived meaning inspectable.** Define totals, rates, deltas, ranks, nulls, estimates, and freshness. Never make “—” ambiguously mean zero, missing, or not applicable.
9. **Interaction must preserve comparison.** Filtering and pagination must not make users remember hidden values needed for a decision.
10. **Know when not to change it.** Keep a dense, plain table when it already supports fast exact comparison better than a more visual alternative.

## Common Mistakes

| Mistake | Corrective question |
| --- | --- |
| Cardifying every row | Which values must remain simultaneously comparable? |
| Default alphabetical order | Is lookup or prioritization the task? |
| One badge color per state | Would the hierarchy survive grayscale or low vision? |
| Freezing many columns | What is the minimum context needed while scrolling? |
| Hiding fields on mobile | Which task becomes impossible when they disappear? |
| Showing every decimal | What precision can change the decision? |
| Treating blanks as zero | Which null state is actually present? |
| Adding mini charts everywhere | Does pattern perception outweigh exact retrieval here? |

## Reporting

Use [review-output.md](references/review-output.md). A review may conclude `Clear`; never invent density or styling problems to fill a quota.
