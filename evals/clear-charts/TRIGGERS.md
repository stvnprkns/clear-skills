# Trigger tests

The skill description is part of the product. Test whether it activates on the right work and stays out of unrelated work.

## Should trigger

1. “Audit this revenue line chart and tell me the highest-impact improvements.”
2. “What chart should I use to compare retention across cohorts?”
3. “The y-axis makes these bars look dramatic. Is this misleading?”
4. “Improve this D3 scatterplot without changing the data.”
5. “Should this dashboard chart use a legend or direct labels?”
6. “My chart connects across missing observations. What should I do?”

## Should not trigger by itself

1. “Draw an architecture diagram for our event pipeline.” → `clear-diagrams`
2. “Rewrite this dashboard empty-state copy.” → writing/interface skill
3. “Make this button hover animation feel better.” → UI/motion skill
4. “Create a spreadsheet budget.” → spreadsheet workflow
5. “Explain this SQL query.” → general code reasoning
6. “Design the overall information architecture of this analytics dashboard.” → `clear-dashboards` / `clear-visuals` once available

## Boundary cases

- “Review this dashboard.” `clear-charts` may be useful for chart-level findings, but should not claim ownership of dashboard hierarchy.
- “Visualize this workflow.” Do not trigger solely because of the word “visualize”; this is likely a diagram task.
- “Create an infographic with three charts.” Chart rules apply to the charts, but overall composition belongs to `clear-visuals`/future infographic or explainer orchestration.
