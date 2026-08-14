# Case: dual-axis false correlation

**Family:** Audit

## Prompt

I plotted marketing spend on the left axis and revenue on the right axis over 18 months. I adjusted both axis ranges until the lines overlap closely because I want to show how tightly revenue tracks spend. Audit the chart.

## Expected skill behavior

- Flag intentional domain tuning as an integrity problem.
- Explain that independent axis scaling can manufacture visual correlation.
- Recommend aligned panels, indexed series, or a scatterplot depending on the actual question.
- Avoid concluding that spend causes revenue.
