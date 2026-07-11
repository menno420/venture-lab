# Session — kit-tests CI: run the SupabaseStore suite

> **Status:** `complete`

- **📊 Model:** claude-fable-5 · medium · ci-maintenance
- **session:** extend the HOST-OWNED `kit-tests` workflow so the new
  `test_supabase_store` module (landed in PR #23) runs in CI alongside
  `test_membership` and `test_http_realpath` — 35 tests total.
- **started (date -u):** Sat Jul 11 2026 (born-red first commit)

## ⟲ Previous-session review

Previous-session review: PR #23 (SupabaseStore) filled the four stub
`SupabaseStore` methods in `candidates/membership-kit/server/app.py` and added
`server/test_supabase_store.py` — 12 HTTP-layer tests against an in-process
stub PostgREST server with vendored request/response shapes. That branch
predated nothing in the gate, but the kit-tests workflow invocation on `main`
still runs only `test_membership test_http_realpath` (23 tests), so the new
suite is green locally and inside the buyer zip but NOT enforced as a named CI
check. Lesson carried forward: a suite that CI never runs is a suite that can
rot silently — the enforcement wire must follow the tests in.

## 💡 Session idea

The kit-tests check exists precisely so candidate suites are ENFORCED, not
merely present. One-line closure: add `test_supabase_store` to the unittest
module list in `.github/workflows/kit-tests.yml` so the full 35-test
membership-kit server suite (15 membership + 8 real-path HTTP + 12 Supabase)
reds the check on any failure.

## Scope

- `.github/workflows/kit-tests.yml`: extend the unittest invocation in
  `candidates/membership-kit/server` to
  `python3 -m unittest test_membership test_http_realpath test_supabase_store -v`.
- This card. Nothing else — no `control/`, no `docs/launch/`, no kit code.

## Work log

- Born-red first commit: workflow edit + this card.
- Edited `.github/workflows/kit-tests.yml`: unittest invocation now runs
  `test_membership test_http_realpath test_supabase_store` (step name updated
  to mention SupabaseStore). No other workflow changes.
- Verified locally in `candidates/membership-kit/server`:
  `python3 -m unittest test_membership test_http_realpath test_supabase_store -v`
  → `Ran 35 tests ... OK`.
- `python3 bootstrap.py check --strict --session-log .sessions/2026-07-11-kit-tests-supabase-ci.md`
  green before push.
- Close-out commit flips this card to `complete`; PR merges once
  substrate-gate AND kit-tests are green on the head (kit-tests must show the
  full 35-test suite).
