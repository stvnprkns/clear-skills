# Table Review Output

Report no more than five findings; use fewer when warranted.

## Decision frame

- **Reader and decision**
- **Lookup key**
- **Primary comparison direction**
- **Required precision**
- **Assessment** — what works and the largest obstacle

## Findings

Use no more than five rows in a markdown table:

| Priority | Location | Current | Recommended | Why |
| --- | --- | --- | --- | --- |

Use `CRITICAL`, `HIGH`, `MEDIUM`, or `LOW`. Cite the exact row, column, header, control, state, screenshot region, or `path/to/file:line`; use `Not verified` rather than inventing a location. Describe the observed table decision in **Current**, make **Recommended** actionable, and explain the retrieval, comparison, or integrity cost in **Why**. Prioritize corrupted meaning, mixed grain, inaccessible interaction, and failed comparison before polish. Omit `LOW` polish by default; when there are no findings, omit the table and state `No actionable table findings`.

One semantic root cause equals one finding. Put sorting consequences, misleading amounts, row styling, and acceptance criteria caused by the same mixed-grain structure inside that one finding. Do not split them into separate findings merely because they appear in different columns or states.

## Rethink

Include only when a table is the wrong primary representation. State the actual task, proposed form, preserved secondary table need, and tradeoff.

## Keep

Protect one to three inspected decisions such as dense spacing, semantic order, aligned numerics, stable identity, or useful sticky context.

## Verification

State which representative data, long-label, empty, loading, narrow, keyboard, and assistive states were actually inspected. Mark others `Not verified`.

## Verdict

End with exactly one: **Rethink**, **Revise**, **Refine**, or **Clear**.
