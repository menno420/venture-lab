# Session — ORDER 003: fix the real Stripe path (D1/D2/D3)

> **Status:** `in-progress`

- **📊 Model:** claude-opus-4.8 · high · payment-path remediation
- **session:** ORDER 003 (P0) — unfreeze ⚑B/⚑D by making the $49 membership-kit Stripe path survive a REAL purchase
- **started (date -u):** Sat Jul 11 00:58:55 UTC 2026

## ⟲ Previous-session review

Previous-session review: the prior kit-upgrade waves (PR #13/#14) vendored substrate-kit v1.7.1 but never touched the payment path. ORDER 004 (PR #15) repaired control-bus state and marked ⚑B/⚑D FROZEN. The D1 lesson (binding forever): the $49 kit's "Stripe pre-wired" headline had 13 green tests that injected checkout events synthesized from memory — real `checkout.session.completed` events carry `customer_email: null` with the buyer address at `customer_details.email`, and the success-URL used the invalid `{CHECKOUT_EMAIL}` placeholder (Stripe expands `{CHECKOUT_SESSION_ID}` only). This session fixes the real path and proves it with HTTP-layer tests against VENDORED real Stripe payloads.

## 💡 Session idea

Payment code cannot be verified by payloads authored from memory. Vendor a real Stripe `checkout.session.completed` fixture, drive the actual `/webhook` HTTP route with it (plus a natively-computed valid Stripe-Signature so the signature path is exercised without live keys), and assert a membership grant. A green test that never hit the real event shape is a bug in the test.

## Scope (ORDER 003)

- D1a: grant path reads `customer_details.email` (real events have `customer_email: null`); pass buyer email into the Checkout Session at creation.
- D1b: replace `{CHECKOUT_EMAIL}` success-URL with `{CHECKOUT_SESSION_ID}`.
- HTTP-layer real-path tests with vendored payloads + Stripe signature verification; cover buyer-facing routes.
- D2: buyer-zip README refreshed to v0.2 reality.
- D3: loud MOCK-mode warning without real keys.
- Rebuild both buyer zips via package.sh; commit dists.

## Work log

(in progress)
