#!/usr/bin/env python3
"""Render each visual eval HTML artifact to its checked-in PNG fixture."""

from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
def main() -> int:
    cases = sorted((ROOT / "evals").glob("*/visual/*/bad.html"))
    for source in cases:
        target = source.with_name("expected.png")
        subprocess.run(
            [
                "npx",
                "playwright",
                "screenshot",
                "--browser",
                "chromium",
                "--viewport-size",
                "960,720",
                source.resolve().as_uri(),
                str(target),
            ],
            check=True,
            cwd=ROOT,
        )
        print(target.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
