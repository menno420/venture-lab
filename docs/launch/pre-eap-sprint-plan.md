# Pre-EAP-read-only publish sprint plan

> **Status:** `reference`
>
> A one-page wind-down plan for the ~2 days of write access left before the
> **Claude Code Projects EAP goes read-only on 2026-07-21**. It splits the work
> into two lists that must not be confused: **AGENT-LANDS-THESE** (repo work that
> needs the write seat — must land before the cutover) and **OWNER-CLICKS-THESE**
> (publish clicks that do *not* need the seat and survive the cutover, but
> compete for finite owner attention — batch them into one pre-cutover session).
> Grounded in the refreshed state ledger [`../current-state.md`](../current-state.md)
> (#254, HEAD `7d5229f`), the veto-ready menu
> [`../ideas/2026-07-18-veto-ready-menu.md`](../ideas/2026-07-18-veto-ready-menu.md)
> (#247, DIST-9), the live [`../publishing/OWNER-QUEUE.md`](../publishing/OWNER-QUEUE.md),
> and [`CATALOG.md`](CATALOG.md)'s advisory publish order. No invented deadlines;
> where a funnel stage is dark (Gumroad views/sales are owner-dashboard-only) it
> says so. Advisory only — the seat performs no publish/spend/account action.

## The clock (read first)

- **Cutover: 2026-07-21, EAP goes read-only** (extended through 2026-07-21 —
  `control/inbox.md` ORDER 015, Anthropic mail 2026-07-14). Written 2026-07-19;
  **~2 days of write access remain.**
- **What read-only means for autonomy on the 21st:**
  - **No repo landing.** After cutover the autonomous seat and any scheduled
    routines can no longer push, open/merge PRs, or update docs. Anything that
    must live *in the repo* has to land **before** the 21st.
  - **Owner clicks still work.** Publishing is a manual **owner** action (upload
    a dist zip to Gumroad, paste listing copy, click publish) on the owner's own
    account — it does **not** depend on EAP write access, so it is unaffected by
    the cutover. The value of doing clicks *before* cutover is only that the seat
    can still update supporting docs, answer questions, and fix listing copy
    while it has write access; the clicks themselves are not time-boxed by the
    EAP.
  - **The repo is being left boot-clean** for a fresh seat (per
    [`../current-state.md`](../current-state.md)) — so the highest-value agent
    work is what makes the wind-down orderly, not a scramble.
- **One live revenue clock spans the cutover:** the LIVE Stripe Webhook Test Kit
  ($29) is under a measurement kill clock — **T+7 checkpoint 2026-07-19 (today),
  T+14 kill rule 2026-07-26** (≥1 organic sale OR ≥1 qualified inbound, else
  pause/delist). Both the funnel diagnostic ([`funnel-diagnostic.md`](funnel-diagnostic.md),
  #252) and the keep/iterate/delist packet
  ([`kill-clock-decision-packet.md`](kill-clock-decision-packet.md), #253) are
  already landed and owner-ready, so this decision needs **no repo work** before
  cutover — it is an owner read + call.

## AGENT-LANDS-THESE (needs the write seat — land before 2026-07-21)

Priority order for the remaining ~2 write days. These are the highest-leverage
**agent-buildable** (`can-build-autonomously`) slices from the veto-ready menu
(#247). **Owner veto is still the filter** — none of these are pre-approved, and
none is claimed "ready" here; they are ranked candidates for the closing write
window. Anything owner-gated (proofread, publish, spend, decisions) is **not** on
this list — it cannot be cleared by landing a PR.

1. **DIST-9 — this plan.** Landing now. Makes the split below explicit so the
   owner's pre-cutover session and the seat's last write days don't collide.
2. **DIST-2 — "Owner publish hour" sequencer** (extends
   [`OWNER-LAUNCH-HOUR.md`](OWNER-LAUNCH-HOUR.md)). A generated, copy-paste-ordered
   click-run for the queued publishes in the exact sequence that unlocks bundles
   earliest. This is the *build* that makes OWNER-CLICKS-THESE below fast; it is
   the single agent slice with the most direct leverage on owner throughput, and
   it must land **before** cutover to be useful for the pre-cutover click session.
3. **BOOK-6 — native-speaker proofread TOOLING** (spellcheck-in-CI + length-band
   checker + structured proofread-packet format). The only writing-lane work that
   moves the proofread-gated book cluster **without** owning the gate — it makes
   the owner's (always-owner-only) native-speaker pass a fast structured review
   instead of a cold full read. Tooling-only, high leverage, agent-buildable.
4. **DIST-5 — static catalog landing microsite** (agent-buildable static HTML
   in-repo; hosting/domain stays an owner step). Gives channel posts one branded
   destination instead of N Gumroad links. Larger (M–L); land only if 1–3 are
   done with write time to spare.

> Discipline: each lands born-red → READY `claude/` PR → CI green → merge, exactly
> as #249–#254 did. Do **not** start a slice that can't finish-and-land before
> the 21st — an unlanded PR is lost to the read-only cutover.

## OWNER-CLICKS-THESE (does NOT need the seat — batch into one pre-cutover session)

These publish clicks survive the cutover, but scattering them wastes the owner's
attention and delays every bundle unlock. Run them **top-down in one session**;
this mirrors [`CATALOG.md`](CATALOG.md)'s advisory publish order and the live
[`../publishing/OWNER-QUEUE.md`](../publishing/OWNER-QUEUE.md). Every item is an
owner click; the seat executes none of them.

1. **The webhook trio → the bundle unlock (highest leverage per click).**
   Publish the three remaining webhook kits — **GitHub Webhook Test Kit (D6)**,
   **Slack Webhook Test Kit (D20)**, **Shopify Webhook Test Kit (D19)**, $29 each
   — on the same Gumroad account and flow as the already-LIVE Stripe kit. Then
   **create the Webhook Verifier Bundle ($79)** — one extra click turns the four
   live singles into an anchor SKU. (Stripe is already live since 2026-07-12, so
   it carries no blocking row; the bundle is hard-gated only on D6 + D20 + D19.)
2. **The API-robustness four → its bundle.** Publish **Idempotency Key (D7)**,
   **Rate-Limit (D18)**, **Pagination (D15)**, **JWT Auth (D9)** — same dev-tool
   buyer/account — then **create the API Robustness Bundle ($79)**. Same
   singles→bundle move as step 1.
3. **Membership + template pair → Ship-It Bundle.** Publish the **Membership-Site
   Boilerplate Kit (D11, ⚑B, $49)** + **Agent-Workflow Template Pack (D21, ⚑D,
   $19 PWYW)**, then **create the Ship-It Bundle ($59)**. (See the freeze note
   below.)
4. **The rest, as attention allows** — agent-ops guides & tools (D1, D12, D3,
   D14, D13, D10, D5) and the AI Novella Production Kit (D2, writing-category
   note). Lower-friction content SKUs; no bundle gate.
5. **The live-SKU T+7/T+14 call** (owner read, no click required unless
   delisting). Use [`kill-clock-decision-packet.md`](kill-clock-decision-packet.md)
   (#253); signal = ≥1 organic sale OR ≥1 qualified inbound by 2026-07-26.

## Freeze / gate honesty (do not misread these)

- **⚑B / ⚑D are NOT frozen.** ORDER 003 froze the ⚑B membership-kit ($49) and ⚑D
  template-pack ($19) publish clicks on 2026-07-10; the repo records that freeze
  as **LIFTED 2026-07-11** — the real-Stripe-path gate landed (PR #16, squash
  `912da3e`, real-path HTTP tests green + 9/9 non-author verification) and the
  unfreeze was applied (see [`membership-kit/owner-actions.md`](membership-kit/owner-actions.md)
  and [`template-packs/owner-actions.md`](template-packs/owner-actions.md), both
  "UNFROZEN 2026-07-11"). They are owner-clickable today. The append-only
  `control/inbox.md` still shows ORDER 003 `status: new` **by protocol** (the lane
  never edits the inbox; done-state lives in the repo, not the order) — that is
  not a live freeze. **Honest caveat (⚑A):** a *live* purchase is still unverified
  — "unfrozen" means the owner may click when ready, not that payments are
  live-proven.
- **Genuinely owner-only, and NOT clearable by any pre-cutover repo work:**
  native-speaker NL/DE **proofread pass** (hard-gates 19+ book rows; an AI can
  *tool* the gate — BOOK-6 above — but cannot clear it); the **LENGTH-BAND-PREP**
  one-word ratify (Night Kiln NL omnibus); the **R5 `_api-hardening-core`** refactor
  nod; the **photo-pack originals** handoff (owner-held off-repo). All
  publish/spend/external-account actions are owner-only always, before and after
  the cutover.
- **No invented numbers.** Gumroad views and sales are owner-dashboard-only; the
  seat does not see them. Any funnel stage the repo can't observe is marked "not
  measured (owner-dashboard-only)", never guessed. Counts (1 LIVE + 19 READY SKUs
  + 3 bundles, 28 OWNER-QUEUE decisions) are per #254 / the live OWNER-QUEUE at
  authoring; re-derive from the generated file rather than trusting a copied
  total.
