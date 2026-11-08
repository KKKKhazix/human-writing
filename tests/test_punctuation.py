"""check_prose.py 标点计数的回归测试。运行 python3 -m unittest discover -s tests"""

import subprocess
import sys
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "human-writing" / "scripts" / "check_prose.py"


def check(text: str) -> tuple[int, str]:
    result = subprocess.run(
        [sys.executable, "-I", str(SCRIPT), "-"],
        input=text,
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout


class ColonTests(unittest.TestCase):
    def test_time_is_not_a_colon(self):
        code, _ = check("我们约在下午10:30见面，他迟到了。")
        self.assertEqual(code, 0)

    def test_ratio_is_not_a_colon(self):
        code, _ = check("面粉和水按1：1混合，揉十分钟。")
        self.assertEqual(code, 0)

    def test_prompt_colon_still_fails(self):
        code, out = check("一句话总结：这事不行。")
        self.assertEqual(code, 1)
        self.assertIn("中文冒号共 1 处", out)

    def test_markdown_table_alignment_row_is_not_a_colon(self):
        code, out = check(
            "| 材料 | 推进 |\n| :--- | :---: |\n| 先查材料够不够 | 每段带来新东西 |\n"
        )
        self.assertEqual(code, 0, out)

    def test_colon_inside_table_cell_still_fails(self):
        code, out = check("| 材料 | 推进 |\n| --- | --- |\n| 核心是：先查材料 | 每段带来新东西 |\n")
        self.assertEqual(code, 1)
        self.assertIn("中文冒号共 1 处", out)


class DashTests(unittest.TestCase):
    def test_double_dash_counts_once(self):
        code, out = check("他推门进来——手里拿着伞。")
        self.assertEqual(code, 1)
        self.assertIn("破折号共 1 处", out)

    def test_separate_dashes_count_separately(self):
        _, out = check("他推门进来——手里拿着伞——又走了。")
        self.assertIn("破折号共 2 处", out)


if __name__ == "__main__":
    unittest.main()
