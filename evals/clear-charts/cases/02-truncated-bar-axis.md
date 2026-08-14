# Case: truncated bar axis

**Family:** Audit

## Prompt

Audit this design: a vertical bar chart compares satisfaction scores of 94.1, 94.6, 95.0, and 95.3. The y-axis runs from 93.5 to 95.5 because otherwise the bars look almost identical. The title is “Team D crushes everyone on satisfaction.”

## Expected skill behavior

- Flag the cropped bar baseline as a critical/high integrity issue because bar length encodes magnitude from the baseline.
- Recommend a position-based representation (dot/range) if showing the narrow differences is genuinely useful.
- Flag the title as overstating the magnitude; do not claim statistical significance without evidence.
- Do not insist every position-based chart must start at zero.
