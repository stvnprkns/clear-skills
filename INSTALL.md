# Install Clear in Codex

Codex scans `.agents/skills` from the working directory through the repository root and also supports user-scoped skills.

## Install the suite

Link every Clear skill into the default user-scoped location:

```bash
./scripts/link_codex_skills.sh
```

Or target a repository:

```bash
./scripts/link_codex_skills.sh /path/to/your-repo/.agents/skills
```

Existing destinations are preserved and reported as skipped.

## Install one skill

```bash
mkdir -p /path/to/your-repo/.agents/skills
ln -s /absolute/path/to/clear-skills/skills/clear-tables \
  /path/to/your-repo/.agents/skills/clear-tables
```

Codex supports symlinked skill folders. Restart Codex if a newly linked skill does not appear automatically.

## Invoke

Mention a domain explicitly:

```text
Use $clear-diagrams to audit this architecture map.
Use $clear-dashboards to rethink this KPI environment.
Use $clear-tables to improve this comparison table.
```

Use `$clear-visuals` when the correct representation is undecided or the artifact crosses multiple domains. Individual skills can also trigger implicitly from their descriptions.
