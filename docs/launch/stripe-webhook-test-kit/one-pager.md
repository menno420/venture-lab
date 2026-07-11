# Stripe Webhook Test Kit v0.1 — one-pager (internal)

> **Status:** `reference`

**Product:** Stripe Webhook Test Kit v0.1 — a stdlib-only dev tool that fires
real-shape signed Stripe events at a developer's local webhook endpoint and flags
the gotchas that silently lose orders. **$29 one-time.**

**One-line pitch:** Test your Stripe webhook handler against the event shapes
Stripe really sends — before you ship and silently drop sales.

## The four checks it runs

1. **fire** — the handler ACCEPTS a correctly-signed real event (HTTP 2xx).
2. **fire --forge** — the handler REJECTS a forged/badly-signed event (HTTP 4xx),
   proving signature verification is actually running.
3. **check-email** — the buyer email is read from `customer_details.email`;
   top-level `customer_email` is `null` on a normal Checkout completion.
4. **lint-url** — the `success_url` uses ONLY `{CHECKOUT_SESSION_ID}`; any other
   placeholder is passed through to the buyer's browser verbatim.

## What it does NOT do (honest)

- Does not talk to the real Stripe API, the developer's database, or any live account.
- Does not validate business logic — only the webhook edge behaviour.
- Not a "battle-tested payments" library, and not a substitute for Stripe's own
  CLI `stripe listen`. It checks the specific real-shape gotchas (null
  `customer_email`, invalid `success_url` placeholder, missing signature
  verification, timestamp tolerance) that repeatedly break first integrations.

## Free-article funnel plan (all steps are owner clicks, ⚑ — none queued)

1. ⚑ Free technical article: "Your Stripe webhook says customer_email is null —
   here's why (and the fix)" on dev.to / Hashnode. Draft lives at
   `docs/launch/stripe-webhook-test-kit/gotcha-article.md`.
2. ⚑ Free public gist / GitHub repo mirror of `GOTCHAS.md`.
3. ⚑ Answer the canonical StackOverflow question ("Stripe checkout
   customer_email null") with the fix + a soft link.
4. ⚑ Gumroad / Lemon Squeezy $29 listing (copy in `LISTING.md`, bundle in
   `dist/stripe-webhook-test-kit-v0.1.zip`).
5. ⚑ r/stripe + r/SaaS posts.

None of these are queued. The publish click is earned only after the v0.1
real-path HTTP test is green in CI against the vendored fixtures and the
coordinator reviews the evidence (see `publish-owner-action.md`).

## Conservative revenue

- $29 one-time. Conservative first-90-day: **0–5 sales ($0–$145).**
- Zero distribution = **$0**. Revenue depends entirely on the owner-gated seeding
  landing search traffic.

## Validation signal (from intake)

Within 14 days / 3 owner-click steps of the free gotcha article going live, ≥1 of:
(a) the article draws ≥50 organic visits, (b) ≥3 saves/stars on the free gist or
repo mirror, or (c) the first paid sale. No signal by the budget cap =
**ledgered negative.**
