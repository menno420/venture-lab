# server/ — running the membership backend

Stdlib-only Python. No pip install, no build step.

## Run the tests (proves the logic)

```bash
cd candidates/membership-kit/server
python3 -m unittest test_membership -v      # 15 tests: grant/deny/idempotency/persistence + store config
python3 -m unittest test_http_realpath -v   # 8 tests: real Stripe payload + signature over HTTP
python3 -m unittest test_supabase_store -v  # 12 tests: Supabase store over HTTP vs a stub PostgREST
```

`test_membership` covers: purchase grants access, unpaid users are denied,
duplicate purchases are idempotent, emails normalize, non-purchase events grant
nothing, empty emails are rejected, and the store factory (including the loud
Supabase→JSON fallback). No network, no Stripe, deterministic.

`test_supabase_store` drives `SupabaseStore` over **real HTTP** against an
in-process **stub PostgREST server** whose request/response shapes mirror real
PostgREST (insert, select-with-filter, upsert, exact count, and non-2xx error
handling; auth headers asserted). It proves the wire contract with **no live
Supabase project** and no third-party packages. A live round-trip against a real
project stays owner-gated — see the Supabase OWNER-ACTION below.

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
| `supabase`      | `SupabaseStore`| Supabase keys| Hosted persistence via Supabase's PostgREST REST API — **implemented** (stdlib `urllib` only). See below. |

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

### Supabase hosted persistence — implemented, a config flip away

`SupabaseStore` implements the **same** `MembershipStore` contract as the file
store, backed by Supabase's PostgREST REST API (`{SUPABASE_URL}/rest/v1/members`)
using **stdlib `urllib` only** — no `supabase` package, no third-party HTTP
client. Each operation maps to a documented PostgREST call:

| Method         | PostgREST call |
|----------------|----------------|
| `grant`        | `GET ?email=eq.<email>&select=email,source&limit=1` (idempotency check), then `POST ?on_conflict=email` with `Prefer: resolution=merge-duplicates,return=representation` |
| `has_access`   | `GET ?email=eq.<email>&select=email&limit=1` → `bool(rows)` |
| `all_members`  | `GET ?select=email,source` |
| `count`        | `GET ?select=email` with `Prefer: count=exact` + `Range: 0-0` → total from the `Content-Range` header |

Auth on every call is the pair Supabase requires: an `apikey` header and an
`Authorization: Bearer <SUPABASE_KEY>` header. The key is read from the
environment, sent only as request headers, and **never logged or echoed** —
error messages carry the HTTP status + response body, never the key value.

Going hosted:

1. Create a Supabase project + a `members` table (**OWNER-ACTION** below).
2. Set `SUPABASE_URL` / `SUPABASE_KEY` in `.env` (use the **service_role** key —
   server-side writes need to bypass row-level security). NAMES only in the repo;
   never paste a key value.
3. Set `STORE_BACKEND=supabase`.

No change to `app.py` is required — the store is swapped at startup by
`make_store()`. Guardrails / defaults:

- **Local (`json`) is the DEFAULT.** No accounts needed to run the kit.
- No top-level `supabase` import — importing the module never crashes on a
  missing package.
- If `STORE_BACKEND=supabase` is selected but `SUPABASE_URL`/`SUPABASE_KEY` are
  unset, the server does **not** crash: `make_store()` prints a **loud
  `!!!`-barred `SUPABASE FALLBACK` banner** to stderr (same style as the MOCK
  banner) and falls back to the local JSON store — never a silent success,
  never a hard stop. (Direct `SupabaseStore(url="", key="")` construction still
  raises a clear, actionable error for callers who want fail-fast.)

The store's wire contract is proven by `test_supabase_store.py` (real HTTP vs a
stub PostgREST server). A **live** round-trip against a real Supabase project is
**UNVERIFIED** until the owner completes the OWNER-ACTION.

### OWNER-ACTION — create the Supabase project + `members` table

*(owner-gated; the kit ships local-by-default, so this is optional — do it only
to turn on hosted persistence.)*

- **WHAT:** Create a free Supabase project and a `members` table with columns
  `email text` (PRIMARY KEY or UNIQUE — the `on_conflict=email` upsert depends
  on a unique constraint) and `source text`.
- **WHERE:** [supabase.com](https://supabase.com) → new project → SQL Editor
  (or Table Editor). Project URL + API keys live under **Project Settings → API**.
- **HOW:** In the SQL Editor run:
  ```sql
  create table if not exists public.members (
    email  text primary key,
    source text
  );
  ```
  Then copy the **Project URL** and the **service_role** key into
  `server/.env` as `SUPABASE_URL` / `SUPABASE_KEY` (values never committed), and
  set `STORE_BACKEND=supabase`.
- **WHY:** The kit can persist members in hosted Supabase instead of a local
  file, so membership survives across machines/restarts and is queryable in the
  Supabase dashboard. The store code is implemented and HTTP-tested; only the
  live project + keys are missing.
- **UNBLOCKS:** Hosted persistent membership (the "Auth + user DB → Supabase"
  row of the stack table) — members shared across instances, not tied to one
  local `members.json`.
- **VERIFIED-WHEN:** With the three env vars set, `python3 app.py` starts
  **without** the `SUPABASE FALLBACK` banner and prints `store=supabase`; a
  `POST /mock-purchase?email=you@example.com` then `GET /members?email=you@example.com`
  returns 200, and the row is visible in the Supabase Table Editor.

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
