#!/usr/bin/env python3
"""Static accessibility preflight for rendered-web source.

This catches a small set of high-confidence structural defects. It cannot prove
WCAG conformance, visual quality, keyboard behavior, or user comprehension.
"""

from __future__ import annotations

import argparse
import json
import sys
from html.parser import HTMLParser
from pathlib import Path


FOCUSABLE = {"a", "button", "input", "select", "textarea", "summary"}


class AccessibilityParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.issues: list[dict[str, object]] = []
        self.ids: dict[str, int] = {}
        self.labels: list[tuple[str, int]] = []
        self.hidden_depth = 0
        self.stack: list[tuple[str, bool]] = []
        self.table_stack: list[dict[str, object]] = []

    def issue(self, rule: str, message: str) -> None:
        self.issues.append({"rule": rule, "line": self.getpos()[0], "message": message})

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        hidden_here = values.get("aria-hidden", "").lower() == "true"
        self.stack.append((tag, hidden_here))
        if hidden_here:
            self.hidden_depth += 1

        element_id = values.get("id")
        if element_id:
            if element_id in self.ids:
                self.issue("duplicate-id", f"Duplicate id '{element_id}' (first seen on line {self.ids[element_id]}).")
            else:
                self.ids[element_id] = self.getpos()[0]

        if tag == "img" and "alt" not in values:
            self.issue("img-alt", "Image is missing an alt attribute; use contextual alt text or alt='' when decorative.")

        if tag == "label" and values.get("for"):
            self.labels.append((values["for"], self.getpos()[0]))

        tabindex = values.get("tabindex")
        focusable = (tag in FOCUSABLE and values.get("disabled") is None) or (tabindex is not None and tabindex != "-1")
        if self.hidden_depth and focusable:
            self.issue("aria-hidden-focus", f"Focusable <{tag}> is inside aria-hidden content.")

        if tag == "svg" and values.get("role") == "img":
            named = bool(values.get("aria-label") or values.get("aria-labelledby"))
            if not named and not self.hidden_depth:
                self.issue("svg-name", "SVG with role='img' needs an accessible name.")

        if tag == "table":
            self.table_stack.append({"line": self.getpos()[0], "headers": 0})
        elif tag == "th" and self.table_stack:
            self.table_stack[-1]["headers"] = int(self.table_stack[-1]["headers"]) + 1

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag: str) -> None:
        if tag == "table" and self.table_stack:
            table = self.table_stack.pop()
            if table["headers"] == 0:
                self.issue("table-headers", f"Table opened on line {table['line']} has no <th> header cells.")

        for index in range(len(self.stack) - 1, -1, -1):
            open_tag, hidden_here = self.stack[index]
            if open_tag == tag:
                del self.stack[index:]
                if hidden_here:
                    self.hidden_depth -= 1
                break

    def finalize(self) -> None:
        for target, line in self.labels:
            if target not in self.ids:
                self.issues.append({"rule": "label-target", "line": line, "message": f"Label references missing id '{target}'."})


def inspect(path: Path) -> list[dict[str, object]]:
    parser = AccessibilityParser()
    parser.feed(path.read_text(encoding="utf-8"))
    parser.finalize()
    return parser.issues


def main() -> int:
    argument_parser = argparse.ArgumentParser(description=__doc__)
    argument_parser.add_argument("files", nargs="+", type=Path)
    argument_parser.add_argument("--json", action="store_true")
    args = argument_parser.parse_args()

    results = {str(path): inspect(path) for path in args.files}
    failures = sum(len(issues) for issues in results.values())
    if args.json:
        print(json.dumps({"files": results, "issue_count": failures}, indent=2))
    else:
        for path, issues in results.items():
            for issue in issues:
                print(f"{path}:{issue['line']}: {issue['rule']}: {issue['message']}")
        if not failures:
            print(f"Static accessibility preflight passed for {len(results)} file(s).")
        print("Boundary: static preflight does not prove WCAG conformance or usability.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
