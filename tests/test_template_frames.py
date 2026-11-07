"""check_prose.py 的回归测试。运行 python3 -m unittest discover -s tests"""

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


class TemplateFrameTests(unittest.TestCase):
    def test_era_opener_fails(self):
        code, out = check("在当今快节奏的时代，大家都很忙。")
        self.assertEqual(code, 1)
        self.assertIn("时代套话开头", out)

    def test_rallying_close_fails(self):
        code, out = check("我喝完那杯就走了。\n\n让我们一起品味生活吧！")
        self.assertEqual(code, 1)
        self.assertIn("号召式结尾", out)

    def test_summary_close_fails(self):
        code, out = check("他第二天又去了。总而言之，这家店还行。")
        self.assertEqual(code, 1)
        self.assertIn("总而言之", out)

    def test_enumeration_skeleton_warns(self):
        _, out = check("首先，价格便宜。其次，离家近。最后，老板人好。")
        self.assertIn("提纲骨架", out)


class PivotTests(unittest.TestCase):
    def test_buzhinshi_ershi_fails(self):
        code, out = check("咖啡不仅仅是一种饮品，而是一种生活方式。")
        self.assertEqual(code, 1)
        self.assertIn("禁用翻案句", out)

    def test_plain_buzhi_not_hard_failure(self):
        code, _ = check("他不只是来送饭的，还顺手把碗洗了。")
        self.assertEqual(code, 0)


class LineNumberTests(unittest.TestCase):
    def test_road_sign_reports_its_own_line(self):
        _, out = check("第一段写完了。\n\n值得注意的是，第二段在第三行。")
        self.assertIn("模型路标，第 3 行", out)


class CleanProseTests(unittest.TestCase):
    def test_concrete_prose_passes(self):
        code, out = check(
            "我一天喝两杯咖啡，上午一杯美式，下午三点左右再来一杯拿铁。"
            "楼下那家店我去了快两年，老板记得我要少冰。"
        )
        self.assertEqual(code, 0)
        self.assertIn("未发现", out)


if __name__ == "__main__":
    unittest.main()
