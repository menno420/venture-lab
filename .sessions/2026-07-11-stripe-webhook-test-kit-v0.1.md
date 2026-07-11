# Session — Stripe Webhook Test Kit v0.1

> **Status:** `in-progress`

- **📊 Model:** claude-opus-4.8 · high · revenue-lane candidate build
- **session:** Build Stripe Webhook Test Kit v0.1 ($29) — fresh vendored real Stripe fixtures + stdlib HTTP-layer harness + tests + zip; reuse zero membership-kit code.
- **started (date -u):** 2026-07-11 (born-red first commit)

## ⟲ Previous-session review

Previous-session review: ORDER 003 proved the real Stripe path in candidates/membership-kit/server (customer_email null → customer_details.email; {CHECKOUT_SESSION_ID}-only success URL; stdlib t=,v1= HMAC-SHA256 signature verification; vendored real payloads + PROVENANCE; HTTP-layer real-path tests). This candidate packages those PAID-FOR lessons as a standalone dev tool — writing FRESH code and FRESH vendored fixtures, reusing zero membership-kit bytes.

## 💡 Session idea

Sell the gotchas this lane already paid to learn: a stdlib test harness that fires REAL-shape signed Stripe events at a dev's local webhook endpoint and flags the customer_email-null trap and invalid success-URL placeholders — the exact bugs that cost the $49 kit its first launch.

## Scope

- Fresh vendored real Stripe payload fixtures + PROVENANCE (verified vs stripe-go SDK).
- Stdlib Python harness (+ JS port): signs fixtures with real HMAC-SHA256 Stripe-Signature, fires at a local endpoint, pass/fail output; customer_email-null gotcha check; success-URL placeholder lint.
- HTTP-layer real-path test suite (harness → stub handler).
- README, launch one-pager + listing + NOT-QUEUED publish OWNER-ACTION, free gotcha article.
- package.sh → dist/stripe-webhook-test-kit-v0.1.zip; verify suite runs from inside the extracted zip.

## Work log

(in progress — filled at close-out)
