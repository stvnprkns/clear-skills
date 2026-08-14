#!/usr/bin/env python3
"""Lightweight repository validator for Clear skills."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
FIELD_RE = re.compile(r"^(name|description):\s*(.*)$", re.M)
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+\.md(?:#[^)]+)?)\)")


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        return [f"{skill_dir.relative_to(ROOT)}: missing SKILL.md"]

    text = skill_file.read_text(encoding="utf-8")
    fm = FRONTMATTER_RE.search(text)
    if not fm:
        errors.append(f"{skill_file.relative_to(ROOT)}: missing YAML frontmatter")
    else:
        frontmatter = fm.group(1)
        name_match = re.search(r"^name:\s*([^\n]+)$", frontmatter, re.M)
        desc_match = re.search(r"^description:\s*(?:>-\s*)?(.*)$", frontmatter, re.M)
        if not name_match:
            errors.append(f"{skill_file.relative_to(ROOT)}: missing name")
        else:
            name = name_match.group(1).strip().strip('"\'')
            if name != skill_dir.name:
                errors.append(
                    f"{skill_file.relative_to(ROOT)}: frontmatter name '{name}' "
                    f"does not match directory '{skill_dir.name}'"
                )
        if not desc_match:
            errors.append(f"{skill_file.relative_to(ROOT)}: missing description")

    for md in skill_dir.rglob("*.md"):
        content = md.read_text(encoding="utf-8")
        for raw_target in LINK_RE.findall(content):
            target = raw_target.split("#", 1)[0]
            if target.startswith(("http://", "https://")):
                continue
            resolved = (md.parent / target).resolve()
            if not resolved.exists():
                errors.append(
                    f"{md.relative_to(ROOT)}: broken Markdown link -> {raw_target}"
                )

    agent_yaml = skill_dir / "agents" / "openai.yaml"
    if agent_yaml.exists() and not agent_yaml.read_text(encoding="utf-8").strip():
        errors.append(f"{agent_yaml.relative_to(ROOT)}: empty openai.yaml")

    return errors


def main() -> int:
    if not SKILLS.exists():
        print("No skills directory found", file=sys.stderr)
        return 1

    skill_dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    if not skill_dirs:
        print("No skills found", file=sys.stderr)
        return 1

    errors: list[str] = []
    for skill_dir in skill_dirs:
        errors.extend(validate_skill(skill_dir))

    if errors:
        print("Validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(skill_dirs)} skill(s):")
    for skill_dir in skill_dirs:
        print(f"- {skill_dir.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
