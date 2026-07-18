# venture-lab — Next Tasks (curated menu + owner go-live steps)

> **Status:** `owner-guidance`
>
> Written 2026-07-17 for the fresh-start cleanup. This is the **curated,
> owner-actionable digest** of the standing backlog for a recreated project:
> (1) the 38-proposal veto menu, grouped and scannable; (2) the **exact owner
> steps to turn the finished products into revenue**; (3) the open owner items.
> The full, unabridged proposal set (with per-item pitch / risk / unblocks)
> stays in [`ideas/2026-07-17-overnight-menu.md`](ideas/2026-07-17-overnight-menu.md);
> the click-level publish queue stays in
> [`publishing/OWNER-QUEUE.md`](publishing/OWNER-QUEUE.md). Nothing here has been
> built or clicked — every ⚑ item is an owner action.

---

## 0. Context (why this file exists)

The Claude Code Projects EAP goes **read-only 2026-07-21**; the owner is winding
down autonomy and **recreating projects fresh**. A recreated seat should be able
to pick the next move from this one file. Two facts shape everything below:

- **Revenue, not inventory, is the binding constraint.** 1 product is LIVE with
  0 organic sales; 10 more are built and publish-READY but every publish is an
  owner click. The highest-leverage work is distribution + the owner go-live
  clicks, not more product.
- **Merging is not deploying, and money never moves without the owner.** No
  spend / account-creation / publish / payment step is ever taken by an agent
  (CONSTITUTION hard rail §13).

---

## 1. ⚑ Owner go-live steps — turn the finished products into revenue

These are the click-gated steps that stand between "built + verified" and "first
dollar." **Names only below — never commit real secret values** (`.env.example`
files name the vars; the owner fills their own).

### 1a. Stripe Webhook Test Kit — $29 (ALREADY LIVE, protect it)

Live on Gumroad in measurement mode. Nothing to wire; the owner action is a
**keep/pivot/delist decision at the kill clock**:

- **⏲ T+7 funnel checkpoint — 2026-07-19.** Read the Gumroad dashboard
  (views/sales) + the dev.to post reactions. (Agents can't see either — the
  numbers live only on the owner's dashboard.)
- **⏲ T+14 kill-rule — 2026-07-26:** ≥1 organic sale OR ≥1 qualified inbound,
  else pause/delist per the packet. Record:
  [`launch/stripe-webhook-test-kit/LAUNCH-LOG.md`](launch/stripe-webhook-test-kit/LAUNCH-LOG.md).
- Buyer-side note: the kit is a self-hosted harness a **buyer** runs with their
  own `SWTK_WEBHOOK_SECRET` (their Stripe `whsec_…`). That is a product-runtime
  var the buyer supplies — **not** an owner go-live secret.

### 1b. Membership-Site Boilerplate Kit — $49 (publish-READY; needs keys for real money)

The kit **runs in MOCK mode with zero keys** (no accounts needed to demo the
purchase→access loop). To take **real** money the owner sets env var **names**
below in `candidates/membership-kit/server/.env` (copy from
[`.env.example`](../candidates/membership-kit/server/.env.example); never commit
the real values):

1. **`STRIPE_SECRET_KEY`** — Stripe → Developers → API keys. Start with the
   **`sk_test_…`** test key. Turns on the real `/create-checkout-session` call.
2. **`STRIPE_WEBHOOK_SECRET`** — the `whsec_…` webhook signing secret. Turns on
   native `/webhook` signature verification (bad/stale signatures → HTTP 400
   before any membership is granted).
3. **`DISCORD_INVITE_URL`** — Server Settings → Invites. Optional; powers the
   invite-on-purchase hook.
4. **Persistence — pick one:**
   - Default = local JSON file (`STORE_BACKEND=json`) — zero setup, fine to launch.
   - Hosted = Supabase: set **`STORE_BACKEND=supabase`** + **`SUPABASE_URL`** +
     **`SUPABASE_KEY`** (Project Settings → API; use the service-role key for
     server-side writes). Needs a `members` table (see
     [`server/README.md`](../candidates/membership-kit/server/README.md)).
   - **Note — there is NO `DATABASE_URL` in this kit.** The membership kit's real
     persistence env is **`SUPABASE_URL` / `SUPABASE_KEY`** (Supabase PostgREST),
     falling back loudly to the local JSON store when unset. If a brief says
     "set DATABASE_URL", that name is not used here (grep-confirmed 0 hits).
5. **Publish click** — post the Gumroad listing (see OWNER-QUEUE decision **D6**,
   default storefront **Gumroad**) once the owner is satisfied with a real-key
   test run.

> Go-live sequence, condensed:
> `STRIPE_SECRET_KEY` (sk_test_…) → `STRIPE_WEBHOOK_SECRET` (whsec_…) →
> [optional `DISCORD_INVITE_URL`] → [optional `STORE_BACKEND=supabase` +
> `SUPABASE_URL` + `SUPABASE_KEY`] → verify a real test purchase → publish click.

### 1c. The 10 publish-READY SKUs — the owner publish wave

All 10 are built + priced + listing-drafted + verified; the only thing missing is
the owner posting them. The click-level queue is
[`publishing/OWNER-QUEUE.md`](publishing/OWNER-QUEUE.md) (generated — re-run
`scripts/derive_owner_queue.py` after any packet change). At the last regen:

- **19 decisions (D1–D19)**, each with a **bolded default** — "go with defaults"
  is a one-word reply (most are "storefront = Gumroad").
- **45 publish sequences**, **19 hard-gated** (illustration commissions, native-
  speaker proofreads, photo originals) → **268 unchecked owner clicks** total.
- The 10 dev/agent + writing SKUs: Membership-Site Boilerplate Kit $49 ·
  Agent-Workflow Template Pack $19 PWYW · Agent Fleet Field Manual $39 ·
  Kill-Rule Intake Kit $15 · The False-Green Test Trap $15 · The Agent
  Merge-Wall Cookbook $19 · GitHub Webhook Test Kit $29 · Owner-Click Queue Kit
  $19 · Multi-Agent Control-Plane Pack $29 · AI Novella Production Kit $29.

### 1d. The book catalog publish wave

Large NL/EN catalog, but its revenue path is stalled on **KDP account + tax/bank
interview** and, for the NL editions, the **owner-only native-speaker proofread
pass** (19 hard-gated OWNER-QUEUE rows — an AI cannot clear it). REV-7 (below) is
the spec for a de-risked KDP-first launch wave.

---

## 2. ⚑ Open owner items (non-product)

- **Failsafe seat write-wall.** The persistent failsafe wake session
  (pinned-research env) has **no write access** to venture-lab — `git push`
  returns **403, "access to this repository is not enabled for this session"**.
  The backstop can observe but not land. **Owner action:** enable venture-lab
  write for that seat, or accept observe-only. (Per-seat token wall, not
  repo-wide — the coordinator seat pushed/landed normally.)
- **Native-speaker proofread pass** on the ready NL editions — the single binding
  lever on the ~13 ready NL editions (4 closest titles carry a mechanical
  `PRE-QA.md` to make the read guided, not cold).
- **Length-band ratify** (one word):
  `candidates/adult-novels/the-night-kiln/LENGTH-BAND-PREP.md` (De Morgendeur /
  De Oogstslag).

---

## 3. The backlog menu — 38 proposals (veto-ready)

Curated from [`ideas/2026-07-17-overnight-menu.md`](ideas/2026-07-17-overnight-menu.md)
(full pitch/risk/unblocks per item there). Effort = diff size, not time.
**⚑ = has an owner-gated publish/spend/account step.** Skim, veto what you don't
want; survivors become claimed slices.

### Product / sellables (P-1…P-12)

| # | Proposal | Effort | Notes |
|---|---|---|---|
| P-1 | Slack Webhook Test Kit $29 | M | N+1 off the proven webhook-kit template; ⚑ publish |
| P-2 | Shopify Webhook Test Kit $29 | M | Bigger commercial audience than agent-ops; ⚑ publish |
| P-3 | Webhook Test Kit Trio bundle $59 | S | AOV upsell; gated on P-1 + GWTK being live; ⚑ |
| P-4 | Auto-Merge Enabler Cookbook $19 | M | Distill the enabler doctrine; ⚑ publish |
| P-5 | The Salt Bell — NL edition (*De zoute klok*) | M | Highest NL-market-fit title; ⚑ proofread + publish |
| P-6 | NL editions for EN-only adult novels (Wire Garden) | L | NL parity; ⚑ proofread + publish |
| P-7 | YA line — first NL edition (pilot one) | L | New NL sub-shelf; ⚑ |
| P-8 | The Paper Orange — German (DE) edition | L | Ambitious; opens DE adult market; ⚑ |
| P-9 | Audiobook / narration-ready EDITION-SPEC | M | First audio-channel asset; spec only |
| P-10 | Night Kiln trilogy omnibus (EN + NL) | S–M | Recombine completed manuscripts; ⚑ publish |
| P-11 | Trilingual board-book "First Library" bundle | M | First children's-line bundle; ⚑ |
| P-12 | Pricing experiment — PWYW launch + tiered bundle | S | First deliberate pricing signal; ⚑ price clicks |

### Publishing pipeline / automation (PUB-1…PUB-9)

| # | Proposal | Effort | Notes |
|---|---|---|---|
| PUB-1 | NL spellcheck-in-CI lane (advisory) | M | Wire spylls + OpenTaal nl_NL over NL manuscripts |
| PUB-2 | EN spellcheck lane (`en_US` hunspell) | M | Mirror PUB-1 for the larger EN catalog |
| PUB-3 | Productionize `categorize.py` (the PRE-QA filter) | S | Commit the ephemeral filter + unit test |
| PUB-4 | `NOTES.md`-sourced allowlist as tested artifact | M | Sustainable allowlist maintenance |
| PUB-5 | PRE-QA scaffold generator for remaining titles | M | Scale PRE-QA coverage without hand-effort |
| PUB-6 | Length-band / expansion-ratio checker | S | Mechanizes PRE-QA §5; live number for the ruling |
| PUB-7 | Structured proofread packet + correction-capture | L | Tools the owner's proofread pass (still owner-only) |
| PUB-8 | Manuscript-QA linter bundle | M | Doubled-word/quote-nesting/name-consistency checks |
| PUB-9 | OWNER-QUEUE staleness / proofread-gate drift checker | S | Guarantees the generated queue never drifts |

### Revenue path / distribution (REV-1…REV-8)

| # | Proposal | Effort | Notes |
|---|---|---|---|
| REV-1 | Real-Stripe-path spec + vendored-payload test harness | M | Unfreezes membership $49 + template $19; ⚑ live-key run |
| REV-2 | "Why zero sales" funnel diagnostic for SWTK | S | Evidence for the 2026-07-19 checkpoint; ⚑ dashboard |
| REV-3 | Conversion / UTM instrumentation spec | S | Per-channel attribution; ⚑ owner pastes UTM URLs |
| REV-4 | Static catalog / SEO microsite (build in-repo) | M | Evergreen funnel-top; ⚑ hosting/deploy |
| REV-5 | Product Hunt / HN / Reddit launch kit + email capture | M | Repeatable launch playbook; ⚑ every send |
| REV-6 | Free-tier lead magnet + bundle-economics memo | S | Top-of-funnel email; ⚑ ESP/storefront |
| REV-7 | Book-catalog revenue path — KDP-first spec | M | Sequences the dormant catalog; ⚑ KDP account |
| REV-8 | Cross-sell hub + storefront consolidation | L | Raises AOV across the kit family; ⚑ storefront |

### Ops / infra / repo-health (OPS-1…OPS-9)

| # | Proposal | Effort | Notes |
|---|---|---|---|
| OPS-1 | Retire the empty legacy root `claims/` dir | S | One canonical claim home (`control/claims/`) |
| OPS-2 | Heartbeat-freshness advisory on `control/status.md` | S | Fast "is the heartbeat trustworthy?" read |
| OPS-3 | Promote owner-gate lint from advisory → required | S | Owner-facing queue can't silently go malformed |
| OPS-4 | Scheduled sweeper to prune merged-PR claim files | M | `control/claims/` reflects only in-flight work |
| OPS-5 | Docs-freshness checker — flag stamped docs lagging HEAD | S–M | Turns "is this brief current?" into a check |
| OPS-6 | Doc link-checker + planted-set orphan checker | M | Cross-doc refs stay resolvable |
| OPS-7 | Auto-merge / merge-queue readiness self-check | M | Detects the required-check misconfig early |
| OPS-8 | One canonical `START-HERE.md` + orientation self-test | M | Collapse the 5 cross-pointing boot docs to one |
| OPS-9 | Machine-readable `STATE.json` + 60-second dashboard | L | Cuts per-session orientation cost |

---

## 4. Fresh-start / relaunch hygiene (recommended before or at recreation)

Scaffolding this cleanup PR flagged (banners added; deletion left as an owner/
relaunch call so nothing load-bearing is removed unilaterally):

- **Retire the `control/*` message-bus** (inbox / outbox / status / README) and
  its ORDER stack — EAP-era fleet ceremony; a single-owner recreated project
  takes orders directly. (Banners added this PR.)
- **Reconsider the auto-merge apparatus** — `auto-merge-enabler.yml` + the
  born-red session-card gate (`substrate-gate.yml` + `.sessions/` cards). Note:
  the earlier rationale ("agent seats can't arm/self-merge, so the enabler is the
  only merger") was based on a **false standing wall** — merging own green PRs is
  normal agent work (proven by direct agent merges). Correcting that belief
  **dissolves the frozen-PR class** directly: agents merge their own green PRs,
  so a mergeable green PR never sits waiting. The enabler is now a convenience,
  not the sole sanctioned merger; decide whether to keep it as a convenience or
  simplify. (Workflow files left intact this PR — a workflow change is an
  owner-gated relaunch step.)
- **OPS-1:** delete the empty legacy root `claims/` dir (holds only a README).
- **OPS-8:** collapse the five cross-pointing boot docs (`CONSTITUTION.md`,
  `AGENT_ORIENTATION.md`, `NEXT-SESSION.md`, `current-state.md`,
  `reading-path.md`) into one thin `START-HERE.md` router.
- **`docs/seat-digest.md`** is a generated render — regenerate or drop it at
  relaunch (not hand-edited here).
- Archive the EAP-era history docs (`eap-closeout-walkthrough-2026-07-14.md`,
  `_merge_verification_2026-07-15.md`, `NEXT-SESSION.md`) — banners added this PR;
  delete or move to `docs/retro/` at relaunch.
