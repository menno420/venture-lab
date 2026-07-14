# Session — Night close-out slice: The Wire Garden vetting packet + keyword rows + queue regen + heartbeat

> **Status:** `complete`

- **📊 Model:** fable-5 · BOOKS-lane night close-out slice · night run 2026-07-14
- **started (date -u):** Tue Jul 14 03:56:13 UTC 2026
- **closed (date -u):** Tue Jul 14 04:03:32 UTC 2026
- **branch:** `claude/night-wire-garden-packet` — READY PR #188
- **session:** The recorded follow-up slice owed by PR #187 (The Wire Garden
  manuscript, merged `a9e202d`; its DECISIONS.md and the 03:43:50Z heartbeat
  line both record "vetting packet queued as follow-up slice"). Scope, per
  the #166 remedy class and the sweetwater-sea precedent (PR #184): the
  manuscript-first vetting packet `docs/publishing/vetting/the-wire-garden.md`
  (collision re-scan honoring the DECISIONS.md findings — exact-title
  collision with the 2025 Marcum thriller, subtitle *A novella of the
  Dodendraad* MANDATORY; NL pre-name *De draadtuin* recorded), keyword-map
  rows (full-map V057 first-claim-wins scan FIRST), ONE
  `derive_owner_queue.py` regen + counts-sync to `docs/current-state.md` +
  `docs/NEXT-SESSION.md`, and the night close-out heartbeat (re-stamp the
  stale `updated:` line + ONE final night-summary line).
- **walls:** no edits to the manuscript, `control/inbox.md`, workflows, or
  triggers; no publish, spend, or external action — every publish click
  stays ⚑ owner-gated in the packet's §7. This card was born-red and held
  substrate-gate red by design until this completion flip.
- **verify:** `python3 bootstrap.py check --strict`

## Results (as landed)

- **Vetting packet** `docs/publishing/vetting/the-wire-garden.md`
  (7-section sweetwater-sea manuscript-first form; §7 `OWNER-GATE` heading
  parseable, gate rows as ⚑ Owner checkboxes, NO inline ⚑ in numbered
  steps; all 6 owner clicks queued, none performed): 15,900w re-measured
  verbatim from the committed manuscript; §2 collision re-scan (two web
  queries, accessed 2026-07-14) CONFIRMS the DECISIONS.md finding — *The
  Wire Garden* (Casimir Voss Book 3), W. D. Marcum, 2025-11 espionage/AI
  technothriller, live on Amazon in Kindle + 2 print editions —
  genre-disjoint, series-branded on the other side; the DECISIONS-preserved
  retitle option is DECLINED and the subtitle *"A novella of the
  Dodendraad"* made MANDATORY in every listing context; the register
  itself is empty (no Dodendraad fiction in English surfaced — a real §2
  finding recorded, not buried). NL pre-name *De draadtuin* (*Een novelle
  van de dodendraad*) recorded in §3 as the seat follow-up, not claimed.
  Price $4.99 on the verified $3.99–$5.99 band; KDP Select YES per the
  V049 per-title rule.
- **Keyword-map rows** (`docs/publishing/keyword-map.md`): full-map V057
  first-claim-wins scan run FIRST at proposal (stem greps) and RE-RUN at
  apply (each new phrase appears exactly once as an ownership row) — zero
  collisions, no existing claim touched. Added: 2 browse-node first-claims
  (Historical Fiction → **World War I** era sub-node — sibling of Paper
  Orange's World War II node, Ultramarine-parent sub-node precedent —
  and Genre Fiction → **Animals**), 7 EN keyword ownership rows, and C3's
  **fifth Netherlands era-register** (WWI 1915–1918 neutral-border /
  Dodendraad → The Wire Garden; the "outside all four registers" rule
  sentence advanced to five). Watched adjacencies recorded in the C2
  pattern (`Dutch` / `Netherlands` / `wartime` / `letters` stems — the
  last vs Seed Catalogue Courtship's §3 novel-in-letters reservation);
  NO widow stems drafted, deliberately (the C2 widow cluster already
  carries three titles).
- **ONE owner-queue regen** (`python3 scripts/derive_owner_queue.py`,
  exit 0): **19 decisions / 44 click-run sequences / 262 owner clicks
  (16 hard-gated), 46/46 inputs parsed clean** — from the PR #186
  baseline of 19 / 43 / 256 (16), 45/45. Manual-review empty.
- **Counts-sync** (re-derived by grep, not memory): `docs/current-state.md`
  — adult novels 11 titles/13 EN manuscripts → **12 titles/14 EN
  manuscripts** (Wire Garden PR #187, 15,900w); vetting packets 44 →
  **45** (31 book + 13 product + 1 probe); owner-queue paragraph to the
  new counts. `docs/NEXT-SESSION.md` — same corrections in its catalog
  snapshot + owner-queue paragraph.
- **Heartbeat close-out** (`control/status.md`): the stale `updated:`
  line re-stamped **2026-07-14T04:01:48Z** from `date -u` (tonight's
  earlier sessions appended progress lines without re-stamping it), plus
  ONE final night-summary line — continuation wave complete: product #10
  + 2 new EN novellas (Sweetwater Sea, Wire Garden) + 7 NL editions
  (catalog 13/13) + 8 large-print specs + verdicts applied + V020 probe;
  trading round 6 + retrospective + 2 infra improvements; all lists done,
  no remainder. No other status lines rewritten; `control/inbox.md`
  untouched.
- READY PR #188 (never draft) left to the enabler's auto-merge; this seat
  armed nothing and merged nothing.

## ⟲ Previous-session review

previous-session review: `.sessions/2026-07-14-night-wire-garden.md` (the
manuscript slice this session closes out — PR #187, two-writer split).
What held up: its DECISIONS.md wrote the packet's §2 for it — the
write-time collision honesty (superseding the shortlist's stale "clean"
scan with the Marcum ASIN, subtitle verdict, and an explicit "retitle
option preserved for the vetting packet, where the collision must be
re-scanned and decided" contract) meant this slice started from a
recorded finding and a named decision point instead of a surprise; the
re-scan confirmed it unchanged, and the NL pre-name (*De draadtuin*)
carried forward for free, exactly as the pre-naming convention intends.
Honest nit, same class the nl-completion review already called: the card
records "vetting packet = recorded follow-up slice" in four places
(card, DECISIONS, shortlist, heartbeat) but names no durable owed-list
location and no owner of the debt — this slice existed only because the
coordinator assignment carried it; a title whose night ends one slice
earlier would have shipped with the debt recorded but unscheduled.

## 💡 Session idea

💡 **Teach `check_ledger_drift.py` to nag on owner-queue counts drift.**
This slice's cheapest-to-botch step was the counts-sync: the derived
counts (19/44/262, 16 hard-gated, 46/46) are hand-copied into THREE prose
sites — `docs/current-state.md`, `docs/NEXT-SESSION.md`, and the
heartbeat line — and nothing but session discipline (the #166 remedy
class) catches a missed site; tonight's stale "4 adult NL editions" line
and the un-restamped `updated:` line show exactly how prose copies rot.
Guard recipe: extend `scripts/check_ledger_drift.py` (advisory, exits 0)
to re-derive the counts the same way `derive_owner_queue.py`'s `run()`
computes them (import it — the kill-clock checker already imports the
parser, no forked grammar) and grep the `N decisions … N … sequences …
N … clicks` prose spans in `docs/current-state.md` +
`docs/NEXT-SESSION.md`, nagging on mismatch; test target alongside the
existing ledger-drift tests. Deduped against the prior 💡 set: NL
pre-naming at EN write time (nl-completion — executed by #187, distinct);
series-canonical NL glossary file (nl-final — glossary, not counts);
batched owed follow-throughs (night-book-variants — process, not a
checker); per-concept outcome rows (night-new-title); HARD-GATED
annotation rendering (night-v020-probe — queue OUTPUT formatting, not
counts-prose drift); hoisted shared clicks (nl-editions-vetting). No
prior card proposes mechanizing the counts-sync check.

## Work log

- 2026-07-14T03:56:13Z — Branch `claude/night-wire-garden-packet` from
  origin/main (`a9e202d`). Inbox re-read at HEAD: no conflicting ORDER
  (ORDER 011 item 7 mandates this regen class). Claims dir README-only.
  Born-red card + claim committed first (`5a944f0`) and pushed.
- 2026-07-14T03:57Z–04:00Z — §2 collision re-scan (2 web queries): Marcum
  thriller confirmed live (Kindle + 2 print editions); no EN Dodendraad
  fiction anywhere. V057 full-map stem scan at proposal: clean. Packet
  written on the sweetwater-sea form; keyword-map rows + C3 fifth
  register added; scan re-run at apply: each phrase owned exactly once.
- 2026-07-14T04:01Z — ONE `derive_owner_queue.py` regen (exit 0, counts
  above); counts-sync to current-state + NEXT-SESSION; heartbeat
  re-stamped 2026-07-14T04:01:48Z + night-summary line appended.
- 2026-07-14T04:02Z — Pre-flip `python3 bootstrap.py check --strict`:
  ONLY the designed born-red hold findings. Work committed (`cc75401`
  packet+map, `64ab0e6` regen+counts, `44d07a5` heartbeat), pushed;
  READY PR #188 opened, left to the enabler.
- 2026-07-14T04:03:32Z — Flip commit: Status → `complete`, ender sections
  written, claim `control/claims/night-wire-garden-packet.md` deleted in
  this same commit; strict re-run green before push.
