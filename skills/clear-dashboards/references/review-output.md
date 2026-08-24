# Dashboard Review Output

## Decision frame

- **Audience, decision, cadence**
- **Current scope and freshness**
- **Primary path:** monitor → diagnose → decide/act
- **Assessment**

## Findings

Use no more than five rows in a markdown table:

| Priority | Location | Current | Recommended | Why |
| --- | --- | --- | --- | --- |

Use `CRITICAL`, `HIGH`, `MEDIUM`, or `LOW`. Cite the exact view, control, state, screenshot region, or `path/to/file:line`; use `Not verified` rather than inventing a location. Describe the observed state in **Current**, make **Recommended** actionable, and explain the decision or comprehension cost in **Why**. Consolidate systemic issues and list every affected location in one row. Prioritize metric integrity, misleading state, broken hierarchy, and lost scope before individual chart polish. Omit `LOW` polish by default; when there are no findings, omit the table and state `No actionable dashboard findings`.

## Cross-view effects

For each systemic change, name affected views, controls, and responsive states. Do not repeat the same root cause as separate card findings.

## Keep

Protect inspected hierarchy, quiet states, coordinated filters, or useful density.

## Verification

State which default, filtered, stale, empty, loading, error, partial, narrow, keyboard, and action states were tested.

## Verdict

End with **Rethink**, **Revise**, **Refine**, or **Clear**.
