# Membership-Site Boilerplate Kit — v0.1

A documented, tested starter you drop into a repo to launch a paid
membership site: **auth + payments + invite-on-purchase + gated content**,
wired end-to-end. Runs in **mock mode with zero accounts** so you can see the
whole purchase→access flow working before you sign up for anything.

> This is **v0.1** — a credible minimal slice, honest about its scope. The
> membership-grant flow is real and tested today; the production integrations
> (Supabase, live Stripe, Discord) are documented and gated behind env keys
> you supply. See "Owner setup" and the ⚑ owner-action items in the repo
> ledger for exactly what a buyer wires in.

## What the kit is

A stdlib-only Python backend + a self-contained landing page + a gated members
area, packaged as a starter buyers pay for. The value is not the code volume —
it's that the payment→membership→gated-access path is **already wired, already
tested, and demonstrable in one command** with no accounts. You clone it, run
it, see the flow, then paste your keys to go live.

## What's included

```
candidates/membership-kit/
├── README.md              ← this file
├── LISTING.md             ← ready-to-publish marketplace copy
├── design-tokens.json     ← brand tokens (colors/fonts/spacing) as hard data
├── web/
│   ├── index.html         ← landing page (hero + features + pricing CTA)
│   ├── styles.css         ← styled from design-tokens.json values
│   └── members.html       ← gated members-area stub
└── server/
    ├── app.py             ← stdlib http.server backend (mock + real Stripe)
    ├── .env.example       ← placeholder keys with owner markers
    ├── test_membership.py ← unittest proving grant/deny/idempotency
    └── README.md          ← run + wire-up instructions
```

## The stack

| Concern        | Production integration        | v0.1 status |
|----------------|-------------------------------|-------------|
| Auth + user DB | Supabase                      | documented, env-gated |
| Payments       | Stripe Checkout + webhooks    | real code path, env-gated; **mock mode works now** |
| Community      | Discord invite-on-purchase    | hook in webhook handler, env-gated |
| Gated content  | membership-store access check | **real + tested now** |

The backend is stdlib-only: it imports and runs with **no pip installs**. Real
Stripe calls live behind `if STRIPE_SECRET_KEY:` guards, so the file runs
without the `stripe` package installed.

## Quickstart (mock mode — zero accounts)

```bash
cd candidates/membership-kit/server
python3 -m unittest test_membership -v     # prove the logic
python3 app.py                             # starts on http://localhost:8000
```

Then, in another terminal, drive the full flow with no keys:

```bash
curl http://localhost:8000/                        # landing page HTML
curl -X POST "http://localhost:8000/mock-purchase?email=buyer@example.com"
curl "http://localhost:8000/members?email=buyer@example.com"   # access GRANTED
curl "http://localhost:8000/members?email=nobody@example.com"  # 402 DENIED
```

`/mock-purchase` grants membership exactly the way a real Stripe webhook would,
so the members area unlocks immediately — the entire purchase→access loop is
demonstrable before any account exists.

## Owner setup (going live — what a buyer supplies)

Copy `server/.env.example` to `server/.env` and fill in your own accounts/keys:

| Env var                  | Where to get it                        |
|--------------------------|----------------------------------------|
| `STRIPE_SECRET_KEY`      | Stripe dashboard → Developers → API keys (use `sk_test_…` first) |
| `STRIPE_WEBHOOK_SECRET`  | Stripe dashboard → Webhooks → signing secret |
| `DISCORD_INVITE_URL`     | Discord → Server settings → Invites    |
| `SUPABASE_URL` / `SUPABASE_KEY` | Supabase project → Settings → API |

With `STRIPE_SECRET_KEY` set, `/create-checkout-session` and `/webhook` take the
real Stripe path; without it, the server stays in mock mode. **No secret ships
in this repo** — `.env.example` holds placeholders only.

## Honest v0.1 scope

- **Real now:** the membership store, the grant-on-purchase logic, the
  deny-when-unpaid gate, idempotent duplicate-purchase handling, the landing
  page, the members stub, and the mock end-to-end flow. All tested.
- **Owner-gated (documented, not performed):** live Stripe test-mode E2E,
  Discord invite delivery, Supabase-backed persistent users. Each is a wired
  code path waiting on a key — see the ⚑ owner-action items in
  `docs/research/venture-ledger.md`.
- **Not in v0.1:** email receipts, refund/cancellation webhooks, multi-tier
  plans, a real database (the store is in-memory). These are the next
  increment, not a hidden gap.
