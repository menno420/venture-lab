# Pre-Publish Gate Review — First Revenue Lane

Date: 2026-07-11  
Repository: `menno420/venture-lab`  
Scope: `candidates/membership-kit/`, `candidates/template-packs/`, `candidates/stripe-webhook-test-kit/`

## Gate verdict

**Do not publish `candidates/membership-kit/` yet.** There is one critical publish-blocker in the real-payment boundary: a partially configured Stripe deployment can create real Checkout Sessions while `/webhook` accepts unsigned JSON and grants membership.

When `STRIPE_WEBHOOK_SECRET` is set, the Stripe signature verification path itself is **verified clean**: it verifies the raw request body before JSON parsing, uses timing-safe comparison, accepts any valid `v1=` during rotation, enforces the 300-second timestamp tolerance, and rejects missing/bad/stale signatures before grant.

The Stripe Webhook Test Kit signing and `--forge` behavior are also **verified clean**: both Python and Node ports generate the real `Stripe-Signature` HMAC shape and `--forge` uses a deliberately wrong secret to detect handlers that accept forged events.

## PUBLISH-BLOCKER

### 1. Real Checkout can be enabled while `/webhook` accepts unsigned grants

- **Severity:** Critical / publish-blocker
- **Area:** Stripe signature verification, member-grant correctness, real-money payment path
- **Files:**
  - `candidates/membership-kit/server/app.py`
  - `candidates/membership-kit/server/.env.example`
  - `candidates/membership-kit/README.md`

#### Evidence

- The live Checkout path is enabled by `STRIPE_SECRET_KEY` alone: `/create-checkout-session` imports `stripe` and creates a real Checkout Session whenever `_stripe_secret_key()` is non-empty.
- The webhook verifies signatures only when `_webhook_secret()` is non-empty. If `STRIPE_WEBHOOK_SECRET` is missing, `/webhook` falls through to the unsigned mock branch, parses raw JSON, and calls `handle_purchase_event()`.
- Mock mode is defined as “neither Stripe key is set,” so the partially configured state `STRIPE_SECRET_KEY=set` and `STRIPE_WEBHOOK_SECRET=unset` is not true mock mode, but the webhook still accepts unsigned events.
- `handle_purchase_event()` grants membership for any event with `type == "checkout.session.completed"` and an email in `customer_details.email` or `customer_email`.

#### Concrete exploit / failure scenario

1. Owner deploys with `STRIPE_SECRET_KEY=sk_live_...` or `sk_test_...` but forgets `STRIPE_WEBHOOK_SECRET`.
2. `/create-checkout-session` can now create real Stripe Checkout URLs.
3. An attacker posts unsigned JSON directly to `/webhook`:

   ```json
   {
     "type": "checkout.session.completed",
     "data": {
       "object": {
         "id": "cs_fake",
         "customer_details": { "email": "attacker@example.com" }
       }
     }
   }
   ```

4. The app grants `attacker@example.com` without a Stripe signature or payment.

#### Publish requirement

Before publishing, make partial Stripe configuration fail closed. Recommended behavior:

- If either `STRIPE_SECRET_KEY` or `STRIPE_WEBHOOK_SECRET` is set, require both before serving the real Stripe path.
- `/webhook` must never grant from unsigned JSON unless the app is in explicit full mock mode with no Stripe keys at all.
- Prefer failing startup or returning a clear 5xx configuration error for partial Stripe config.

## VERIFIED CLEAN

### 2. Membership-kit signature verification is solid when `STRIPE_WEBHOOK_SECRET` is set

- **Severity:** Verified clean
- **Area:** Stripe signature verification
- **File:** `candidates/membership-kit/server/app.py`

The verifier:

- rejects a missing `Stripe-Signature` header;
- parses `t=` and all `v1=` signatures;
- rejects missing timestamp, missing signature, and malformed timestamp;
- computes HMAC-SHA256 over `f"{timestamp}." + raw_body`;
- uses `hmac.compare_digest()` for timing-safe comparison;
- accepts any matching `v1=` value, which supports secret rotation;
- enforces a 300-second replay/timestamp tolerance;
- runs before JSON parsing and before member grant.

The HTTP handler returns HTTP 400 on signature/timestamp failures and does not grant. Malformed JSON after a valid signature returns HTTP 400 and does not grant.

### 3. Stripe Webhook Test Kit signing and forge mode are solid

- **Severity:** Verified clean
- **Area:** Stripe webhook test harness
- **Files:**
  - `candidates/stripe-webhook-test-kit/swtk.py`
  - `candidates/stripe-webhook-test-kit/swtk.js`

Both ports implement the real Stripe v1 scheme:

- header shape: `t=<unix_ts>,v1=<hex_hmac_sha256>`;
- message: `timestamp + "." + raw fixture bytes`;
- key: webhook signing secret from an environment variable;
- `--forge`: signs with a deliberately wrong secret while keeping the header structurally valid.

A handler returning 2xx to `fire --forge` is correctly reported as insecure.

## FIX-SOON

### 4. No event-level idempotency; duplicate processing is email-idempotent only

- **Severity:** Medium
- **Area:** member-grant correctness, future fulfillment reliability
- **File:** `candidates/membership-kit/server/app.py`

The current store prevents duplicate member rows by normalized email. That is good for the current static membership grant, but it does not persist processed Stripe `event.id` or Checkout Session IDs. Stripe retries can re-run side effects if the product later adds real Discord API delivery, email delivery, tier changes, or other fulfillment.

Recommendation: persist processed Stripe event IDs or Checkout Session IDs before adding paid side effects beyond the current static invite URL.

### 5. Partial failure after payment lacks a documented recovery path

- **Severity:** Medium
- **Area:** member-grant correctness, buyer support
- **Files:**
  - `candidates/membership-kit/server/app.py`
  - `candidates/membership-kit/server/README.md`

`handle_purchase_event()` calls `store.grant()` directly. JSON write failures or Supabase failures can raise through the HTTP handler. Stripe will retry non-2xx deliveries, but the buyer-facing docs do not explain how an owner should recover a paid customer whose payment succeeded but member grant failed.

Recommendation: document operational recovery steps: inspect Stripe webhook attempts, fix storage/config, replay the event, and verify the member row. A later code increment should log non-secret diagnostic context and return an intentional 5xx on grant failure.

### 6. Marketplace listing overclaims Discord delivery

- **Severity:** Medium
- **Area:** buyer-experience truth
- **Files:**
  - `candidates/membership-kit/LISTING.md`
  - `candidates/membership-kit/server/app.py`
  - `candidates/membership-kit/README.md`

The listing says the kit has invite-on-purchase and that the Discord invite hook fires when payment lands. Actual code returns the configured static `DISCORD_INVITE_URL`; it does not call the Discord API, mint an invite, email the buyer, or otherwise deliver a Discord invite out of band.

Recommendation: change listing copy before publish to say the kit returns a configured Discord invite URL and includes a Discord invite seam; real Discord delivery is owner-gated.

### 7. Marketplace listing has stale v0.1 / in-memory-store copy

- **Severity:** Medium
- **Area:** buyer-experience truth
- **Files:**
  - `candidates/membership-kit/LISTING.md`
  - `candidates/membership-kit/README.md`

The listing FAQ still calls the product an “honest v0.1” and says the in-memory store is a next step. The product README and code are v0.2 with JSON-file persistence implemented and tested.

Recommendation: update listing copy to v0.2 and remove stale in-memory-store language.

### 8. Timestamp/replay testing is possible but under-documented in the test kit

- **Severity:** Low-to-medium
- **Area:** buyer-experience truth, test-kit completeness
- **Files:**
  - `candidates/stripe-webhook-test-kit/README.md`
  - `candidates/stripe-webhook-test-kit/swtk.py`
  - `candidates/stripe-webhook-test-kit/swtk.js`

The kit exposes `--timestamp`, so a buyer can test stale timestamp rejection manually. The README says the kit catches timestamp tolerance, but the quickstart only documents valid `fire` and bad-signature `fire --forge` runs.

Recommendation: add a README example using an old `--timestamp`, add a named stale mode, or soften the claim.

### 9. Fixture provenance is faithful today but not pinned to immutable source revisions

- **Severity:** Low-to-medium
- **Area:** fixture provenance / auditability
- **File:** `candidates/stripe-webhook-test-kit/fixtures/PROVENANCE.md`

The provenance document cites Stripe SDK files on `master`. The current field names and webhook signature scheme remain faithful to Stripe SDK shapes, and the document is honest that fixture values are illustrative. However, `master` is moving; future SDK changes could make the verification hard to reproduce.

Recommendation: pin the provenance links to commit SHAs in addition to the human-readable file names.

## NICE-TO-HAVE

### 10. Placeholder secrets are acceptable, but could be made impossible to confuse with real values

- **Severity:** Low
- **Area:** secret handling
- **File:** `candidates/membership-kit/server/.env.example`

No real secrets were found in the environment template. It uses conventional placeholders such as `sk_test_...` and `whsec_...`. For beginner buyers, placeholders like `__PASTE_STRIPE_SECRET_KEY_HERE__` would be even harder to mistake for configured values.

### 11. Distribution zips appear clean from listing inspection

- **Severity:** Low
- **Area:** distribution hygiene
- **Files:**
  - `candidates/membership-kit/package.sh`
  - `candidates/stripe-webhook-test-kit/package.sh`
  - `candidates/template-packs/package.sh`

The committed zips were inspected with `unzip -l`. They did not list `.env`, `members.json`, `.git`, nested `dist`, pycache, or obvious secret-bearing files. Packaging scripts use explicit allow-lists or clean staged bundles.

## Product-by-product notes

### `candidates/membership-kit/`

Do not publish until the partial Stripe config blocker is fixed. The signed webhook path is strong, but the product must fail closed when Stripe is only partially configured.

### `candidates/stripe-webhook-test-kit/`

Generally publishable after copy/docs polish. Signing and forge behavior are verified clean. Improve timestamp-tolerance discoverability and pin provenance links for stronger auditability.

### `candidates/template-packs/`

No payment-path code issues found in this review. Zip listing did not show obvious secret/runtime artifacts.

## Checks performed

```bash
python3 -m unittest discover -s candidates/membership-kit/server -v
python3 -m unittest discover -s candidates/stripe-webhook-test-kit -v
for z in candidates/*/dist/*.zip; do echo --- "$z"; unzip -l "$z" | sed -n '1,120p'; done
python3 - <<'PY'
# Exploit proof: set STRIPE_SECRET_KEY only, leave STRIPE_WEBHOOK_SECRET unset,
# POST unsigned checkout.session.completed JSON to /webhook, and observe grant.
PY
git status --short
```

