# Membership-Site Boilerplate Kit — v0.2

A documented, tested starter you drop into a repo to launch a paid
membership site: **auth + payments + invite-on-purchase + gated content**,
wired end-to-end. Ships in **MOCK mode by default** — it runs with zero
accounts and **no real payments** — so you can see the whole purchase→access
flow working before you sign up for anything, then paste your keys to go live.

> **v0.2** — a credible minimal slice, honest about its scope. The
> membership-grant flow is real, persisted, and tested today, and the real
> Stripe webhook path is verified against **real live-shape Stripe payloads at
> the HTTP layer** (see `server/fixtures/` + `server/test_http_realpath.py`).
> The remaining production integrations (Supabase, live Stripe keys, Discord)
> are documented and gated behind env keys you supply. See "Owner setup" below.

## What the kit is

A stdlib-only Python backend + a self-contained landing page + a gated members
area, packaged as a starter buyers pay for. The value is not the code volume —
it's that the payment→membership→gated-access path is **already wired, already
persisted, already tested against real Stripe payloads, and demonstrable in one
command** with no accounts. You clone it, run it, see the flow, then paste your
keys to go live.

## What's included

```
candidates/membership-kit/
├── README.md              ← this file
├── QUICKSTART.md          ← one-command demo + go-live steps
├── LISTING.md             ← ready-to-publish marketplace copy
├── design-tokens.json     ← brand tokens (colors/fonts/spacing) as hard data
├── web/
│   ├── index.html         ← landing page (hero + features + pricing CTA)
│   ├── styles.css         ← styled from design-tokens.json values
│   └── members.html       ← gated members-area stub
└── server/
    ├── app.py                 ← stdlib http.server backend (mock + real Stripe)
    ├── .env.example           ← placeholder keys with owner markers
    ├── test_membership.py     ← unittest proving grant/deny/idempotency/persistence
    ├── test_http_realpath.py  ← HTTP-layer tests: real Stripe payload + signature
    ├── fixtures/              ← real, source-verified Stripe event payloads
    └── README.md              ← run + wire-up instructions
```

## The stack

| Concern        | Production integration        | v0.2 status |
|----------------|-------------------------------|-------------|
| Auth + user DB | Supabase                      | **store implemented** (PostgREST via stdlib `urllib`), HTTP-tested vs a stub PostgREST; live project owner-gated |
| Payments       | Stripe Checkout + webhooks    | real code path, **native signature verification**, **HTTP-tested against real live-shape payloads**; env-gated; **MOCK mode by default** |
| Community      | Discord invite-on-purchase    | hook in webhook handler, env-gated |
| Gated content  | membership-store access check | **real + persisted + tested** |
| Persistence    | JSON file (default) / Supabase | **real + tested**; survives process restart. Hosted **Supabase** backend implemented (stdlib REST) + HTTP-tested vs a stub PostgREST; local `json` stays the default and Supabase falls back loudly to it when keys are absent |

The backend is stdlib-only: it imports and runs with **no pip installs**. The
Stripe webhook signature is verified with a native stdlib HMAC-SHA256 check (no
`stripe` package needed to test the real signature path); the live
`/create-checkout-session` call is the only place that lazily imports `stripe`,
guarded by `if STRIPE_SECRET_KEY:`.

## Quickstart (MOCK mode — zero accounts, no real payments)

```bash
cd candidates/membership-kit/server
python3 -m unittest test_membership -v       # 15 tests — grant/persistence logic + store config
python3 -m unittest test_http_realpath -v    # 8 tests  — real Stripe payload over HTTP
python3 -m unittest test_supabase_store -v   # 12 tests — Supabase store over HTTP vs a stub PostgREST
python3 app.py                               # starts on http://localhost:8000
```

On startup with no keys the server prints a **loud MOCK-mode banner** to stderr
— no real payments happen and it never pretends otherwise. Then, in another
terminal, drive the full flow with no keys:

```bash
curl http://localhost:8000/                        # landing page HTML
curl -X POST "http://localhost:8000/mock-purchase?email=buyer@example.com"
curl "http://localhost:8000/members?email=buyer@example.com"   # access GRANTED (200)
curl "http://localhost:8000/members?email=nobody@example.com"  # DENIED (402)
```

`/mock-purchase` grants membership exactly the way a real Stripe webhook would,
so the members area unlocks immediately — the entire purchase→access loop is
demonstrable before any account exists. Members persist to `server/members.json`,
so they survive a restart. Every mock-mode reply carries a `"warning"` field —
never a silent success.

## The real Stripe path (verified)

`server/test_http_realpath.py` starts the actual server and POSTs **real,
source-verified** `checkout.session.completed` event payloads (in
`server/fixtures/`, provenance in `fixtures/PROVENANCE.md`) with a valid
`Stripe-Signature` over the raw bytes. It proves, at the HTTP layer:

- The **real live shape** — buyer email at `customer_details.email`, with
  top-level `customer_email` `null` — grants membership (the app prefers
  `customer_details.email`, falling back to `customer_email` for legacy/guest).
- A **valid signature** grants (HTTP 200); a **bad signature** and a **stale
  timestamp** are both rejected (HTTP 400) before any grant.
- Stripe's `{CHECKOUT_SESSION_ID}` success URL lands a buyer: after a webhook
  grant, `GET /members?session_id=cs_...` resolves the buyer and serves the
  gated page.

## Owner setup (going live — what a buyer supplies)

Copy `server/.env.example` to `server/.env` and fill in your own accounts/keys:

| Env var                  | Where to get it                        |
|--------------------------|----------------------------------------|
| `STRIPE_SECRET_KEY`      | Stripe dashboard → Developers → API keys (use `sk_test_…` first); gates the live `/create-checkout-session` call |
| `STRIPE_WEBHOOK_SECRET`  | Stripe dashboard → Webhooks → signing secret (`whsec_…`); gates native `/webhook` signature verification |
| `DISCORD_INVITE_URL`     | Discord → Server settings → Invites    |
| `SUPABASE_URL` / `SUPABASE_KEY` | Supabase project → Settings → API |

With `STRIPE_WEBHOOK_SECRET` set, `/webhook` verifies every signature natively
over the raw body and rejects bad/stale ones with HTTP 400 before granting. With
`STRIPE_SECRET_KEY` set, `/create-checkout-session` takes the real Stripe path
(and stamps the buyer's `customer_email` so the webhook is deterministic).
Without those keys the server stays in **MOCK mode** and says so loudly. **No
secret ships in this repo** — `.env.example` holds placeholders only.

## Honest v0.2 scope

- **Real now:** the membership store with **file-backed persistence that
  survives a restart** (atomic writes), the grant-on-purchase logic, the
  deny-when-unpaid gate, idempotent duplicate-purchase handling, **native
  Stripe webhook signature verification** (valid/bad/stale all covered), the
  `session_id`→buyer resolution behind the `{CHECKOUT_SESSION_ID}` success URL,
  the landing page, the members stub, the mock end-to-end flow, and the
  **Supabase store's PostgREST wire contract** (insert/select/upsert/count/error
  handling). All tested — 15 store/config unit tests + 8 HTTP-layer Stripe
  real-path tests + 12 HTTP-layer Supabase-store tests (vs a stub PostgREST).
- **Owner-gated (documented, not performed):** live Stripe test-mode E2E with
  your own keys, Discord invite delivery, and a **live** Supabase round-trip.
  The Supabase store is implemented and HTTP-tested against a stub PostgREST;
  only a real project + `members` table + keys are missing (six-field
  OWNER-ACTION in `server/README.md`). Each is a wired code path waiting on a
  key — see the ⚑ owner-action items in `docs/research/venture-ledger.md`.
- **Not in v0.2:** email receipts, refund/cancellation webhooks, multi-tier
  plans, and Supabase persistence turned on **by default** (the store is
  implemented and HTTP-tested, but local `json` remains the default until the
  owner supplies a project + keys). These are the next increment, not a hidden
  gap.
