# Marketplace listing copy — Stripe Webhook Test Kit v0.1

> **Status:** `reference`

**Title:** Stripe Webhook Test Kit — catch the gotchas before you ship

**Subtitle:** Fire real-shape signed Stripe events at your local webhook endpoint
and prove your handler behaves. Stdlib only. No account, no dependencies.

**Price:** $29 (one-time)

## Description

Most Stripe webhook bugs don't show up in a happy-path test — they show up in
production, when a real `checkout.session.completed` event arrives shaped slightly
differently than you assumed, and an order silently disappears.

The Stripe Webhook Test Kit signs vendored, real-shape Stripe events with the
actual `Stripe-Signature` scheme and fires them over HTTP at your local endpoint,
then checks your handler the way Stripe actually behaves. It catches the four
gotchas that repeatedly break first Stripe integrations:

- **Buyer email is `null`.** On a normal Checkout completion the top-level
  `customer_email` is `null` — the address lives in `customer_details.email`. Read
  the wrong field and you drop the sale.
- **Forged events accepted.** If your handler skips signature verification, anyone
  who knows your endpoint URL can post fake events. The kit fires a forged event and
  checks you reject it.
- **Broken `success_url`.** Stripe only expands `{CHECKOUT_SESSION_ID}`. Any other
  placeholder reaches the buyer's browser verbatim. The kit lints for it.
- **Replayable requests.** The kit checks your handler enforces the 300-second
  timestamp tolerance.

Runs in Python or Node, entirely from the standard library. No `pip install`, no
`npm install`, no Stripe account required to run the tests.

## What's inside

- The harness in two languages: `swtk.py` (Python) and `swtk.js` (Node), same four
  commands.
- An example correct webhook handler (`stub_handler.py`) you can adapt.
- Vendored real-shape Stripe fixtures + `PROVENANCE.md` documenting exactly how
  every field was verified against Stripe's own SDK source.
- An HTTP-layer real-path test suite (`test_http_realpath.py`) — every event is
  signed and POSTed over real HTTP.
- A one-page `GOTCHAS.md` checklist.

## Requirements

- Python 3.8+ or Node 14+.
- No Stripe account, no dependencies, no build step.
- Your webhook signing secret is read from an environment variable — no secret
  values are stored in the kit.

## What it does NOT do (so you know what you're buying)

- It does not talk to the real Stripe API, your database, or any live account.
- It does not validate your business logic — only the webhook edge behaviour.
- It is not a "battle-tested payments" library, and not a replacement for Stripe's
  own CLI (`stripe listen`). It is a focused checker for the specific real-shape
  gotchas above.
