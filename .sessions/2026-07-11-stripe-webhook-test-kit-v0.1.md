# Session — Stripe Webhook Test Kit v0.1

> **Status:** `complete`

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

- **Built:** `candidates/stripe-webhook-test-kit/` — stdlib harness `swtk.py` (Python) + `swtk.js` (Node port, same four subcommands `fire`/`check-email`/`lint-url`/`list`, hand-rolled arg parsing, zero deps); example correct handler `stub_handler.py` (real `t=,v1=` HMAC-SHA256 verification, 300s tolerance, `customer_details.email` → `customer_email` fallback); `package.sh` → deterministic `dist/stripe-webhook-test-kit-v0.1.zip`.
- **Vendored:** three FRESH real-shape fixtures with their own `fixtures/PROVENANCE.md` (field names verified vs stripe-go SDK; signature scheme vs `webhook/client.go`): `checkout_session_completed.json` (null top-level `customer_email`, buyer email in `customer_details.email`), `checkout_session_completed_legacy_email.json` (legacy/guest path, top-level `customer_email` populated, `customer_details` null), `payment_intent_succeeded.json`. Reused zero membership-kit bytes. No real customer data or secrets — signing secret read from env NAME only.
- **Tests:** `test_http_realpath.py` — HTTP-layer real-path suite; every event signed with the real Stripe-Signature scheme and POSTed over actual HTTP to a handler on an ephemeral port. In-repo run: **Ran 14 tests ... OK** (all green).
- **Packaging:** `sh package.sh` built the 12-file zip (harness Py+JS, handler, tests, fixtures + PROVENANCE, README, GOTCHAS). Verified from INSIDE the extracted zip: **Ran 14 tests ... OK**, and `node swtk.js list` lists the 3 fixtures.
- **Adversarial verification:** suite includes forged-signature rejection (correct handler → 400), an insecure-handler-accepts-forgery case the kit's `forged_fire_pass` verdict correctly marks FAIL, stale-timestamp rejection (outside 300s tolerance → 400), and an independent HMAC recomputation cross-check of the signature bytes. JS `lint-url {CHECKOUT_EMAIL}` exits non-zero as required.
- **Verified vs unverified:** VERIFIED — the harness fires correctly-signed and forged real-shape events over real HTTP and the 14-test suite is green both in-repo and from the built zip; fixture field NAMES/types are SDK-verified. UNVERIFIED — fixture VALUES (ids, example.com emails, amounts, timestamps) are illustrative, not captured from a live account; no contact with the live Stripe API, and no marketplace publish (that click is NOT-QUEUED, earned only after CI-green + coordinator review).
