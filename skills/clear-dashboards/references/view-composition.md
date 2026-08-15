# View Composition

## Principle

Compose views as an argument from state to explanation to detail, not as independent rectangles.

## Use when

- summary and detail must coexist;
- a selection in one view explains another;
- charts and tables serve complementary pattern/lookup tasks;
- spatial hierarchy can reduce search.

## Reject when

- every card has equal weight regardless of consequence;
- views repeat the same measure without adding a comparison;
- legends, periods, units, or identities drift between views;
- cross-filtering silently changes unrelated totals;
- layout order follows implementation rather than reading priority.

## Prefer instead

Use a hierarchy such as:

```text
scope + freshness
→ material state / exception
→ drivers and comparison
→ affected entities
→ action or deeper investigation
```

Keep common controls near their scope. Align related views. Use chart for pattern and table for exact affected records rather than forcing either to do both.

## Escape conditions

- A dense expert console may prioritize simultaneous visibility over spacious hierarchy.
- Equal-sized panels can work for symmetric monitoring units with equal consequence.
- Repetition can aid comparison when geometry and scales are deliberately consistent.

## Audit signals

- most important exception is below decorative summaries;
- layout requires zig-zag reading;
- same color changes meaning across cards;
- filters affect hidden or surprising views;
- detail has no route back to overview.
