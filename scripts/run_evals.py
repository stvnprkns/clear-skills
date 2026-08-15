#!/usr/bin/env python3
"""Run repeated baseline/skill samples and blind pairwise judging for Clear."""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import shlex
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIMENSIONS = ["question", "representation", "comparison", "integrity", "hierarchy", "restraint", "specificity", "accessibility"]


def cases(eval_root: Path) -> list[dict[str, str]]:
    found = []
    for prompt in sorted((eval_root / "cases").glob("*.md")):
        found.append({"id": prompt.stem, "prompt": str(prompt), "artifact": ""})
    for prompt in sorted((eval_root / "visual").glob("*/prompt.md")):
        found.append({"id": f"visual-{prompt.parent.name}", "prompt": str(prompt), "artifact": str(prompt.parent / "expected.png")})
    return found


def command_argv(command: str, artifact: str = "") -> list[str]:
    """Expand an optional {artifact} token without invoking a shell."""
    argv = []
    for token in shlex.split(command):
        if "{artifact}" in token:
            if not artifact:
                continue
            token = token.replace("{artifact}", artifact)
        argv.append(token)
    return argv


def run_command(command: str, payload: str, timeout: int, artifact: str = "") -> str:
    completed = subprocess.run(
        command_argv(command, artifact), input=payload, text=True, capture_output=True, timeout=timeout, check=False
    )
    if completed.returncode:
        raise RuntimeError(f"command failed ({completed.returncode}): {completed.stderr.strip()}")
    return completed.stdout.strip()


def run_with_retries(command: str, payload: str, timeout: int, retries: int, artifact: str = "") -> str:
    last_error: Exception | None = None
    for attempt in range(retries + 1):
        try:
            return run_command(command, payload, timeout, artifact)
        except (RuntimeError, subprocess.TimeoutExpired) as exc:
            last_error = exc
            if attempt == retries:
                raise
    assert last_error is not None
    raise last_error


def blind_pair(rng: random.Random, baseline: str, skill_response: str) -> tuple[list[tuple[str, str]], dict[str, str]]:
    pair = [("baseline", baseline), ("skill", skill_response)]
    rng.shuffle(pair)
    return pair, {"A": pair[0][0], "B": pair[1][0]}


def blind_pair_for_sample(seed: int, case_id: str, sample: int, baseline: str, skill_response: str) -> tuple[list[tuple[str, str]], dict[str, str]]:
    """Use a randomized starting side, then alternate sides to limit position imbalance."""
    digest = hashlib.sha256(f"{seed}:{case_id}".encode("utf-8")).digest()
    skill_first = bool(digest[0] & 1) ^ bool((sample - 1) & 1)
    pair = [("skill", skill_response), ("baseline", baseline)] if skill_first else [("baseline", baseline), ("skill", skill_response)]
    return pair, {"A": pair[0][0], "B": pair[1][0]}


def task_payload(case: dict[str, str], with_skill: bool, skill: Path) -> str:
    prompt = Path(case["prompt"]).read_text(encoding="utf-8")
    artifact = f"\nArtifact to inspect: {case['artifact']}\n" if case["artifact"] else ""
    skill_instruction = f"\nUse the skill at {skill}. Read only the references relevant to this task.\n" if with_skill else ""
    return f"{prompt}{artifact}{skill_instruction}\nRespond as if to the user. Do not discuss this benchmark."


def judge_payload(case: dict[str, str], a: str, b: str, rubric: Path, dimensions: list[str]) -> str:
    score_example = ",".join(f'"{key}":0' for key in dimensions)
    return f"""You are a strict blind pairwise judge. Score the two responses against the case and rubric.
Do not reward verbosity. Red-line failures override totals. Return JSON only with this schema:
{{"winner":"A|B|tie","reason":"brief","A":{{{score_example}}},"B":{{{score_example}}}}}

CASE
{Path(case['prompt']).read_text(encoding='utf-8')}

RUBRIC
{rubric.read_text(encoding='utf-8')}

RESPONSE A
{a}

RESPONSE B
{b}
"""


def parse_judgment(raw: str, dimensions: list[str]) -> dict[str, Any]:
    text = raw.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0]
    data = json.loads(text)
    if data.get("winner") not in {"A", "B", "tie"}:
        raise ValueError("judge winner must be A, B, or tie")
    for side in ("A", "B"):
        if set(data.get(side, {})) != set(dimensions):
            raise ValueError(f"judge {side} scores must contain exactly {dimensions}")
        if any(not isinstance(data[side][key], int) or not 0 <= data[side][key] <= 3 for key in dimensions):
            raise ValueError("judge scores must be integers from 0 to 3")
    return data


def write_report(
    run_dir: Path,
    records: list[dict[str, Any]],
    dimensions: list[str],
    skill_name: str,
    selected_cases: int,
    total_cases: int,
    samples: int,
) -> None:
    scores: dict[str, dict[str, list[int]]] = {
        "baseline": defaultdict(list), "skill": defaultdict(list)
    }
    wins = defaultdict(int)
    for record in records:
        judgment = record["judgment"]
        mapping = record["mapping"]
        winner = judgment["winner"]
        wins["tie" if winner == "tie" else mapping[winner]] += 1
        for letter, mode in mapping.items():
            for dimension in dimensions:
                scores[mode][dimension].append(judgment[letter][dimension])

    lines = [
        f"# {skill_name} regression report",
        "",
        f"Coverage: {selected_cases}/{total_cases} cases at {samples} sample(s) per condition",
        f"Pairs judged: {len(records)}",
        "",
        "## Pairwise result",
        "",
    ]
    lines.append(f"- Clear wins: {wins['skill']}")
    lines.append(f"- Baseline wins: {wins['baseline']}")
    lines.append(f"- Ties: {wins['tie']}")
    lines.extend(["", "## Mean score by dimension", "", "| Dimension | Baseline | Clear | Delta |", "| --- | ---: | ---: | ---: |"])
    for dimension in dimensions:
        baseline = mean(scores["baseline"][dimension])
        skill = mean(scores["skill"][dimension])
        lines.append(f"| {dimension} | {baseline:.2f} | {skill:.2f} | {skill - baseline:+.2f} |")
    lines.extend(["", "## Gate", ""])
    integrity_delta = mean(scores["skill"].get("integrity", [0])) - mean(scores["baseline"].get("integrity", [0]))
    restraint_delta = mean(scores["skill"].get("restraint", [0])) - mean(scores["baseline"].get("restraint", [0]))
    total_delta = mean(v for values in scores["skill"].values() for v in values) - mean(v for values in scores["baseline"].values() for v in values)
    passed = total_delta > 0 and integrity_delta >= 0 and restraint_delta >= 0
    complete = selected_cases == total_cases and samples >= 3
    if not complete:
        result = "PROVISIONAL"
        qualifier = "Focused/incomplete coverage cannot satisfy the release gate."
    else:
        result = "PASS" if passed else "FAIL"
        qualifier = "Complete configured coverage."
    lines.append(
        f"**{result}** — overall delta {total_delta:+.2f}; integrity {integrity_delta:+.2f}; "
        f"restraint {restraint_delta:+.2f}. {qualifier}"
    )
    (run_dir / "REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill", default="clear-charts", help="Skill directory name under skills/ and evals/")
    parser.add_argument("--baseline-cmd", required=True, help="Command that reads a task on stdin and writes a response to stdout")
    parser.add_argument("--skill-cmd", help="Defaults to --baseline-cmd; skill instructions are added to the task")
    parser.add_argument("--judge-cmd", required=True, help="Command that reads judge prompt on stdin and writes JSON")
    parser.add_argument("--samples", type=int, default=3)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--timeout", type=int, default=300)
    parser.add_argument("--retries", type=int, default=1, help="Retries per failed or timed-out model command")
    parser.add_argument("--case", action="append", dest="selected")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.samples < 2:
        parser.error("--samples must be at least 2 to measure stochastic behavior")

    skill = ROOT / "skills" / args.skill
    eval_root = ROOT / "evals" / args.skill
    rubric = eval_root / "RUBRIC.md"
    config = eval_root / "config.json"
    if not skill.is_dir() or not rubric.is_file():
        parser.error(f"missing skill or rubric for {args.skill}")
    dimensions = json.loads(config.read_text(encoding="utf-8")).get("dimensions", DEFAULT_DIMENSIONS) if config.exists() else DEFAULT_DIMENSIONS
    if not isinstance(dimensions, list) or len(dimensions) < 2 or any(not isinstance(key, str) for key in dimensions):
        parser.error("config dimensions must be a list of at least two strings")

    all_cases = cases(eval_root)
    selected = [case for case in all_cases if not args.selected or case["id"] in args.selected]
    if not selected:
        parser.error("no matching cases")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = args.output or ROOT / "eval-results" / stamp
    run_dir.mkdir(parents=True, exist_ok=True)
    records = []

    for case in selected:
        case_dir = run_dir / case["id"]
        case_dir.mkdir(exist_ok=True)
        for sample in range(1, args.samples + 1):
            sample_dir = case_dir / f"sample-{sample}"
            sample_dir.mkdir(exist_ok=True)
            judgment_file = sample_dir / "judgment.json"
            if judgment_file.exists():
                saved = json.loads(judgment_file.read_text(encoding="utf-8"))
                records.append({"case": case["id"], "sample": sample, **saved})
                print(f"{case['id']} sample {sample}/{args.samples} (resumed)")
                continue

            baseline_file = sample_dir / "baseline.md"
            skill_file = sample_dir / "skill.md"
            if baseline_file.exists():
                baseline = baseline_file.read_text(encoding="utf-8").rstrip("\n")
            else:
                baseline = run_with_retries(args.baseline_cmd, task_payload(case, False, skill), args.timeout, args.retries, case["artifact"])
                baseline_file.write_text(baseline + "\n", encoding="utf-8")
            if skill_file.exists():
                skill_response = skill_file.read_text(encoding="utf-8").rstrip("\n")
            else:
                skill_response = run_with_retries(args.skill_cmd or args.baseline_cmd, task_payload(case, True, skill), args.timeout, args.retries, case["artifact"])
                skill_file.write_text(skill_response + "\n", encoding="utf-8")

            mapping_file = sample_dir / "mapping.json"
            if mapping_file.exists():
                mapping = json.loads(mapping_file.read_text(encoding="utf-8"))
                outputs = {"baseline": baseline, "skill": skill_response}
                pair = [(mapping["A"], outputs[mapping["A"]]), (mapping["B"], outputs[mapping["B"]])]
            else:
                pair, mapping = blind_pair_for_sample(args.seed, case["id"], sample, baseline, skill_response)
                mapping_file.write_text(json.dumps(mapping, indent=2) + "\n", encoding="utf-8")

            raw_judgment = run_with_retries(
                args.judge_cmd,
                judge_payload(case, pair[0][1], pair[1][1], rubric, dimensions),
                args.timeout,
                args.retries,
                case["artifact"],
            )
            (sample_dir / "judge-raw.txt").write_text(raw_judgment + "\n", encoding="utf-8")
            judgment = parse_judgment(raw_judgment, dimensions)
            judgment_file.write_text(json.dumps({"mapping": mapping, "judgment": judgment}, indent=2) + "\n", encoding="utf-8")
            records.append({"case": case["id"], "sample": sample, "mapping": mapping, "judgment": judgment})
            (run_dir / "records.json").write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")
            print(f"{case['id']} sample {sample}/{args.samples}")

    (run_dir / "records.json").write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")
    write_report(run_dir, records, dimensions, args.skill, len(selected), len(all_cases), args.samples)
    print(f"Report: {run_dir / 'REPORT.md'}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, ValueError, json.JSONDecodeError, subprocess.TimeoutExpired) as exc:
        print(f"run-evals: {exc}", file=sys.stderr)
        raise SystemExit(2)
