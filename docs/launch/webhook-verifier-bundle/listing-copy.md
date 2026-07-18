# Webhook Verifier Bundle ($79) — listing copy

> **Status:** `reference`
>
> Ready-to-paste copy for a **Gumroad bundle** of the four webhook verifier
> kits (Stripe + GitHub + Slack + Shopify, $29 each). **HARD-GATED:** a Gumroad
> bundle references its component products as existing live products — it cannot
> be created until the not-yet-published component kits are live. Stripe is
> already LIVE; the gate is on the GitHub ($29, OWNER-QUEUE **D6**), Slack ($29,
> **D20**), and Shopify ($29, **D19**) publish clicks. The buyer artifact is the
> bundle zip (`webhook-verifier-bundle-v0.1.zip`, sha256
> `28f61d8a33309310640375581ff7a6d2f1320bc03bdecbbc1c08c83d5aaf26c8`) which
> contains the four component buyer zips verbatim; per-component pins are in the
> [§7 packet](../../publishing/vetting/webhook-verifier-bundle.md) §1 /
> [`candidates/webhook-verifier-bundle/MANIFEST.json`](../../../candidates/webhook-verifier-bundle/MANIFEST.json).

## Title
```
Webhook Verifier Bundle — Stripe + GitHub + Slack + Shopify Test Kits
```

## Short description (≤ 200 chars)
```
All four webhook signature verifier kits — Stripe, GitHub, Slack, Shopify — for $79 instead of $116 separately. Stdlib-only, account-free, one command to run each kit's tests. $37 off.
```

## Long description
```
Every one of these providers signs its webhooks with an HMAC-SHA256 keyed by a shared secret — but they disagree on the three things that actually break integrations: what bytes get signed (the raw body alone, or a timestamped basestring), how the digest is encoded (hex vs. base64), and whether there's a replay window. Wire up more than one provider and you hit the same class of bug four different ways.

This bundle is all four verifier test kits in one download:

- Stripe — Stripe-Signature: t= timestamp + v1= HMAC-SHA256(secret, "{t}.{body}"), constant-time, replay window. (Already live.)
- GitHub — X-Hub-Signature-256: sha256= hex of HMAC-SHA256(secret, raw body), no timestamp.
- Slack — X-Slack-Signature: v0= hex of HMAC-SHA256(secret, "v0:{ts}:{body}"), 5-minute window.
- Shopify — X-Shopify-Hmac-Sha256: base64 (not hex) of HMAC-SHA256(secret, raw body), no timestamp.

Each kit ships real-shape fixtures, a correct example handler, a GOTCHAS list of the mistakes that silently pass a naive verifier, and an HTTP real-path test suite you run in one command — true-pass plus the tamper / wrong-secret / (replay or malformed) rejection cases. No vendor account, no API key, no network.

Same honest v0.x scope as the individual listings: these are verifier test kits, not full webhook frameworks. They prove your signature handling is correct against real-shape payloads; they don't host your endpoint or manage delivery retries. Nothing here is hype.
```

## Bullets
```
- All four webhook verifier kits — Stripe, GitHub, Slack, Shopify — one download, $79 vs $116 bought separately ($37 / ~32% off)
- Each kit: real-shape fixtures + correct example handler + GOTCHAS + a one-command HTTP real-path test suite (true-pass, tamper-fail, wrong-secret-fail, replay/malformed-fail)
- Covers the three things that break webhook verification: signed bytes (raw vs. timestamped basestring), encoding (hex vs. base64), and replay windows
- Stdlib-only Python (with a JS parity port alongside) — no account, no API key, no network, no dependencies
- Each artifact pinned by sha256; the bundle contains the four kits' own published zips verbatim
```

## FAQ
```
Q: Can I buy just one kit?
Yes — each is sold separately at $29 (Stripe is live; GitHub / Slack / Shopify are their own listings). The bundle is for people wiring up more than one provider; it saves $37 and three checkouts.

Q: What exactly do I download?
One zip that contains the four component kits' own buyer zips (byte-for-byte, sha256-pinned) plus a README, QUICKSTART, and MANIFEST. Unzip the bundle, then unzip whichever kit you need — each is self-contained.

Q: Do the kits depend on each other?
No. Each kit is standalone and provider-specific. They pair only in the sense that a team integrating several providers wants the correct reference and a runnable tamper test for each.

Q: Are these full webhook frameworks?
No — they're verifier test kits. They prove signature handling is correct against real-shape fixtures. Honest v0.x scope, same as the individual listings.
```
