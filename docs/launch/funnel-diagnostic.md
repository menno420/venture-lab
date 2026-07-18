# Funnel diagnostic — the one live listing (Stripe Webhook Test Kit, $29)

> **Status:** `reference`

An honest, repo-grounded read of **why the one LIVE listing has zero organic
sales**, written for the **T+7 checkpoint (2026-07-19)** and the **T+14 kill
rule (2026-07-26)**. It separates three candidate causes — **traffic**,
**listing-copy**, **price** — states what the repo actually knows about each
(and what it does **not** measure), and gives the **cheapest owner-executed test
of each**.

This is a diagnostic only. It changes nothing live: no listing edit, no price
change, no publish, no spend. Every owner test below is a **click the owner
performs**, never an agent action. It pairs with the upcoming **MISC-3 live-SKU
kill-clock decision packet**, which turns the T+14 call into a two-minute read;
this doc is the evidence that packet consumes.

---

## The subject and the clock

| Fact | Value | Source |
| --- | --- | --- |
| Product | Stripe Webhook Test Kit v0.1 | [`stripe-webhook-test-kit/LISTING.md`](stripe-webhook-test-kit/LISTING.md) |
| Price | **$29 one-time** (`price_cents 2900`, USD) | [`LAUNCH-LOG.md`](stripe-webhook-test-kit/LAUNCH-LOG.md) |
| Live since (T) | **2026-07-12T16:25Z**, Gumroad, owner-published | [`LAUNCH-LOG.md`](stripe-webhook-test-kit/LAUNCH-LOG.md) |
| Listing URL | `mennomagic01.gumroad.com/l/stripe-webhook-test-kit` (HTTP 200, published, not compliance-blocked) | [`LAUNCH-LOG.md`](stripe-webhook-test-kit/LAUNCH-LOG.md) |
| Funnel top | Free gotcha article, live on dev.to since 2026-07-12T17:18Z, 4 tags, links to listing 2× | [`LAUNCH-LOG.md`](stripe-webhook-test-kit/LAUNCH-LOG.md) |
| T+7 checkpoint | **2026-07-19** (tomorrow) | [`CATALOG.md`](CATALOG.md) live-listing caveat |
| T+14 kill rule | **2026-07-26** — signal = ≥1 organic sale OR ≥1 qualified inbound, else pause/delist | [`LAUNCH-LOG.md`](stripe-webhook-test-kit/LAUNCH-LOG.md) |
| Agent effort cap | ~50k tokens of launch-support effort per the runbook | [`LAUNCH-LOG.md`](stripe-webhook-test-kit/LAUNCH-LOG.md) |

The funnel is fully wired end-to-end and verified: **dev.to article → Gumroad
listing → checkout → receipt → download**. The owner completed a **discounted
test purchase** on 2026-07-12 that walked checkout → receipt → the 19.4 KB ZIP
download with a working button ([`LAUNCH-LOG.md`](stripe-webhook-test-kit/LAUNCH-LOG.md),
"Owner test purchase — VERIFIED"). So the mechanics are not the problem: a buyer
who reaches the page **can** buy and **will** receive the product. The zero is a
zero of *organic* sales, not of a broken pipe.

---

## What the repo can and cannot see (read this first)

The single most important honesty point for this diagnostic:

> **Sales and views are owner-dashboard-only. Agent surfaces do NOT see them.**
> Gumroad's own analytics (views/sales per product) is the authoritative
> signal, and it is readable only from the owner's dashboard. The only
> agent-visible engagement signal is dev.to's public **reactions / comments**;
> the private article view counter is also owner-dashboard-only.
> — [`LAUNCH-LOG.md`](stripe-webhook-test-kit/LAUNCH-LOG.md), "Measurement plan"
> and "Funnel measurement".

This means the repo contains **no traffic numbers, no view counts, no
click-through data, and no sales count** — not because they are hidden, but
because no analytics is wired to any agent-readable surface. The LAUNCH-LOG is
explicit that the **base case is 0 sales until a distribution channel is wired**,
so "payback is INDEFINITE absent traffic."

Therefore this diagnostic will **not invent a funnel number**. Where a stage is
unmeasured it says so, and names the cheapest way for the owner to measure it.
That is the whole game: most of the funnel is currently *dark*, and the cheapest
next move is almost certainly to **turn on a light**, not to rewrite copy or drop
the price blind.

---

## The three hypotheses, ranked by what the evidence supports

Zero organic sales has exactly three funnel-shaped causes. Ordered by how much
the repo evidence points at each:

```
   article views  →  listing visits  →  purchase
   └─ TRAFFIC ─────┘  └─ COPY ────────┘  └─ PRICE ─┘
      (H1)               (H2)               (H3)
```

A sale requires all three stages to pass. Zero sales means **at least one** stage
is at (or near) zero. Diagnose top-down: a copy or price fix is worthless if no
one reaches the page.

### H1 — TRAFFIC problem (nobody is arriving) — *best supported*

**Claim:** the listing has near-zero qualified visitors, so there is nothing for
copy or price to convert.

**Evidence for:**
- The LAUNCH-LOG names distribution — not inventory or the product — as the
  binding constraint, and states the base case is **0 sales until a distribution
  channel is wired**. The dev.to article is published but the downstream funnel
  (gist → StackOverflow answer → r/stripe) is described as **still
  owner-gated / not yet executed**.
- `CATALOG.md`: "Distribution, not catalog size, is the binding constraint."
- The article's four discovery tags went live and it links to the listing 2×, so
  the *path* exists — but a single dev.to post with no active seeding is a
  low-traffic top.

**What's measured:** the article is live and correctly wired (HTTP 200, tags,
2× product link). **What's NOT measured:** how many people actually read the
article, how many clicked through to Gumroad, and how many landed on the listing.
All three are owner-dashboard-only and currently unread in-repo.

**Cheapest test:** *see the owner-action section, H1.* In one sentence: **read
the two dashboards you already have** before assuming anything else is broken.

### H2 — LISTING-COPY problem (visitors arrive but don't buy) — *cannot be judged without H1*

**Claim:** traffic reaches the page but the copy fails to convert it.

**Evidence for / against:** the listing copy is strong on the honesty axis this
repo prizes — a specific pain ("an order silently disappears"), four concrete
named gotchas (null `customer_email`, forged events, broken `success_url`,
replayable requests), a clear "what it does NOT do" section, and stdlib/no-account
framing ([`LISTING.md`](stripe-webhook-test-kit/LISTING.md)). There is **no
evidence the copy is the blocker** — and equally, no evidence it converts, because
visit and conversion counts are unmeasured.

**Honest note:** you cannot diagnose copy on zero traffic. If H1 shows the page is
getting real visits (say, dozens+) and still zero sales, H2 becomes the live
suspect. Until then, rewriting copy is guessing.

**What's NOT measured:** listing visit count and visit→purchase rate
(owner-dashboard-only).

**Cheapest test:** *see owner-action section, H2* — a one-line title/subtitle A/B
is far cheaper than a full rewrite, and only worth doing once H1 confirms traffic.

### H3 — PRICE problem ($29 is wrong) — *weakest supported, cheapest to test*

**Claim:** visitors reach the page, the copy lands, but $29 is the wrong number.

**Evidence for / against:** $29 is internally consistent everywhere
(`LISTING.md`, `publish-owner-action.md`, and the live page all read `price_cents
2900` — [`LAUNCH-LOG.md`](stripe-webhook-test-kit/LAUNCH-LOG.md) catalog-parity
entry). The repo has a **pricing-experiment spec on the menu** (MISC-2 / R6:
PWYW floor + anchor) but it targets the AI Novella Kit, not this SKU, and there is
**no evidence $29 is too high or too low** — no abandoned-checkout data, no price
objections in any inbound (there is no inbound yet).

**Honest note:** with zero traffic, price is the *least* likely cause and, like
copy, undiagnosable from repo data. But a price test is the **cheapest single
lever** to pull if H1 confirms traffic and H2 doesn't explain the gap: on Gumroad
it is one field edit and (optionally) enabling "pay what you want" with a floor.

**What's NOT measured:** checkout-abandonment / add-to-cart-without-purchase
(owner-dashboard-only, if Gumroad surfaces it at all at this volume).

---

## What the owner would click to test each hypothesis

Owner-action only. Nothing here is auto-executed; an agent cannot read a Gumroad
dashboard, edit a live listing, or change a price — every step is a click the
owner performs. Ordered cheapest-first and top-of-funnel-first. **Do H1 before
touching H2 or H3** — it is the only step that tells you which hypothesis is even
live, and it costs one login.

### H1 — is it traffic? (cheapest; do this first)
1. **Open the Gumroad dashboard** for the Stripe Webhook Test Kit and read two
   numbers: **listing views** and **sales**, since 2026-07-12.
2. **Open the dev.to dashboard** for the gotcha article and read its **view
   count** (private, owner-only) plus public reactions/comments.
3. Read the result off this tiny table:

   | dev.to views | Gumroad listing views | Reading |
   | --- | --- | --- |
   | ~0 | ~0 | **Pure traffic problem (H1).** Nobody is arriving. Fix distribution first; copy/price are moot. |
   | many | ~0 | Article isn't sending clicks — a **funnel-top→listing** problem (still H1-ish: the article hook or its call-to-action, not the listing copy). |
   | — | many, 0 sales | Traffic is fine → **H2/H3 are now live.** Proceed below. |

   *Cost: two logins, ~5 minutes, $0.*
4. If H1 is confirmed (the common case per the LAUNCH-LOG base case), the cheapest
   *fix* is the already-drafted, owner-gated distribution steps — post the free
   article's follow-ons (gist, a StackOverflow answer to a real
   `customer_email is null` question, an r/stripe reply) that the LAUNCH-LOG lists
   as not-yet-executed. That is a distribution action, tracked separately; this
   doc's job is only to point the finger correctly.

### H2 — is it copy? (only if H1 shows real traffic + zero sales)
1. In Gumroad, edit **only the title/subtitle** to lead with the single sharpest
   gotcha ("Your Stripe webhook says `customer_email` is null — catch it before
   you ship") — the article's proven hook — and leave the body untouched.
2. Watch views→sales for a bounded window. *Cost: one field edit, reversible, $0.*
3. Do **not** rewrite the whole description first; the body already meets the
   repo's honesty bar. A headline swap is the cheapest copy test that isolates the
   variable.

### H3 — is it price? (only if H1 shows traffic and H2 doesn't close the gap)
1. In Gumroad, either lower the price by one step **or** enable **pay-what-you-want
   with a floor** (the MISC-2 / R6 pattern: a floor buys first-sale signal without
   giving it away). One field edit, reversible.
2. Watch views→sales for a bounded window. *Cost: one field edit, $0.*
3. A price move is the cheapest single lever but the **least** evidence-supported
   cause — spend it last, and only after traffic is confirmed real.

---

## Bottom line for the T+7 checkpoint

- The funnel **mechanics are proven** (owner test purchase walked the full buyer
  path); zero sales is not a broken pipe.
- The **most-supported cause is H1 (traffic)** — the repo's own stated base case
  is "0 sales until distribution is wired," and the downstream distribution steps
  are drafted but owner-gated / not yet executed.
- **H2 (copy) and H3 (price) cannot be honestly diagnosed** from repo data,
  because listing visits and conversion are owner-dashboard-only and currently
  unread. Rewriting copy or cutting price *before* reading the dashboard is
  guessing.
- **Cheapest next action:** the owner reads the two dashboards (H1 step 1–3),
  ~5 minutes, $0. That one read collapses three hypotheses to one and tells the
  T+14 kill-rule call (2026-07-26) whether the honest verdict is *"never got
  traffic — try the drafted distribution steps"* or *"got traffic, didn't
  convert — then test copy, then price."*

Feed this into the **MISC-3 live-SKU kill-clock decision packet** when it lands:
this doc is the *diagnosis*, MISC-3 is the *keep / iterate / delist decision* the
diagnosis informs.

---

## Provenance

Derived, not invented — no fabricated metrics, no invented traffic or sales
numbers. Where a funnel number is absent it is marked "not measured
(owner-dashboard-only)" rather than estimated. Sources:

- Live-SKU facts, price, launch timestamps, kill rule, measurement plan, test
  purchase, "0 sales base case" —
  [`stripe-webhook-test-kit/LAUNCH-LOG.md`](stripe-webhook-test-kit/LAUNCH-LOG.md).
- Live status, kill-clock dates, "distribution is the binding constraint" —
  [`CATALOG.md`](CATALOG.md) live-listing caveat.
- Listing copy under diagnosis —
  [`stripe-webhook-test-kit/LISTING.md`](stripe-webhook-test-kit/LISTING.md) and
  [`stripe-webhook-test-kit/one-pager.md`](stripe-webhook-test-kit/one-pager.md).
- Kill-clock checker + T+7/T+14 semantics —
  `scripts/check_kill_clocks.py` (per `.sessions/2026-07-13-night-killclock-advisory.md`).
- DIST-3 / REV-2 spec —
  [`../ideas/2026-07-18-veto-ready-menu.md`](../ideas/2026-07-18-veto-ready-menu.md).
- Pricing-experiment pattern referenced for H3 — MISC-2 / R6 in the same menu.
