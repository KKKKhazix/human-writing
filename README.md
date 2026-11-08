<p align="center">
  <img src="./assets/readme-cover.svg" alt="活人感写作" width="100%">
</p>

<p align="center">
  <a href="https://github.com/KKKKhazix/human-writing/releases/latest"><img alt="GitHub Release" src="https://img.shields.io/github/v/release/KKKKhazix/human-writing?style=flat-square&color=C4473A"></a>
  <a href="./LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-313131?style=flat-square"></a>
  <a href="https://agentskills.io"><img alt="Agent Skills" src="https://img.shields.io/badge/Agent_Skills-standard-6B6258?style=flat-square"></a>
</p>

<p align="center">
  <a href="#快速安装">快速安装</a> ·
  <a href="#它做什么">写作流程</a> ·
  <a href="#仓库结构">仓库结构</a> ·
  <a href="https://github.com/KKKKhazix/human-writing/issues">提交问题</a>
</p>

> AI 写的中文读着挺顺，读完却说不出是谁写的。这个 Skill 想治的就是这个毛病。

装上以后，模型写知乎回答、公众号文章、博客、论坛长帖、人物故事、科普、评测、小说和口播稿，会先看手里有没有东西可写，再像一个具体的人那样把事讲出来。这个人知道一些事，也有拿不准的地方，敢下判断，偶尔岔开一句，还能把话接回来。

## 它做什么

动笔之前，它先清点材料。

现实题材的材料不够，它就去查。查不到就问你，一次最多问三个问题。你不让问，它就把文章写短，不拿车轱辘话凑字数，也不替你编一段没发生过的亲历。虚构题材可以放开编人物和情节，每场戏仍然要有人想要点什么，做了点什么，戏演完以后有东西变了。

材料过关以后，写的时候盯着三件事。

| 材料 | 推进 | 中文 |
| :--- | :--- | :--- |
| 现实稿核准事实、数字、引语和亲历，虚构稿检查人物、行动和因果 | 每段都要带来一件新东西，新事实、新动作都算，写过的意思不换个说法再写一遍 | 白话打底，在意词序和停顿，清掉报告腔、模型腔和翻案腔 |

初稿写完还有一道关。它会逐段看文章有没有在原地转圈，砍掉重复的解释，调一调长短句，再清掉冒号、破折号、`不是……而是……` 这类翻案腔和常见的 AI 黑话。检查脚本只管写明了的硬规则，文风好不好它不管。

## 快速安装

最省事的办法，是把下面这句话发给你的 Agent。

```text
帮我安装这个 skill：https://github.com/KKKKhazix/human-writing
```

Agent 会自己读仓库，找到 `human-writing` 文件夹装好，装完显示名叫活人感写作。Claude Code、Codex 和其他支持 Agent Skills 标准的工具都能这么装。

Claude Code 也可以走插件市场。

```text
/plugin marketplace add KKKKhazix/human-writing
/plugin install human-writing@human-writing
```

<details>
<summary><strong>手动安装</strong></summary>

从 [Releases](https://github.com/KKKKhazix/human-writing/releases/latest) 下载 `human-writing-版本号.zip`，解压后把整个 `human-writing` 文件夹放进 Skills 目录，文件夹名别改。只复制 `SKILL.md` 不够用，`references/` 和 `scripts/` 也得一起带上。

```text
Claude Code   ~/.claude/skills/human-writing/
Codex         ~/.agents/skills/human-writing/
```

别的工具放进它自己的 Skills 目录就行。

</details>

装好以后照常提需求，写东西、改稿、去 AI 味都会用上它。想点名用，就在需求里写上活人感写作。

```text
用活人感写作，把下面这些材料写成一篇知乎回答。
```

聊天窗口装不了 Skill，就用[蒸馏版](./human-writing/dist/human-writing-lite.md)。把它整段贴进去，跟在写作需求后面。

## 1.2.0 改了什么

这一版基本都在处理大家提的反馈，合进了 Shann5、qshanx 和 TZPlus 的 PR，谢谢他们。

- 写小说时心理描写被删光的问题修了。改稿时删的只是动作后面那句重复的情绪解释，动作看不出来的心理照样要写。
- 检查脚本会拦 `在当今……时代` 这种开头、`让我们……吧` 这种结尾和 `不仅仅是……而是……`。误判也少了几类，`10:30` 里的冒号、引号里的人物对白都不再算违规。
- description 压到两百来字，写明公文、合同、技术文档、代码和翻译不用它。
- 这份 README 照它自己的规则重写了一遍。以前的版本被人在 Issue 里说一股 AI 味，说得没错。

完整变更见 [CHANGELOG.md](./CHANGELOG.md)。

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
├── dist/
│   └── human-writing-lite.md
├── references/
│   ├── forum-prose.md
│   ├── reality.md
│   ├── fiction.md
│   ├── formats.md
│   └── revision.md
└── scripts/
    └── check_prose.py
tests/
.claude-plugin/
└── marketplace.json
```

| 位置 | 干什么的 |
| :--- | :--- |
| [`SKILL.md`](./human-writing/SKILL.md) | 入口。材料门槛、现实和虚构怎么分、写作流程、交稿前的禁令，都在这一份里 |
| [`forum-prose.md`](./human-writing/references/forum-prose.md) | 知乎、公众号、论坛长帖怎么写，节奏和措辞的具体做法 |
| [`reality.md`](./human-writing/references/reality.md) | 写真人、历史、新闻、数据和个人经历时，事实的边界在哪 |
| [`fiction.md`](./human-writing/references/fiction.md) | 小说、故事、虚构散文和对白的写法 |
| [`formats.md`](./human-writing/references/formats.md) | 短内容、口播、演讲、教程、评测这些特殊形式 |
| [`revision.md`](./human-writing/references/revision.md) | 初稿写完以后一遍一遍怎么改 |
| [`check_prose.py`](./human-writing/scripts/check_prose.py) | 查成稿有没有踩到硬禁令 |
| [`human-writing-lite.md`](./human-writing/dist/human-writing-lite.md) | 蒸馏版，不到两千字，给聊天窗口直接粘贴 |
| [`tests/`](./tests) | 检查脚本的测试 |

</details>

## 参与开发

改了检查脚本，在仓库根目录跑一遍测试。

```bash
python3 -m unittest discover -s tests -v
```

每个 PR 上 CI 都会跑这些测试，再用 `check_prose.py` 把这份 README 查一遍。

## 反馈

MIT 协议开源。仓库里只有原创的规则和脚本，没有第三方文章、训练语料或模型权重。

碰到规则互相打架、误报，或者某个模型上表现不对，欢迎[提 Issue](https://github.com/KKKKhazix/human-writing/issues)。附上你的提示词和模型输出片段，再说说你觉得应该是什么样，排查起来会快很多。

<p align="center">
  <sub>活人感写作 · Human Writing</sub>
</p>
