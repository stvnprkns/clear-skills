# Consolidated Review

## Assessment

State the reader, actual question, chosen representation strategy, what works, and the largest obstacle in no more than four sentences.

## Findings

Report no more than five cross-domain root causes in a markdown table:

| Priority | Owner | Location | Current | Recommended | Why |
| --- | --- | --- | --- | --- | --- |

- **Priority:** use `CRITICAL`, `HIGH`, `MEDIUM`, or `LOW` and order rows by impact, then leverage.
- **Owner:** name one Clear domain.
- **Location:** cite the exact view, component, chart element, screenshot region, or `path/to/file:line`; use `Not verified` rather than inventing precision.
- **Current:** describe the observed design decision, including affected views or domains when systemic.
- **Recommended:** give a concrete change and name downstream states or views that must change with it.
- **Why:** explain the effect on comprehension, integrity, or decision effort.

Omit `LOW` polish by default. When there are no findings, omit the table and state `No actionable visual findings`.

Do not include a finding from every domain by default. When two owners identify the same root cause, assign it to the primary decision owner and mention secondary effects.

## Representation rethink

Include only when the overall form is mismatched. State requested form, actual question, task, primary form, secondary need/form, tradeoff, and migration constraints.

## Keep

Protect two or three inspected system-level decisions: visual language, stable identity, hierarchy, interaction, notation, or density.

## Verification

Separate rendered artifact, source semantics, data integrity, responsive states, interaction, and accessibility. Never infer runtime success from source alone.

## Verdict

End with exactly one: **Rethink**, **Revise**, **Refine**, or **Clear**.
