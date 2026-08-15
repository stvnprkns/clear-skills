# Case: mobile hides the decision

**Family:** Audit

## Prompt

On desktop a vendor table shows name, risk, renewal, value, owner, and actions. At 360px CSS hides every column except name and owner. Users approve renewals on phones from a row action. Audit it.

## Expected skill behavior

- Flag removal of risk, renewal, and value from the approval context.
- Recommend priority columns plus accessible row detail or controlled horizontal comparison.
- Keep identity visible and test keyboard/touch behavior.
- Do not prescribe stacked cards automatically.
