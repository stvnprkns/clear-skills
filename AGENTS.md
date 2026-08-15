# AGENTS.md

This is the source of truth for agents editing the Clear skill repository.

## What this repository is

Clear is a suite of agent skills for visual information design. It helps agents choose, create, critique, and improve representations so that people can understand information with less cognitive work and without distortion.

The repository is documentation-first. A skill may include scripts where deterministic validation or generation is useful, but design judgment belongs in Markdown instructions and references.

## Authoring model

Each skill lives in `skills/<skill-name>/`.

- `SKILL.md` is the entry point. Keep it compact and high-leverage.
- `references/*.md` contain deeper rules, decision tables, failure modes, and examples.
- `agents/openai.yaml` contains OpenAI-facing display metadata when useful.
- Repository-level evals live in `evals/<skill-name>/`; do not put eval prompts into the skill context.

Use progressive disclosure: the skill should know *which* reference to read without loading every reference for every task.

## Rule ownership

Every durable rule has exactly one owner. Other skills may hand off to the owner but should not maintain copies.

Ownership:

| Skill | Owns |
| --- | --- |
| `clear-visuals` | Representation-level orchestration, cross-domain review, final consolidation |
| `clear-charts` | Quantitative chart selection, encoding, scales, chart labeling, chart color semantics, chart interaction |
| `clear-diagrams` | Process, system, hierarchy, architecture, graph topology, relationship diagrams |
| `clear-dashboards` | Multi-view information hierarchy, KPI environment, dashboard controls, cross-view relationships |
| `clear-explainers` | Narrative sequencing, progressive reveal, simulation, explanatory interaction |
| `clear-tables` | Exact-value retrieval, tabular comparison, dense rows/columns, sorting and scanability |
| `clear-dataviz` | Specialized or unconventional quantitative visual forms not covered by standard chart grammar |

When a problem crosses domains, assign the rule to the domain whose design decision is primary and mention secondary effects rather than duplicating the rule.

## SKILL.md structure

A domain `SKILL.md` should usually contain:

1. YAML frontmatter with concise `name` and `description`.
2. A short philosophy statement.
3. Hand-offs to adjacent Clear skills.
4. A **Quick Reference** table linking to deeper files.
5. Numbered **Core Principles**.
6. A **Common Mistakes** table.
7. A short **Reporting** section pointing to the review contract.

Do not add a second index of reference files after the Quick Reference table.

## Reference file standard

References are not essays. They are decision support for an agent in the middle of work.

Prefer this hierarchy:

- **Principle** — durable judgment.
- **Constraint** — when a design should be rejected or flagged.
- **Pattern** — a reliable way to solve the problem.
- **Escape condition** — when the rule should not be applied mechanically.

Good references contain explicit tradeoffs and counterexamples. Avoid generic statements such as “use color thoughtfully” or “choose an appropriate chart.”

## Prescriptiveness

Be exact where the evidence is exact, and conditional where design judgment depends on context.

Bad:

> Always start every axis at zero.

Better:

> Bar length encodes magnitude from a baseline, so quantitative bar axes normally require a zero baseline. Position-based line and dot charts can use a narrower domain when it is disclosed and does not exaggerate the intended comparison.

## Clear critique behavior

A Clear review is not a lint report.

- Prioritize comprehension and integrity before polish.
- Find root causes, not every symptom.
- Report the smallest number of changes that would create the greatest improvement.
- Preserve good decisions explicitly.
- Recommend a different representation only when the current one materially impairs the user’s question.
- Never invent criticism to fill a quota.

## Context preservation

When improving an artifact:

- preserve the user’s data and factual meaning;
- preserve the existing visual system when it is defensible;
- preserve working interactions unless they cause a clear comprehension or accessibility problem;
- do not replace the project’s visualization stack just because another library is preferred;
- separate design judgment from implementation preference.

## Evidence and verification

For source-backed audits, cite the exact chart, component, file, or line when possible. For visual claims, inspect the rendered artifact when available. For code claims that depend on runtime behavior, do not infer success from source alone.

When implementing a change, verify the relevant states and responsive sizes where possible.

## Eval policy

A new rule should ideally earn its way into the skill through representative failures.

Before adding a broad principle:

1. Identify at least one realistic case where the baseline agent behaves poorly.
2. Add or update an eval case.
3. Confirm that the proposed rule improves the target behavior without causing obvious regressions in nearby cases.
4. Prefer one stronger rule over several overlapping reminders.

Keep 20–35% of text cases as restraint cases. Add a rendered `visual/<case>/` fixture with `bad.html`, `expected.png`, and `prompt.md` for rules that depend on visual inspection. Use `scripts/run_evals.py --skill <skill-name>` for repeated baseline/skill samples and blind pairwise judging; smoke tests are infrastructure checks, not evidence that a skill improves behavior.

The goal is not maximum instruction coverage. It is reliable improvement in design judgment.

## Naming

All domain skills use the `clear-` prefix. The prefix is the user-facing family marker and should remain predictable.

Use nouns that describe the domain: `clear-charts`, `clear-diagrams`, `clear-tables`.
