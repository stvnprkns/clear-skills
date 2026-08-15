# clear-charts evals

This benchmark tests whether `clear-charts` improves representation judgment, integrity, and restraint—not whether an agent repeats visualization terminology.

## Benchmark contract

```text
same case × N baseline samples ─┐
                               ├─ randomized anonymous pair → judge → report
same case × N Clear samples ───┘
```

- Use at least three samples for meaningful runs; the runner refuses one-sample comparisons.
- Give baseline and Clear the same artifact and user prompt.
- Add only the skill path/instruction to the Clear condition.
- Randomize A/B order before judging.
- Preserve every raw response, mapping, judgment, and aggregate report.
- Do not reward verbosity.
- Require a failing or weak eval before adding a broad rule.

## Run

`scripts/run_evals.py` is model-vendor neutral. Each command must read one prompt from stdin and write its response to stdout. The judge must return the JSON contract embedded in its prompt.

For runners that accept image files, include an `--image={artifact}`-style token in all three command templates. The runner replaces it with the visual fixture path for visual cases and removes that token for text cases. Keep the placeholder and flag in one argument.

```bash
python3 scripts/run_evals.py \
  --skill clear-charts \
  --baseline-cmd "your-agent-command" \
  --skill-cmd "your-agent-command" \
  --judge-cmd "your-judge-command" \
  --samples 5
```

Use `--case 09-small-multiples --case visual-spaghetti-lines` for a focused run. Results go to ignored `eval-results/<timestamp>/` directories unless `--output` is supplied.

The runner checkpoints baseline and skill outputs before judging, retries failed commands once by default, and resumes completed samples when rerun with the same output directory. Use `--retries 0` to disable retries.

## Case families

- **Create** — select/design a representation from a question and data.
- **Audit** — identify the few highest-impact failures in an artifact.
- **Rethink** — reject the requested abstraction when it impairs the real task.
- **Restraint** — preserve strong or contextually justified decisions.
- **Visual** — inspect rendered PNG evidence rather than a prose-only description.

The visual library stores `bad.html`, a deterministic `expected.png` rendering, and `prompt.md` for each case. “bad.html” is the input implementation name, not a guarantee that every choice is wrong; restraint cases intentionally use the same contract.

Regenerate visual fixtures with:

```bash
python3 scripts/render_visual_evals.py
```

## Gate

Pass only when Clear improves overall mean score and does not regress integrity or restraint. Pairwise wins support diagnosis but do not override a red-line failure. Report results as measured values; never place aspirational scores in release copy.

Focused subsets are diagnostic and are always reported as `PROVISIONAL`. A `PASS` or `FAIL` release gate requires every configured text and visual case with at least three samples per condition.
