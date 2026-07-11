# Membership-Site Boilerplate Kit — listing copy

> **Status:** `reference`

Ready-to-paste copy for a Gumroad / Lemon Squeezy / Stripe-payment-link product page. Each block below is meant to be copied as-is into the matching storefront field.

## Title
```
Membership-Site Boilerplate Kit — paid membership loop, zero frameworks
```

## Short description (≤ 200 chars)
```
A stdlib-only Python starter for paid memberships: pre-wired payment → membership → gated-access loop, runs in mock mode with zero accounts. v0.x — Stripe path pre-wired, not yet live-tested.
```

## Long description
```
The Membership-Site Boilerplate Kit is a small, honest starting point for a paid-membership site. It ships a stdlib-only Python http.server backend, a static landing page, and a gated members-area stub — with the payment → membership → gated-access loop already wired together. Run it in mock mode with zero accounts to watch the whole loop work before you connect anything.

Under the hood the membership-grant logic, the deny-when-unpaid 402 gate, idempotent duplicate-purchase handling, and JSON file persistence are all unit-tested. Stripe Checkout and its webhook handler are included and pre-wired to that logic. Brand tokens live in JSON, so you can reskin without touching the code.

This is an honest v0.x. The live Stripe path has not been through a live purchase — connecting a real Stripe test-mode account and running an end-to-end purchase is your next step, not something this kit claims to have verified. No tested-payments claim is made here. You get the code, you own it, you finish the last mile.
```

## Bullets
```
- Stdlib-only Python — no web framework, no dependency tree to audit
- Runs in mock mode with zero accounts, so you see the loop before wiring Stripe
- Stripe Checkout + webhook handler included and pre-wired to the grant logic
- Deny-when-unpaid 402 gate on the members area (unit-tested)
- Idempotent purchases — a repeated webhook never double-grants (unit-tested)
- Unit-tested membership-grant logic and restart-surviving JSON persistence
- Brand tokens as JSON — reskin without editing logic
- Small and agent-buildable — extend it in a single agent session
```

## FAQ
```
Q: Is the Stripe payment path live-tested?
A: No. The Stripe Checkout + webhook code is included and pre-wired, and the membership-grant logic it drives is unit-tested — but the live Stripe path has not been through a live purchase. Running a real test-mode purchase end to end is your next step. This kit makes no tested-payments claim.

Q: What do I get?
A: The membership-kit-v0.2.zip: the stdlib-only backend, the static landing page, the gated members stub, the pre-wired Stripe Checkout + webhook code, brand-token JSON, and the unit tests for the grant logic.

Q: Refunds?
A: [Owner to set refund policy — placeholder.]

Q: License?
A: Single-project starter license. Note this is a v0.x release — treat it as a starting point you finish and own, not a finished product.

Q: Support?
A: Best-effort, community-level. This is a starter kit, not a managed service.
```
