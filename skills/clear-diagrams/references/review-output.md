# Diagram Review Output

Use at most five findings and prioritize topology and truth before visual polish.

## Decision frame

- **Reader and decision**
- **Relationship to trace**
- **Scope and truth status**
- **Assessment** — what works and the primary obstacle

## Findings

Use no more than five rows in a markdown table:

| Priority | Location | Current | Recommended | Why |
| --- | --- | --- | --- | --- |

Use `CRITICAL`, `HIGH`, `MEDIUM`, or `LOW`. Cite the exact node, edge, group, path, screenshot region, or `path/to/file:line`; use `Not verified` rather than inventing a location. Describe the observed structure in **Current**, make **Recommended** actionable, and explain the tracing or truth cost in **Why**. Consolidate one topological cause into one row and list every affected location. Treat wrong topology, ambiguous edge semantics, false boundaries, and unreadable primary paths as higher priority than spacing or icon style. Omit `LOW` polish by default; when there are no findings, omit the table and state `No actionable diagram findings`.

## Rethink

Include only when the diagram family is mismatched. Name the actual topology, replacement, preserved information, and cost.

## Keep

Protect one to three inspected choices such as familiar notation, clear direction, stable grouping, or an intentionally schematic layout.

## Verification

State whether source semantics, rendered overview/detail, alternate/error paths, narrow layout, and non-color reading were inspected. Mark unknown states `Not verified`.

## Verdict

End with exactly one: **Rethink**, **Revise**, **Refine**, or **Clear**.
