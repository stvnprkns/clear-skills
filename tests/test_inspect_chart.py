import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "skills" / "clear-charts" / "scripts" / "inspect-chart.py"
SPEC = importlib.util.spec_from_file_location("inspect_chart", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class InspectChartTests(unittest.TestCase):
    def test_surfaces_evidence_not_verdicts(self):
        chart = {
            "mark": "bar",
            "encoding": {
                "x": {"field": "team", "type": "nominal"},
                "y": {"field": "score", "type": "quantitative", "scale": {"domain": [93.5, 95.5]}},
            },
        }
        findings = MODULE.inspect(chart)
        self.assertIn("nonzero-magnitude-domain", {item.code for item in findings})
        self.assertFalse(any("verdict" in item.observation.lower() for item in findings))

    def test_does_not_flag_nonzero_line_domain(self):
        chart = {
            "title": "Sensor deviation",
            "description": "Hourly temperature near its operating target.",
            "mark": "line",
            "encoding": {
                "x": {"field": "time", "type": "temporal"},
                "y": {"field": "temperature", "type": "quantitative", "scale": {"domain": [98, 102]}},
            },
        }
        findings = MODULE.inspect(chart)
        self.assertNotIn("nonzero-magnitude-domain", {item.code for item in findings})

    def test_flags_independent_layered_y_axes(self):
        chart = {
            "title": "Spend and revenue",
            "description": "Monthly measures.",
            "layer": [
                {"mark": "line", "encoding": {"y": {"field": "spend", "type": "quantitative"}}},
                {"mark": "line", "encoding": {"y": {"field": "revenue", "type": "quantitative"}}},
            ],
            "resolve": {"scale": {"y": "independent"}},
        }
        findings = MODULE.inspect(chart)
        self.assertIn("dual-axis-candidate", {item.code for item in findings})


if __name__ == "__main__":
    unittest.main()
