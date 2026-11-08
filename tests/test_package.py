"""Skill 包本身的一致性检查。运行 python3 -m unittest discover -s tests"""

import importlib.util
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "human-writing"
SKILL = SKILL_DIR / "SKILL.md"
REVISION = SKILL_DIR / "references" / "revision.md"
CHECKER = SKILL_DIR / "scripts" / "check_prose.py"


def frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    assert match, "SKILL.md 缺少 frontmatter"
    fields = {}
    for line in match.group(1).splitlines():
        key, _, value = line.partition(": ")
        fields[key] = value
    return fields


def load_checker():
    spec = importlib.util.spec_from_file_location("check_prose", CHECKER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def quoted_terms(line: str) -> set[str]:
    return set(re.findall(r"“([^”]+)”", line))


def revision_line(prefix: str) -> str:
    for line in REVISION.read_text(encoding="utf-8").splitlines():
        if line.startswith(prefix):
            return line
    raise AssertionError(f"revision.md 里找不到以“{prefix}”开头的段落")


class SkillMetadataTests(unittest.TestCase):
    def test_frontmatter_follows_agent_skills_spec(self):
        fields = frontmatter(SKILL.read_text(encoding="utf-8"))
        self.assertEqual(fields.get("name"), SKILL_DIR.name)
        description = fields.get("description", "")
        self.assertTrue(0 < len(description) <= 1024, len(description))
        self.assertNotRegex(description, r"[<>]")

    def test_versions_agree(self):
        version = (SKILL_DIR / "VERSION").read_text(encoding="utf-8").strip()
        heading = re.search(r"^# 活人感写作 (\S+)$", SKILL.read_text(encoding="utf-8"), re.MULTILINE)
        changelog = re.search(r"^## (\d+\.\d+\.\d+)", (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"), re.MULTILINE)
        marketplace = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
        self.assertEqual(heading.group(1), version)
        self.assertEqual(changelog.group(1), version)
        self.assertEqual(marketplace["plugins"][0]["version"], version)

    def test_marketplace_points_at_the_skill(self):
        marketplace = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
        plugin = marketplace["plugins"][0]
        self.assertEqual(plugin["source"], "./")
        for path in plugin["skills"]:
            self.assertTrue((ROOT / path / "SKILL.md").is_file(), path)

    def test_referenced_files_exist(self):
        text = SKILL.read_text(encoding="utf-8")
        for path in set(re.findall(r"`((?:references|scripts)/[^`\s]+)", text)):
            self.assertTrue((SKILL_DIR / path).is_file(), path)


class RuleSyncTests(unittest.TestCase):
    """revision.md 写明检查脚本的硬禁词必须和规则完全一致。"""

    def setUp(self):
        self.checker = load_checker()

    def test_hard_jargon_matches_revision(self):
        line = revision_line("下面这些词在本 Skill 中作为绝对禁词处理。")
        words = line.split("处理。", 1)[1].split("。", 1)[0].split("、")
        self.assertEqual(set(words), set(self.checker.HARD_JARGON))

    def test_hard_stops_match_revision(self):
        terms = quoted_terms(revision_line("搜索“说白了”"))
        self.assertEqual(terms, set(self.checker.HARD_STOPS))

    def test_road_signs_match_revision(self):
        terms = quoted_terms(revision_line("检查模型常用的洞察路标。"))
        self.assertEqual(terms, set(self.checker.ROAD_SIGNS))


class ReadmeTests(unittest.TestCase):
    def test_readme_passes_its_own_checker(self):
        result = subprocess.run(
            [sys.executable, "-I", str(CHECKER), str(ROOT / "README.md")],
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
