# Interaction and Accessibility

## Principle

Use interaction to reduce search while preserving orientation, comparison, and semantic table structure.

## Use when

- sorting answers repeatable ranking questions;
- filters target real subsets;
- sticky headers/identity preserve context in a long or wide table;
- row expansion reveals secondary detail without breaking the primary scan;
- virtualization is necessary for performance.

## Reject when

- pagination splits values that must be compared;
- filter state is hidden or impossible to clear;
- sort direction or priority is ambiguous;
- horizontal scroll separates row identity from values;
- virtualization breaks focus, screen-reader row counts, or find-in-page without mitigation;
- a responsive layout silently removes decision-critical columns.

## Prefer instead

Use native table semantics for read-only grids. Give every header an unambiguous accessible name and scope/association. Make sortable headers buttons with current sort state. Preserve focus during updates. Provide a summary/caption, meaningful empty states, and explicit null labels.

On narrow screens, choose among priority columns + row detail, controlled horizontal scroll with sticky identity, or a task-specific alternate view. Do not stack every cell into cards by default.

When horizontal overflow preserves a legitimate wide comparison, expose it: keep row identity pinned, show that additional columns exist, preserve column count/group labels, and provide keyboard-operable scrolling or navigation. A clipped edge with no cue is not discoverability.

When users build a shortlist or selection across sorting/filtering, keep it persistent and visibly scoped. Announce selection/filter changes where appropriate, return focus predictably after updates, and do not silently discard excluded or hidden records from the audit trail.

## Escape conditions

- ARIA grid is appropriate for spreadsheet-like editing/navigation, but it carries a larger keyboard contract than a native table.
- Pagination can improve performance and orientation when cross-page comparison is not required and totals/filter state persist.
- Hiding columns is acceptable when they are genuinely secondary and remain discoverable.

## Audit signals

- focus disappears after sort/filter;
- headers are visually present but not programmatically associated;
- icon-only sort lacks state/name;
- selection uses color alone;
- empty/loading/error rows corrupt column alignment;
- mobile users cannot reach row actions or identity.
