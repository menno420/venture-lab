# Quickstart — Membership-Site Boilerplate Kit

Run the whole purchase → access flow in one command, with **zero accounts**.

## 1. Prove the logic (optional, 2 seconds)

```bash
cd server
python3 -m unittest test_membership -v    # 13 tests, no network, no keys
```

## 2. Start the server (one command)

```bash
cd server
python3 app.py            # -> http://localhost:8000  (mock mode, no keys)
```

You'll see `mode=mock | store=json`. Leave it running.

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
`server/members.json`, so they survive a restart.

## 4. Go live (when you're ready)

```bash
cp server/.env.example server/.env
# paste your Stripe TEST keys (sk_test_…, whsec_…) into server/.env
```

With `STRIPE_SECRET_KEY` set, `/create-checkout-session` and `/webhook` take the
real Stripe path — the same code you just watched in mock mode. See `README.md`
and `server/README.md` for the full wire-up (Stripe, Discord, Supabase).

## What's in this bundle

- `README.md` — what the kit is, the stack, honest v0.x scope.
- `QUICKSTART.md` — this file.
- `design-tokens.json` — brand colors/fonts/spacing the landing page consumes.
- `web/` — landing page (`index.html` + `styles.css`) + gated `members.html`.
- `server/` — stdlib-only backend (`app.py`), test suite, `.env.example`, docs.

No third-party dependencies. `python3` is all you need to run it.
