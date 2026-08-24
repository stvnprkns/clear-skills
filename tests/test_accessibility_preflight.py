import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "clear-visuals" / "scripts" / "check_web_accessibility.py"
SPEC = importlib.util.spec_from_file_location("accessibility_preflight", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


class AccessibilityPreflightTests(unittest.TestCase):
    def inspect(self, html: str):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "test.html"
            path.write_text(html, encoding="utf-8")
            return MODULE.inspect(path)

    def test_accepts_basic_semantic_content(self):
        issues = self.inspect('<img src="x.png" alt="Trend rises"><label for="q">Query</label><input id="q"><table><tr><th scope="col">A</th></tr><tr><td>1</td></tr></table>')
        self.assertEqual(issues, [])

    def test_finds_structural_failures(self):
        issues = self.inspect('<div aria-hidden="true"><button>Hidden</button></div><img src="x.png"><label for="missing">X</label><table><tr><td>1</td></tr></table>')
        rules = {issue["rule"] for issue in issues}
        self.assertEqual(rules, {"aria-hidden-focus", "img-alt", "label-target", "table-headers"})


if __name__ == "__main__":
    unittest.main()
