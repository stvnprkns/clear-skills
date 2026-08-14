# Install Clear in Codex

## Repo-scoped installation

Codex scans `.agents/skills` from the working directory up through the repository root.

From the Clear repository, link the skill into a target repository:

```bash
mkdir -p /path/to/your-repo/.agents/skills
ln -s /absolute/path/to/clear-skills/skills/clear-charts \
  /path/to/your-repo/.agents/skills/clear-charts
```

Codex supports symlinked skill folders.

## User-scoped installation

To make Clear Charts available across repositories:

```bash
mkdir -p "$HOME/.agents/skills"
ln -s /absolute/path/to/clear-skills/skills/clear-charts \
  "$HOME/.agents/skills/clear-charts"
```

Codex normally detects skill changes automatically. If a new or changed skill does not appear, restart Codex.

## Invoke

In Codex CLI / IDE, use the skills UI or mention the skill with `$clear-charts`.

The skill also allows implicit invocation. Its `description` is intentionally scoped so chart/data-visualization tasks can trigger it while diagram-only or general UI work should not.

## Future distribution

Once Clear contains multiple mature skills, package the suite as a plugin for easier installation and distribution. Until then, keeping the skill directly inspectable in the repository makes iteration and eval work simpler.
