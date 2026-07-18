# Kill-clock decision packet — the one live listing (Stripe Webhook Test Kit, $29)

> **Status:** `reference`

A **pre-written decision packet** for the **T+14 kill-clock call on 2026-07-26**,
so the owner's **keep / iterate / delist** decision on the one LIVE listing is a
**two-minute read, not a cold re-derivation** under a deadline. It carries (a) the
kill rule **exactly as written in the repo**, (b) the **exact evidence to check**
before deciding, (c) the **three options each with their concrete consequences**,
and (d) an **owner-only action checklist**.

This packet **changes nothing live**: no listing edit, no price change, no
publish, no spend. The decision is **owner-only and is never auto-executed** — an
agent cannot read the Gumroad dashboard, edit the listing, change the price, or
delist the product. Every action below is a click the owner performs.

It **pairs with, and does not duplicate,** the DIST-3 funnel diagnostic
([`funnel-diagnostic.md`](funnel-diagnostic.md), merged #252): that doc *diagnoses*
which funnel stage is broken (traffic vs copy vs price); this packet is the
*decision* that diagnosis feeds. Read the diagnostic for the "why"; read this for
the "so what do I do."

---

## The subject and the clock (30-second orientation)

| Fact | Value | Source |
| --- | --- | --- |
| Product | Stripe Webhook Test Kit v0.1 | [`stripe-webhook-test-kit/LISTING.md`](stripe-webhook-test-kit/LISTING.md) |
| Price | **$29 one-time** (`price_cents 2900`, USD) | [`LAUNCH-LOG.md`](stripe-webhook-test-kit/LAUNCH-LOG.md) |
| Live since (T) | **2026-07-12T16:25Z**, Gumroad, owner-published | [`LAUNCH-LOG.md`](stripe-webhook-test-kit/LAUNCH-LOG.md) |
| Listing URL | `mennomagic01.gumroad.com/l/stripe-webhook-test-kit` | [`LAUNCH-LOG.md`](stripe-webhook-test-kit/LAUNCH-LOG.md) |
| T+7 checkpoint | **2026-07-19** (mid-window review) | [`LAUNCH-LOG.md`](stripe-webhook-test-kit/LAUNCH-LOG.md) |
| **T+14 decision — this packet** | **2026-07-26** | [`LAUNCH-LOG.md`](stripe-webhook-test-kit/LAUNCH-LOG.md) |
| Signal to date | **not measured (owner-dashboard-only)** — agent surfaces do not see sales/views | [`funnel-diagnostic.md`](funnel-diagnostic.md) |

The funnel is proven end-to-end: an owner **test purchase on 2026-07-12** walked
checkout → receipt → the 19.4 KB ZIP download. The mechanics are not the
question; the question at T+14 is whether the *organic-sale signal* cleared the
bar.

---

## (a) The kill rule — as actually written in the repo

Quoted verbatim from
[`stripe-webhook-test-kit/LAUNCH-LOG.md`](stripe-webhook-test-kit/LAUNCH-LOG.md),
section **"Kill rule (concrete dates)"** — no paraphrase, no invented threshold:

> - **T (listing-live)** = **2026-07-12T16:25Z** (first verification).
> - **T+7 (checkpoint)** = **2026-07-19** — coordinator mid-window review.
> - **T+14 (deadline)** = **2026-07-26** — **signal = ≥1 organic sale OR ≥1
>   qualified inbound within 14 days of the listing going live.** No signal by
>   T+14 → ledger ⚑E a **NEGATIVE** and **pause / delist** the product.
> - **Effort cap:** cap further agent launch-support effort on this candidate at
>   **~50k tokens** per the runbook. Exceeding that budget without a signal is a
>   ledgered negative.

The same bar is carried, identically, in the §7 KILL-CHECK line of the vetting
packet and the owner queue:

> KILL-CHECK: ⏲ 2026-07-19 T+7 funnel checkpoint ·
>   ⏲ 2026-07-26 T+14 kill-rule deadline (≥1 organic sale OR ≥1 qualified
>   inbound, else ledger ⚑E NEGATIVE + pause/delist per LAUNCH-LOG.md)
>
> — [`docs/publishing/vetting/stripe-webhook-test-kit.md`](../publishing/vetting/stripe-webhook-test-kit.md) §7;
> mirrored in [`docs/publishing/OWNER-QUEUE.md`](../publishing/OWNER-QUEUE.md).

**Plain restatement (no new thresholds):** by **2026-07-26**, if there has been
**at least one organic sale OR at least one qualified inbound** (a real prospect
email/DM referencing the kit) since the listing went live on 2026-07-12, the
signal has **cleared**. If **neither** has happened, the rule's default action is
to **ledger ⚑E a NEGATIVE and pause / delist**.

---

## (b) The exact evidence to check before deciding

The signal is **owner-dashboard-only**. No agent surface, and nothing in this
repo, records sales or views — this is by design, not an oversight
([`funnel-diagnostic.md`](funnel-diagnostic.md), "What the repo can and cannot
see"). So the decision starts with **one login the owner performs**, not with any
number an agent can supply.

**Check these, in order, before choosing an option:**

1. **The kill-rule signal itself (the only input that binds the rule).**
   - **Open the Gumroad dashboard** for the Stripe Webhook Test Kit → read
     **sales since 2026-07-12**. Is it **≥ 1 organic sale**? (The 2026-07-12
     owner *test* purchase does **not** count — the rule says *organic*.)
   - **Check for a qualified inbound** — any real prospect email/DM referencing
     the kit since 2026-07-12. Is there **≥ 1**?
   - **≥ 1 of either → signal CLEARED.** **0 of both → signal NOT cleared**, and
     the rule's default is pause/delist.
   - *In-repo value today: **not measured (owner-dashboard-only)**.*

2. **If — and only if — the signal is 0, diagnose *why* before deciding, using
   the DIST-3 diagnostic.** The diagnostic separates the zero into three
   funnel-shaped causes and tells you which is even live. Do **H1 first** — it is
   the only step that says which hypothesis to trust:

   | Hypothesis | Question | What the repo already knows |
   | --- | --- | --- |
   | **H1 — traffic** | Did anyone arrive? | *Best-supported.* LAUNCH-LOG base case is "0 sales until a distribution channel is wired"; downstream distribution steps drafted but **owner-gated / not executed**. Views = **not measured**. |
   | **H2 — copy** | Did visitors fail to convert? | *Cannot judge without H1.* Listing copy meets the repo's honesty bar; visit→purchase rate = **not measured**. |
   | **H3 — price** | Is $29 wrong? | *Weakest-supported, cheapest to test.* $29 internally consistent everywhere; no abandoned-checkout / objection data = **not measured**. |

   The **cheapest read** (per the diagnostic, "H1 step 1-3"): open the Gumroad +
   dev.to dashboards, read **listing views** and **article views**, ~5 minutes,
   $0 — that one read collapses three hypotheses to one. See
   [`funnel-diagnostic.md`](funnel-diagnostic.md) for the full traffic/copy/price
   test menu; this packet does not repeat it.

3. **The effort already spent** — the rule caps agent launch-support at **~50k
   tokens**; exceeding that without a signal is itself a ledgered negative. If the
   cap is near/exceeded, that weighs against "iterate."
   *In-repo value: not separately metered here — treat the cap as a ceiling on
   further agent effort, not as a spent-to-date figure.*

---

## (c) The three options, each with its concrete consequences

Pick **one**. The rule's *default* on a 0 signal is delist; keep and iterate are
the deliberate alternatives, each with a real cost.

### Option 1 — KEEP (hold the listing live, unchanged)
- **What it means:** leave the $29 listing live as-is; do not delist, do not
  edit, do not spend further agent effort.
- **Consequences:**
  - The listing keeps costing **$0 to host** (Gumroad has no standing fee) — a
    dormant listing is cheap to keep.
  - But it also produces **no new signal on its own** — with distribution still
    owner-gated, KEEP is "0 sales continues" (the LAUNCH-LOG base case).
  - **Departs from the rule's default** on a 0 signal (which is pause/delist), so
    KEEP is only honest if paired with an explicit reason (e.g., "distribution
    was never actually attempted, so the bar was never fairly tested").
- **Ledger:** if choosing KEEP on a 0 signal, record *why* the NEGATIVE is being
  deferred rather than logged, so the next clock isn't a re-derivation.

### Option 2 — ITERATE (run the cheapest owner test, then re-decide)
- **What it means:** before killing, pull the **single cheapest lever the DIST-3
  diagnostic points at** for whichever hypothesis is live — most likely **H1
  distribution** (post the drafted, owner-gated follow-ons: gist → a real
  StackOverflow answer → an r/stripe reply), or, only if H1 shows real traffic, a
  one-line **H2 title/subtitle swap** or an **H3 price/PWYW-floor** test.
- **Consequences:**
  - Buys **one more measurement window** — but **extends the clock**, so set a
    new bounded deadline (the rule is a 14-day window; iterating restarts, not
    pauses, the "is there signal?" question).
  - Each lever is **reversible and ~$0** (one field edit, or an owner paste-post),
    but iterating **draws down the ~50k-token effort cap** — past the cap without
    signal is a ledgered negative regardless.
  - **Only honest if H1 is checked first** — iterating on copy/price with zero
    traffic is guessing ([`funnel-diagnostic.md`](funnel-diagnostic.md), H2/H3
    "cannot be judged without H1").
- **Ledger:** record which lever, the new bounded window, and the current
  token-cap headroom.

### Option 3 — DELIST (execute the rule's default)
- **What it means:** the rule's stated action on a 0 signal — **ledger ⚑E a
  NEGATIVE and pause / delist** the product.
- **Consequences:**
  - **Honestly closes** the flagship revenue candidate's first listing with a
    recorded negative — the repo's TRUTH bar rewards a ledgered negative over an
    indefinite dormant "maybe."
  - **Reversible:** a Gumroad listing can be unpublished and re-published later; a
    delist is a pause, not a deletion of the product or its in-repo assets.
  - **Frees the ~50k effort cap** from this candidate and redirects attention to
    distribution-first work (the #249–#252 lead-magnet/diagnostic baton) or other
    SKUs.
  - **Cost:** the funnel top (the live dev.to article) and the wired pipeline are
    left standing but unmonetized until/unless re-listed.
- **Ledger:** ⚑E NEGATIVE with the date, the 0-signal fact, and a one-line "why"
  (per the LAUNCH-LOG rule).

---

## (d) Owner-action checklist (owner-only — never auto-executed)

An agent cannot read the dashboard, edit the listing, change the price, or
delist. **Every box below is a click the owner performs.**

- [ ] **On or before 2026-07-26**, open the **Gumroad dashboard** for the Stripe
      Webhook Test Kit and read **organic sales since 2026-07-12** (excluding the
      2026-07-12 owner test purchase).
- [ ] Check for **≥ 1 qualified inbound** (a real prospect email/DM referencing
      the kit) since 2026-07-12.
- [ ] **Signal decision:** is it **≥ 1 organic sale OR ≥ 1 qualified inbound**?
      - [ ] **Yes → signal CLEARED.** The kill rule does not fire; **KEEP** the
            listing (Option 1) and record the clearing signal. Done.
      - [ ] **No → signal is 0.** Continue below.
- [ ] **If 0:** open the Gumroad + dev.to dashboards and read **listing views**
      and **article views** (the DIST-3 diagnostic H1 read, ~5 min, $0) to see
      *which* hypothesis is live.
- [ ] **Choose one and record it in the ⚑E ledger with a one-line why:**
      - [ ] **KEEP** (Option 1) — only with an explicit reason for deferring the
            default NEGATIVE.
      - [ ] **ITERATE** (Option 2) — name the single cheapest lever (H1
            distribution first), set a new bounded window, note the token-cap
            headroom.
      - [ ] **DELIST** (Option 3) — the rule's default: ledger ⚑E NEGATIVE +
            pause/delist on Gumroad (owner click).
- [ ] Whatever the choice, **write the outcome to the LAUNCH-LOG / ⚑E ledger** so
      the next clock is not a cold re-derivation.

*Nothing above is performed by an agent. The owner reads the dashboards, makes
the call, and clicks. This packet only makes the call a two-minute read.*

---

## Provenance

Derived, not invented — no fabricated metrics, no invented sales/traffic numbers.
The kill rule is **quoted verbatim**; where a datum is absent it is marked **"not
measured (owner-dashboard-only)"** rather than estimated. Sources:

- Kill rule (verbatim), concrete dates, effort cap, measurement plan, "0 sales
  base case", owner test purchase —
  [`stripe-webhook-test-kit/LAUNCH-LOG.md`](stripe-webhook-test-kit/LAUNCH-LOG.md).
- KILL-CHECK ⏲ line + ⚑E NEGATIVE/pause-delist disposition —
  [`../publishing/vetting/stripe-webhook-test-kit.md`](../publishing/vetting/stripe-webhook-test-kit.md) §7,
  mirrored in [`../publishing/OWNER-QUEUE.md`](../publishing/OWNER-QUEUE.md).
- Traffic vs listing-copy vs price hypotheses, "what the repo can/cannot see",
  and the cheapest owner-executed test of each —
  [`funnel-diagnostic.md`](funnel-diagnostic.md) (DIST-3 / REV-2, #252).
- MISC-3 spec —
  [`../ideas/2026-07-18-veto-ready-menu.md`](../ideas/2026-07-18-veto-ready-menu.md).
