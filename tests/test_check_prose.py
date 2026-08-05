from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "human-writing" / "scripts" / "check_prose.py"


def run_checker(text: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(CHECKER), "-"],
        input=text,
        text=True,
        capture_output=True,
        check=False,
    )


class CheckProseCliTests(unittest.TestCase):
    def test_clean_text_passes(self) -> None:
        result = run_checker(
            "写作先得有东西可写。事实和心意站得住，句子朴素一点也没关系。"
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("未发现这份检查器覆盖的问题", result.stdout)

    def test_forbidden_shapes_fail_with_actionable_labels(self) -> None:
        result = run_checker(
            "先说结论：写作不是堆砌漂亮句子，而是完成认知跃迁的关键抓手。\n"
            "更微妙的是，它还能形成内容闭环——让观点沉淀下来。"
        )

        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        for label in ("中文冒号", "破折号", "硬停词", "黑话", "模型路标", "禁用翻案句"):
            with self.subTest(label=label):
                self.assertIn(label, result.stdout)

    def test_metadata_code_and_urls_are_ignored(self) -> None:
        result = run_checker(
            "---\n"
            "title: 先说结论\n"
            "---\n\n"
            "正文没有问题。\n\n"
            "`先说结论：认知跃迁`\n\n"
            "```text\n"
            "不是旧办法，而是新办法。\n"
            "```\n\n"
            "资料见 https://example.com/a:b。"
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("未发现这份检查器覆盖的问题", result.stdout)

    def test_context_jargon_warns_without_failing(self) -> None:
        result = run_checker("把溶液静置片刻，可以看到杯底出现沉淀。")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("需要结合语境判断", result.stdout)
        self.assertIn("沉淀", result.stdout)


if __name__ == "__main__":
    unittest.main()
