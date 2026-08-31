<p align="center">
  <img src="./assets/readme-cover.svg" alt="Human-Voice Writing" width="100%">
</p>

<p align="center">
  <a href="https://github.com/KKKKhazix/human-writing/releases/tag/v1.1.0"><img alt="Version 1.1.0" src="https://img.shields.io/badge/version-1.1.0-C4473A?style=flat-square"></a>
  <a href="./LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-313131?style=flat-square"></a>
  <a href="https://github.com/KKKKhazix/human-writing/releases/latest"><img alt="GitHub Release" src="https://img.shields.io/github/v/release/KKKKhazix/human-writing?style=flat-square&color=6B6258"></a>
</p>

<p align="center">
  <a href="#quick-install">Quick Install</a> ·
  <a href="#what-it-does">How It Works</a> ·
  <a href="#repo-structure">Repo Structure</a> ·
  <a href="https://github.com/KKKKhazix/human-writing/issues">Open an Issue</a>
</p>

> AI writing has a common problem: you finish reading it and think "that's pretty smooth," but you couldn't tell who wrote it. Human-Voice Writing is meant to fix exactly that.

Makes the model write pieces that read like a specific person talking — someone who knows some things, has opinions, occasionally goes off on a tangent, and then brings it back. Works for Quora answers, Medium/Substack articles, blog posts, long-form forum pieces, profiles, explainers, reviews, fiction, voiceover scripts, and most other English writing scenarios.

## What it does

Before writing, it solves a prerequisite question: do you actually have enough material to write about.

Non-fiction: if the material isn't enough, research; if research doesn't turn anything up, ask follow-up questions or shorten the piece — never pad with circular repetition to hit a word count. Fiction: create freely, but every scene still needs a goal, an action, and a change.

Once material clears the bar, it manages three things:

| Material | Progression | English |
| :--- | :--- | :--- |
| Non-fiction verifies facts, numbers, quotes, and first-hand experience. Fiction checks character, action, and causation. | Every paragraph brings something new — new fact, new action, new example, or new consequence. Never rehash. | Plain language carries the weight. Watch word order and pacing. Strip corporate tone, model-speak, and contrarian-pivot sentences. |

After the first draft, there's another gate. The skill checks each paragraph for circular reasoning, cuts repeated explanations, adjusts sentence-length rhythm, and blocks colon abuse, em-dashes, the "It's not X, it's Y" contrarian pivot, and common AI jargon. The checker script only enforces hard rules already written down — it doesn't decide style for you.

## Quick install

Send this to your Agent:

```bash
Help me install this skill: https://github.com/KKKKhazix/human-writing
```

The Agent will read the repo, find `human-writing`, and complete installation. After installation, it shows as "Human-Voice Writing."

<details>
<summary><strong>If your Agent doesn't support direct installation</strong></summary>

Download from [Releases](https://github.com/KKKKhazix/human-writing/releases/latest), or copy the entire [`human-writing`](./human-writing) folder into your local Skills directory. Keep the folder name as `human-writing`.

```text
~/.agents/skills/human-writing/
```

</details>

Use it like this after installation:

```text
Use $human-writing to turn my material into a piece with human voice and natural English rhythm.
```

## What changed in 1.1.0

Version 1.0 used string-based bans to block AI smell — banning "It's not X, it's Y," banning colons, banning a list of buzzwords. It worked, but the model would rephrase in different words while doing the exact same thing. "You think X — but actually Y," "only later did I realize," and "not A, but B" are all the same posture. Readers recognize the posture, not the exact words.

Version 1.1 moves the defense from wording to action: what's banned is the act of "setting up a misconception the reader doesn't have, then knocking it down" — regardless of what words it wears. The detection script was upgraded accordingly: added warnings for contrarian-pivot variants, AI-style parallelism, and lyrical metaphor padding; added statistical checks for sentence-length variance and conjunction density; and removed normal English expressions that were being falsely flagged. A ~2,000-word distilled version is also included — paste directly into ChatGPT, Claude, or any chat window.

See [CHANGELOG.md](./CHANGELOG.md) for the full change list.

## Repo structure

<details>
<summary><strong>Click to expand full directory</strong></summary>

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
```

| Path | Purpose |
| :--- | :--- |
| [`SKILL.md`](./human-writing/SKILL.md) | Entry point. Material gate, real-vs-fiction branching, writing workflow, delivery bans — everything in one file |
| [`forum-prose.md`](./human-writing/references/forum-prose.md) | How to write Quora answers, Medium posts, long-form forum pieces — rhythm, phrasing, concrete techniques |
| [`reality.md`](./human-writing/references/reality.md) | Factual boundaries for real people, history, news, data, and personal experience |
| [`fiction.md`](./human-writing/references/fiction.md) | Creation rules for fiction, stories, fictional essays, and dialogue |
| [`formats.md`](./human-writing/references/formats.md) | Short content, voiceover scripts, speeches, tutorials, reviews, and other special formats |
| [`revision.md`](./human-writing/references/revision.md) | How to revise after the first draft — per-pass checklist |
| [`check_prose.py`](./human-writing/scripts/check_prose.py) | Checks finished prose for hard-ban violations |
| [`human-writing-lite.md`](./human-writing/dist/human-writing-lite.md) | Distilled version, under 2,000 words — paste directly into a chat window |

</details>

## Feedback

MIT licensed. This repo contains only original rules and tools — no third-party articles, training corpora, or model weights.

If you hit rule conflicts, false positives, or behavior that's wrong on a particular model, please [open an issue](https://github.com/KKKKhazix/human-writing/issues). Including your prompt, model output snippet, and what you expected it to look like makes debugging much faster.

<p align="center">
  <sub>活人感写作 · Human-Voice Writing · 1.1.0</sub>
</p>
