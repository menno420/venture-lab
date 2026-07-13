# Membership-Site Boilerplate Kit — listing copy

> **Status:** `reference`

Ready-to-paste copy for a Gumroad / Lemon Squeezy / Stripe-payment-link product page. Each block below is meant to be copied as-is into the matching storefront field. Refreshed 2026-07-13 to v0.2 reality (HTTP-layer real-path verification landed; the earlier "not yet live-tested" copy undersold what is now tested and oversimplified what is not). Price: **$49 one-time** (precedent: `owner-actions.md` ⚑B, `candidates/membership-kit/LISTING.md`).

## Title
```
Membership-Site Boilerplate Kit — paid membership loop, zero frameworks
```

## Short description (≤ 200 chars)
```
Stdlib-only Python starter for paid memberships: checkout → webhook → grant → gated access, pre-wired, tested against real-shape Stripe payloads over HTTP. Mock mode by default: zero accounts.
```

## Long description
```
The Membership-Site Boilerplate Kit is a small, honest starting point for a paid-membership site. It ships a stdlib-only Python http.server backend, a static landing page, and a gated members-area stub — with the payment → membership → gated-access loop already wired together. Run it in mock mode with zero accounts to watch the whole loop work before you connect anything; the server prints a loud MOCK-MODE banner so you always know no real money is moving.

The webhook path is not "pre-wired and hope": it is exercised at the HTTP layer against vendored, real-shape Stripe checkout.session.completed payloads (provenance documented in the bundle), with native HMAC-SHA256 Stripe-Signature verification, timestamp-tolerance enforcement, and forged-signature rejection — the gotchas that break first Stripe integrations. It reads the buyer's email from customer_details.email (the field real events actually populate), uses only the {CHECKOUT_SESSION_ID} placeholder Stripe supports, and fails CLOSED if you set your Stripe key but forget the webhook secret — a misconfigured deploy rejects unsigned webhooks instead of minting free memberships. 36 tests ship in the bundle and run with plain python3 -m unittest.

Under the hood: unit-tested membership grants, a deny-when-unpaid 402 gate, idempotent duplicate-purchase handling, restart-surviving JSON persistence by default, and an optional Supabase (PostgREST) store — stdlib urllib, tested against a stub PostgREST, falling back loudly to JSON when keys are absent. Brand tokens live in JSON, so you can reskin without touching the code.

This is an honest v0.2. The code path is HTTP-tested against real-shape payloads, but it has not been through a live purchase on a live Stripe account — connecting your own Stripe test-mode account and running an end-to-end purchase is your first step after download, not something this kit claims to have done for you. You get the code, you own it, you finish the last mile.
```

## Bullets
```
- Stdlib-only Python — no web framework, no pip install, no dependency tree to audit
- Runs in mock mode with zero accounts — loud MOCK-MODE banner, no silent fake successes
- Webhook path HTTP-tested against vendored real-shape Stripe payloads (provenance included)
- Native Stripe-Signature verification: HMAC-SHA256, timestamp tolerance, forged events rejected
- Fails closed on misconfiguration — Stripe key without webhook secret rejects unsigned grants
- Deny-when-unpaid 402 gate + idempotent purchases (a repeated webhook never double-grants)
- JSON persistence by default; optional Supabase store, tested, with loud fallback
- 36 bundled tests run with python3 -m unittest; brand tokens as JSON for no-code reskins
```

## FAQ
```
Q: Is the Stripe payment path live-tested?
A: The webhook path is tested at the HTTP layer against vendored real-shape Stripe payloads with real signature verification — but no live purchase on a live Stripe account has been run. Your first step after download is a Stripe test-mode purchase end to end. This kit makes no live-payments claim.

Q: What do I get?
A: The membership-kit-v0.2.zip: the stdlib-only backend, the static landing page, the gated members stub, the pre-wired Stripe Checkout + webhook code, vendored Stripe fixtures with their provenance notes, brand-token JSON, and the full 36-test suite (grant logic, HTTP real-path, Supabase store).

Q: What does it NOT do?
A: It does not talk to live Stripe, Supabase, or Discord until you paste your own keys; it is not a hosted service; and it is not a "battle-tested payments" library — it is a wired, tested starting point you finish and own.

Q: Refunds?
A: [Owner to set refund policy — placeholder.]

Q: License?
A: Single-project starter license. Note this is a v0.x release — treat it as a starting point you finish and own, not a finished product.

Q: Support?
A: Best-effort, community-level. This is a starter kit, not a managed service.
```
