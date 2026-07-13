# 4 · Recipe 3: the born-red HOLD (make "not finished" a red check)

Arming auto-merge at PR open (chapter 3) creates a new hazard: the PR now
merges the moment it goes green, whether or not the session that opened it
is actually done. If your agents open work-in-progress PRs — and a
disciplined fleet does, committing a session journal *first* so a crashed
session leaves evidence — you need "not finished yet" to be a **red
check**, not a convention.

## The 24-second false-green

The source repo's enforcement engine carries the incident that mandates
this, in the docstring of the exact function that fixes it: a sibling repo
merged a PR **24 seconds after open** because the PR's only content was an
in-progress session card, the format checks passed, auto-merge was
pre-armed, and nothing encoded "in-progress means not mergeable." The
engine's hold message is a committed constant:

> born-red HOLD: this PR ADDS a session card that declares an
> in-progress/drafted Status — the gate holds the merge red until the
> card flips complete (designed hold, not a defect). Without this hold a
> card-only born-red PR with auto-merge pre-armed merges the instant CI
> reports (superbot-games #40 merged in 24 s on exactly this).

## The discipline, mechanized

The fleet's convention: every session's **first commit** is a journal file
declaring `Status: in-progress`. The required gate's added-file lane then
holds the PR red — loudly, with the designed-hold banner — until the
session's **last commit** flips the journal to `complete`. The engine
grades an added card by what it *declares*:

- **No status badge at all** → grammar red (every journal carries one from
  its first commit).
- **Badge declares in-progress / wip / hold / drafted** → the designed
  HOLD. Nothing else about the card is graded — mid-flight incompleteness
  is expected, the hold is one finding, not a pile of them.
- **Badge declares complete** → the card claims to be a finished
  close-out, so it gets the *full* completeness check (required markers
  present, no unresolved fill-slots).

Two hard-won subtleties from the engine's committed history:

1. **Check the status VALUE, not the badge's presence.** A reopened card
   that kept its completion markers from a previous PR read as green under
   a presence-only check, and auto-merge landed the PR without its
   close-out (the engine cites this as its "KL-1 lesson").
2. **Machine-drafted cards hold too.** The engine's auto-draft state
   (`drafted`, with unresolved `[[fill:]]` slots) is real write-back but
   not a finished session — it holds the gate exactly like born-red.

The merge choreography that falls out, fully mechanical: born-red journal
commit → work commits → ender commit flips the journal → same push re-runs
the gate green → the pre-armed auto-merge lands the PR. Merge order equals
work order, with no one watching.

## The recipe

`recipes/born-red-hold-gate.yml` is a self-contained bash distillation of
the added-card lane: diff out files ADDED under your journal path, read
each one's status badge line, hold red on in-progress tokens with the
designed-hold banner, pass everything else through to your real test
steps. The production version does this in a Python engine with far more
grammar; the recipe keeps the load-bearing rule — *added journal declaring
unfinished status = designed red* — in ~30 lines you can adopt today.

**Sources** (public repo `menno420/venture-lab`):
`bootstrap.py` @ `6c46941` (`BORN_RED_HOLD_MESSAGE` constant with the
superbot-games #40 24-second citation; `IN_PROGRESS_TOKENS`;
`check_added_card` declared-status lanes; KL-1 status-value lesson;
`drafted`/`[[fill:]]` hold); `.github/workflows/substrate-gate.yml` @
`4776045` (the live required gate this rides in).
