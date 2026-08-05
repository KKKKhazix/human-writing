<p align="center">
  <img src="./assets/readme-cover.svg" alt="活人感写作" width="100%">
</p>

<p align="center">
  <a href="https://github.com/KKKKhazix/human-writing/releases/tag/v1.0.0"><img alt="Version 1.0.0" src="https://img.shields.io/badge/version-1.0.0-C4473A?style=flat-square"></a>
  <a href="./LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-313131?style=flat-square"></a>
  <a href="https://github.com/KKKKhazix/human-writing/releases/latest"><img alt="GitHub Release" src="https://img.shields.io/github/v/release/KKKKhazix/human-writing?style=flat-square&color=6B6258"></a>
</p>

<p align="center">
  <a href="#快速安装">快速安装</a> ·
  <a href="#它怎么工作">写作流程</a> ·
  <a href="#仓库结构">仓库结构</a> ·
  <a href="https://github.com/KKKKhazix/human-writing/issues">提交问题</a>
</p>

> 一套通用中文创作与改稿 Skill。它先确认有没有东西可写，再处理结构、节奏和措辞。

适用于知乎回答、论坛长帖、公众号文章、博客、评论、人物故事、历史叙事、行业解读、科普、教程、评测、个人叙事、小说、故事、对白、口播和演讲稿。

## 它管三件事

| 01　材料 | 02　推进 | 03　中文 |
| :--- | :--- | :--- |
| 现实写作核准事实、数字、引语和亲历。虚构写作检查人物、行动与因果。 | 每个新段落都要带来新事实、新动作、新例子、新区别或新后果。 | 白话打底，重视词序、停顿、照应和分寸，清除报告腔与模型腔。 |

现实内容不会用想象补事实。虚构内容可以创造人物、场景、对白和情节，不会被现实写作的来源要求绑住。两种写法在入口处分开，最后再用各自的标准审稿。

## 快速安装

把下面这句话发给你的 Agent。

```bash
帮我安装这个skill：https://github.com/KKKKhazix/human-writing
```

Agent 会读取仓库、找到 `human-writing`，并完成安装。安装后显示名为「活人感写作」。

<details>
<summary><strong>当前 Agent 不能直接安装时</strong></summary>

可以从 [Releases](https://github.com/KKKKhazix/human-writing/releases/latest) 下载 `human-writing.skill`，也可以把仓库里的 [`human-writing`](./human-writing) 文件夹完整复制到本机 Skills 目录。文件夹名必须保留为 `human-writing`。

```text
~/.agents/skills/human-writing/
```

</details>

安装后可以这样调用。

```text
使用 $human-writing，把我的材料写成一篇有活人感和中文韵律的作品。
```

## 它怎么工作

```mermaid
flowchart LR
    A["判断现实或虚构"] --> B["检查材料或人物行动"]
    B --> C["直接写第一稿"]
    C --> D["按文体修正"]
    D --> E["检查硬规则"]
```

| 现实写作 | 虚构创作 |
| :--- | :--- |
| 材料不够时，先研究、追问或缩短。真人经历、数字和原话都要能说明来路。 | 可以创造现场、对白、心理与结局。每个主要场景仍要有目标、动作或变化。 |

初稿完成后，Skill 会检查段落有没有真正往前走，删除重复解释，处理中文节奏，并清除冒号、破折号、翻案句、商业黑话和常见模型腔。检查脚本只执行已经写明的硬规则，不替作者决定文体。

## 仓库结构

<details>
<summary><strong>展开查看完整目录</strong></summary>

```text
human-writing/
├── SKILL.md
├── VERSION
├── LICENSE
├── agents/
│   └── openai.yaml
├── references/
│   ├── forum-prose.md
│   ├── reality.md
│   ├── fiction.md
│   ├── formats.md
│   └── revision.md
└── scripts/
    └── check_prose.py
tests/
└── test_check_prose.py
```

| 位置 | 用途 |
| :--- | :--- |
| [`SKILL.md`](./human-writing/SKILL.md) | 入口、材料门槛、现实与虚构分流、写作流程和交付禁令 |
| [`forum-prose.md`](./human-writing/references/forum-prose.md) | 知乎回答、论坛长帖、公众号文章和其他长篇散文写法 |
| [`reality.md`](./human-writing/references/reality.md) | 真人、历史、新闻、数据、评测、教程和个人经历的事实边界 |
| [`fiction.md`](./human-writing/references/fiction.md) | 小说、故事、虚构散文、对白和剧本的创作规则 |
| [`formats.md`](./human-writing/references/formats.md) | 短内容、口播、演讲、教程、评测、对白和诗歌等形式规则 |
| [`revision.md`](./human-writing/references/revision.md) | 初稿完成后的删改、节奏、词语和事实检查 |
| [`check_prose.py`](./human-writing/scripts/check_prose.py) | 检查成稿是否命中明确禁用项 |

</details>

## 开发与验证

检查脚本只使用 Python 标准库。在仓库根目录运行下面的命令，可以验证干净稿通过、违禁稿失败，以及代码和网址不被误报。

```bash
python3 -m unittest discover -s tests -v
```

## 开源与反馈

本项目采用 [MIT License](./LICENSE)。仓库只包含原创规则与工具，不包含第三方文章全文、训练语料或模型权重。

如果你发现规则冲突、误报，或者它在某个模型上表现异常，欢迎[提交 Issue](https://github.com/KKKKhazix/human-writing/issues)。带上原始提示词、输出片段和预期结果，会更容易复现问题。

<p align="center">
  <sub>活人感写作 · Human Writing · 1.0.0</sub>
</p>
