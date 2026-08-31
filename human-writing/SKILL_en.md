---
name: human-writing-en
description: General-purpose English writing and revision skill. For Quora answers, long-form forum posts, Medium/Substack blog articles, reviews, personal essays, profiles, historical narratives, news and industry analysis, explainers, tutorials, reviews, personal narratives, fiction, stories, dialogue, voiceover scripts, and speeches. By default, writes as a specific person who has done the reading, done the legwork, and wants to lay things out clearly. Preserves the natural feel and rhythm of a long-form English internet post — the sense that a real person is talking to you — while avoiding hollow corporate tone, rally-cry speech mode, marketing copy, and model-speak. Non-fiction longform checks whether material is sufficient before drafting; when material is thin, researches, asks follow-up questions, or shortens — never pads with repeated explanations. Real-world content additionally verifies facts, quotes, data, and user experience. Fiction may freely create characters, scenes, dialogue, psychology, and plot. Finished prose absolutely may not use contrarian-pivot sentences ("It's not X, it's Y") and their variants, or business buzzwords and model-stock phrases. Does not build author profiles, personal rule libraries, or personal writing skills.
---

# Human-Voice Writing 1.1.0

By default, writes articles that read like a long-form post worth finishing. The reader should feel a specific person on the other side. This person knows some things, and doesn't know others. They're willing to give details, willing to take a stance, occasionally go off on a tangent, and then bring it back.

Don't mistake "human voice" for catchphrases, swearing, typos, and internet memes. It comes primarily from material, second from the speaker's position, and last from tone.

## Gate 1: What makes this piece hold up

This step comes before outlining and drafting. The user's target word count doesn't let you skip it.

Real-world pieces rely on the first two categories of material; fiction relies on the third. Mixed work separates the two first.

- Experiences, facts, numbers, actions, direct quotes, and judgments the user has explicitly provided.
- Cases, data, product processes, biographical details, and historical context that have already been researched and can be verified.
- In fiction: events, character actions, and scene changes the author is authorized to create.

In non-fiction, an AI's improvised "imagine someone who…," unattributed hypothetical scenarios, common-sense extrapolations, abstract speculation about consequences, metaphors, and synonymous rewrites — none of these may pad the piece. Explaining "easy data entry," "voice preserves state," and "retrieval finds old content" five times each still leaves you with only three pieces of material.

Fiction may create characters, settings, and details without finding real-world sources for them. Each major paragraph or scene still needs an action, a choice, a relationship shift, an information shift, or a consequence. Changing the scenery and rephrasing, with nothing actually happening, cannot pad the piece either.

For non-fiction aimed at roughly 2,000 words, first list at least five specific pieces of material internally, noting where each came from — which user quote or which reliable source. A single summary category doesn't count. The five pieces must also form an actual process, not five adjacent truisms.

If you can't list five pieces for non-fiction, don't write the long piece yet. No titles or long-form body text on this pass. Target word count, user pressure, and "just write it" cannot multiply material.

When real-world material is thin, pick exactly one of these approaches:

- Factual topics with public sources available: research first, then recount. Having search tools and not using them still counts as no material.
- Personal experience or private judgment that requires user material: ask all at once — up to three questions — and don't deliver a draft simultaneously.
- User explicitly forbids follow-up questions: research what you can, recount afterward, and if five pieces are met, write to the original target length. If research still leaves fewer than five, narrow the topic and deliver at most a ~1,000-word short answer. A piece that's visibly shorter than the target is better than fake examples and repeated explanations filling the gap.

Before drafting non-fiction, record where each important piece of material came from. Content with no verifiable source can't hold up a factual paragraph. For fiction, check instead that each scene is supported by a character goal, an action, or a change — don't fabricate sources for fictional details. Don't hand these internal checks to the user.

Non-fiction opinion pieces have one high-frequency error to block immediately. The user gives three abstract ideas — "easy input," "voice preserves state," "AI can retrieve old content" — and asks for 1,200+ words. That's still only three pieces of material. You cannot pad each with use cases, significance, risks, and future outlooks, then stretch into a dozen paragraphs. First find real products, real usage processes, research, or user experience. If you can't find any, ask. If the user won't let you ask and research still falls short, write a short answer.

## Read references by task

- For new or substantially rewritten Quora answers, long-form forum posts, Medium/Substack articles, blog posts, reviews, profiles, and industry pieces, read `references/forum-prose.md`.
- For real people, history, news, products, data, reviews, tutorials, business information, and user experience, also read `references/reality.md`.
- For fiction, stories, fictional essays, dialogue, and scripts, switch to `references/fiction.md`. When the user asks for a forum-style story or first-person narrative, also read `references/forum-prose.md`.
- When short content, personal narrative, tutorials, reviews, voiceover scripts, speeches, scripts, dialogue, and poetry need special handling, read `references/formats.md`.
- After the first draft is complete, then read `references/revision.md`. Don't load detailed revision rules before drafting.

Don't load all reference files at once "just in case" — only read what the current task actually hits. A genuinely mixed task may load multiple files, but `references/revision.md` stays until after the first draft. During creation, keep positive goals front and center; the delivery prohibitions listed in this file are checked item by item after the first draft is done.

## When multiple rules apply simultaneously

Process in this order:

1. What the current user has explicitly specified: genre, real vs. fictional nature, tone, and delivery format.
2. What the piece promises about reality. Real content obeys factual boundaries; fiction obeys character logic, causation, and world rules.
3. Rules in `references/fiction.md`, `references/reality.md`, and `references/formats.md` that directly apply to the current task.
4. The default prose style in `references/forum-prose.md` and this file.
5. Revision rules in `references/revision.md` and checker-script warnings.

Specific genres override general defaults. Non-fiction source requirements cannot be forced onto pure fiction. The structural completeness expected of prose cannot be forced onto poetry stanzas or character dialogue. Checker scripts can only enforce hard prohibitions already written down; warnings don't decide genre for the author.

## First, determine what the piece promises about reality

### Non-fiction

Real people, real events, numbers, quotes, and user experience must all be verified. The user did not provide first-hand experience, on-the-ground detail, dialogue, or interior thoughts — you may not fill those in as fact.

### Fiction

You may create characters, places, scenes, dialogue, interior thoughts, and endings. Characters, timing, causation, and world rules must remain internally consistent throughout.

### Mixed work

First separate what must be accurate (the real-world parts) from what may be created. Only verify facts that affect the story and real-world judgment.

When the user says "fiction," "fictional," "hypothetical," "just make it up" — create freely. When the user demands real, documentary, first-hand, or historically faithful — verify first, then write.

## Before writing, find your speaking position

Answer these five questions internally. Don't hand the answers to the user verbatim.

1. Who is talking about this. What gives them the right to know, and where are they only speculating.
2. What prompted them to speak now. It could be a news item, an experience, a question, or a small thing that's been bugging them.
3. What material they have to support the piece. Prioritize actions, numbers, time, place, direct quotes, failures, costs, and what happened afterward.
4. Where they have a clear judgment. What that judgment is based on, and where it stops.
5. What the reader would most naturally ask next after the last paragraph.

If the non-fiction piece has too little for item 3, go back to the pre-draft material check. Don't pad with philosophy, symbolism, imagined scenes, or repeated conclusions. A 10,000-word non-fiction piece needs enough material to unfold across multiple stages, cases, or real-world relationships. Fiction that lacks character goals, actions, and scene changes should go back to `references/fiction.md` to build out the story — don't ask the user for nonexistent real-world sources.

When real-world material is insufficient, stop here. If public sources exist, research. If the piece depends on user experience, emotion, or private judgment, ask all of these at once:

- What actually happened between you and this thing.
- Which moment, number, action, or quote stands out most to you.
- What judgment you most want to make right now.

Don't hand over an empty draft and hope the user fills in the human voice.

When the user demands immediate delivery and material can't be supplemented, a shorter, denser piece is better than an unfounded one. Length is the goal; material boundaries are the line. Fiction creates freely per its authorization; length is supported by events and scene changes.

When personal experience is missing critical material, ask at most three questions. If the user explicitly asks for no follow-ups or for immediate output, research first, then narrow the topic or shorten the length — never attribute new experiences to the user.

## The first draft writes with a person

The first draft starts from a specific speaker and specific material. Write like you're explaining to someone who's interested but doesn't know the story — handling the questions that arise as you go.

Below is the default mode for modern plain prose. Poetry, scripts, character dialogue, and experimental writing follow their own genre rules and must not be mangled to fit prose syntax.

- Get to the event quickly. Open with a direct answer, a scene that just happened, or an unusual small fact. Don't preview the essay's structure.
- Unless the user explicitly wants a list or tutorial, don't name the topic as "two costs, three causes, four stages." Categories should emerge from the material — don't use categorization as a substitute for the essay.
- One paragraph finishes one thing. It can cover an action, fill in background, do a calculation, explain a reason, acknowledge a doubt, or offer a judgment.
- Each new paragraph must introduce something new. A new fact, a new action, a new example, a new distinction, or a new consequence. Restating the same point in different words doesn't count as progress.
- The next paragraph picks up the question left by the previous one. Progress comes from material and causation, not from signposts like "at a deeper level" or "the real issue."
- Get the subject and action on the page first, then add time, reasons, conditions, and examples. Long sentences are fine — the reader just needs to know who did what early on.
- Let plain language carry the weight. The literary quality emerges from word order, pacing, and restraint — not from rare words, string-of-idioms passages, or forced allusions.
- When the action, detail, or direct quote has already conveyed the feeling, stop. Don't chase it with explanation for the reader's benefit.
- Normal repetition, amplification, self-correction, and brief tangents are allowed. Each must arise from the immediate context — no performing casualness at fixed intervals.
- Opinions can lean. Emotions can show. Put the reasoning nearby so the reader knows this is the author's view.
- Non-fiction humor comes from the absurdity of the situation itself — no separate jokes grafted on, no forced quips attached to serious material. Fiction humor belongs to the characters, relationships, and scenes.
- Paragraphs don't need to be the same length. End plain sentences with a plain period. A one-sentence paragraph is reserved for places that genuinely need a pause.
- When the story is told, stop. Don't force a升华 (soaring conclusion), call back to the opening, or declare historical significance. Echoes are only kept when the thing's function or meaning has actually shifted, and returning to a macro scale at the end is only allowed when the essay has been operating at that scale throughout. Don't summarize the essay again in the final paragraph.

Calibrate with these sentences:

> He left Shanghai after graduation and went to Chengdu. That quant trading program had been running for a while, and he figured he could try it full-time. Whether the income would hold — nobody knew at the time.

This is closer to the target than "He closed off an easy road and bet his fate on the table." The first version gives actions, conditions, and risk. The second gives only posture.

## Don't wear the forum costume

Forum feel is not "bro," "guys," "thanks for asking," or "let me pour a cup of tea and take my time." Cigarette butts, beer, cold bread, late-night screens, and a phone ringing in the quiet don't magically add realism either.

In non-fiction, unattributed precise timestamps, expressions, weather, room furnishings, and dialogue are fake details. The more specific the fake detail, the stronger the AI smell. In fiction, you may create all of these — but the details must follow the character's perspective and actions, not just dress the piece in forum clothing.

What's actually useful in non-fiction is source attribution. Write clearly where the author learned this, where they were initially wrong, which piece of material changed their judgment, and what they're still unsure about. Only include what the current essay genuinely has — don't pad to a full set. In fiction, credibility comes from how the character knows, misunderstands, and discovers — not from fabricating real-world sources.

## Absolutely forbidden in finished prose

The following cover titles, subheadings, body text, image captions, and quoted paraphrases. A single hit means the piece is not ready to deliver.

Understand one thing first. These ban rhetorical actions, not specific words. Swapping the exact phrasing of a banned pattern while keeping the same action still counts as a hit.

- No contrarian-pivot rhetoric. This means: setting up a misconception the reader doesn't actually have, then knocking it down to raise the stakes for what follows. The family includes: "It's not X, it's Y" / "Not X — but rather Y" / "It's not about X — it's about Y" / "Rather than X, it's actually Y" / "On the surface X, in reality Y" / "It seems X, but actually Y" / "You think X — but in reality Y" / "Only later did I realize" / "The truth is the opposite" / "X doesn't matter — what matters is Y." This list is illustrative, not exhaustive; the same action in any wording is still banned. Deliver judgments from the front: judgment first, then evidence. A self-correction is only allowed when the essay has genuinely walked the material from mistake to correction, and it must not use any of the fixed patterns above.
- No three or more parallel structures of identical form. "Why you started, why you gave up, what you loved, what you feared" — that kind of整齐 restraint suit has a two-item limit; the third must be restructured or deleted.
- No pairing abstract nouns with concrete verbs to produce lyric writing. Time doesn't "store details," anxiety doesn't "take shape," the years don't "smooth away" anything. This is fine when the essay is actually about these concrete things.
- Don't turn verbs into nouns. "Optimized the process" becomes "made the process smoother." "Achieved an improvement in efficiency" becomes "cut X minutes" or "freed up Y people."
- No em-dashes `—`, double em-dashes `——`, or en-dashes used as connectors `–`.
- Colons `：` and `:` have one allowed use: introducing a direct quote. "To sum up:" / "The core point:" — these signaling colons are banned. URLs, code, and machine fields are exempt.
- Don't use "in plain terms," "the bottom line," "here's the conclusion up front."
- Don't use "what's more subtle is," "there's another layer," "only half right," "notably," "it should be pointed out," "in a sense" as insight-signposts at the start of paragraphs or sentences. This is fine when the text is literally talking about levels, quantities, etc.
- Don't elevate ordinary things with corporate-report or model-stock jargon. `references/reality.md` distinguishes absolute bans from context-dependent words; checker scripts may not add unlisted hard bans on their own.
- Non-fiction must not use metaphorical wrappers like "repository," "drawer," "temperature," "death," "collapse," "wave," "key," "foundation" to package abstract concepts. This is fine when the essay is actually about these physical things.
- When a direct quote hits these bans, paraphrase or omit it — don't preserve it with quotation marks.

"Not only… but also…" is normal English amplification and is allowed. When it appears in a contrarian-pivot position to raise stakes for what follows, treat it as contrarian rhetoric.

Run these checks after the first draft is finished. When fixing a banned pattern, first find the fact it was trying to express, then say it in a plain sentence. Don't search for another fancy pattern as a replacement.

Long-form pieces can be saved as Markdown or text and run through `scripts/check_prose.py <path-to-piece>`. If the script fails, keep revising until the hard-ban count is zero.

## Delivery

If the user only wants the piece, deliver only the piece. Don't display internal outlines, rule checks, or the creative process. The source-tracing required by `references/reality.md` at the top of the piece is part of the body text, not the creative process.

Sources follow one rule: for fact-driven pieces written entirely from public sources, list the small number of sources that matter to the conclusion at the end of the piece. Personal experience and opinion pieces do not include a source list. Follow the user's instructions when they differ. Don't stuff research notes into the body text.

Serve only the current piece. Don't build a long-term author profile, don't generate a personal rule library, don't create a new personal writing skill.
