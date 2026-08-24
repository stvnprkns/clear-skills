# Clear

[![skills.sh](https://skills.sh/b/stvnprkns/clear-skills)](https://skills.sh/stvnprkns/clear-skills)

**Design skills for making complex information understandable.**

Clear is a suite of agent skills for creating, auditing, and improving charts, diagrams, dashboards, tables, interactive explainers, and other forms of visual information.

The system is deliberately opinionated: it optimizes for comprehension, integrity, and decision usefulness before novelty or decoration.

> Visualization is not the output. Understanding is the output.

## Included skills

- `clear-visuals` — umbrella routing, cross-domain review, and final consolidation
- `clear-charts` — quantitative charts and plots
- `clear-tables` — exact retrieval, dense comparison, sorting, and scanability
- `clear-diagrams` — systems, flows, architecture, hierarchy, and relationships
- `clear-dashboards` — recurring multi-view monitoring and decision environments
- `clear-explainers` — narrative sequence, progressive reveal, and simulation
- `clear-dataviz` — specialized quantitative forms that exceed standard chart grammar

Each skill uses the same judgment architecture: actual question → cognitive/perceptual task → competing representations → rejection and escape conditions → evidence-backed review. Every domain has text evals, a restraint case, and at least one rendered visual fixture.

## Repository structure

```text
clear-skills/
├── AGENTS.md
├── README.md
├── SOURCES.md
├── skills/
│   ├── clear-visuals/
│   ├── clear-charts/
│   ├── clear-tables/
│   ├── clear-diagrams/
│   ├── clear-dashboards/
│   ├── clear-explainers/
│   └── clear-dataviz/
├── evals/
│   └── <skill-name>/
│       ├── README.md, RUBRIC.md, config.json
│       ├── cases/
│       └── visual/
└── scripts/
    ├── render_visual_evals.py
    ├── run_evals.py
    └── validate_skills.py
```

## Why the skill is split into references

`SKILL.md` contains the durable operating philosophy and the rules that should be present whenever the skill activates. Deeper guidance is loaded only when a task needs it.

This keeps the initial context small while allowing the skill to contain serious domain knowledge. It also makes individual rule packs easier to improve without turning `SKILL.md` into an encyclopedia.

## Using in Codex

Codex supports skills as directories containing a required `SKILL.md` plus optional `references/`, `scripts/`, `assets/`, and `agents/openai.yaml` resources.

Install the whole suite with `scripts/link_codex_skills.sh`, or link an individual `skills/<skill-name>` directory. Invoke a domain explicitly, such as `$clear-diagrams`, or use `$clear-visuals` when the representation is undecided or crosses domains.

## Install from skills.sh

Install the suite from its public GitHub source:

```bash
npx skills add stvnprkns/clear-skills
```

The installer discovers every valid `SKILL.md` in the repository and lets you install the complete suite or selected Clear skills.

## Using in Claude Code / other Agent Skills-compatible tools

The core skill follows the Agent Skills `SKILL.md` convention. Tools differ in installation and invocation syntax, but the Markdown instructions and relative references are intentionally portable.

## Validate the repository

```bash
python3 scripts/validate_skills.py
```

The validator checks required metadata, local Markdown links, reference targets, and naming consistency.

Run deterministic chart-spec evidence checks with `skills/clear-charts/scripts/inspect-chart.py`. Run repeated baseline/Clear comparisons with `scripts/run_evals.py --skill <skill-name>`.

## Design principle

Clear is not a visual-style library. It should be willing to say:

- this should be a table, not a chart;
- this chart is technically correct but makes the reader perform the key comparison;
- this interaction adds complexity without adding understanding;
- this visual is already strong and should not be redesigned.

That judgment is the product.
