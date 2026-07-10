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
| `/health`                   | GET    | both  | Mode + store backend + member count |

The **same** `handle_purchase_event()` runs for `/mock-purchase` and the real
`/webhook`, so the mock flow exercises the exact grant logic that ships.

## Persistence (v0.2) — members survive a restart

Membership now lives behind a pluggable `MembershipStore` interface, selected by
the `STORE_BACKEND` env var. The HTTP layer never knows which backend is active.

| `STORE_BACKEND` | Backend        | Needs        | Notes |
|-----------------|----------------|--------------|-------|
| `json` (default)| `JsonFileStore`| nothing      | Persists to a JSON file with **atomic writes** (`os.replace`). Survives process restart. |
| `supabase`      | `SupabaseStore`| Supabase keys| Drop-in-ready skeleton — see below. |

Default (file-backed) — proves persistence with zero accounts:

```bash
python3 app.py                                                   # store=json
curl -X POST "http://localhost:8000/mock-purchase?email=buyer@example.com"
# Ctrl-C to kill, then re-run `python3 app.py`
curl "http://localhost:8000/members?email=buyer@example.com"     # 200 — STILL a member
```

- File path defaults to `server/members.json`; override with `MEMBERS_DB_PATH`.
- `members.json` is **git-ignored** — local member data is never committed.
- Reading an absent DB writes nothing; the file appears only on the first grant.

### Supabase drops in later — a config flip, no app rework

`SupabaseStore` implements the **same** `MembershipStore` contract as the file
store, so going hosted is:

1. Fill `SUPABASE_URL` / `SUPABASE_KEY` in `.env` (owner-gated — no keys today).
2. Set `STORE_BACKEND=supabase`.
3. Fill the documented PostgREST call bodies in `SupabaseStore` (the request
   shapes are written inline as comments next to each method).

No change to `app.py` is required — the store is swapped at startup by
`make_store()`. Guardrails: there is no top-level `supabase` import (importing
the module never crashes on a missing package), and selecting the backend
without keys raises a clear, actionable error **at startup** — *"set
SUPABASE_URL/KEY or use STORE_BACKEND=json"* — rather than failing mid-request.

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
