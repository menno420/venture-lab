# Session — Night write-slice: The Wire Garden (concept #2), two-writer manuscript

> **Status:** `complete`

- **📊 Model:** fable-5 · BOOKS-lane night session · night run 2026-07-14
- **session:** night worker, coordinator-dispatched write-slice (concept #2 of
  the 2026-07-14 shortlist, `docs/ideas/2026-07-14-adult-title-concepts.md`):
  The Wire Garden as a complete 12-chapter novella, split across two writers
  — this seat lands front matter + chapters 1–6 + DECISIONS.md; a second
  writer lands chapters 7–12, the shortlist-doc marking, and the flip.
- **verify:** `python3 bootstrap.py check --strict`
- **started:** 2026-07-14T03:02Z
- **closed:** 2026-07-14T03:44:53Z

## ⟲ Previous-session review
previous-session review: `.sessions/2026-07-14-night-new-title.md` (the
Sweetwater card — the same generative rung, one slice earlier tonight; PR
#182). Inherited state at this seat's start HEAD
`5e35bf0eaa0d6c7239bf5cb84add109f0f1f4e46` (first writer's half): born-red
card + claim (`0e608b6`), DECISIONS.md ledger (`6e3018d`), front matter +
chapters 1–6 (`2640455`, `28ff3d8`; file `wc -w` 7994 at `28ff3d8`), READY
PR #187 with the enabler's squash auto-merge armed, strict check exit 1
with ONLY the designed born-red hold findings. ONE executable craft rule
transferred from the Sweetwater card: **counts are re-measured from the
file at hand, never copied forward.** Executed here verbatim: the
DECISIONS.md Scope/length placeholder was replaced at the flip with the
verbatim output of `wc -w` run against the committed manuscript after the
final content commit — `15900
candidates/adult-novels/the-wire-garden/en/the-wire-garden.md` — not the
first writer's running 7,994 plus this seat's chapter sums; the shortlist
Status paragraph and the status.md heartbeat carry the same re-measured
figure. Honest nit on that card: its 💡 designs the per-concept outcome
row (concept · state · shipped_pr · outcome, updated in the same PR that
lands the manuscript) — but the shortlist doc that same session landed
shipped WITHOUT the table: the one artifact the idea needed, in the one
file the session was already writing. Tonight's graduation of concept #2
therefore had no row to update and instead truth-maintained three prose
sites (intro-blockquote verdict, concept header, ranked-table Verdict
cell) — exactly the multi-site drift the proposed row was meant to
prevent.

## 💡 Session idea
Write concept #2 of the 2026-07-14 shortlist (The Wire Garden, 26/30) as a
complete 12-chapter literary-historical novella in the house band
15,000–16,000, two writers on one branch/PR: first seat front matter +
ch 1–6 + the verified-vs-invented Dodendraad ledger; second seat ch 7–12,
the honest re-measure, the shortlist-doc WRITTEN marking, ONE heartbeat,
and the flip. All publishing stays ⚑ owner-gated; nothing under
`docs/publishing/` modified (vetting packet = recorded follow-up slice).
One READY PR (#187) left to the enabler. This card was born-red and held
substrate-gate red by design until this completion flip.

## 💡 Idea (deduped vs sibling cards)
💡 **Pre-name the NL title in DECISIONS.md at write time — standing
practice for every new manuscript.** Executed this session: The Wire
Garden's DECISIONS.md carries ***De draadtuin*** (subtitle *Een novelle
van de dodendraad*), scan clean at write time — the first brand-new EN
title to land with its NL title pre-named in the same PR as the
manuscript, so the future NL slice starts from a scanned candidate.
Deduped honestly against the newest sibling cards (`ls -t .sessions/`),
and the dedupe FOUND A PRIOR: `2026-07-14-night-nl-completion.md`'s 💡 is
this same convention ("pre-name the NL title in every new EN adult title's
DECISIONS.md at write time", proposed from the NL-slice cost side earlier
tonight). This card therefore records EXECUTION, not novelty: the
convention's first from-scratch application to a new title is on PR #187,
and the standing-practice step (the convention line in the adult-novels
lane README/template) remains that sibling card's idea, still unclaimed.
The Sweetwater card's 💡 (per-concept outcome table) and
night-v020-probe's (HARD-GATED annotation rendering) are different ideas.

## Outcome
- Complete manuscript delivered:
  `candidates/adult-novels/the-wire-garden/en/the-wire-garden.md` — **The
  Wire Garden**, subtitle *A novella of the Dodendraad*, 12 chapters, full
  arc July 1915 → summer 1919, Castelré/Dodendraad premise per the
  shortlist. Honest count, verbatim, re-measured from the committed file at
  this flip: `wc -w` = **15900** — inside the 15,000–16,000 band, top edge.
  Two-writer split: ch 1–6 first seat (7,994 at handoff), ch 7–12 this seat
  (region counts: ch7 1425 · ch8 1362 · ch9 1248 · ch10 1410 · ch11 1241 ·
  ch12 1276).
- Historical spine ledgered:
  `candidates/adult-novels/the-wire-garden/DECISIONS.md` — verified
  Dodendraad spine (construction/voltage/structure/schakelhuizen, disputed
  length kept as "some three hundred kilometres", contested death toll
  never totaled in prose — the village counts only its own, requisition
  decrees at documented classes, Achelse Kluis billing, armistice teardown)
  vs marked inventions (all named characters; the beekeeping-at-the-wire
  premise wholly invented; no honey-requisition order claimed anywhere).
- Title collision recorded honestly: exact-title collision surfaced at
  write time (*The Wire Garden*, W. D. Marcum, 2025 espionage thriller,
  live on Amazon) — genre-disjoint, subtitle mandatory, retitle option
  preserved for the vetting packet. NL title pre-named: *De draadtuin*
  (*Een novelle van de dodendraad*), scan clean.
- Shortlist doc `docs/ideas/2026-07-14-adult-title-concepts.md` marked:
  concept 2 **WRITTEN this session** (Status paragraph + honest
  collision-scan correction), ranked-table Verdict → WRITTEN (PR #187),
  intro verdict **2 WRITTEN · 3 unwritten**, next-slice pointer → #3 The
  Salt Bell (24/30).
- ⚑ `docs/publishing/**` untouched: the vetting packet (collision re-scan,
  keyword rows, §7 owner clicks) is the recorded follow-up slice; no
  publish, spend, or external action by this session.
- ONE night-progress heartbeat line appended to `control/status.md`
  (2026-07-14T03:43:50Z).
- Claim `control/claims/night-wire-garden.md` deleted in this flip commit
  per the claims README.

## Work log
- 2026-07-14T03:02Z — Branch `claude/night-wire-garden` from origin/main
  (`0375099`). Claims scan clean (`control/claims/` README-only); no
  `candidates/adult-novels/the-wire-garden` at HEAD; no open PR touching it.
  Born-red card + claim committed as the first commit (`0e608b6` at
  03:02Z) and pushed; READY PR #187 opened immediately; PR activity
  subscribed. Auto-merge left to the enabler workflow, untouched by this
  seat.
- 2026-07-14T03:03Z — `candidates/adult-novels/the-wire-garden/DECISIONS.md`
  committed (`6e3018d`): verified-vs-invented Dodendraad ledger, the
  disputed-length and contested-death-toll handling, the title-collision
  finding (W. D. Marcum 2025 thriller; subtitle mandatory), the *De
  draadtuin* NL pre-naming.
- 2026-07-14T03:12Z–03:18Z — Manuscript first half committed in 3-chapter
  chunks per house drafting convention: `2640455` (03:12Z, front matter +
  ch. 1–3), `28ff3d8` (03:18Z, ch. 4–6). Per-chapter `wc`-region counts at
  `28ff3d8`: ch1 1449 · ch2 1364 · ch3 1353 · ch4 1208 · ch5 1167 ·
  ch6 1378; file total (front matter included) `wc -w` = 7994 — inside the
  first-half band 7,600–8,000. Handoff state for the second writer: ch 7–12
  per the outline, honest re-measure at the flip.
- 2026-07-14T03:42:11Z–03:42:29Z — Second seat: manuscript second half
  committed in 3-chapter chunks per house drafting convention: `c2eee79`
  (03:42:11Z, ch 7–9), `feedde6` (03:42:29Z, ch 10–12 + THE END). Honest
  post-final-content-commit count, re-measured from the committed file:
  `wc -w` = 15900.
- 2026-07-14T03:43:50Z — DECISIONS.md Scope/length placeholder replaced
  with the verbatim re-measured count; shortlist doc marked (concept 2
  WRITTEN, verdict 2 WRITTEN · 3 unwritten, next-slice → The Salt Bell);
  ONE heartbeat line appended to `control/status.md`; committed together
  (`20e7547`) and pushed.
- 2026-07-14T03:44Z — Pre-flip `python3 bootstrap.py check --strict` on
  `20e7547`: the ONLY findings were this card's own by-design born-red
  hold (in-progress badge + missing flip sections + open claim) —
  everything else green.
- 2026-07-14T03:44:53Z — Flip commit: Status badge → `complete`, `closed:`
  set, ⟲ previous-session review + 💡 sections added, Outcome finalized,
  `control/claims/night-wire-garden.md` deleted, same commit.
  `python3 bootstrap.py check --strict` fully green at flip; pushed. PR
  #187 left to the enabler's armed squash auto-merge.
