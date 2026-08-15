# Case: Sankey without conservation

**Family:** Audit

## Prompt

Audit a Sankey of website visits where each stage independently counts events, users can repeat events, and outgoing widths do not reconcile with incoming widths. The title says “Where every user goes.”

## Expected skill behavior

- Flag false flow/conservation semantics and the unsupported “every user” claim.
- Clarify whether the data are paths, transitions, or independent event counts.
- Choose a valid transition/flow form or standard comparisons.
- Do not fix only labels or colors.
