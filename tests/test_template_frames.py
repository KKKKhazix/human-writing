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

    def test_common_opener_fails_at_sentence_start(self):
        code, out = check("众所周知，咖啡因会让人兴奋。")
        self.assertEqual(code, 1)
        self.assertIn("套话开头", out)

    def test_model_sample_still_caught(self):
        code, out = check(
            "在当今快节奏的时代，咖啡早已成为很多人的日常。\n\n"
            "我每天喝两杯，上午一杯，下午一杯。\n\n"
            "让我们一起品味生活中的每一杯咖啡吧！"
        )
        self.assertEqual(code, 1)
        self.assertIn("时代套话开头", out)
        self.assertIn("号召式结尾", out)


class TemplateFrameScopeTests(unittest.TestCase):
    """套话开头只查开篇和句首，号召式结尾只查末段的引号外文字。"""

    def test_dialogue_let_us_passes(self):
        code, out = check("“让我们走吧。”她把伞递给他。")
        self.assertEqual(code, 0, out)

    def test_reported_let_us_passes(self):
        code, out = check("老板说让我们先回去吧，明天再来。")
        self.assertEqual(code, 0, out)

    def test_let_us_before_the_last_paragraph_passes(self):
        code, out = check("让我们先回去吧，他说。\n\n第二天我们又去了一趟，店还是关着。")
        self.assertEqual(code, 0, out)

    def test_dangdai_without_era_noun_passes(self):
        code, out = check("在当今的物价下，这笔钱撑不了三个月。")
        self.assertEqual(code, 0, out)

    def test_era_phrase_after_the_opening_passes(self):
        code, out = check("我第一次去那家店是在前年。\n\n他说在这个行业里，在当今社会，熟客比广告管用。")
        self.assertEqual(code, 0, out)

    def test_zhongsuozhouzhi_mid_sentence_passes(self):
        code, out = check("这个道理众所周知，可没人照做。")
        self.assertEqual(code, 0, out)

    def test_quoted_summary_word_passes(self):
        code, out = check("“总而言之，你得走。”他说完就挂了电话。")
        self.assertEqual(code, 0, out)


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
