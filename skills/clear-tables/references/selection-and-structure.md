# Selection and Structure

## Principle

Choose a table when exact retrieval or multi-attribute comparison dominates. Define its grain before styling.

## Use when

- readers find a known entity and retrieve several fields;
- precise values, dates, identifiers, or text matter;
- alternatives share attributes that must be compared;
- users must verify, edit, export, or reconcile records.

## Reject when

- the primary task is trend, distribution, relationship, or spatial pattern;
- rows mix incompatible entities or time grains;
- the table exists only because it mirrors a database;
- every answer requires scanning all cells and performing arithmetic.

## Prefer instead

| Task | Primary form | Secondary form |
| --- | --- | --- |
| known-item lookup | searchable table | detail drawer |
| compare 2–4 alternatives by attributes | alternatives as columns | recommendation summary |
| compare many entities by measures | entities as rows | inline bars for one key measure |
| find distribution/outliers | chart | table for exact selected values |
| edit records | editable grid/form | audit history |

### Decision funnels

When one dataset supports elimination, portfolio comparison, and finalist inspection, keep one authoritative table but give each stage a deliberate state:

1. **Eliminate** with explicit hard-constraint results. Keep excluded rows recoverable and name every failure reason.
2. **Compare** viable rows with declared measure directions. If showing dominance, define it against the eligible set and selected measures; never present it as an unexplained overall score.
3. **Shortlist** two to four alternatives in a transposed attribute-by-alternative comparison when simultaneous exact comparison is the final task.

Persist filters, excluded counts, shortlist membership, and source values across these states. Do not make readers reconstruct a decision after switching modes.

## Escape conditions

- A short prose list can beat a two-column table when sequence and explanation matter more than alignment.
- A card layout can work when each entity has distinct actions and cross-entity comparison is secondary.
- Transpose a table when there are few alternatives and many attributes, but reject horizontal overflow that hides the comparison.

## Examples

For 18 vendors with value, renewal date, SLA, owner, risk, and discount, use vendors as rows. Put identity, risk, renewal, and value before secondary fields. Sort by actionable risk/renewal by default; support name lookup separately.

## Audit signals

- unclear row entity;
- repeated values indicating an undeclared hierarchy;
- totals mixed with detail but styled identically;
- units embedded inconsistently in cells;
- primary key scrolls out of view;
- card grid forces vertical memory for comparison.
