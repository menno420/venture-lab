# Session — ORDER 011 item 4: apply sim verdicts V053/V057/V049

> **Status:** `complete`

- **📊 Model:** fable-5 · worker slice · ORDER 011 item 4 (sim-verdict application, night run)
- **session:** Consume the three newly-served sim-lab verdicts relayed by ORDER 011 item 4 (`control/inbox.md` @ `c3cb320`; source sim-lab `control/outbox.md` @ `32ff5c3`, fetched and read IN FULL — VERDICT 053 approve · VERDICT 057 approve · VERDICT 049 reject; verdict texts canonical over the order's one-line summaries) and apply each ruling minimally: V053 → both 2026-07-13 ideation batch docs' Kill-Rule-2 channel-risk notes; V057 → `docs/publishing/keyword-map.md` first-claim-wins convention header; V049 → `docs/publishing/PUBLISHING-PLAN.md` §4 KDP Select rows (rejection recorded per the pre-registered REJECT consequence, proposal text kept verbatim). No publish click unlocked; owner gates untouched; no §7 OWNER-GATE block or packet row changed → no OWNER-QUEUE regen (checked, not assumed).
- **started (date -u):** Mon Jul 13 23:17:08 UTC 2026
- **closed (date -u):** Mon Jul 13 23:32 UTC 2026

## ⟲ Previous-session review

Previous session (`.sessions/2026-07-13-night-product-slice.md`, ORDER 011
item 1, PR #169): two of its choices paid off directly here — (1) its
heartbeat ack line settled the "ack in your inbox thread" ambiguity with a
recorded rationale (lane-never-edits-inbox + CI append-only gate override
the order's phrasing), so this slice added its item-4 line under the same
Night-progress heading instead of re-deriving the convention; (2) its fresh
night batch's sole BUILD already stepped off the incumbent agent-ops
funnel, which meant V053's reserve-one-untested-channel consequence landed
as a compliance citation, not a retrofit. Honest nit: its heartbeat closed
with "ORDER 011 items 2–6 not started by this slice" while item 6 had
already landed (PR #171 merged before this slice began) — per-item
progress lines age fast on a multi-session night; stating only what the
slice itself did (and dating it) would avoid the drift.

## 💡 Session idea

**A consumed-verdicts ledger with staleness triggers.** Sim verdicts now
land in venture-lab as prose annotations scattered across surfaces (V037–
V041 in four vetting packets, V049 in PUBLISHING-PLAN §4, V053 across two
batch docs, V057 in the keyword-map header) and several carry LIVE
staleness conditions — V053 stales at the first incumbent organic sale;
V057 stales if the map's 14 × (2 + 7) claim shape restructures; V037/V040
park price arms behind named measurement bars. Nothing enumerates
"which verdicts has this seat consumed, where did each land, and what
event invalidates it." One table (e.g. `docs/publishing/verdicts-ledger.md`:
verdict id · ruling · applied-to files · application guard · staleness
trigger) would let the SWTK T+7 checkpoint session (2026-07-19) answer
"which applied convictions stale if one unit sold?" by grep instead of
re-reading every annotated doc — and an advisory checker à la
`check_kill_clocks.py` could nag when a recorded trigger event is on file.
Deduped against `.sessions/`: order-010-verdicts proposed a `PARKED-BAR:`
token for parked PRICE arms specifically; night-queue-killcheck proposed
the ⏲ DUE checker for kill clocks; no existing card proposes indexing
consumed verdicts or their staleness conditions.

## Scope (as landed)

- Read all three verdicts IN FULL at source (sim-lab `32ff5c3`
  `control/outbox.md` L859/L939/L1019; saved to scratchpad; fetch clean).
- V053 (approve): `docs/products/ideas-2026-07-13.md` Kill-Rule-2 note —
  measured 9-of-9-cell citation + reserve-≥1-untested-channel backstop +
  0-organic-sales application guard + independence boundary;
  `docs/products/ideas-2026-07-13-night.md` — compliance citation (its
  sole BUILD already sits on an untested channel).
- V057 (approve): `docs/publishing/keyword-map.md` — header gains the
  measured 12-cell basis (tiling buys 6.5%–144.7% at every nonzero γ);
  KEEP BOTH stays the argued exception; γ = 0 boundary + 14 × (2 + 7)
  application guard; first-claim bullet cites the ratification.
- V049 (reject): `docs/publishing/PUBLISHING-PLAN.md` §4 — blanket
  "KDP Select: **Yes**" STRUCK as a recommendation posture; enrollment is
  a per-title OWNER decision gated on the committed b* crossover table;
  90-day one-title live probe named; V037–V041 rows inherit the per-title
  gate; field-6 proposal text kept verbatim (fork not re-opened).
- Heartbeat line appended under `control/status.md` Night-progress; inbox
  untouched (append-only gate; convention per the item-1 ack rationale).
- Decide-and-flag: V049's venture-lab landing surface chosen as
  PUBLISHING-PLAN §4 only (the verdict's own `target:` names it first);
  the 14 vetting packets' §7 "KDP Select" rows were NOT mass-edited —
  they inherit the per-title gate by the §4 note's clause (5), keeping
  the diff minimal and the owner queue regen-free.
