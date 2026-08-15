#!/usr/bin/env python3
"""Deterministic command fixture for smoke-testing the eval orchestrator."""

import json
import re
import sys


prompt = sys.stdin.read()
if "strict blind pairwise judge" in prompt:
    schema = re.search(r'"A":\{([^}]+)\}', prompt)
    keys = re.findall(r'"([a-z-]+)":0', schema.group(1)) if schema else []
    scores = {key: 2 for key in keys}
    print(json.dumps({"winner": "tie", "reason": "orchestrator smoke fixture", "A": scores, "B": scores}))
else:
    print("Fixture response for orchestration validation.")
