# EAP close-out walkthrough — venture-lab seat, 2026-07-14

> **Status:** `historical`
>
> ⚠️ **DEPRECATED / HISTORICAL — do not act on this file.** It is the 2026-07-14
> end-of-EAP close-out surface; its counts and owner-click totals are stale and
> its EAP timeline no longer governs (EAP goes read-only 2026-07-21; projects
> are being recreated fresh). For the current owner surface use
> [`publishing/OWNER-QUEUE.md`](publishing/OWNER-QUEUE.md) and
> [`current-state.md`](current-state.md) / [`NEXT-TASKS.md`](NEXT-TASKS.md).
>
> ORDER 014(b) deliverable (`control/inbox.md` @ `37e3c05`): the owner's
> end-of-EAP review surface for this seat. Five sections: what shipped (A),
> how to verify the current state (B), every pending owner decision and
> click (C), a 5-minute cold-start tour (D), and handoff notes (E). Written
> 2026-07-14 at HEAD `37e3c05`; counts re-verified by re-running the
> generators at that HEAD, not copied from memory. Parked, cited, not
> chased here: the 262 owner publish clicks (16 hard-gated sequences) and
> the grading pass time-gated to 2026-07-17T09:05Z.

## A. What this seat did during the EAP

Compact and PR-cited. Depth, method, walls, friction, and wishlist live in
the definitive audit — [`audits/eap-project-audit-2026-07-14.md`](audits/eap-project-audit-2026-07-14.md)
(PR #192, attribution fix PR #193) — this section does not restate it.

- **Scale (audit-measured, full population 2026-07-14):** venture-lab
  152 session cards · 224 commits · 192 PRs; sibling trading-strategy
  71 · 130 · 121. All CI red ever on both repos (182 runs) is the designed
  born-red session-card gate; no test has ever failed (audit §7).
- **Products: 1 live + 10 publish-READY + 2 hard-gated.** Stripe Webhook
  Test Kit $29 LIVE on Gumroad since 2026-07-12 (verification PR #74,
  owner buyer-path test PR #86) — the only external publish, owner-clicked.
  Publish-READY, every click queued and none performed: membership-kit $49,
  template-packs $19 PWYW, Agent Fleet Field Manual $39, kill-rule-intake
  $15, False-Green Test Trap $15, Merge-Wall Cookbook $19 (2026-07-13 night
  run, tally PR #137), GitHub Webhook Test Kit $29, Multi-Agent
  Control-Plane Pack $29 (PR #164), Owner-Click Queue Kit $19 (PR #153),
  AI Novella Production Kit $29 (PR #169). Hard-gated honest: photo packs
  (owner-held originals), Ship-It Bundle $59 (needs two live referents).
- **Books: 13 EN adult manuscripts + 13/13 NL editions.** Highlights: The
  Sweetwater Sea 15,243w (PR #182), The Wire Garden 15,900w (PR #187), the
  4-NL-edition wave PRs #183–#186, 4 more NL editions + 8 large-print
  EDITION-SPECs (PR #172 + siblings), Night Kiln Book 3 *The Harvest Rows*
  23,334w (PR #174), 27 board-book texts (tally PR #137 + PR #138), plus
  the 2026-07-13 night wave (~215k words, 19 books-lane PRs, NIGHT REPORT
  in `control/outbox.md`).
- **Publishing pipeline as structured data:** 45 vetting packets (31 book +
  13 product + 1 pre-registered probe), the keyword/category map with
  first-claim-wins collision scans (PR #100), the owner-queue generator
  (PR #101, hardened PR #153) rendering every owner gate into
  [`publishing/OWNER-QUEUE.md`](publishing/OWNER-QUEUE.md), and the V020
  audience-separation probe pre-registered with its decision rule
  (PR #179). Sim verdicts applied at source: PRs #163/#173.
- **Self-built operating infrastructure:** auto-merge enabler (PR #59) —
  ≈90 PRs landed by it across the 2026-07-13 runs; substrate-gate as a
  required check (evidence at PR #55); advisory ledger-drift + kill-clock
  checkers (PRs #128/#133); owner-gate lint (PR #156); the EAP audit
  itself (PRs #192/#193).

## B. Current state + how to run/verify

State snapshot: [`current-state.md`](current-state.md) (counts-synced
through the Wire Garden regen). Landing path: born-red session card →
READY `claude/*` PR → CI green → the enabler lands it; lanes never arm or
merge their own PRs.

Exact commands, each executed at HEAD `37e3c05` on 2026-07-14 with the
observed result:

1. `python3 bootstrap.py check --strict` — the pre-push gate. Observed:
   `check: all checks passed.`, exit 0. (On an in-flight branch the only
   designed red is a born-red session card.)
2. `python3 scripts/derive_owner_queue.py` — regenerates
   [`publishing/OWNER-QUEUE.md`](publishing/OWNER-QUEUE.md). Observed:
   exit 0, `parsed 46 of 46 inputs clean (45 packets + keyword map); 19
   decisions, 262 owner clicks across 44 click-run sequences`, and **no
   diff** against the committed file (the queue at HEAD is fresh).
3. `python3 bootstrap.py seat-digest` — regenerates `docs/seat-digest.md`.
   Observed: exit 0, no diff against the committed digest.
4. Per-candidate packaging — run from each candidate dir:
   `cd candidates/<name> && bash package.sh`. All **11** script paths
   verified present at HEAD: `agent-fleet-field-manual`,
   `ai-novella-production-kit`, `false-green-test-trap`,
   `github-webhook-test-kit`, `kill-rule-intake-kit`, `membership-kit`,
   `merge-wall-cookbook`, `multi-agent-control-plane-pack`,
   `owner-click-queue-kit`, `stripe-webhook-test-kit`, `template-packs`.
   Committed artifact spot-check: `sha256sum
   candidates/stripe-webhook-test-kit/dist/stripe-webhook-test-kit-v0.1.zip`
   → `d3ac5f88…eeb0d8`, matching the packet §1 pin.
5. Advisory (exit 0 always): `python3 scripts/check_ledger_drift.py` ·
   `python3 scripts/check_kill_clocks.py --today "$(date -u +%F)"` ·
   `python3 scripts/lint_owner_gates.py`.

## C. OWNER ACTIONS checklist

Source of truth: [`publishing/OWNER-QUEUE.md`](publishing/OWNER-QUEUE.md)
at HEAD (generated; re-derived clean for this doc). Totals: **19 decisions
(D1–D19) + 262 pending clicks across 44 click-run sequences (16
hard-gated), plus 1 live/completed sequence (SWTK)** — 45 sequence
headings in all. Plus two asks that are NOT in OWNER-QUEUE.md (C.3
below). One-letter replies work: `"go with defaults"` resolves every
D-item to its bolded recommendation at once; or answer per item
(`D13: C`). Deep-link base:
<https://github.com/menno420/venture-lab/blob/main/docs/publishing/vetting/>.

### C.1 Decisions D1–D19 (each: recommendation in bold + VERIFY)

**Storefront picks — D1–D9, D12** (all: reply `Dn: A`; A = **Gumroad**
(the queue's bolded default — the click-scripts' HOW is written against
it, same account as the live SWTK listing), B = Lemon Squeezy; same zip +
copy either way). VERIFY for each: the packet §7 storefront step gets
checked with your letter, the eventual listing URL returns HTTP 200 on the
chosen storefront, and a re-run of `python3 scripts/derive_owner_queue.py`
shows the D-item resolved.

| D# | Product | Recommendation | Packet (deep link) |
|---|---|---|---|
| D1 | Agent Fleet Field Manual | **Gumroad** | [agent-fleet-field-manual.md](https://github.com/menno420/venture-lab/blob/main/docs/publishing/vetting/agent-fleet-field-manual.md) §7 step 2 |
| D2 | AI Novella Production Kit | **Gumroad** | [ai-novella-production-kit.md](https://github.com/menno420/venture-lab/blob/main/docs/publishing/vetting/ai-novella-production-kit.md) §7 step 2 |
| D3 | The False-Green Test Trap | **Gumroad** | [false-green-test-trap.md](https://github.com/menno420/venture-lab/blob/main/docs/publishing/vetting/false-green-test-trap.md) §7 step 2 |
| D4 | GitHub Webhook Test Kit | **Gumroad** | [github-webhook-test-kit.md](https://github.com/menno420/venture-lab/blob/main/docs/publishing/vetting/github-webhook-test-kit.md) §7 step 2 |
| D5 | Kill-Rule Intake Kit | **Gumroad** | [kill-rule-intake-kit.md](https://github.com/menno420/venture-lab/blob/main/docs/publishing/vetting/kill-rule-intake-kit.md) §7 step 2 |
| D6 | Membership-Site Boilerplate Kit | **Gumroad** | [membership-kit.md](https://github.com/menno420/venture-lab/blob/main/docs/publishing/vetting/membership-kit.md) §7 step 2 |
| D7 | The Agent Merge-Wall Cookbook | **Gumroad** | [merge-wall-cookbook.md](https://github.com/menno420/venture-lab/blob/main/docs/publishing/vetting/merge-wall-cookbook.md) §7 step 2 |
| D8 | Multi-Agent Control-Plane Pack | **Gumroad** | [multi-agent-control-plane-pack.md](https://github.com/menno420/venture-lab/blob/main/docs/publishing/vetting/multi-agent-control-plane-pack.md) §7 step 2 |
| D9 | Owner-Click Queue Kit | **Gumroad** | [owner-click-queue-kit.md](https://github.com/menno420/venture-lab/blob/main/docs/publishing/vetting/owner-click-queue-kit.md) §7 step 2 |
| D12 | Agent-Workflow Template Pack | **Gumroad** | [template-packs.md](https://github.com/menno420/venture-lab/blob/main/docs/publishing/vetting/template-packs.md) §7 step 2 |

**D10 — Photo Packs storefront** (hard gate: nothing in that sequence
proceeds without it). Reply `D10: A` — **Gumroad** (recommended default;
Discover gives audience-free browse) or B = Ko-fi (better per-sale net
≈$4.30 vs $3.56, no marketplace browse).
[photo-packs.md](https://github.com/menno420/venture-lab/blob/main/docs/publishing/vetting/photo-packs.md)
§7 step 4. VERIFY: §7 step 4 checked; on queue regen the photo-packs
sequence drops its HARD-GATED banner once its gates clear.

**D11 — Photo Packs price** (hard gate). Reply `D11: A` — **$5 fixed per
pack** (recommended default; floor $3; PWYW ruled out — ORDER 010 / V039,
sim-lab `afe18f3`; optional two-pack bundle $9.99 inside the ruled
[$9.09, $10] band). Same packet, §7 step 5. VERIFY: listing shows $5
fixed per pack (and $9.99 if the bundle is created); §7 step 5 checked.

**D13 — The Painted Stones illustration** (hard gate). Reply `D13: C` —
**Park (C), the seat's recommendation** (A = Commission ~$1,300–$5,200,
B = AI art: near-zero cost but KDP AI disclosure + unsettled image IP).
[the-painted-stones.md](https://github.com/menno420/venture-lab/blob/main/docs/publishing/vetting/the-painted-stones.md)
§7 step 2, evidence §5, brief §6a. VERIFY: the letter is recorded in §7;
if C, the sequence stays parked (still HARD-GATED on regen — correct); if
B, the KDP AI-disclosure click becomes mandatory at publish.

**D14 — The Puddle Museum illustration** (hard gate). Reply `D14: C` —
**Park (C), the seat's recommendation** (same A/B/C shape;
reflection-rendering risk flagged in §5).
[the-puddle-museum.md](https://github.com/menno420/venture-lab/blob/main/docs/publishing/vetting/the-puddle-museum.md)
§7 step 2. VERIFY: as D13.

**D15 — The Weigh House subtitle.** Reply `D15: A` — **"An Amsterdam
Crime Novel"** (recommended default; B = "A Novel", C = "A Novella").
[the-weigh-house.md](https://github.com/menno420/venture-lab/blob/main/docs/publishing/vetting/the-weigh-house.md)
§7 step 2. VERIFY: KDP title-availability recheck run at upload (§2 was
None-but-inconclusive); the confirmed title+subtitle recorded in §7.

**D16 — The Windmill Mouse illustration** (hard gate). Reply `D16: C` —
**Park (C), the seat's recommendation** (same A/B/C shape).
[the-windmill-mouse.md](https://github.com/menno420/venture-lab/blob/main/docs/publishing/vetting/the-windmill-mouse.md)
§7 step 2. VERIFY: as D13.

**D17 — Ultramarine title.** Reply `D17: A` — **The Widow's Blue — "A
Novel of Delft, 1654"** (recommended default, §2 evidence; B = keep
Ultramarine + subtitle, accepting Navarro/Lowry/Warhammer burial; C = The
Secret of Holland).
[ultramarine.md](https://github.com/menno420/venture-lab/blob/main/docs/publishing/vetting/ultramarine.md)
§7 step 2. VERIFY: KDP title-availability recheck at upload for the
chosen title; D18's coupling then renders against it on queue regen.

**D18 — Weduwenblauw title coupling** (one click, two editions). Reply
`D18: A` — **Weduwenblauw** (recommended default, pairs with The Widow's
Blue; fallback Het blauw van de weduwe; Ultramarijn is blocked by van
Woerden regardless).
[weduwenblauw.md](https://github.com/menno420/venture-lab/blob/main/docs/publishing/vetting/weduwenblauw.md)
§7 step 2. VERIFY: KDP + bol.com title-availability recheck at upload;
the EN↔NL pair recorded in both packets' §7.

**D19 — Keyword map C1, Literary Fiction dispute.** Reply `D19: A` —
**accept the proposed resolution: The Slow Word keeps Literary Fiction;
Ultramarine swaps to Literature & Fiction → Women's Fiction → Domestic
Life**.
[keyword-map.md](https://github.com/menno420/venture-lab/blob/main/docs/publishing/keyword-map.md)
§2 C1. VERIFY: on approval the affected packet's §6 and the map's
ownership rows are edited (packets are edited ONLY on this approval), the
full-map first-claim scan re-runs clean, and D19 drops from the regenerated
queue.

### C.2 Two asks NOT in OWNER-QUEUE.md (from `control/status.md` @ HEAD)

- **NK2 — Night Kiln Book Two length band** (blocks the De Morgendeur / De
  Oogstslag hard-gated sequences and the EN Book Two write). Reply
  `NK2: A` or `NK2: B` — A = keep the packet's 20–30k plan (Book Three
  *The Harvest Rows* shipped inside it at 23,334w, PR #174), B = 16k
  parity with Book One. The seat recorded the tension both ways and has
  **no default on file** for this one — it is a genuine owner call.
  Where: [the-night-kiln versions](https://github.com/menno420/venture-lab/tree/main/candidates/adult-novels/the-night-kiln)
  · ask logged in [`../control/status.md`](../control/status.md).
  VERIFY: the ruling lands in the night-kiln packet/versions README and
  the two blocked NL sequences reference it on the next queue regen.
- **R5-C — trading-strategy A/B/C letter** (not this repo's queue — recon
  surprise, easy to miss). The sibling seat awaits one letter on the
  BTC Bollinger-breakout out-of-sample proposal:
  [trading-strategy `docs/proposals/r5c-btc-bollinger-breakout-oos-proposal.md`](https://github.com/menno420/trading-strategy/blob/main/docs/proposals/r5c-btc-bollinger-breakout-oos-proposal.md).
  Reply `R5-C: A|B|C` after reading the proposal's option block (options
  live in that doc; not restated here to avoid drift). VERIFY: the
  trading seat's `control/status.md` drops the ask from its ⚑ queue on
  its next heartbeat.

### C.3 The 262 clicks, summarized by sequence

Every click is pre-chewed in the packet's §7 (WHAT · DEFAULT · UNBLOCKS,
paste-ready); this table is the map, the queue is the checklist. Packet
paths are `docs/publishing/vetting/<file>` (deep-link base in C above).

**Ready click-runs — 28 sequences, 152 clicks** (typical shape: account →
storefront/title pick → zip/manuscript upload + sha check → listing copy →
price → publish click + test purchase):

| Sequence | Packet file | Clicks | Price default |
|---|---|---|---|
| Agent Fleet Field Manual | agent-fleet-field-manual.md | 6 | **$39** |
| Agent-Workflow Template Pack | template-packs.md | 6 | **$19 PWYW** |
| AI Novella Production Kit | ai-novella-production-kit.md | 5 | **$29** |
| De Waag | de-waag.md | 6 | **€4.99** |
| GitHub Webhook Test Kit | github-webhook-test-kit.md | 5 | **$29** |
| Het trage woord | het-trage-woord.md | 6 | **€4.99** |
| Kill-Rule Intake Kit | kill-rule-intake-kit.md | 6 | **$15** |
| Membership-Site Boilerplate Kit | membership-kit.md | 6 | **$49** |
| Multi-Agent Control-Plane Pack | multi-agent-control-plane-pack.md | 5 | **$29** |
| Owner-Click Queue Kit | owner-click-queue-kit.md | 5 | **$19** |
| The Agent Merge-Wall Cookbook | merge-wall-cookbook.md | 6 | **$19** |
| The False-Green Test Trap | false-green-test-trap.md | 6 | **$15** |
| The Glass Rectory | the-glass-rectory.md | 5 | **$4.99** |
| The Halfway Ferry | the-halfway-ferry.md | 5 | **$3.99** |
| The Marginalia Society | the-marginalia-society.md | 5 | **$3.99** |
| The Marmalade Post | the-marmalade-post.md | 5 | **$3.99** |
| The Night Kiln | the-night-kiln.md | 5 | **$4.99** |
| The Paper Orange | the-paper-orange.md | 5 | **$4.99** |
| The Pepper Ledger | the-pepper-ledger.md | 5 | **$3.99** |
| The Salvage Orchard | the-salvage-orchard.md | 5 | **$4.99** |
| The Seed Catalogue Courtship | the-seed-catalogue-courtship.md | 5 | **$3.99** |
| The Slow Word | the-slow-word.md | 5 | **$4.99** |
| The Sweetwater Sea | the-sweetwater-sea.md | 6 | **$4.99** |
| The Twelfth Cake | the-twelfth-cake.md | 6 | **$3.99** (+ mid-Nov launch-timing call) |
| The Weigh House | the-weigh-house.md | 5 | **$4.99** (after D15) |
| The Wire Garden | the-wire-garden.md | 6 | **$4.99** (subtitle mandatory) |
| Ultramarine | ultramarine.md | 5 | **$4.99** (after D17) |
| Weduwenblauw | weduwenblauw.md | 6 | **€4.99** (after D18) |

**Hard-gated click-runs — 16 sequences, 110 clicks** (each blocked by a
D-item above or a physical owner dependency; first blocker named):

| Sequence | Packet file | Clicks | Blocked on |
|---|---|---|---|
| De Driekoningentaart | de-driekoningentaart.md | 7 | EN first + NL proofread gate |
| De geborgen boomgaard | de-geborgen-boomgaard.md | 7 | EN first + NL proofread gate |
| De glazen pastorie | de-glazen-pastorie.md | 7 | EN first + NL proofread gate |
| De Marmeladepost | de-marmeladepost.md | 7 | EN first + NL proofread gate |
| De Morgendeur | de-morgendeur.md | 8 | **NK2 length-band ruling** (C.2) + NL Book One first |
| De Nachtoven | de-nachtoven.md | 7 | EN first + NL proofread gate |
| De Oogstslag | de-oogstslag.md | 8 | **NK2 length-band ruling** (C.2) + NL Books One–Two first |
| De papieren sinaasappel | de-papieren-sinaasappel.md | 6 | NL proofread gate |
| De zoete zee | de-zoete-zee.md | 7 | EN first + NL proofread gate |
| Liefde in de kantlijn | liefde-in-de-kantlijn.md | 7 | EN first + NL proofread gate |
| Photo Packs (2 packs) | photo-packs.md | 9 | owner-held full-res originals + licensing pass; D10/D11 |
| Ship-It Bundle | bundle-starter.md | 6 | membership-kit + template-packs must be LIVE first (⚑B/⚑D) |
| The Painted Stones | the-painted-stones.md | 7 | D13 illustration decision |
| The Puddle Museum | the-puddle-museum.md | 7 | D14 illustration decision |
| The Windmill Mouse | the-windmill-mouse.md | 7 | D16 illustration decision |
| V020 Probe (Paper Orange EN↔NL) | v020-probe-audience-separation.md | 3 | both Paper Orange publish clicks, ≤48h apart |

**Live/completed — 1 sequence (read-only):** Stripe Webhook Test Kit —
3 DONE rows (published 2026-07-12 at
<https://mennomagic01.gumroad.com/l/stripe-webhook-test-kit>); kill
clocks armed: T+7 funnel checkpoint 2026-07-19, T+14 kill-rule 2026-07-26.

## D. A 5-minute verify-it-yourself tour

Cold start, no context assumed. Timings are budget, not promise.

- **0:00 — get the tree.**
  `git clone https://github.com/menno420/venture-lab && cd venture-lab && git log -1 --oneline`
  (or in an existing clone: `git fetch origin main && git reset --hard origin/main`).
- **0:45 — the gate.** `python3 bootstrap.py check --strict` → expect
  `check: all checks passed.`, exit 0.
- **1:45 — the owner queue is derived, not hand-written.**
  `python3 scripts/derive_owner_queue.py && git status --short docs/publishing/OWNER-QUEUE.md`
  → expect the `46 of 46 inputs clean … 19 decisions, 262 owner clicks
  across 44 click-run sequences` summary and NO diff (regeneration is
  byte-stable at HEAD).
- **2:30 — the sellable artifact is pinned.**
  `sha256sum candidates/stripe-webhook-test-kit/dist/stripe-webhook-test-kit-v0.1.zip`
  → expect `d3ac5f88…eeb0d8` (matches the packet §1 pin in
  `docs/publishing/vetting/stripe-webhook-test-kit.md`).
- **3:00 — the one live product.** Open
  <https://mennomagic01.gumroad.com/l/stripe-webhook-test-kit> → the $29
  listing (the seat's only external publish; owner-clicked 2026-07-12).
- **3:30 — the digest is derived too.** `python3 bootstrap.py seat-digest`
  → exit 0, `git status --short docs/seat-digest.md` shows no diff.
- **4:00 — the kill clocks are armed.**
  `python3 scripts/check_kill_clocks.py --today "$(date -u +%F)"` → expect
  the SWTK T+7 (2026-07-19) / T+14 (2026-07-26) checkpoint lines.
- **4:30 — your queue.** Open
  [`publishing/OWNER-QUEUE.md`](publishing/OWNER-QUEUE.md), read §1
  (19 decisions, defaults bolded), then answer per section C above —
  `"go with defaults"` is a complete answer for D1–D19.

## E. Handoff notes

Batons the next phase inherits, with where each lives:

1. **Friday grading fires on the coordinator seat** — weekly BUSINESS cron
   `trig_01UsNU4JRps4b7jiAMdEfXNi`, time-gated to **2026-07-17T09:05Z**,
   executor live, dry-run CLEAN (`control/status.md` trigger disposition).
   Known wrinkle recorded there: a FOREIGN one-shot
   `trig_01YXNmgqYeYQ1LuepsLmbNCG` (2026-07-17T09:00Z, non-seat session)
   may duplicate the fire — recorded only, not touched. No grading
   delivery record exists yet; only the dry-run is on file (audit §11).
2. **SWTK measurement window:** T+7 funnel checkpoint 2026-07-19
   (`trig_01V9DZrTtDU81Sm7vektX9fa`), T+14 kill-rule 2026-07-26
   (`trig_01SNkNWfSXoAdz1ALf4YNbC6`) — ≥1 organic sale or ≥1 qualified
   inbound, else NEGATIVE + pause/delist per the packet.
3. **Shortlist of 3 unwritten adult-title concepts**, rubric-scored and
   ready as the next write-slice menu
   ([`ideas/2026-07-14-adult-title-concepts.md`](ideas/2026-07-14-adult-title-concepts.md)):
   The Salt Bell 24/30 (next-ranked) · The Lamp Room 24/30 · The Eleven
   Cities 23/30 (retitle first).
4. **Ideas backlog:** [`ideas/README.md`](ideas/README.md) lifecycle +
   the 💡 line on every session card; 14 WEBSITE-IDEA markers and the
   pending SIM-REQUESTs sit in `control/outbox.md` awaiting manager
   routing.
5. **Parked audit follow-ons**
   ([`audits/eap-project-audit-2026-07-14.md`](audits/eap-project-audit-2026-07-14.md)):
   the five paste-ready ANTHROPIC asks A–E (§9: merge classifier vs
   two-party review · branch-delete 403 / 187 dead branches · trigger
   lifecycle opacity · owner-approval surface for the 262 clicks · MCP
   staleness/pagination) and the open FLEET-FIX items (§5–§7):
   distinctly-named born-red check so designed red is filterable ·
   guard-fires appends committed before final push (telemetry `d1b0208`
   stranded off-main, `c0fce7c` lost) · drop/rename the ORDER header's
   constant `status:` field · retire the legacy root `claims/` alias ·
   queue the "Automatically delete head branches" owner click.
6. **Same-day siblings (ORDER 014(a)), dispatched separately on the final
   day:** ORDER 013 (INC-44 — conventions rules 2–3 rewrite to the enabler
   doctrine) and the advisory `d1b0208` cherry-pick decide-and-flag.
   Verify their terminal state in `control/status.md` at HEAD before
   assuming either landed — this doc deliberately does not claim them.
7. **Parked (cite, do not chase):** the 262 owner publish clicks / 16
   hard-gated sequences (section C — owner surface, no agent path) and
   the grading pass time-gated to 2026-07-17T09:05Z (item 1).
