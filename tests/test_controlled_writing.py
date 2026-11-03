"""验证语言检查保留受保护材料，并报告实际执行状态。"""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_controlled_writing.py"


def run_check(text, *options, script=SCRIPT):
    return subprocess.run(
        [sys.executable, "-B", str(script), "-", *options],
        input=text, text=True, capture_output=True,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )


class ControlledWritingTests(unittest.TestCase):
    def test_protected_material_and_original_line_numbers(self):
        text = '''---
title: it is worth noting that
---
```python
message = "it is worth noting that"
```
~~~text
it is worth noting that
~~~
> it is worth noting that
`it is worth noting that`
$$
\\text{it is worth noting that}
$$
\\[\\text{it is worth noting that}\\]
\\begin{align}
\\text{it is worth noting that}
\\end{align}
“it is worth noting that”
"it is worth noting that"
    it is worth noting that
https://example.org/importantly
./importantly/data.csv
The value is $importantly$ and \\(importantly\\).
It is worth noting that the value is positive.
'''
        result = run_check(text, "--json", "--no-dictionary")
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        boilerplate = [f for f in report["findings"] if f["engine"] == "SLOP"]
        self.assertEqual(len(boilerplate), 1, boilerplate)
        self.assertEqual(boilerplate[0]["line"], len(text.splitlines()))
        self.assertFalse(any(f["line"] < 24 for f in report["findings"]), report)

    def test_plain_text_still_checked_in_both_languages(self):
        result = run_check("值得注意的是，误差下降。\n\nIt is worth noting that errors decrease.", "--json")
        report = json.loads(result.stdout)
        self.assertEqual({f["line"] for f in report["findings"] if f["engine"] == "SLOP"}, {1, 3})

    def test_no_quality_grade_or_rewrite_verdict(self):
        result = run_check("It is worth noting that we leverage this result.")
        self.assertNotIn("需重写", result.stdout)
        self.assertNotIn("评分", result.stdout)

    def test_missing_engine_is_execution_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            isolated = Path(directory) / SCRIPT.name
            isolated.write_text(SCRIPT.read_text(), encoding="utf-8")
            result = run_check("We measure the error.", "--json", script=isolated)
        self.assertEqual(result.returncode, 2, result.stdout)
        self.assertFalse(json.loads(result.stdout)["complete"])

    def test_missing_input_reports_incomplete_json(self):
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [sys.executable, "-B", str(SCRIPT), str(Path(directory) / "missing.md"), "--json"],
                capture_output=True, text=True,
            )
        self.assertEqual(result.returncode, 2)
        self.assertFalse(json.loads(result.stdout)["complete"])

    def test_hard_findings_fail_only_in_strict_mode(self):
        text = "We don't measure the error."
        normal = run_check(text, "--json")
        strict = run_check(text, "--json", "--strict")
        self.assertTrue(any(f["severity"] == "hard" for f in json.loads(normal.stdout)["findings"]))
        self.assertEqual(normal.returncode, 0)
        self.assertEqual(strict.returncode, 1)


if __name__ == "__main__":
    unittest.main()
