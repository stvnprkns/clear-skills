# Rethink the Chart

## Principle

Treat the requested form as a hypothesis. Recommend replacement only when another representation materially improves the primary task or removes an integrity failure.

## Rethink record

Use this compact chain:

```text
REQUESTED FORM → ACTUAL QUESTION → PERCEPTUAL TASK → PRIMARY REPRESENTATION
                                                ↘ SECONDARY NEED → SECONDARY REPRESENTATION
```

For every recommendation, name what the replacement sacrifices. A rethink without a cost is advocacy, not judgment.

## Use when

- the form encodes a different relationship than the question;
- exact lookup is primary but marks make it slower;
- the chart asks for serial memory, mental arithmetic, or repeated legend lookup;
- interaction hides the overview needed to choose what to inspect;
- aggregation, normalization, or scale choice removes decision-critical context;
- responsive constraints make the primary task impossible.

## Reject when

Do not rethink merely because:

- another chart is more fashionable;
- a pie, gridline, non-zero line domain, six colors, or interaction violates a slogan;
- the current chart is unfamiliar but task-fit;
- the improvement is cosmetic and would disrupt a working visual system;
- the reviewer wants to demonstrate expertise.

## Prefer instead

| Actual task | Weak requested form | Strong primary candidate | Preserve secondarily when |
| --- | --- | --- | --- |
| rank endpoint change | many-line overlay | ranked delta / slope | path and timing explain the change |
| retrieve several exact fields | dashboard of charts | table | distributions or exceptions need overview |
| compare close magnitudes | truncated bars | dot plot | zero-relative magnitude also matters |
| compare relative growth | raw-value overlay | indexed overlay | absolute base size changes the decision |
| compare every component | stacked bars | aligned dots/small multiples | total + composition is also central |
| find geographic ranking | choropleth | ranked bar | adjacency or spatial clustering matters |
| see distribution and uncertainty | mean bars | point + interval/distribution | operational totals need a companion view |

## Escape conditions

- Keep the requested form if users have learned it and the alternative produces only a marginal gain.
- Keep a simple pie for a small, meaningful whole when approximate share is the task and no close comparison is needed.
- Keep a non-zero line domain for narrow process/sensor deviations when disclosed and absolute magnitude is not the claim.
- Keep gridlines when precise across-distance lookup matters.
- Keep stable categorical colors across coordinated views when identity continuity reduces search.
- Keep interaction when the default answers the primary question and interaction adds genuine detail.

## Examples

### Twenty-four customers

- Requested form: 24-line chart.
- Actual question: Which customers expanded or contracted most?
- Perceptual task: Rank endpoint change.
- Primary: Ranked delta with absolute and percent change when both matter.
- Secondary: Selected customer time series for trajectory and timing.
- Cost: The primary view no longer shows every intermediate month; the secondary view restores it.

### Thirty categories

Do not solve category count mechanically.

| Need | Use | Reject when |
| --- | --- | --- |
| see full rank | show all in a sorted, scrollable list with persistent labels | scrolling prevents needed cross-item comparison |
| see top contributors | top N + explicit “other” and access to full list | tail items are individually actionable |
| find one known item | searchable/filterable table | overview and distribution are primary |
| compare meaningful groups | group/facet by domain structure | grouping is invented only to reduce count |
| identify exceptions | distribution + labeled outliers | every category needs direct action |

### Interesting but irrelevant

A statistically unusual weekend spike should not become the focal annotation when the decision concerns weekday staffing and weekend work is out of scope. Retain it if omission would mislead totals or model interpretation; otherwise keep it discoverable but subordinate.

## Audit signals

- requested form is repeated as a requirement without evidence;
- primary answer appears only after hover/filtering;
- chart contains trajectories but the question asks only for endpoints;
- chart shows exact labels but the task is pattern detection—or vice versa;
- alternative is recommended without tradeoffs;
- proposed redesign removes material context;
- no-change is never considered.
