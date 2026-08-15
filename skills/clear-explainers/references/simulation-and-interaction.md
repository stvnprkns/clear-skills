# Simulation and Interaction

## Principle

Use interaction to let readers test a bounded explanation, not to outsource the explanation to exploration.

## Use when

- varying an input reveals sensitivity or mechanism;
- counterfactual comparison changes understanding;
- selecting an entity connects general model to a concrete case;
- uncertainty or range is better understood through repeated outcomes.

## Reject when

- control-output relationship is undocumented;
- defaults bias the claim without rationale;
- impossible parameter combinations are allowed;
- animation speed or randomness becomes the evidence;
- controls lack keyboard operation or current values.

## Prefer instead

Declare input meaning, range, default, assumptions, output, and non-modeled effects. Preserve a baseline and allow reset. Show comparison, not just the newest state. Seed or explain randomness where reproducibility matters.

## Escape conditions

- A guided preset can be better than free controls for novice audiences.
- Static scenarios can replace a simulator when only a few meaningful cases exist.
- Open exploration is valid after a coherent default explanation.

## Audit signals

- no baseline/reset;
- output updates without explaining why;
- invalid inputs produce plausible-looking results;
- uncertainty shown as decorative noise;
- keyboard and reduced-motion states absent.
