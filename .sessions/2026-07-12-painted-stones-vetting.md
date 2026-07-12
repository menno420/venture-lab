# Session — The Painted Stones vetting packet (Tier-1 title #2 → reclassified kids, parks at illustration gate)

> **Status:** `in-progress`

- **📊 Model:** fable-5 · painted-stones-vetting
- **session:** advance the book-catalog second revenue line by ONE non-gated
  increment: run the one-pass title-vetting checklist
  (`docs/publishing/CHECKLIST.md`, PR #90) top-to-bottom for **The Painted
  Stones** — the publishing plan's Tier-1 title #2 (PR #87, §2) — producing
  `docs/publishing/vetting/the-painted-stones.md`. Headline finding: the
  plan misclassified this title as an adult cover-only standalone; the
  manuscript is a 13-spread kids picture book, so the packet works the
  checklist's KIDS path and parks at the §5 illustration owner-gate.
  Nothing is published; no account, spend, or click is performed.
- **started (date -u):** Sun Jul 12 21:54:26 UTC 2026

## Scope

- `docs/publishing/vetting/the-painted-stones.md` — new worked vetting
  packet (second per-title instance of the checklist template).
- `docs/publishing/README.md` — index row so the packet is reachable.
- `control/claims/2026-07-12-painted-stones-vetting.md` — claim (born-red
  first commit, deleted at close per `control/claims/README.md`).
- This card (born-red first commit; flipped `complete` last commit).
- Does NOT touch `control/inbox.md`, `control/status.md`,
  `control/outbox.md`, `PUBLISHING-PLAN.md`, or any trigger. No
  publish/spend/account action — the illustration money-decision and all
  §7 clicks stay queued owner blocks.

## Work log

- Synced `main` fresh; HEAD `c1214b8` == `git ls-remote origin main`.
- Grounding reads: `docs/publishing/PUBLISHING-PLAN.md` (PR #87),
  `docs/publishing/CHECKLIST.md` (PR #90), exemplar packet
  `docs/publishing/vetting/the-slow-word.md` (PR #91),
  `candidates/childrens-books/painted-stones/` (all 3 language files +
  DECISIONS.md).
- **Reclassification verified mechanically:** `candidates/adult-novels/`
  holds only README + the-slow-word + the-weigh-house + ultramarine — no
  adult "Painted Stones" exists; the actual manuscript is the kids picture
  book (13 spreads, ages 4–8).
- Word counts measured (`wc -w`, frontmatter/spread-markers/illustration
  notes stripped): EN 565 (file self-reports 556), NL 570, DE 552 — all in
  the picture-book fiction band (~500–800), category-correct as kids.
- Fresh web + storefront-style collision re-check (2026-07-12): exact title
  open (agrees with plan §7), but component words sit in a crowded
  rock-painting craft-book cluster → verdict Low; series subtitle
  "A Little Notebook Mystery" recommended as differentiator.
