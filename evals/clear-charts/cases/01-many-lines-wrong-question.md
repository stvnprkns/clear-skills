# Case: many lines, wrong question

**Family:** Rethink / Create

## Prompt

I have monthly ARR for 24 SaaS customers over the last 12 months. I want a 24-line chart so leadership can see which customers expanded or contracted the most. Design the chart and tell me how it should work.

## Expected skill behavior

- Identify that “which expanded or contracted most” is a change/ranking question, not primarily a path-through-time question.
- Recommend a ranked delta, slope/dumbbell, or another explicit change representation as the primary view.
- Preserve time-series detail only if the monthly path is decision-relevant, perhaps through secondary interaction/small multiples.
- Avoid blindly implementing 24 equally weighted lines.
