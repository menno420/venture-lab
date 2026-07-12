# 2026-07-12 — Keyword/category allocation map (catalog-level, PR #94 card idea)

> **Status:** complete

## 💡 Session idea
💡 **Quarterly keyword SERP snapshot.** The allocation map records who owns
each phrase but says nothing about whether the phrase still WORKS: once a
quarter, for each owned keyword, record the top-10 Amazon search results
(title/author/format, one line each) in a dated snapshot next to the map.
Diffing snapshots detects niche crowding (a phrase suddenly dominated by new
entrants) and decay (results drifting off-intent) — turning the map from a
one-time allocation ledger into ongoing monitoring, and giving the "watched
adjacency" rows (C2) their actual watching mechanism.

## Previous-session review
previous-session review: `.sessions/2026-07-12-ultramarine-vetting.md`
(PR #98) — genuine strength: it worked the title-fix instead of just
flagging it — three rename candidates each given their own collision
search, with a dated, named rejection (*The Blue Hour*, Paula Hawkins 2024)
that saves the owner from re-deriving the search; one honest nit: its §6
keyword `widow grief literary fiction` was drafted with no glance at the
already-shipped Weigh House keyword set (`widow investigates husband's
death`), which is exactly the isolation failure mode this slice's map now
closes.

## Model
- **📊 Model:** Claude (Fable family) · worker · venture/publishing

## Scope

One work increment: implement the 💡 idea from
`.sessions/2026-07-12-publishing-plan-retier.md` (PR #94) — a catalog-level
KDP category + keyword allocation map so the 14 titles tile the search space
instead of cannibalizing it. Deliverable: NEW `docs/publishing/keyword-map.md`
(ownership table for the four vetted packets' categories/keywords reproduced
verbatim from each packet's §6, a CONFLICTS section with proposed resolutions
— disputed reallocations ⚑ OWNER-flagged, packets NOT edited this slice — and
name-level niche reservations for the remaining unvetted titles), + an index
row in `docs/publishing/README.md`, + a one-line pointer in
`docs/publishing/CHECKLIST.md` at the categories/keywords step. No publish,
spend, account, or external action; `control/status.md`, `control/outbox.md`,
and triggers untouched.

## Outcome
Map landed at `docs/publishing/keyword-map.md` (content commit `d4d90bc`) +
index row in `docs/publishing/README.md` + one-line CHECKLIST §6 pointer;
PR #100 opened READY. 8 category rows + 28 keyword rows reproduced verbatim
from the four vetted packets' §6; conflicts worked: C1 Literary Fiction
dispute (Slow Word keeps; Ultramarine proposed swap to Women's Fiction →
Domestic Life, ⚑ OWNER — no packet edited), C2 "widow" stem kept as watched
adjacency, C3 Netherlands cluster split by genre era; name-level niche
reservations for the ten unvetted titles (Last Good Frequency barred from
Slow Word's radio/signal phrases; kids cluster tiled). Claim file deleted in
this same flip commit per `control/claims/README.md` step 4. No publish,
spend, or account action taken.
