# Choosing the Question

## Principle

Design for the decision the reader must make. A topic is not a question, and a requested chart type is not a task.

## Frame

Write these five lines before choosing a form:

| Field | Meaning | Example |
| --- | --- | --- |
| Decision | What may change after viewing? | Choose accounts for retention outreach |
| Reader | Who decides, with what literacy and time? | VP reviewing weekly portfolio risk |
| Requested form | What was asked for? | 24-customer line chart |
| Actual question | What answer is sought? | Which customers expanded or contracted most? |
| Perceptual task | What must the eye do? | Rank endpoint change |

If no decision exists, state the informational purpose instead: explain, monitor, discover, or document.

## Use when

- the request starts with a chart type;
- multiple representations seem reasonable;
- a dashboard contains data without a clear next action;
- the analyst's interesting finding may differ from the reader's need;
- interaction or annotation depends on whether the mode is explanation or exploration.

## Reject when

Reject a framing that:

- merely restates fields (“show revenue by month”);
- assumes the requested chart is fixed without an explicit constraint;
- invents a business decision not supported by context;
- optimizes for a statistically surprising fact that cannot affect interpretation or action;
- collapses distinct audiences with incompatible tasks into one view.

## Prefer instead

Translate common verbs into perceptual tasks:

| Reader verb | Likely task | Candidate primary forms |
| --- | --- | --- |
| find / look up | exact retrieval | table, labeled value |
| compare | magnitude or position | dot, bar, aligned panels |
| prioritize | rank against value/risk | ranked bar/dot, decision matrix |
| monitor | detect deviation or threshold | time series + reference, control view |
| explain | follow one supported claim | annotated static or staged view |
| explore | test several questions | persistent overview + filters/details |
| understand change | endpoints, path, or rate | delta/slope, line, indexed line |

## Escape conditions

- Preserve a mandated form when legal, publication, brand, or interoperability constraints are real; improve it within those bounds and name the cost.
- For open-ended discovery, do not force a single decision prematurely. Define the first analytical question and allow reversible exploration.
- A chart may support both monitoring and explanation, but the default state still needs one priority.

## Examples

**Requested:** Show statistically significant feature correlations.

**Decision:** Choose variables for a costly follow-up experiment.

**Judgment:** Rank by decision-relevant effect and uncertainty, not p-value alone; suppress correlations that are statistically detectable but too small to affect the experiment.

**Requested:** Annotate the insight on a dashboard chart.

**Decision:** Operators must notice threshold breaches quickly.

**Judgment:** Persist the threshold and current breach. Do not narrate every fluctuation; preserve exploration for diagnosis.

## Audit signals

- title names a topic but not a question or claim;
- chart type appears before reader/task reasoning;
- key comparison requires subtraction or remembering a prior filter state;
- emphasis tracks novelty rather than consequence;
- one view attempts incompatible executive and analyst tasks;
- recommendations cannot say what reader action becomes easier.
