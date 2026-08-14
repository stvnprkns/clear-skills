# Clear

**Design skills for making complex information understandable.**

Clear is a suite of agent skills for creating, auditing, and improving charts, diagrams, dashboards, tables, interactive explainers, and other forms of visual information.

The system is deliberately opinionated: it optimizes for comprehension, integrity, and decision usefulness before novelty or decoration.

> Visualization is not the output. Understanding is the output.

## Status

The first production skill is **`clear-charts`**. It establishes the architecture, critique protocol, rule ownership model, and evaluation approach that future Clear skills should follow.

Planned suite:

- `clear-visuals` — umbrella/orchestration across visual-information domains
- `clear-charts` — quantitative charts and plots **(v1 included)**
- `clear-diagrams` — systems, flows, architecture, relationships
- `clear-dashboards` — multi-view decision environments
- `clear-explainers` — narrative, interactive, and causal explanation
- `clear-tables` — dense structured comparison and exact-value retrieval
- `clear-dataviz` — advanced and unconventional visualization

## Repository structure

```text
clear-skills/
├── AGENTS.md
├── README.md
├── SOURCES.md
├── skills/
│   └── clear-charts/
│       ├── SKILL.md
│       ├── agents/
│       │   └── openai.yaml
│       └── references/
│           ├── chart-selection.md
│           ├── encoding-and-comparison.md
│           ├── scales-and-axes.md
│           ├── labels-and-annotation.md
│           ├── color.md
│           ├── uncertainty-and-missing-data.md
│           ├── interaction.md
│           └── review-output.md
├── evals/
│   └── clear-charts/
│       ├── README.md
│       ├── RUBRIC.md
│       └── cases/
└── scripts/
    └── validate_skills.py
```

## Why the skill is split into references

`SKILL.md` contains the durable operating philosophy and the rules that should be present whenever the skill activates. Deeper guidance is loaded only when a task needs it.

This keeps the initial context small while allowing the skill to contain serious domain knowledge. It also makes individual rule packs easier to improve without turning `SKILL.md` into an encyclopedia.

## Using in Codex

Codex supports skills as directories containing a required `SKILL.md` plus optional `references/`, `scripts/`, `assets/`, and `agents/openai.yaml` resources.

Install or link the `skills/clear-charts` directory into a location Codex scans for skills, then invoke it explicitly from the skill picker/mention flow or allow Codex to match it from the `description` metadata.

## Using in Claude Code / other Agent Skills-compatible tools

The core skill follows the Agent Skills `SKILL.md` convention. Tools differ in installation and invocation syntax, but the Markdown instructions and relative references are intentionally portable.

## Validate the repository

```bash
python3 scripts/validate_skills.py
```

The validator checks required metadata, local Markdown links, reference targets, and naming consistency.

## Design principle

Clear is not a chart-style library. It should be willing to say:

- this should be a table, not a chart;
- this chart is technically correct but makes the reader perform the key comparison;
- this interaction adds complexity without adding understanding;
- this visual is already strong and should not be redesigned.

That judgment is the product.
