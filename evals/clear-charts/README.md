# clear-charts evals

These evals test whether `clear-charts` changes design judgment, not whether an agent can repeat chart terminology.

## Run pattern

For each case, compare:

1. **Baseline** — run the prompt without `clear-charts`.
2. **Skill** — run the same prompt with `clear-charts` available/explicitly selected.
3. Blind-score both using `RUBRIC.md`.

Avoid rewarding verbosity. The skill should often produce **fewer** recommendations than baseline while making better ones.

## Eval families

- **Create** — choose/design a representation from a question and data description.
- **Audit** — identify the few highest-impact problems in an existing chart.
- **Rethink** — detect when the requested/existing chart is the wrong abstraction.
- **Restraint** — leave a strong chart mostly alone.

## Pass condition for v1

The skill should improve median rubric score and must not regress integrity or restraint. A beautiful answer that introduces a misleading scale, unnecessary chart replacement, or fabricated critique fails regardless of average score.
