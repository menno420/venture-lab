# Webhook Verifier Bundle — v0.1

Four small, stdlib-only, account-free **webhook signature verifier kits** in one
download — the Stripe, GitHub, Slack, and Shopify test kits — bundled at a
discount. Each kit proves you are verifying a provider's webhook signature
*correctly* (right algorithm, right signed bytes, right comparison), with
real-shape fixtures and an HTTP-layer test suite you can run in one command with
no vendor account and no secrets.

**Price:** **$79** for all four — versus **$116** bought separately (4 × $29).
That is **$37 off (~32%)**. See [`PROVENANCE.md`](PROVENANCE.md) for the pricing
math and the per-kit artifact pins.

> **What you download:** one zip that contains the four component kits' own
> buyer bundles (their exact `*-v0.1.zip` files, byte-for-byte — pinned by
> sha256 in [`MANIFEST.json`](MANIFEST.json)) plus this README, the
> [`QUICKSTART.md`](QUICKSTART.md), and [`PROVENANCE.md`](PROVENANCE.md). Unzip,
> then unzip whichever kit you need — each is self-contained and documented.

---

## What's included

### 1. Stripe Webhook Test Kit ($29 alone · already LIVE)

Verifies Stripe's `Stripe-Signature` header: the `t=` timestamp and `v1=`
scheme, where the signature is `HMAC-SHA256(signing_secret, "{t}.{raw_body}")`
compared in constant time, with a tolerance window against replay. Ships the
real signed-payload fixtures, a correct example handler, and an HTTP real-path
test suite (true-pass, tamper-fail, wrong-secret-fail, stale-timestamp-fail).
The one kit in the set that is **already live** on Gumroad.

### 2. GitHub Webhook Test Kit ($29 alone)

Verifies GitHub's `X-Hub-Signature-256` header: `sha256=` + hex of
`HMAC-SHA256(webhook_secret, raw_body)`, constant-time compared, signed over the
raw request body with no timestamp. Ships real `push` / `pull_request` / `ping`
fixtures, the delivery-header shape, a correct handler, and the HTTP real-path
suite (true-pass, tamper-fail, wrong-secret-fail, malformed-signature-fail).

### 3. Slack Webhook Test Kit ($29 alone)

Verifies Slack's `X-Slack-Signature` header: `v0=` + hex of
`HMAC-SHA256(signing_secret, "v0:{X-Slack-Request-Timestamp}:{raw_body}")`,
constant-time compared, with a 5-minute timestamp window against replay. Ships
real slash-command / event / interactive fixtures, a correct handler, and the
HTTP real-path suite (true-pass, tamper-fail, wrong-secret-fail,
stale-timestamp-fail).

### 4. Shopify Webhook Test Kit ($29 alone)

Verifies Shopify's `X-Shopify-Hmac-Sha256` header: **base64** (not hex) of
`HMAC-SHA256(client_secret, raw_body)`, constant-time compared, signed over the
raw body with no timestamp basestring. Ships real `orders/create` /
`products/update` / `app/uninstalled` fixtures, a correct handler, and the HTTP
real-path suite (true-pass, tamper-fail, wrong-secret-fail,
malformed-base64-fail).

---

## Why these four together

Every one of these providers signs its webhooks with an HMAC-SHA256 keyed by a
shared secret — but they disagree on **the three things that actually break
integrations**: what bytes get signed (raw body only vs. a timestamped
basestring), how the digest is encoded (hex vs. base64), and whether there is a
replay window. A team wiring up more than one provider hits the same class of
bug four different ways. Buying the set gives you the correct reference and a
runnable tamper/replay test for each, so "did I verify the signature right?"
stops being a guess.

Same honest v0.x scope as the individual listings: these are **verifier test
kits**, not full webhook frameworks. They prove signature handling against
real-shape fixtures; they do not host your endpoint or manage delivery retries.

## Honesty notes

- The four component kits are **not modified** by this bundle. You receive each
  kit's own published buyer zip, pinned by sha256 in `MANIFEST.json`. If a kit
  is later revised, the bundle is re-cut against the new pin.
- Only the **Stripe** kit is live today. This bundle is a storefront **discount
  SKU** over the four kits; on Gumroad it can only be created once its component
  products are all published (see the owner gate in the vetting packet). The
  download works standalone regardless — the four kits inside it are complete.
- There is **zero new product code** here: the bundle is an assembly of four
  already-built, already-tested kits plus this documentation. The test in this
  directory is an **assembly/inventory check**, not a fifth product test suite —
  each kit's own suite ships inside its zip and runs the same way it always has.
