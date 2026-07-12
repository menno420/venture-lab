# 2026-07-12 — SWTK live verification (⚑A, real signing secret)

> **Status:** `red` (in-progress)

⚑A LIVE verification of the Stripe Webhook Test Kit against a REAL Stripe-issued
webhook signing secret (`SWTK_WEBHOOK_SECRET`, owner-placed in the env panel this
launch), firing real-shape signed events at the bundled handler locally.

📊 Model: opus-4.8

## Acceptance test (OWNER-LAUNCH-HOUR.md §1 ⚑A VERIFIED-WHEN)

> `SWTK_WEBHOOK_SECRET` is present in the env panel / local `.env` (value never
> in-repo) AND a signed test-mode `checkout.session.completed` fired at the
> handler returns **HTTP 200**.

Both conditions met — evidence below.

## Evidence (no secret values — env var NAME only)

- **HEAD at run:** `d7896f0285b34ef72a81699050cce5f7df35868b` (hard-synced
  `git fetch origin main && git reset --hard origin/main`; verified
  `git ls-remote origin main` == `git rev-parse HEAD` == `d7896f0`).
- **Secret presence (masked):** `SWTK_WEBHOOK_SECRET: present (len 38)`
  (`[ -n "$SWTK_WEBHOOK_SECRET" ] && echo "present (len $(printf %s "$SWTK_WEBHOOK_SECRET" | wc -c))"`).
  The value never entered a command line, log, card, or commit.

### Live fire (in `candidates/stripe-webhook-test-kit/`)

Handler started reading the secret from env:
`python3 stub_handler.py 8000 &`

1. **Valid signed `checkout.session.completed`** —
   `python3 swtk.py fire --url http://localhost:8000/webhook --fixture checkout_session_completed`
   → **HTTP 200**, `{"received": true, "type": "checkout.session.completed", "buyer_email": "ada.lovelace@example.com"}`.
   `PASS: handler accepted the correctly-signed event.` (exit 0). Buyer email
   resolved from `customer_details.email` (top-level `customer_email` is null) —
   the kit's headline gotcha, on a real-secret-signed event.
2. **Forged signature (negative)** —
   `python3 swtk.py fire ... --fixture checkout_session_completed --forge`
   → **HTTP 400** `{"error": "no matching v1 signature"}`.
   `PASS: handler rejected the forged event (signature verification is working).`
3. **Stale timestamp (negative)** —
   `python3 swtk.py fire ... --fixture checkout_session_completed --timestamp 100000000`
   → **HTTP 400** `{"error": "timestamp outside tolerance (300s)"}`. Handler
   correctly rejected the out-of-tolerance event (the CLI prints its default-path
   "expected 2xx" FAIL line, but a 400 rejection is the correct negative
   behaviour — see the `test_stale_timestamp_rejected` suite assertion).

Handler killed after the run.

### Kit real-path suite

`python3 -m unittest test_http_realpath -v` → **Ran 14 tests in 3.031s / OK**
(exit 0). Every event signed with the real `Stripe-Signature` scheme and POSTed
over real HTTP to a handler on an ephemeral port, using the same real
`SWTK_WEBHOOK_SECRET` now in the env. Negative legs inside the suite:
`test_forged_signature_rejected_by_correct_handler` ok,
`test_stale_timestamp_rejected` ok, `test_kit_flags_insecure_handler` ok.
(Only harmless `ResourceWarning: unclosed socket` notices — no failures.)

## Honest boundary (do NOT overclaim)

This verifies the kit against a **REAL Stripe-issued webhook signing secret** with
**real-shape signed events fired LOCALLY** at the bundled handler (and its own
suite). A **Stripe-server-originated delivery** — an event pushed from Stripe's
infrastructure via the Stripe CLI (`stripe listen`) or a public endpoint — remains
a **separate, optional** step. It is NOT claimed here. What is closed: the kit's
signature/timestamp/email-resolution edge behaviour is proven against a genuine
signing secret, not a self-authored one.

## Remaining OWNER steps (from OWNER-LAUNCH-HOUR.md)

- **⚑E — publish the kit** at $29 (Gumroad/Lemon Squeezy), upload
  `dist/stripe-webhook-test-kit-v0.1.zip`, paste `LISTING.md` copy; VERIFIED-WHEN
  the live listing URL returns HTTP 200 on a purchasable $29 page (T+14 kill
  clock starts here).
- **First-sale verification** — after a real buyer purchases: Dashboard shows a
  succeeded $29 charge; the webhook event log shows `checkout.session.completed`
  delivered 200; buyer email resolves from `customer_details.email`; success
  redirect used `{CHECKOUT_SESSION_ID}` only; buyer received the download.
- **⚑ (funnel) — publish the free gotcha article**
  (`docs/launch/stripe-webhook-test-kit/gotcha-article.md`) — the validation
  clock starts at article publish.
