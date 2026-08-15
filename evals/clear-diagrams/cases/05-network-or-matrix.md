# Case: dense dependency graph

**Family:** Create

## Prompt

Design a view of dependencies among 80 software packages. Engineers need to find direct dependents of a selected package and identify highly coupled clusters; tracing every path at once is not required.

## Expected skill behavior

- Separate overview cluster perception from selected-node dependency lookup.
- Consider network overview with selection/detail or adjacency matrix based on density and labels.
- Avoid promising global edge traceability in a hairball.
- State the tradeoff between cluster overview and exact paths.
