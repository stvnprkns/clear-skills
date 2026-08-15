# Case: mixed row grain

**Family:** Audit

## Prompt

Audit a revenue table where most rows are individual invoices, some rows are customer monthly subtotals, and a final row is annual company revenue. All rows share the same styling and sortable amount column.

## Expected skill behavior

- Identify mixed row entities as an integrity/comparison failure.
- Separate detail, grouped subtotals, and grand total semantically and visually.
- Prevent sorting totals as ordinary records.
- Prioritize grain over cosmetic styling.
