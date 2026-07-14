# Session — Night new adult title: concepts + strongest as complete novella

> **Status:** `in-progress`

- **📊 Model:** fable-5 · BOOKS-lane night session · night run 2026-07-14
- **session:** Generative rung of ORDER 008 item 1 / ORDER 011 item 2: new adult title concepts + strongest written as complete novella.
- **applied:** `candidates/adult-novels/the-sweetwater-sea/{en/the-sweetwater-sea.md,DECISIONS.md}` + `docs/ideas/2026-07-14-adult-title-concepts.md` (+ README backlog link) + this card + claim
- **verify:** `python3 bootstrap.py check --strict`
- **started:** 2026-07-14T01:34Z
- **closed:** (in progress)

## ⟲ Previous-session review
previous-session review: `.sessions/2026-07-14-night-nl-packets.md` (the
latest prior card; ORDER 011 items 2/4/7 follow-through, PR #180, merged
as `a3cf20a`). Inherited state at this slice's start HEAD `d93aee5`
(PR #181, the night-close heartbeat that followed it): that batch had
cleared the four owed NL vetting packets + 28 keyword-map C4 rows +
night-kiln packet un-stale + the ONE owner-queue regen (19 decisions /
37 sequences / 213 clicks, 11 hard-gated), leaving `control/claims/` at
README-only — claim scan clean for this slice, no open PR touching a new
adult-title directory, adult catalog at 10 titles / 12 complete EN
manuscripts (current-state.md @ HEAD). ONE executable craft rule
transferred from it: **counts are re-measured from the file at hand,
never copied forward** (its four NL packets each re-ran `wc -w` against
the merged manuscripts instead of trusting NOTES.md). Executed here
verbatim: the 15,243 on this card, in DECISIONS.md, and in the PR body is
a direct `wc -w` of the committed manuscript, quoted with its path, taken
after the final content commit — alongside the inherited
weigh-house → salvage-orchard drafting shape, executed as committed
3-chapter chunks: `a1d6aba` (front matter + ch. 1–3), `5271759`
(ch. 4–6), `d40bc91` (ch. 7–9), `4308f8d` (ch. 10–12 + DECISIONS.md).
Honest nit: its 💡 (batch the four EN concept-packet graduations) repeats
the exact discoverability debt it quoted from v020-probe's nit — the owed
graduation batch exists only as card prose, with no claimable artifact a
follow-up session would trip over; the shortlist doc this session lands
is partly a hedge against the same rot in the BOOKS ideation lane.

## 💡 Session idea
Run the generative rung of ORDER 008 item 1 / ORDER 011 item 2: generate
NEW adult book title concepts (house lane: literary historical fiction
novellas, Dutch settings, English language, band 15,000–16,000 words),
collision-scan titles against the full existing catalog, shortlist them in
an ideation doc, then write the STRONGEST concept as a complete novella
under `candidates/adult-novels/<new-title>/en/` with its DECISIONS.md. All
publishing stays ⚑ owner-gated; nothing under `docs/publishing/` is
modified by this slice (packet graduation is a follow-up slice per house
convention). One READY PR (#182) left to the enabler. This card is
born-red and holds substrate-gate red by design until the completion flip.

## 💡 Idea (deduped vs sibling cards)
💡 **Cohort idea docs need per-concept outcome rows — the file-level
frontmatter can't score a split cohort.** `docs/ideas/README.md`'s
outcome-record frontmatter (state/shipped_pr/outcome) is file-level, but
tonight's batch splits immediately: concept 1 (The Sweetwater Sea) is
WRITTEN on PR #182 while concepts 2–5 stay open in the same file — so the
honest file-level value is `outcome: open`, which under-reports the
shipped concept, and flipping it to `shipped` when #182 merges would
over-report the four unwritten ones. The "ideas that ship and survive"
sweep the README promises cannot score this file either way. Cheap fix,
two parts: (1) cohort docs carry a per-concept outcome table (concept ·
state · shipped_pr · outcome) that a sweep reads row-wise, with the
file-level block reserved for single-idea files; (2) at the moment a
concept graduates to a write-slice, its row updates in the same PR that
lands the manuscript — the row edit rides the merge, so the record can't
rot. Deduped against tonight's siblings and the 2026-07-13 line:
night-nl-packets' 💡 batches the four EN packet GRADUATIONS (execution of
known debt, publishing surface); night-v020-probe's 💡 fixes the
HARD-GATED annotation rendering in `derive_owner_queue.py` (queue output
accuracy); salvage-orchard's 💡 is the cross-book register-stem checker;
marmalade's is the works-index checker — none touches the idea-cohort
outcome record or how `docs/ideas/` frontmatter scores partially-shipped
batches.

## Outcome
- Complete manuscript delivered:
  `candidates/adult-novels/the-sweetwater-sea/en/the-sweetwater-sea.md` —
  12 chapters, full arc, 1927–1932 Wieringen/Afsluitdijk premise per the
  brief. Honest count, verbatim: `wc -w` = **15243** (includes front
  matter and chapter headings) — inside the 15,000–16,000 band, low end.
- Historical spine ledgered:
  `candidates/adult-novels/the-sweetwater-sea/DECISIONS.md` carries the
  verified-vs-invented ledger (verified spine: Zuiderzeewet 1918,
  steunwet 1925, De Vlieter closed 28 May 1932 13:02, IJsselmeer renaming,
  keileem/zinkstukken technique; marked inventions: all named characters,
  the WR 43, the curing procedure as period-flavoured reconstruction).
- Concept shortlist landed: `docs/ideas/2026-07-14-adult-title-concepts.md`
  (badge `ideas`, linked from the `docs/ideas/README.md` backlog) — 5
  concepts scored /30: The Sweetwater Sea 28 (WRITTEN), The Wire Garden
  26, The Salt Bell 24, The Lamp Room 24, The Eleven Cities 23; concepts
  2–5 are the next write-session's menu.
- ⚑ `docs/publishing/**` untouched: the vetting packet for The Sweetwater
  Sea (collision re-scan, keyword rows, §7 owner clicks) is the recorded
  follow-up slice; no publish, spend, or external action by this session.
- No repo-level `docs/decisions.md` entry: standalone title, no series
  started — the per-title DECISIONS.md is the whole decision record.
- Claim `control/claims/night-new-title.md` deleted in this flip commit
  per the claims README.

## Work log
- 2026-07-14T01:34Z — Branch `claude/night-new-title` from origin/main
  (`d93aee5`). Claims scan clean (README only). Born-red card + claim file
  committed as the first commit (`e308cb8` at 01:35:06Z) and pushed; READY
  PR #182 opened; enabler bot armed squash auto-merge (left in place,
  untouched by this seat).
- 2026-07-14T01:49Z–02:02Z — Manuscript committed in 3-chapter chunks per
  house drafting convention: `a1d6aba` (01:49:29Z, front matter +
  ch. 1–3), `5271759` (01:52:35Z, ch. 4–6), `d40bc91` (01:55:22Z,
  ch. 7–9), `4308f8d` (02:02:33Z, ch. 10–12 + DECISIONS.md). Honest
  post-final-commit count: `wc -w` = 15243.
- 2026-07-14T02:12Z — Shortlist doc
  `docs/ideas/2026-07-14-adult-title-concepts.md` written (badge `ideas`,
  frontmatter per the ideas README, reachability link added to the README
  backlog); card previous-session review / idea / outcome sections
  completed; ONE night-progress heartbeat line appended to
  `control/status.md`; committed together and pushed.
- 2026-07-14T02:12Z — `python3 bootstrap.py check --strict` run: expected
  result is green except this card's own by-design born-red hold
  (in-progress badge + open claim), which is the flip's job.
- 2026-07-14T02:15Z — Flip commit: Status badge → `complete`, `closed:`
  timestamp set, `control/claims/night-new-title.md` deleted, same
  commit. `python3 bootstrap.py check --strict` fully green at flip;
  pushed. PR #182 left to the enabler's armed squash auto-merge.
