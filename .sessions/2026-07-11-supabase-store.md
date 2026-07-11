# Session — SupabaseStore bodies: implement the hosted persistence backend

> **Status:** `in-progress`

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

(filled as work proceeds — flipped to complete as the deliberate last commit)
