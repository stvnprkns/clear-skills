# Clear Charts Eval Rubric

Score each dimension 0–3.

## 1. Question framing

- **0** — Does not identify the reader's real question.
- **1** — Restates the request but does not translate it into a comparison.
- **2** — Identifies the important relationship.
- **3** — Uses the relationship to drive representation and hierarchy decisions.

## 2. Representation choice

- **0** — Clearly mismatched or misleading representation.
- **1** — Plausible but makes the primary comparison unnecessarily difficult.
- **2** — Appropriate representation.
- **3** — Strongly matched to the task; rejects a tempting but inferior form when needed.

## 3. Comparison clarity

- **0** — Key comparison remains hidden or requires substantial mental arithmetic.
- **1** — Comparison exists but remains indirect.
- **2** — Primary comparison is easy to see.
- **3** — Design actively exposes the delta/rank/threshold/relationship the reader needs.

## 4. Integrity

- **0** — Misleading scale, encoding, missing-data treatment, or unsupported claim.
- **1** — Ambiguous or risky treatment.
- **2** — Trustworthy treatment.
- **3** — Explicitly catches a subtle integrity issue and fixes it without overcorrecting.

## 5. Hierarchy and annotation

- **0** — Everything competes equally or explanation is detached from the data.
- **1** — Some hierarchy but primary insight is still easy to miss.
- **2** — Clear hierarchy and useful labeling.
- **3** — Context, emphasis, direct labeling, and annotation work together with minimal decoding.

## 6. Restraint

- **0** — Gratuitous redesign, color, interaction, or recommendation sprawl.
- **1** — Several low-value changes.
- **2** — Mostly focused on meaningful changes.
- **3** — Smallest effective intervention; explicitly preserves strong decisions.

## 7. Specificity

- **0** — Generic best-practice language.
- **1** — Names issues without actionable change.
- **2** — Concrete recommendations tied to the artifact.
- **3** — Recommendations explain why, what to change, and what to preserve.

## 8. Accessibility / non-hover robustness

- **0** — Essential meaning depends on color or hover with no alternative.
- **1** — Mentions accessibility generically.
- **2** — Primary content works without color-only/hover-only decoding.
- **3** — Identifies and fixes a relevant accessibility failure without cluttering unrelated cases.

## Red-line failures

Regardless of total score, fail the case if the response:

- invents data or claims not supported by the prompt/artifact;
- recommends a knowingly misleading scale/encoding;
- converts missing values to zero without evidence;
- treats correlation as causation;
- recommends replacing a clearly appropriate chart solely for novelty;
- hides the primary insight behind interaction.
