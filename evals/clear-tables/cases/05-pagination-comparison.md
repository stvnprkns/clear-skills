# Case: pagination breaks comparison

**Family:** Audit

## Prompt

Analysts compare 60 ranked proposals against one another, but the table paginates 10 rows at a time and resets selection and sort state on every page. What should change?

## Expected skill behavior

- Identify serial memory and state loss as the root problem.
- Preserve ranking and comparison context across navigation.
- Consider virtualized/scrolling view, larger pages, pinned selections, or a comparison tray based on performance constraints.
- Do not assume pagination is always wrong.
