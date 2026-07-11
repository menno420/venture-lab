# Chapter 3 — Born-Red Session Cards: Open Every Unit of Work in the Red

An agent that reports its own completion is a witness testifying on its own behalf. Chapter 2 showed how a green check can lie about what it ran. This chapter is about the same problem one level up: how a *session* can claim to be finished before it is, and the small mechanical discipline that prevents it.

## The loophole

In a sibling lab, a pull request that contained only a session card — no product change, just the record of a unit of work — merged twenty-four seconds after it opened. This is documented as the superbot-games `#40` case, and it is the archetype the born-red rule exists to close. The card declared itself complete, the pull request had auto-merge pre-armed, and the instant CI reported green, it landed. Nobody reviewed it. The "work" was a card asserting work.

The general shape: if the artifact that certifies a unit of work as done is written by the same process that did the work, and merging is automatic on green, then a card that simply *says* "complete" merges itself. The certification and the thing certified are the same object.

## The discipline: born red

Every unit of work opens a **session card** — a markdown file under `.sessions/` — and that card is **born red**: its very first committed state carries `> **Status:** \`in-progress\``. The card is committed *alone*, as the first commit on the branch, before any product code. It flips to `> **Status:** \`complete\`` only as the deliberate last step, once the close-out is actually written.

While the card is red, the merge is **held**. This lane's gate logic (in `bootstrap.py`) treats a pull request that *adds* a session card declaring an in-progress status as a designed hold: the merge stays red until the card flips complete. The gate calls this the born-red HOLD, and its own comment names the failure it prevents — the superbot-games `#40` twenty-four-second merge. Crucially, the hold is a single designed-state finding, not a completeness grade: a mid-flight card is not nagged for missing close-out prose; it is simply held until it declares itself done.

The status *value* is what the gate reads, not merely the badge's presence. An earlier version of the check confirmed only that a `Status:` badge existed, and a card that kept `complete` from a previous session slipped through. The fix (recorded in the gate's own KL-1 comment) was to check the value against a set of in-progress tokens — `in-progress`, `wip`, `hold`, `drafted` — any of which holds the gate.

## The four required markers

For a card to count as a finished close-out, it must carry four markers, each in an exact byte-form the gate scans for:

- **`**Status:**`** — the machine-readable badge, a blockquote line with a backticked lowercase-hyphen value.
- **`📊 Model:`** — the family-level model name the session's own harness reports (e.g. `opus-4.8`, `fable-5`), never a dated ID. The committed card is the attribution ground truth.
- **the exact string "Previous-session review"** — forcing each session to look back at what landed before it, so state is not re-derived from pull-request archaeology.
- **`💡`** — the session idea, the two-to-four lines that say why this work exists.

A card also fails the check if it still carries unresolved `[[fill:]]` slots outside code fences — the markers of an auto-drafted skeleton nobody finished. (The gate strips inline code and fenced blocks before counting, so a card that legitimately *mentions* the token in backticks is not tripped — a subtlety that matters when, as here, a book about the mechanism ships a template that shows it.)

## Why this works

Born-red inverts the default. The default is optimistic: work is assumed done unless something flags it. Born-red is pessimistic: work is assumed *unfinished* — the merge is held red — until the session takes a deliberate, separate, last action to declare completion. You cannot merge a unit of work by forgetting to mark it incomplete, because it started incomplete and stays that way until you say otherwise. The twenty-four-second self-merge becomes impossible: the card is red at open, and flipping it green is a commit a human or a properly-authorized seat can see.

## The rule you take away

Make the record of work born red and separate from the work. Commit the in-progress card first, alone. Hold the merge while it is red. Flip it to complete only as the last deliberate step, and require the specific markers that prove a real close-out was written — not an empty skeleton. The cost is one extra commit per unit of work. The thing it buys is that no unit of work can ever certify itself done by default.
