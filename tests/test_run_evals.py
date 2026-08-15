import importlib.util
import json
import random
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "run_evals.py"
SPEC = importlib.util.spec_from_file_location("run_evals", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class EvalRunnerTests(unittest.TestCase):
    def test_discovers_text_and_visual_cases(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "cases").mkdir()
            (root / "cases" / "one.md").write_text("case", encoding="utf-8")
            (root / "visual" / "two").mkdir(parents=True)
            (root / "visual" / "two" / "prompt.md").write_text("visual", encoding="utf-8")
            (root / "visual" / "two" / "expected.png").write_bytes(b"png")
            found = MODULE.cases(root)
        self.assertEqual([item["id"] for item in found], ["one", "visual-two"])
        self.assertTrue(found[1]["artifact"].endswith("expected.png"))

    def test_blind_pair_is_seeded_and_can_reverse_order(self):
        pair_a, mapping_a = MODULE.blind_pair(random.Random(1), "base", "clear")
        pair_b, mapping_b = MODULE.blind_pair(random.Random(1), "base", "clear")
        self.assertEqual(pair_a, pair_b)
        self.assertEqual(mapping_a, mapping_b)
        self.assertEqual(set(mapping_a.values()), {"baseline", "skill"})

    def test_sample_randomization_is_independent_of_resume_order(self):
        uninterrupted = [
            MODULE.blind_pair_for_sample(42, "case-a", sample, "base", "clear")[1]
            for sample in (1, 2, 3)
        ]
        resumed = [
            MODULE.blind_pair_for_sample(42, "case-a", sample, "base", "clear")[1]
            for sample in (2, 3)
        ]
        self.assertEqual(uninterrupted[1:], resumed)
        self.assertNotEqual(uninterrupted[0]["A"], uninterrupted[1]["A"])

    def test_parse_judgment_accepts_fenced_json_and_rejects_wrong_keys(self):
        dimensions = ["integrity", "restraint"]
        valid = {"winner": "A", "reason": "x", "A": {"integrity": 3, "restraint": 2}, "B": {"integrity": 2, "restraint": 1}}
        parsed = MODULE.parse_judgment(f"```json\n{json.dumps(valid)}\n```", dimensions)
        self.assertEqual(parsed["winner"], "A")
        valid["B"] = {"integrity": 2}
        with self.assertRaises(ValueError):
            MODULE.parse_judgment(json.dumps(valid), dimensions)

    def test_parse_judgment_rejects_out_of_range_scores(self):
        raw = json.dumps({"winner": "tie", "A": {"integrity": 4, "restraint": 2}, "B": {"integrity": 2, "restraint": 2}})
        with self.assertRaises(ValueError):
            MODULE.parse_judgment(raw, ["integrity", "restraint"])

    def test_report_calculates_pass_gate(self):
        records = [{
            "mapping": {"A": "skill", "B": "baseline"},
            "judgment": {
                "winner": "A", "reason": "better",
                "A": {"integrity": 3, "restraint": 3},
                "B": {"integrity": 2, "restraint": 2},
            },
        }]
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            MODULE.write_report(target, records, ["integrity", "restraint"], "clear-test", 2, 2, 3)
            report = (target / "REPORT.md").read_text(encoding="utf-8")
        self.assertIn("Clear wins: 1", report)
        self.assertIn("**PASS**", report)
        self.assertIn("+1.00", report)

    def test_focused_report_is_provisional_even_when_scores_improve(self):
        records = [{
            "mapping": {"A": "skill", "B": "baseline"},
            "judgment": {
                "winner": "A", "reason": "better",
                "A": {"integrity": 3, "restraint": 3},
                "B": {"integrity": 1, "restraint": 1},
            },
        }]
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            MODULE.write_report(target, records, ["integrity", "restraint"], "clear-test", 1, 5, 3)
            report = (target / "REPORT.md").read_text(encoding="utf-8")
        self.assertIn("Coverage: 1/5", report)
        self.assertIn("**PROVISIONAL**", report)
        self.assertNotIn("**PASS**", report)

    def test_run_command_reports_failure_and_timeout(self):
        with self.assertRaises(RuntimeError):
            MODULE.run_command("python3 -c 'import sys; sys.exit(7)'", "", 2)
        with self.assertRaises(subprocess.TimeoutExpired):
            MODULE.run_command("python3 -c 'import time; time.sleep(2)'", "", 1)

    def test_run_with_retries_recovers_once(self):
        with mock.patch.object(MODULE, "run_command", side_effect=[RuntimeError("first"), "ok"]) as command:
            result = MODULE.run_with_retries("agent", "prompt", 5, 1)
        self.assertEqual(result, "ok")
        self.assertEqual(command.call_count, 2)

    def test_artifact_placeholder_becomes_one_cli_argument(self):
        path = "/tmp/visual case.png"
        argv = MODULE.command_argv("codex exec --image={artifact} -", path)
        self.assertEqual(argv, ["codex", "exec", f"--image={path}", "-"])

    def test_artifact_placeholder_is_removed_for_text_case(self):
        argv = MODULE.command_argv("codex exec --image={artifact} -")
        self.assertEqual(argv, ["codex", "exec", "-"])

    def test_run_with_retries_stops_at_limit(self):
        with mock.patch.object(MODULE, "run_command", side_effect=RuntimeError("no")) as command:
            with self.assertRaises(RuntimeError):
                MODULE.run_with_retries("agent", "prompt", 5, 2)
        self.assertEqual(command.call_count, 3)

    def test_skill_instruction_is_only_in_skill_condition(self):
        skill = Path("/tmp/clear-test")
        with tempfile.TemporaryDirectory() as directory:
            prompt = Path(directory) / "prompt.md"
            prompt.write_text("Audit this artifact.", encoding="utf-8")
            case = {"prompt": str(prompt), "artifact": ""}
            baseline = MODULE.task_payload(case, False, skill)
            treatment = MODULE.task_payload(case, True, skill)
        self.assertNotIn(str(skill), baseline)
        self.assertIn(str(skill), treatment)


if __name__ == "__main__":
    unittest.main()
