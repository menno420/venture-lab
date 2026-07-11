# Quickstart — Membership-Site Boilerplate Kit (v0.2)

Run the whole purchase → access flow in one command, with **zero accounts**.

> ⚠️ **This kit ships in MOCK MODE by default — NO REAL PAYMENTS happen.**
> Without keys the server processes "purchases" locally so you can see the flow,
> prints a loud MOCK-mode banner to stderr on startup, and stamps a `"warning"`
> field on every checkout/webhook reply. To take real money you must set the two
> Stripe env vars in step 4 — until then, nothing you do here charges anyone.

## 1. Prove the logic (optional, a few seconds)

```bash
cd server
python3 -m unittest test_membership -v       # 15 tests: grant/deny/idempotency/persistence + store config
python3 -m unittest test_http_realpath -v    # 8 tests: REAL Stripe payload + signature over HTTP
python3 -m unittest test_supabase_store -v   # 12 tests: Supabase store over HTTP vs a stub PostgREST
```

The HTTP tests start the real server and POST **real, source-verified** Stripe
`checkout.session.completed` payloads (in `server/fixtures/`) with a valid
signature — proving the webhook grants on a valid signature and rejects bad or
stale ones (HTTP 400). No keys, no network, no `stripe` package needed.

## 2. Start the server (one command)

```bash
cd server
python3 app.py            # -> http://localhost:8000  (MOCK mode, no keys)
```

You'll see a loud `!!! MOCK MODE: no real payments ... !!!` banner on stderr and
`mode=mock | store=json`. Leave it running.

## 3. Watch a purchase unlock the members area

In a second terminal:

```bash
# Before buying: access is denied (HTTP 402)
curl -i "http://localhost:8000/members?email=buyer@example.com"

# Simulate a purchase (this is exactly what a real Stripe webhook triggers)
curl -X POST "http://localhost:8000/mock-purchase?email=buyer@example.com"

# After buying: the gated members page is served (HTTP 200)
curl -i "http://localhost:8000/members?email=buyer@example.com"
```

That's the entire product loop — checkout → webhook → membership grant → gated
content — running before you sign up for anything. Members persist to
`server/members.json`, so they survive a restart. (This is MOCK mode: no card is
ever charged.)

## 4. Go live (when you're ready) — set these env var NAMES

```bash
cp server/.env.example server/.env
# then set the two Stripe env vars (NAMES below) to your own values in server/.env:
#   STRIPE_SECRET_KEY       your Stripe secret key (start with the sk_test_ one)
#   STRIPE_WEBHOOK_SECRET   your Stripe webhook signing secret (whsec_...)
```

- **`STRIPE_SECRET_KEY`** turns on the real `/create-checkout-session` call
  (and stamps the buyer's `customer_email` so the webhook is deterministic).
- **`STRIPE_WEBHOOK_SECRET`** turns on native `/webhook` signature verification —
  every event's `Stripe-Signature` is checked over the raw body and bad/stale
  ones are rejected with HTTP 400 before any membership is granted.

With either set, the MOCK banner and warnings disappear and the server reports
`mode=stripe`. Never commit real secret **values** — `.env.example` and this
guide name the env vars only. See `README.md` and `server/README.md` for the
full wire-up (Stripe, Discord, Supabase).

## What's in this bundle

- `README.md` — what the kit is, the stack, honest v0.2 scope.
- `QUICKSTART.md` — this file.
- `design-tokens.json` — brand colors/fonts/spacing the landing page consumes.
- `web/` — landing page (`index.html` + `styles.css`) + gated `members.html`.
- `server/` — stdlib-only backend (`app.py`), test suites, `fixtures/`,
  `.env.example`, docs.

No third-party dependencies. `python3` is all you need to run it.
