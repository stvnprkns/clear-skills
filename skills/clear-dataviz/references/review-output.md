# Specialized Dataviz Review Output

## Decision frame

- **Reader and task**
- **Standard baseline**
- **Specialized form and incremental gain**
- **Decoding/implementation cost**
- **Assessment**

## Findings

Use no more than five rows in a markdown table:

| Priority | Location | Current | Recommended | Why |
| --- | --- | --- | --- | --- |

Use `CRITICAL`, `HIGH`, `MEDIUM`, or `LOW`. Cite the exact mark, transformation, interaction, screenshot region, or `path/to/file:line`; use `Not verified` rather than inventing a location. Describe the observed state in **Current**, make **Recommended** actionable, and explain the decoding, integrity, or accessibility cost in **Why**. Consolidate one root cause into one row. Prioritize invalid transformation, false topology, conservation failures, and inaccessible primary meaning. Omit `LOW` polish by default; when there are no findings, omit the table and state `No actionable specialized-dataviz findings`.

## Keep

Protect specialized choices that materially outperform the baseline for the intended audience.

## Verification

Report transformation checks, representative/extreme data, resize, static fallback, color/access, interaction, and stability actually tested.

## Verdict

End with **Rethink**, **Revise**, **Refine**, or **Clear**.
