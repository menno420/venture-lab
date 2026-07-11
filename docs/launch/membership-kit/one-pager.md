# Membership-Site Boilerplate Kit — one-pager

> **Status:** `reference`

## What it is
A stdlib-only Python `http.server` backend plus a static landing page and a gated members-area stub. The payment → membership → gated-access loop is pre-wired end to end. It runs in mock mode out of the box with zero accounts and zero external services, so you can see the whole loop before touching Stripe.

## Who it's for
Indie devs and agent builders who want a paid-membership starting point without adopting a web framework. If you want to own the code, not learn a framework, this is the floor you build up from.

## What's real today
- Membership-grant logic — unit-tested.
- Deny-when-unpaid 402 gate on the members area — unit-tested.
- Idempotent duplicate-purchase handling (a repeated webhook does not double-grant) — unit-tested.
- JSON file persistence that survives a restart — unit-tested.
- Stdlib-only: no framework, no package tree to audit.
- Brand tokens as JSON (name, colors, copy) so you can reskin without editing logic.
- Agent-buildable: small enough to extend with an agent session.

## What's NOT done yet (honest v0.x)
The live Stripe path has not been through a live purchase. Stripe Checkout + webhook code is included and pre-wired, but live-Stripe test-mode E2E, Discord invite delivery, and Supabase-backed persistent users are documented, owner-run next steps — not verified. Do not treat payments as battle-tested.

## Price
$49 one-time (lifetime updates to the v0.x line).

## Conservative revenue expectation
Conservative expectation: 0–2 sales/month with no active distribution; the first month may well be $0. One sale ≈ $49 gross, ≈ $44 net after typical marketplace fees. The market-source '$20K/7-days' headline is unproven — it showed no on-screen revenue evidence — so treat first revenue as unproven until a real sale lands.

## Files shipped
`candidates/membership-kit/dist/membership-kit-v0.2.zip`.
