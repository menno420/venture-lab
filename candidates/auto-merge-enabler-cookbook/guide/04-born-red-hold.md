# 4 · The born-red HOLD (make "not finished yet" a red check)

Arming auto-merge at PR open (chapters 1-2) creates a new hazard: the PR
now merges the moment it goes green — whether or not the session that
opened it is actually done. If your agents open work-in-progress PRs (and a
disciplined fleet does, committing a session journal *first* so a crashed
session still leaves evidence on the branch), you need "not finished yet"
to be a **red check**, not a convention. That is the born-red HOLD, and it
is what makes merge-on-green safe.

## The failure it prevents

Without a HOLD, the smallest possible PR is the most dangerous: a PR whose
only content is a freshly-opened, in-progress session card. Its format
checks pass, auto-merge is pre-armed, CI reports green, and nothing encodes
"in-progress means not mergeable" — so the PR merges seconds after open,
landing an unfinished session. This repo's enforcement engine carries the
incident that mandates the fix as a committed constant:

> born-red HOLD: this PR ADDS a session card that declares an
> in-progress/drafted Status — the gate holds the merge red until the
> card flips complete (designed hold, not a defect). Without this hold a
> card-only born-red PR with auto-merge pre-armed merges the instant CI
> reports.

## The discipline, mechanized

The convention: every session's **first commit** is a journal file
(`.sessions/<date>-<slug>.md`) declaring `> **Status:** `in-progress``. The
session's **last commit** flips that badge to `complete`. In between, the
required gate holds the PR red — loudly, with a designed-hold banner —
because the card it added declares itself unfinished. This cookbook itself
was built that way: its own session card was born
`in-progress` in the first commit and flipped to `complete` in the last,
and the gate held its PR red until the flip.

The gate grades an **added** card by what it *declares*:

- **No status badge at all** → grammar red (every journal carries one from
  its first commit).
- **Badge declares `in-progress` / `wip` / `hold` / `drafted`** → the
  designed HOLD. Nothing else about the card is graded — mid-flight
  incompleteness is *expected*, so the hold is one finding, not a pile of
  them. Completeness is never graded at birth.
- **Badge declares `complete`** → the card claims to be a finished
  close-out, so it gets the *full* completeness check (required markers
  present, `[[fill:]]` slots resolved). A malformed "complete" card reds
  on grammar.

## The choreography that falls out

Fully mechanical, no one watching:

```
born-red journal commit  (Status: in-progress → gate HOLDs the PR red)
   ↓  work commits
ender commit             (flip Status: complete)
   ↓  same push re-runs the gate → green
pre-armed auto-merge lands the PR
```

Merge order equals work order. The enabler armed the PR at open (chapter
2); the gate kept it red through the whole session; the completion flip
turns the required check green; the pre-armed auto-merge fires. Two
hard-won subtleties from this repo's engine history are worth stealing:

1. **Check the status VALUE, not the badge's presence.** A card that kept
   completion markers from a previous PR read as green under a
   presence-only check and merged without its close-out. Grade the
   backticked *value*, not just that a badge exists.
2. **Deletions and modified siblings are graded too.** A PR that *deletes*
   a session card is a hard red (session memory is append-only). A PR that
   only *modifies* a card (every close-out flips one) keeps the full gate
   on each modified card, so a close-out that forgot to flip `complete`
   still reds. An added card can only ADD red to a sibling's verdict, never
   substitute for it.

## The recipe

`recipes/substrate-gate.yml` is the exact production gate, shipped
verbatim. Its `substrate gate (docs + session-log required)` step is the
born-red HOLD in full, with the multi-card, deletion, and modified-sibling
lanes annotated inline (this repo hardened each lane against a specific
merged-loophole incident, cited in the comments). It is a required check;
pair it with the enabler and the HOLD is what keeps "merge on green" from
meaning "merge on half-done."

**Sources** (public repo `menno420/venture-lab`):
`.github/workflows/substrate-gate.yml` @ `aa04700` (the born-red HOLD step;
added-card / modified-sibling / deletion lanes; the control fast lane;
every inline incident citation); the HOLD's live effect verified by this
cookbook's own born-red→complete card flip on its PR, and by the five
2026-07-17 merges (chapter 1) each landing only after its session card
declared `complete`.
