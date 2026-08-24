# Explainer Review Output

## Decision frame

- **Audience starting model**
- **Target model or decision**
- **Narrative spine**
- **Assessment**

## Findings

Use no more than five rows in a markdown table:

| Priority | Location | Current | Recommended | Why |
| --- | --- | --- | --- | --- |

Use `CRITICAL`, `HIGH`, `MEDIUM`, or `LOW`. Cite the exact scene, step, control, state, screenshot region, or `path/to/file:line`; use `Not verified` rather than inventing a location. Describe the observed sequence or behavior in **Current**, make **Recommended** actionable, and explain the mental-model or decision cost in **Why**. Consolidate one narrative root cause into one row and list every affected step. Prioritize unsupported causal claims, missing prerequisites, vanished comparison anchors, and invalid simulation behavior. Omit `LOW` polish by default; when there are no findings, omit the table and state `No actionable explainer findings`.

## Sequence revision

Include only when order is a root cause. Name the current break, revised claim order, persistent anchors, and tradeoff.

## Keep

Protect one to three working scenes, transitions, annotations, controls, or static states.

## Verification

State which first-run, back/replay, deep-link, narrow, reduced-motion, keyboard, and simulation-boundary states were inspected.

## Verdict

End with **Rethink**, **Revise**, **Refine**, or **Clear**.
