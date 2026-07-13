# 6. Session cards and the born-red gate

## The card

Every session commits one card — `.sessions/<date>-<slice>.md` — that
answers, permanently: what was this session, what did it change, on
which model, when, and what did it learn. Minimum fields:

```markdown
# Session — <one-line purpose>

> **Status:** `in-progress`   <- flipped to `complete` as the LAST act

- **📊 Model:** <family-level name> · <role> · <lane/slice>
- **session:** <scope, in one paragraph>
- **started (date -u):** <verbatim date -u output>
- **completed (date -u):** <filled at flip>
```

Field scars:

- **Identity from card #1:** the `📊 Model:` line and the time line
  exist because attribution not written at the moment of work is
  unrecoverable — proven independently by multiple lanes, and
  cross-surface model attribution measurably disagrees (the harness's
  own self-report in the commit is the only reliable source). Record
  the model **family**, not marketing guesses.
- **Timestamps from `date -u`, never the model's sense of time.**
  Commit history is the clock of record.
- Cards are one-file-per-session — like claims, structurally
  conflict-free.

## Born-red: the gate that makes lying expensive

The discipline: the card is committed with `Status: in-progress` as
the session's **first** commit (this is the heartbeat-before-work of
chapter 3, in durable form), and flipped to `complete` — with the
work log, outcomes, and close-out fields filled — as the **deliberate
last** commit. "Born red": the PR starts in a state that declares
itself unfinished.

Now wire CI to HOLD any PR whose ADDED session card still declares
`in-progress`. The properties you get:

- **An unfinished session cannot merge.** If the session dies
  mid-flight, its PR sits red with a card that says exactly how far it
  got — a successor resumes from the card, not from PR archaeology.
- **The flip is an act, not a default.** Completion is claimed by a
  deliberate final commit, in the same PR as the work it describes.
- **The close-out has teeth.** Make the gate (or a strict check) also
  reject fill-me-later placeholder tokens in completed cards — a card
  with an unfilled slot is not complete, whatever its badge says.
- Mind the pre-armed-merge loophole (a production lesson): if
  auto-merge is armed at PR-open, the hold must evaluate the ADDED
  card's status VALUE (not merely the badge's presence), or a
  card-only born-red PR merges the instant checks pass.

## Close-out ritual

The flip commit is a checklist, not a formality: work log with
executed evidence (commands, verbatim outputs, SHAs) · outcome honest
about what is NOT proven · one genuinely new idea for the backlog ·
a short review of the PREVIOUS session's card (cheap continuous
quality pressure: each session audits the last) · claim file deleted
(chapter 4) · status re-stamped (chapter 3).

**On your own unflipped card, the gate showing red is the system
working** — never "fixed" by flipping early. The one anti-pattern that
kills this whole chapter is treating the flip as boilerplate to get CI
green: flip-then-work is just a slower way of having no gate at all.

---

**Sources:** `docs/conventions.md@35e5597` (#7, #10, #11) ·
`.github/workflows/substrate-gate.yml@35e5597` (the production
born-red HOLD: added-card status-VALUE check, pre-armed-merge loophole
fix) · production events: PR #159 (squash `3b159d9`) — a session that
died mid-turn left a born-red PR; the resume session completed the
work and flipped the same card, exactly the recovery path the gate is
designed for (terminal-state amendment: PR #160, squash `765e1f8`).
