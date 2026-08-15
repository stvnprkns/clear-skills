#!/usr/bin/env python3
"""Surface review evidence from Vega-Lite JSON. Never issue design verdicts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable


@dataclass(frozen=True)
class Evidence:
    code: str
    path: str
    observation: str
    question: str


def walk(value: Any, path: str = "$", inherited_mark: str | None = None) -> Iterable[tuple[str, dict[str, Any], str | None]]:
    if isinstance(value, dict):
        mark_value = value.get("mark", inherited_mark)
        mark = mark_value.get("type") if isinstance(mark_value, dict) else mark_value
        yield path, value, mark
        for key, child in value.items():
            yield from walk(child, f"{path}.{key}", mark)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, f"{path}[{index}]", inherited_mark)


def quantitative_channels(spec: dict[str, Any]) -> list[tuple[str, dict[str, Any]]]:
    encoding = spec.get("encoding")
    if not isinstance(encoding, dict):
        return []
    return [
        (channel, definition)
        for channel, definition in encoding.items()
        if isinstance(definition, dict) and definition.get("type") == "quantitative"
    ]


def inspect(spec: dict[str, Any]) -> list[Evidence]:
    findings: list[Evidence] = []

    if not spec.get("title"):
        findings.append(Evidence("missing-title", "$", "No chart title is declared.", "Is purpose supplied by an accessible surrounding figure label?"))
    if not spec.get("description"):
        findings.append(Evidence("missing-description", "$", "No Vega-Lite description is declared.", "Does the rendered artifact provide an equivalent concise summary?"))

    for path, node, mark in walk(spec):
        encoding = node.get("encoding")
        if not isinstance(encoding, dict):
            continue

        if mark in {"bar", "rect", "area"}:
            for channel, definition in quantitative_channels(node):
                scale = definition.get("scale")
                domain = scale.get("domain") if isinstance(scale, dict) else None
                if isinstance(domain, list) and len(domain) >= 2 and all(isinstance(v, (int, float)) for v in domain):
                    if min(domain) > 0 or max(domain) < 0:
                        findings.append(Evidence(
                            "nonzero-magnitude-domain",
                            f"{path}.encoding.{channel}.scale.domain",
                            f"A {mark} mark uses quantitative domain {domain}, which excludes zero.",
                            "Does mark extent encode magnitude from a baseline? If so, use zero or a position-based mark.",
                        ))

        color = encoding.get("color")
        if isinstance(color, dict) and color.get("type") == "nominal":
            scale = color.get("scale")
            domain = scale.get("domain") if isinstance(scale, dict) else None
            scheme_range = scale.get("range") if isinstance(scale, dict) else None
            count = len(domain) if isinstance(domain, list) else len(scheme_range) if isinstance(scheme_range, list) else 0
            if count > 8:
                findings.append(Evidence(
                    "many-categorical-colors",
                    f"{path}.encoding.color",
                    f"The nominal color encoding declares {count} categories/colors.",
                    "Must readers preserve identity across views, or would labels, grouping, selection, or neutral context reduce decoding?",
                ))

        tooltip = encoding.get("tooltip")
        persistent = {key for key in encoding if key in {"text", "detail", "color", "strokeDash", "shape"}}
        if tooltip and not persistent and mark in {"line", "point", "circle"}:
            findings.append(Evidence(
                "tooltip-dependency-candidate",
                f"{path}.encoding.tooltip",
                "Tooltip fields are declared without a persistent identity/detail channel in this unit specification.",
                "Are series identity or decision-critical values available without hover and on keyboard focus?",
            ))

        for channel, definition in quantitative_channels(node):
            axis = definition.get("axis")
            fmt = axis.get("format") if isinstance(axis, dict) else definition.get("format")
            if isinstance(fmt, str):
                match = re.search(r"\.(\d+)f", fmt)
                if match and int(match.group(1)) > 2:
                    findings.append(Evidence(
                        "high-decimal-precision",
                        f"{path}.encoding.{channel}",
                        f"Quantitative formatting requests {match.group(1)} decimal places.",
                        "Does the data quality and reader task justify this precision?",
                    ))

        for channel, definition in encoding.items():
            if not isinstance(definition, dict) or definition.get("type") != "temporal":
                continue
            field = definition.get("field")
            values = node.get("data", {}).get("values") if isinstance(node.get("data"), dict) else None
            if isinstance(field, str) and isinstance(values, list):
                parsed = []
                for row in values:
                    if isinstance(row, dict) and isinstance(row.get(field), str):
                        try:
                            parsed.append(datetime.fromisoformat(row[field].replace("Z", "+00:00")))
                        except ValueError:
                            pass
                deltas = sorted({(b - a).total_seconds() for a, b in zip(sorted(parsed), sorted(parsed)[1:])})
                if len(deltas) > 1:
                    findings.append(Evidence(
                        "irregular-time-intervals",
                        f"{path}.data.values",
                        f"Inline temporal values have {len(deltas)} distinct adjacent intervals.",
                        "Are dates missing, intentionally irregular, or aggregated in a way the chart should disclose?",
                    ))

        for definition in encoding.values():
            if isinstance(definition, dict) and definition.get("stack") == "normalize":
                findings.append(Evidence(
                    "normalized-composition",
                    path,
                    "A channel uses 100% normalized stacking.",
                    "Could materially different absolute totals change the decision? If yes, expose them too.",
                ))
                break

    resolve = spec.get("resolve")
    if isinstance(resolve, dict) and isinstance(resolve.get("scale"), dict):
        independent = [key for key, value in resolve["scale"].items() if value == "independent"]
        if independent:
            findings.append(Evidence(
                "independent-scales",
                "$.resolve.scale",
                f"Independent scales are declared for: {', '.join(independent)}.",
                "Is cross-panel magnitude comparison unimportant and is the scale difference disclosed?",
            ))

    layers = spec.get("layer")
    if isinstance(layers, list):
        y_fields = set()
        for layer in layers:
            if isinstance(layer, dict):
                y = layer.get("encoding", {}).get("y") if isinstance(layer.get("encoding"), dict) else None
                if isinstance(y, dict) and y.get("field"):
                    y_fields.add(y["field"])
        scale_resolution = spec.get("resolve", {}).get("scale", {}).get("y") if isinstance(spec.get("resolve"), dict) else None
        if len(y_fields) > 1 and scale_resolution == "independent":
            findings.append(Evidence(
                "dual-axis-candidate",
                "$.layer",
                f"Layered chart uses independent y scales for fields: {', '.join(sorted(y_fields))}.",
                "Could aligned panels, indexing, or a scatterplot avoid manufactured visual correlation?",
            ))

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec", type=Path, help="Vega-Lite JSON specification")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()
    try:
        spec = json.loads(args.spec.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"inspect-chart: {exc}", file=sys.stderr)
        return 2
    if not isinstance(spec, dict):
        print("inspect-chart: root must be a JSON object", file=sys.stderr)
        return 2

    findings = inspect(spec)
    if args.format == "json":
        print(json.dumps({"artifact": str(args.spec), "evidence": [asdict(item) for item in findings]}, indent=2))
    elif not findings:
        print("No configured evidence candidates found. This is not a Clear verdict.")
    else:
        for item in findings:
            print(f"[{item.code}] {item.path}\n  Observed: {item.observation}\n  Judge: {item.question}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
