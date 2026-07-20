---
state: captured
origin: lab
shipped_pr: null
shipped_repo: null
merged_date: null
outcome: open
---

# Season-2 plan — 2026-07-20 (contingent, post-cutoff)

> **Status:** `ideas`
>
> A **prioritized, contingency-shaped** build plan for the world **after the
> 2026-07-21 write-cutoff.** Where
> [`2026-07-19-execution-roadmap.md`](2026-07-19-execution-roadmap.md) sequenced
> the *pre*-cutoff closing window, this doc plans the *next* season: it does not
> assume a linear backlog, because after the cutover the next move depends on
> **which owner action fires first.** So it is organised as **contingency
> branches** — one ordered list per "IF" — plus a standing upkeep cadence.
> Planning doc only: nothing here is built, priced-live, or published; every
> publish / spend / post / proofread / data-provision remains an **owner** action.
> Priorities are **decide-and-flagged** (my call, stated as such); owner-gated
> items are marked inline.

## How to read this

Each branch is an **ordered list, one line per item**: `id/name · autonomous-safe
| owner-gated · single next-step / unblock condition`. Ordering within a branch is
**my call** (decide-and-flag), tied to the two standing constraints below;
owner-gate labels are copied from the source docs, not re-guessed.

**Two constraints that shape every branch:**

1. **The seat goes read-only 2026-07-21** (`../current-state.md`, "Platform
   wind-down"). After that, *this* seat cannot land repo work — the owner is
   winding down the autonomy apparatus and **recreating some projects fresh**. So
   every **"build"** line below presumes a **fresh writable seat** (post-relaunch)
   picks it up; it is the order *that* seat should follow. **Owner-only actions**
   (post, publish, proofread, provision data) survive the cutover untouched.
2. **Distribution, not inventory, is the binding constraint** (1 LIVE SKU, 0
   organic sales, 19 publish-READY SKUs undiscovered — `../launch/CATALOG.md`).
   New inventory is cheap to build but moves no revenue without a post + a
   distribution path, so distribution work outranks new inventory in every branch.

---

## Branch 1 — IF the owner posts the lead magnets → next distribution slices

> Trigger: the owner posts any of the four free lead magnets from the
> paste-and-post pack (`../launch/submissions/README.md`, #277 — api-robustness
> #243 · agent-ops #246 · membership #250 · AI-novella #251). That is the first
> traffic against the binding constraint. **My call:** the magnet traffic needs
> somewhere to land, be measured, and be captured *before* more top-of-funnel is
> worth adding — so a convert-and-capture destination ranks above more posting.

1. **DIST-5** — static catalog landing microsite (= REV-4) · autonomous-safe to build (owner-gated to go live: hosting/domain) · the single destination magnet readers land on; build the static files in-repo, owner hosts.
2. **DIST-4** — conversion-tracking / UTM + email-capture spec (= REV-3 + REV-5) · owner-gated · unblock: owner email-tool / analytics account spend+setup — so the magnet traffic is *measured and captured*, not spent once.
3. **DIST-6** — launch-kit: Product Hunt / HN / Reddit playbook (= REV-5) · autonomous-safe to build (owner-gated to post) · scales the 11-file submission motion beyond the first channels.
4. **LM-3** — fiction-catalog reader magnet (free first-chapter / sampler) · autonomous-safe to build · opens a *second* funnel (the book catalog) beside the dev-tools funnel; note honestly it converts on a mailing list the repo doesn't yet own (see DIST-4).
5. **MISC-4** — owner-postable catalog one-pager · owner-gated (owner posts it) · a single shareable asset for a newsletter / channel once traffic exists.
6. **DIST-7** — cross-sell hub / storefront consolidation (= REV-8) · owner-gated · unblock: owner live-storefront edits — tie the landed listings together once more than a couple are live.
7. **LM-4** — photo-packs / visual-assets cluster lead magnet · autonomous-safe · *speculative* — only if photo-packs stay a live lane.

---

## Branch 2 — IF vetoes arrive → approved-queue build order

> Trigger: the owner runs a veto pass over the 64-item menu
> (`2026-07-18-veto-ready-menu.md`, #247) — the veto is a *subtractive* filter, so
> the survivors are the greenlit queue. This is the order a **fresh writable seat**
> should build them in (Constraint 1). It mirrors the execution roadmap's Lane A
> tiers (autonomous-safe first), restricted to whatever survives veto. **My call:**
> pipeline-safety tooling before throughput before new inventory — protect and
> route the already-built inventory before adding more.

1. **ENG-6** — `derive_owner_queue.py` idempotence/self-test guard · autonomous-safe · unblock: none (pure repo tooling; closes the D-ref safety story ENG-2 #248 began).
2. **ENG-5** — `check_catalog_registration.py` built-but-unregistered checker · autonomous-safe · unblock: none (guarantees no READY SKU strands invisible — protects the built inventory).
3. **ENG-7** — OWNER-QUEUE staleness / proofread-gate drift checker (= PUB-9) · autonomous-safe · unblock: none (keeps the generated queue trustworthy after packet edits).
4. **ENG-8** — docs-freshness + link/orphan checker (= OPS-5 + OPS-6) · autonomous-safe · unblock: none (cheap `docs/` hygiene for a fresh seat).
5. **MISC-1** — fresh-seat boot hardening for the post-EAP repo · autonomous-safe · unblock: none (the wind-down explicitly wants the repo bootable from itself alone).
6. **MISC-5** — planning-doc conveyor consolidation · autonomous-safe · unblock: none (reconciles the now-*five* planning docs — incl. this one — so no seat re-derives a false "backlog dry").
7. **DIST-2** — "Owner publish hour" sequencer (extends `OWNER-LAUNCH-HOUR.md`) · autonomous-safe to build · unblock: none for the build (the clicks it orders stay owner-only).
8. **BOOK-6** — native-speaker proofread TOOLING (= PUB-1/6/7) · autonomous-safe · unblock: none (tools the book gate; cannot clear it — see Branch 3).
9. **New SKUs (breadth only)** — SKU-4 PayPal/Square Webhook Kit → SKU-5 Timeout/Circuit-Breaker → SKU-11 Timezone/DST → the rest of the veto-menu SKU list, each autonomous-safe, each unblock: a publish click. Ranked LAST: the veto menu's own framing — "none of these move revenue on their own."

*(ENG-4 per-KIT funnel-asset checker folds into ENG-3's shipped per-cluster checker #256 as a second advisory; carry it only if the veto keeps it distinct.)*

---

## Branch 3 — IF a book sells → series-continuation order

> Trigger: any KDP listing records a sale — a demand signal for **that** series, so
> the sold series is continued first. Absent a specific sale, this is the default
> continuation order by **hook-readiness**, grounded in the actual catalog
> (`../current-state.md` "Book catalog"; QA scan 2026-07-20): **two *complete*
> adult trilogies — Ultramarine (Delft, Bk 1–3, closed by *The Common Blue* #278)
> and Lull/DREAMLINE (MG portal-fantasy, Bk 1–3, closed by *The Fourth Hour
> Comes*) — plus a *six-book* Night Kiln cozy series (Bk 1–6; *The Summer Ember*
> #279 paid Bk 5's cold far-kiln hook, and a Bk 7 is planted but unwritten).** All
> book work is autonomous to draft but **owner-gated on the native-speaker
> proofread** before any listing.

1. **The Night Kiln — Book 7** · autonomous-safe to draft · owner-gated (proofread) · the ONLY series carrying an **already-planted forward hook** (Bk 6 seeded Bk 7); shortest novellas (~15.6k), matched cozy series → most read-through per proofread-hour. **First — lowest-friction continuation.** Next hook: pay the planted Bk 6→7 seed (do not over-specify; it is planted, not yet written).
2. **Ultramarine — a Book 4 / companion arc** · autonomous-safe to draft · owner-gated (proofread) · the trilogy **closed** on an organic forward note, so continuation is a **fresh arc seed** (natural thread: Grietje and the East-bound blue-and-white freight), not paying an open hook — needs a new outline first.
3. **Lull / DREAMLINE — a Book 4 / companion arc** · autonomous-safe to draft · owner-gated (proofread **and** the unresolved keyword-map §3 "Lull" mis-scope, literary vs MG, which already blocks keyword reservation) · the trilogy **closed**, so continuation is a **new portal seed**; it inherits the §3 gate, so ranked below Ultramarine.

> **Standing book gate (all three):** the native-speaker proofread is the binding
> lever an AI cannot clear; the 7 existing KDP-ready packages already wait on it
> (`../publishing/OWNER-START-HERE.md` §5, Step 8). A new book adds an eighth item
> to that same queue — write it, but do not list it as available.

---

## Branch 4 — IF trading data is provisioned → round designs

> Trigger: the owner provisions a real data feed. **Scope honesty:** trading is a
> **separate RESEARCH-ONLY repo** (`menno420/trading-strategy`), out of scope for
> venture-lab building — this branch is a cross-ref, not venture work, and no
> venture-lab work is sequenced against it. **Trading direction doc: not located**
> (searched venture cross-refs + the trading-strategy references; the nearest
> artifact is a single strategy proposal —
> `trading-strategy docs/proposals/r5c-btc-bollinger-breakout-oos-proposal.md`,
> cited in `../eap-closeout-walkthrough-2026-07-14.md` — which is *a* strategy, not
> a fundamentals-vs-flows direction doc). The round designs below are sketches for
> whichever data class arrives; they belong to the trading-strategy lane.

1. **IF fundamentals data (statements / ratios / earnings)** → a **value/quality-factor round**: rank the universe by fundamental factors, backtest a long-short, honest in-sample vs OOS split, honest nulls. Belongs in the trading-strategy repo.
2. **IF flows data (order-flow / volume / positioning)** → a **momentum/flow round**: signal from flow imbalance, backtest, honest nulls, no real money (the lane is research-only). Belongs in the trading-strategy repo.
3. **Either way** → the Friday grading is the scoreboard both rounds report into (see the cadence below).

---

## Standing upkeep cadence (runs regardless of which branch fires)

> The recurring maintenance that keeps the ledger honest and the clocks answered.
> **No trigger/cron state is recorded here** — that class is classifier-walled;
> these are date-anchored owner/seat obligations, not armed automation.

- **Friday weekly grading — next 2026-07-24.** The standing trading-research
  scoreboard (ORDER 008 item 4, `control/inbox.md`): every backtest result graded
  honestly. Trading-strategy lane; venture-lab cross-refs only.
- **SWTK T+14 kill-clock decision — 2026-07-26.** The owner reads the funnel
  diagnostic (`../launch/funnel-diagnostic.md`, #252) + the decision packet
  (`../launch/kill-clock-decision-packet.md`, #253) and makes the
  keep/iterate/delist call on the one LIVE listing (kill rule: ≥1 organic sale OR
  ≥1 qualified inbound, else pause/delist). **Owner-gated; the autonomous inputs
  are already written** — nothing to build, only the read.
- **Per-pass repo hygiene (autonomous-safe):** regenerate `OWNER-QUEUE.md`
  (`scripts/derive_owner_queue.py`) after any packet change and sync counts the
  same pass; keep the required `catalog-dref-guard` green; restamp the heartbeat
  (`control/status.md`) LAST each pass; watch the advisory checks (ledger-drift,
  kill-clocks, owner-gate lint) without gating on them.

---

## Provenance

Derived from the repo at `main@d2d49ec` (PR #281), no fabricated metrics:

- Catalog counts (1 LIVE + 19 READY + 3 hard-gated bundles; the four lead magnets;
  the submission pack #277) — `../launch/CATALOG.md` and `../current-state.md`.
- The book catalog shape (two complete trilogies + a six-book Night Kiln, Bk 7
  planted-unwritten; the proofread gate; the Lull §3 keyword mis-scope) —
  `../current-state.md` "Book catalog", `../publishing/OWNER-START-HERE.md` §5, and
  the 2026-07-20 owner-surface QA scan.
- Every branch's line items, owner-gate labels, and unblock conditions —
  `2026-07-18-veto-ready-menu.md` (#247) and `2026-07-19-execution-roadmap.md`
  (its Lane A ordering), the source docs this contingency-shapes rather than
  re-derives.
- The two constraints (write-cutoff 2026-07-21 · distribution binding) —
  `../current-state.md` "Platform wind-down" and the execution roadmap's
  standing-context section.
- Trading scope + the "direction doc: not located" finding —
  `../publishing/TRANSITION-DOSSIER.md` (trading out of scope here) and
  `../eap-closeout-walkthrough-2026-07-14.md` (the nearest strategy proposal, which
  is not a direction doc).
