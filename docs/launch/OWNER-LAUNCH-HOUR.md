# OWNER LAUNCH HOUR — Stripe Webhook Test Kit ($29)

> **Status:** `owner-guidance`

**STATUS: QUEUED (2026-07-11)**

One atomic ~1-hour runbook for the owner to take the $29 Stripe Webhook Test Kit
from "built + verified in-repo" to "first external revenue." It consolidates the
three standing owner rows for this candidate — ⚑A (add Stripe keys), ⚑E (publish
the kit), and first-sale verification — into a single sequence the owner runs
end-to-end. **No agent publishes, spends, or creates an account; the owner
performs every click.** This packet does not duplicate the ⚑E click-script — it
links to [`stripe-webhook-test-kit/publish-owner-action.md`](stripe-webhook-test-kit/publish-owner-action.md)
for the marketplace detail and builds the launch sequence around it.

---

## Evidence / gates

**Fresh at-HEAD real-path run (this slice, 2026-07-11).** The kit's real-path
HTTP suite was re-run at HEAD against the VENDORED real-shape Stripe payload
fixtures — every event is signed with the real `Stripe-Signature` scheme and
POSTed over real HTTP to a handler on an ephemeral port. Trimmed but faithful
excerpt (`python3 -m unittest test_http_realpath -v` in
`candidates/stripe-webhook-test-kit/`):

```
test_checkout_fixture_has_null_top_level_email ... ok
test_forged_signature_rejected_by_correct_handler ... ok
test_kit_flags_insecure_handler ... ok
test_legacy_event_accepted_via_fallback ... ok
test_legacy_fixture_uses_top_level_email ... ok
test_lint_accepts_session_id_placeholder ... ok
test_lint_rejects_checkout_email_placeholder ... ok
test_payment_intent_event_accepted ... ok
test_payment_intent_fixture_shape ... ok
test_resolve_email_legacy_fallback ... ok
test_resolve_email_prefers_customer_details ... ok
test_signature_matches_independent_hmac ... ok
test_stale_timestamp_rejected ... ok
test_valid_signature_accepted ... ok
----------------------------------------------------------------------
Ran 14 tests in 3.033s

OK
```

Exit code `0`; run at HEAD `3f7c415` (this branch's born-red card commit). The run
exercises all five gate behaviours: null top-level `customer_email` →
`customer_details.email` fallback; the legacy top-level-email fixture; forged-
signature reject; stale-timestamp reject; and the `success_url`
`{CHECKOUT_SESSION_ID}`-only lint.

**CI.** The same suite runs as an enforced check in
[`.github/workflows/kit-tests.yml`](../../.github/workflows/kit-tests.yml), job
`stripe-webhook-test-kit-tests` (`python3 -m unittest test_http_realpath -v`).
This packet's PR triggers a fresh CI run on its head SHA; the green run URL is
filled in below once it completes.

- **Fresh real-path CI green on head `e821a8c`:** [`kit-tests` run 29170727273](https://github.com/menno420/venture-lab/actions/runs/29170727273) — conclusion **success** (both jobs `stripe-webhook-test-kit-tests` and `membership-kit-tests` green) — and the required [`substrate-gate` run 29170727282](https://github.com/menno420/venture-lab/actions/runs/29170727282) — conclusion **success**. This documentation-only commit re-runs the identical suite. (Earlier confirmation: [`kit-tests` run 29170630449](https://github.com/menno420/venture-lab/actions/runs/29170630449) was green on the pre-card-flip head `ea16f06`, before `substrate-gate` cleared.)

**Binding lesson (re-stated, do not regress).** A real
`checkout.session.completed` event carries `customer_email: null`, with the
buyer's address in `customer_details.email` — read the wrong field and the sale is
silently dropped. Stripe expands **only** `{CHECKOUT_SESSION_ID}` in a
`success_url`; any other placeholder reaches the buyer's browser verbatim.

---

## The Launch Hour — three owner actions

Each row uses the lane's six-field owner-action grammar
(WHAT · WHERE · HOW · WHY · UNBLOCKS · VERIFIED-WHEN). Run them in order.

### 1. ⚑A — Add Stripe keys (close the last live-E2E leg)

> **Adaptation note (honest).** ⚑E publishes through a **marketplace-hosted**
> checkout (Gumroad / Lemon Squeezy — see the ⚑E click-script). The marketplace
> hosts payment and delivery, so **the $29 sale itself needs NO self-hosted
> Stripe checkout and NO Stripe API keys.** The repo describes no self-hosted
> checkout for this product, and this packet invents none. The Stripe keys in
> ⚑A serve a narrower purpose: they let the owner run the kit against a **live
> test-mode Stripe webhook** to close the one remaining unverified leg of the
> kit's own gate (the local + CI real-path runs are green; a live test-mode
> round-trip is still UNVERIFIED, per status.md ORDER 003 caveat).

- **WHAT:** create a free Stripe account (test mode) and set the kit's webhook
  signing-secret env var so the kit can fire a live test-mode event at a handler.
  The only env var the kit reads is **`SWTK_WEBHOOK_SECRET`** (the default in
  `swtk.py` `--secret-env` and in `stub_handler.py`). Env var **NAME only** — the
  `whsec_...` value never enters the repo. (The separate membership-kit server
  path uses `STRIPE_SECRET_KEY` + `STRIPE_WEBHOOK_SECRET` per status.md ⚑A; that
  is a different product and is **not** needed for the test kit's launch.)
- **WHERE:** the value goes in the claude.ai env panel and/or the owner's local
  `.env` — **never** committed to the repo. The `whsec_...` secret itself is read
  from the Stripe Dashboard.
- **HOW:** 1) Sign in to the Stripe Dashboard, test mode. 2) Developers → Webhooks
  → Add endpoint; select `checkout.session.completed`. 3) Copy the endpoint's
  signing secret (`whsec_...`). 4) Export it locally as `SWTK_WEBHOOK_SECRET`
  (never hardcode, never commit). 5) Start the bundled handler
  (`SWTK_WEBHOOK_SECRET=whsec_... python3 stub_handler.py 8000`) or your own, then
  fire a live/vendored event (`python3 swtk.py fire --url
  http://localhost:8000/webhook --fixture checkout_session_completed`).
- **WHY:** the real-path suite is green locally and in CI, but a live test-mode
  round-trip is the last UNVERIFIED leg; closing it removes the final "unproven
  against real Stripe" caveat before asking anyone to pay.
- **UNBLOCKS:** the honest "verified against a live test-mode Stripe event" claim,
  and the owner's own confidence to publish ⚑E.
- **VERIFIED-WHEN:** `SWTK_WEBHOOK_SECRET` is present in the env panel / local
  `.env` (value never in-repo) AND a signed test-mode `checkout.session.completed`
  fired at the handler returns **HTTP 200**.

### 2. ⚑E — Publish the kit

- **WHAT:** publish the Stripe Webhook Test Kit v0.1 listing at **$29** and upload
  the bundle `candidates/stripe-webhook-test-kit/dist/stripe-webhook-test-kit-v0.1.zip`.
- **WHERE:** Gumroad or Lemon Squeezy (Discover), signed into the owner's own
  account.
- **HOW:** follow the click detail in
  [`stripe-webhook-test-kit/publish-owner-action.md`](stripe-webhook-test-kit/publish-owner-action.md)
  (do not duplicate it here): upload the zip, paste the listing copy from
  [`stripe-webhook-test-kit/LISTING.md`](stripe-webhook-test-kit/LISTING.md), set
  price $29, publish, copy the public product URL.
- **WHY:** revenue-lane candidate #1 (eval-001, score 4.05); the ⚑E gates are
  already met (in-CI green + R23 non-author verification — see status.md).
- **UNBLOCKS:** the first-ten-customers funnel and the first external dollar.
- **VERIFIED-WHEN:** the live listing URL returns **HTTP 200** on a purchasable
  $29 page. (T = this listing-live timestamp; the kill-rule clock starts here.)

### 3. First-sale verification

- **WHAT:** after a real buyer purchases, confirm the sale is real and the handler
  behaved. Check, in order: (a) Stripe/marketplace Dashboard → Payments shows a
  **succeeded $29 charge**; (b) the Webhooks event log shows
  `checkout.session.completed` **delivered 200**; (c) the real event's buyer email
  resolves from **`customer_details.email`** (top-level `customer_email` is
  `null`); (d) the success redirect used **`{CHECKOUT_SESSION_ID}`** only; (e) the
  buyer received the download.
- **WHERE:** the Stripe Dashboard (Payments + Webhooks event log) and the
  marketplace order record.
- **HOW:** open the Dashboard after the first order notification; read the charge,
  the webhook delivery status, and the event's `customer_details.email` /
  `customer_email` fields; confirm the buyer's success-page URL and their
  download.
- **WHY:** proves the kit's own headline gotcha (null `customer_email`) is handled
  on a REAL event, not just fixtures — the honest close of the build.
- **UNBLOCKS:** the kill-rule "≥1 organic sale" signal and return-on-agent-labor
  measurement.
- **VERIFIED-WHEN:** one real **$29 payment** is visible in the Dashboard AND the
  webhook event is **logged 200**.

---

## Conservative earnings + payback (EXPECT BAD RESULTS — never overstate)

Every figure below is an assumption unless marked measured; assumptions are marked.

- **Per-sale net (illustrative).** Price **$29 gross**. Raw Stripe fee
  2.9% + $0.30 = **$1.14** → net ≈ **$27.86/sale**. *Assumption / upper bound:*
  this uses the raw Stripe rate; a marketplace host (Gumroad / Lemon Squeezy)
  takes a **larger** cut than raw Stripe, so the real net will be **lower** than
  $27.86 — treat $27.86 as a best-case ceiling, not the expected net.
- **Sunk build cost.** ≈ **284k tokens** metered (vs a **120k** intake cap,
  ~2.3× — a headlined NEGATIVE in status.md; ~90k of it was CI-status polling).
  The dollar value of that token spend is an **OWNER-CONFIRMED input**, not an
  agent figure; at an *illustrative* $10–30 / 1M-token blended rate it is
  ≈ **$3–9**. On that basis a **single** sale's ~$27.86 net covers the sunk
  build-token cost.
- **BASE CASE (conservative) = 0 sales.** No distribution channel is wired yet, so
  the honest base case is **zero sales** and therefore **payback time is
  INDEFINITE / possibly never** absent traffic. No monthly revenue is projected or
  promised.
- **The real gap is distribution.** No first-ten-customers path is actually wired
  — the free gotcha article, gist, StackOverflow answer, and subreddit posts are
  all still owner-gated ⚑ clicks (see the kit one-pager funnel plan). Without at
  least one of those live and drawing high-intent traffic, realistic revenue is
  ~**$0**.

---

## Kill rule

- **Signal:** ≥1 organic sale **OR** ≥1 qualified inbound within **14 days** of the
  listing going live. **T = the ⚑E listing-live timestamp; deadline = T + 14
  days.**
- **No signal by T+14:** ledger ⚑E a **NEGATIVE** and **pause / delist** the
  product.
- **Effort cap:** cap further agent launch-support effort on this candidate at
  ~**50k tokens**. Exceeding that budget without a signal = a ledgered negative.

---

## Closing note

No secret values live anywhere in this repo — only env var **names** appear
(`SWTK_WEBHOOK_SECRET`), and the signing secret is read from the environment at
run time, never stored, logged, or echoed. Agents plan and queue; the **owner
performs every click** — account creation, key entry, publish, and the first-sale
check are all owner actions.
