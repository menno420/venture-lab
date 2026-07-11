# Session — SupabaseStore bodies: implement the hosted persistence backend

> **Status:** `complete`

- **📊 Model:** claude-opus-4.8 · high · kit-backend-implementation
- **session:** implement the `SupabaseStore` method bodies so the membership-kit can persist members in hosted Supabase (PostgREST) instead of the local JSON/mock store — stdlib HTTP only, no third-party deps.
- **started (date -u):** Sat Jul 11 2026 (born-red first commit)

## ⟲ Previous-session review

Previous-session review: PR #16 (ORDER 003) fixed the real Stripe path — the grant reads `customer_details.email`, the success URL uses `{CHECKOUT_SESSION_ID}`, and HTTP-layer tests drive the actual `/webhook` route against VENDORED real-shape Stripe payloads with a natively-computed `Stripe-Signature`. The binding lesson carried forward: never claim an integration works on payloads authored from memory — vendor the real request/response shapes and drive them over real HTTP. This session applies that same discipline to the storage layer: the `SupabaseStore` in `server/app.py` was a documented skeleton whose four data methods (`grant`, `has_access`, `all_members`, `count`) all raised `NotImplementedError`. This session fills them against PostgREST's REST API using stdlib `urllib` only, and proves them with HTTP-layer tests against an in-process stub PostgREST server whose request/response shapes are vendored from the PostgREST + Supabase docs (not memory).

## 💡 Session idea

A storage backend cannot be verified by shapes invented from memory any more than a payment path can. Stand up an in-process stub PostgREST server that mirrors the REAL PostgREST request/response contract (verified via the PostgREST + Supabase doc sources, URLs recorded), point `SupabaseStore` at it over real HTTP, and assert: insert (POST + `Prefer: return=representation`), select (GET with `col=eq.` filters + `select=`), upsert (`Prefer: resolution=merge-duplicates` + `on_conflict=`), count (`Prefer: count=exact` → `Content-Range` total), and error handling (non-2xx → raised, never leaking the key). A live Supabase round-trip stays OWNER-GATED and is reported UNVERIFIED.

## Scope

- Fill `SupabaseStore.grant / has_access / all_members / count` in `candidates/membership-kit/server/app.py` using stdlib `urllib` PostgREST calls; auth via `apikey` + `Authorization: Bearer <SUPABASE_KEY>`. No secret VALUES anywhere; keys never logged.
- Keep MOCK/local (`STORE_BACKEND=json`) the DEFAULT; loud fallback warning (MOCK-banner style) when `STORE_BACKEND=supabase` is selected without `SUPABASE_URL`/`SUPABASE_KEY` — fall back to the local file store rather than crash.
- HTTP-layer tests against a stub PostgREST server; shapes vendored from doc sources (URLs recorded in the work log).
- OWNER-ACTION (six fields) documenting the owner's Supabase project + `members` table creation; MOCK/local stays default.
- README v0.2 + `.env.example` updates; rebuild the buyer zip (store ships inside it).

## Work log

**Prior state (evidence):** `server/app.py` `SupabaseStore` was a documented
skeleton — constructor + `_headers()` real, but `grant`/`has_access`/`all_members`/
`count` each `raise NotImplementedError(...)`. `STORE_BACKEND=json` (default
`JsonFileStore`) was the live backend.

**Implemented (server/app.py):** filled the four methods against PostgREST via
stdlib `urllib` (added `_request` + `_select_one` helpers). `grant` = idempotency
SELECT then upsert POST (`on_conflict=email`, `Prefer:
resolution=merge-duplicates,return=representation`); `has_access` = filtered
SELECT → `bool(rows)`; `all_members` = `select=email,source`; `count` =
`count=exact` + `Range: 0-0` → `Content-Range` total. Auth = `apikey` +
`Authorization: Bearer <SUPABASE_KEY>`; key never logged/echoed (errors carry
status+body). Added a shared `_loud_banner` helper; `make_store()` now warns
LOUDLY and falls back to the local JSON store when `STORE_BACKEND=supabase` is
selected without keys (never a crash, never silent); direct construction still
raises. Local `json` stays the DEFAULT.

**Vendored PostgREST/Supabase shapes (fetched, not memory):** `tables_views.rst`
(filter/select/insert/upsert), `pagination_count.rst` (`count=exact` +
`Content-Range` + `Range: 0-0`), Supabase `creating-routes.mdx` (`/rest/v1/` +
`apikey`/`Bearer`). `docs.postgrest.org`/`supabase.com` 403 through the agent
proxy, so the doc *sources* on `raw.githubusercontent.com` were used (same
pattern as the ORDER-003 Stripe fixtures). URLs recorded in
`test_supabase_store.py`.

**Tests:** new `test_supabase_store.py` — 12 HTTP-layer tests driving the store
over real HTTP against an in-process stub PostgREST server (insert, select,
upsert, count, non-2xx error handling with a no-key-leak assertion, auth headers,
idempotency, email URL-encoding). `test_membership.py` Supabase tests updated
(skeleton `NotImplementedError` → construction/auth/loud-fallback). 15 membership
+ 8 Stripe + 12 Supabase = 35 green locally and from the rebuilt buyer zip.

**Docs + packaging:** README v0.2 + `server/README.md` (method→PostgREST table +
six-field Supabase OWNER-ACTION for the project + `members` table),
`.env.example` service_role note, QUICKSTART test counts. Store ships inside the
buyer zip → `package.sh` copies `test_supabase_store.py`; `dist/membership-kit-v0.2.zip`
rebuilt (20 files). Did NOT touch `control/`, the substrate-gate workflow, or
`docs/launch/**/owner-actions.md`.

**Verified vs unverified:** VERIFIED = the PostgREST wire contract
(insert/select/upsert/count/error request+response shapes, auth headers,
idempotency, URL-encoding, loud fallback) by HTTP-layer tests against a stub
PostgREST. UNVERIFIED (OWNER-GATED) = a live round-trip against a real Supabase
project (needs the owner's project + `members` table + `SUPABASE_URL`/`SUPABASE_KEY`;
OWNER-ACTION in `server/README.md`).
