#!/usr/bin/env python3
"""Lightweight repository validator for Clear skills."""

from __future__ import annotations

import re
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EVALS = ROOT / "evals"

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


def validate_evals(skill_name: str) -> list[str]:
    errors: list[str] = []
    eval_dir = EVALS / skill_name
    if not eval_dir.exists():
        return errors

    text_cases = sorted((eval_dir / "cases").glob("*.md"))
    config = eval_dir / "config.json"
    if not config.exists():
        errors.append(f"{eval_dir.relative_to(ROOT)}: missing config.json")
    else:
        try:
            dimensions = json.loads(config.read_text(encoding="utf-8")).get("dimensions")
            if (
                not isinstance(dimensions, list)
                or len(dimensions) < 2
                or len(set(dimensions)) != len(dimensions)
                or any(not isinstance(item, str) or not re.fullmatch(r"[a-z-]+", item) for item in dimensions)
            ):
                errors.append(f"{config.relative_to(ROOT)}: invalid dimensions")
        except json.JSONDecodeError as exc:
            errors.append(f"{config.relative_to(ROOT)}: invalid JSON ({exc})")
    restraint = 0
    for case in text_cases:
        content = case.read_text(encoding="utf-8")
        for heading in ("## Prompt", "## Expected skill behavior"):
            if heading not in content:
                errors.append(f"{case.relative_to(ROOT)}: missing {heading}")
        if "**Family:** Restraint" in content:
            restraint += 1
    if text_cases:
        ratio = restraint / len(text_cases)
        if not 0.20 <= ratio <= 0.35:
            errors.append(
                f"{eval_dir.relative_to(ROOT)}: restraint cases are {restraint}/{len(text_cases)} "
                "(expected 20–35%)"
            )

    visual_dir = eval_dir / "visual"
    if visual_dir.exists():
        for case_dir in sorted(path for path in visual_dir.iterdir() if path.is_dir()):
            for filename in ("bad.html", "prompt.md", "expected.png"):
                artifact = case_dir / filename
                if not artifact.exists() or artifact.stat().st_size == 0:
                    errors.append(f"{case_dir.relative_to(ROOT)}: missing or empty {filename}")
            png = case_dir / "expected.png"
            if png.exists() and png.read_bytes()[:8] != b"\x89PNG\r\n\x1a\n":
                errors.append(f"{png.relative_to(ROOT)}: invalid PNG signature")
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
        errors.extend(validate_evals(skill_dir.name))

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
