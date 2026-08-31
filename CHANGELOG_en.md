# Changelog

## 1.1.0 (2026-08-05)

One sentence summarizes the core change: bans moved up from string level to rhetorical-action level; detectors fill blind spots, reduce false positives, and add a statistics layer.

### SKILL.md

Rewrote "absolutely must not appear in finished text." The "not X but Y" sentence-pattern list was upgraded to a rhetorical-action-level definition of contrarian voice, with nine known variants listed as examples rather than boundaries, and replacement actions specified (judge from the positive side first—state the verdict, then the evidence). Genuine self-corrections earned through real material may stay, but cannot follow a canned formula. Three new action-level bans: three or more identical parallel clauses, lyrical metaphors that pair concrete verbs with abstract nouns, and nominalization. Colons reclassified: colons introducing direct quotes are allowed; suggestive colons remain banned. "Not only X but also Y" demoted from hard ban to contextual judgment. Fixed three internal conflicts: the 600-character short-answer cap for "continue asking" is now explicitly the fallback for "fewer than five pieces of material after research"; source delivery unified into one rule; research-trace disclosure clarified as not counting as revealing creative process.

### references/revision.md

Pass 5 added a "contrarian-voice variant comparison table" covering seven disguise types. Added three new checks: parallel clauses, lyrical metaphors, and nominalization. Moved the hard-ban terms "closed loop," "playbook," "imagination space," and "no loss" to contextual-judgment words. Added a model-favored lyrical-word list (settle, arrive, faint light, crease, etc.) and a bracket-highlight density check. Pass 7 clarified that big words in a user-supplied title are exempt from the big-word-at-end ban.

### references/forum-prose.md

The "let sentences breathe" section gained four quantifiable anti-model-voice fixes: sentence-length variation, halving conjunctions (with before/after examples), turning nominalizations back into verbs, and repeating where repetition is correct. Added two original demonstration passages: "judge from the positive side, do not use contrarian framing to inflate" and "long and short sentences breathe on their own."

### scripts/check_prose.py

Fixed three categories of missed detections in the contrarian-sentence regex: cross-sentence "。but rather," variant words "rather than / better to," all now flagged as failures. Added a warning layer for contrarian-voice variants (thought X actually Y, only realized later, not A but B, has nothing to do with, surface/appear to), three-or-more identical parallel clauses, nominalization patterns, model-favored lyrical words, and dense bracket highlights. Added a statistics layer: sentence-length coefficient-of-variation too low, conjunction density too high (thresholds based on the CCL 2023 human vs. machine Chinese corpus study). False-positive fixes: "not shameful" no longer triggers a hard-stop; "playbook," "imagination space," and "closed loop" moved to contextual-judgment words; colons introducing direct quotes demoted to warnings.

### New

dist/human-writing-lite.md — a distilled version under 2,000 characters for ChatGPT, Qianwen Office, WorkBuddy, and other chat or weaker-model scenarios.

## 1.0.0 (2026-08-05)

First open-source release.
