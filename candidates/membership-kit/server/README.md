# server/ — running the membership backend

Stdlib-only Python. No pip install, no build step.

## Run the tests (proves the logic)

```bash
cd candidates/membership-kit/server
python3 -m unittest test_membership -v
```

Covers: purchase grants access, unpaid users are denied, duplicate purchases
are idempotent, emails normalize, non-purchase events grant nothing, and empty
emails are rejected. No network, no Stripe, deterministic.

## Run the server (mock mode — works now, zero accounts)

```bash
python3 app.py            # http://localhost:8000  (mode=mock)
```

Drive the full purchase → access loop with no keys:

```bash
curl http://localhost:8000/                                      # landing page
curl -X POST "http://localhost:8000/mock-purchase?email=buyer@example.com"
curl "http://localhost:8000/members?email=buyer@example.com"     # 200 — access granted
curl "http://localhost:8000/members?email=nobody@example.com"    # 402 — denied
curl http://localhost:8000/health                                # {mode, members}
```

## Routes

| Route                       | Method | Mode  | Purpose |
|-----------------------------|--------|-------|---------|
| `/`, `/index.html`          | GET    | both  | Landing page |
| `/styles.css`               | GET    | both  | Landing/members CSS |
| `/members`                  | GET    | both  | Gated page; 402 if `?email=` is not a member |
| `/mock-purchase?email=`     | POST   | mock  | Grants membership like a real webhook (demo) |
| `/create-checkout-session`  | POST   | both  | Real Stripe Checkout URL (if keyed), else mock hint |
| `/webhook`                  | POST   | both  | Stripe event → grant + Discord invite |
| `/health`                   | GET    | both  | Mode + member count |

The **same** `handle_purchase_event()` runs for `/mock-purchase` and the real
`/webhook`, so the mock flow exercises the exact grant logic that ships.

## Owner steps — wire real Stripe TEST keys

1. Create a free Stripe account and grab your **test** secret key (`sk_test_…`).
2. `cp .env.example .env` and paste `STRIPE_SECRET_KEY` + `STRIPE_WEBHOOK_SECRET`.
3. `pip install stripe` (only needed for real mode — mock mode needs nothing).
4. `export $(grep -v '^#' .env | xargs)` then `python3 app.py` → `mode=stripe`.
5. Forward test webhooks with the Stripe CLI:
   `stripe listen --forward-to localhost:8000/webhook`.
6. Trigger `stripe trigger checkout.session.completed` and watch a membership
   get granted.

These steps are **owner-gated** (they require creating a Stripe account and
pasting keys) — see the ⚑ owner-action items in `docs/research/venture-ledger.md`.
Nothing here has been performed by the build agent.
