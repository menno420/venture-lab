# Marketplace listing copy — Idempotency Key Test Kit v0.1

> **Status:** `reference`

**Title:** Idempotency Key Test Kit — prove a retry can't charge twice

**Short description (≤200 chars, 190):** Point it at your endpoint and prove your
Idempotency-Key handling: safe retries run once, same-key/different-body is
rejected, concurrent retries don't double-charge. Stdlib only. No account.

**Price:** $29 (one-time)

## Description

A network timeout is not a failed request — it's an *unknown* one. Your client
retries, and if your endpoint isn't idempotent, the customer is charged twice.
The bug is invisible in a green unit-test suite, because a unit test never fires
two concurrent requests with the same key.

The Idempotency Key Test Kit points at your own `POST` endpoint and proves the
five properties a correct `Idempotency-Key` implementation must satisfy —
runnable in seconds, no vendor account, no live API, stdlib only. It is **not** a
webhook-signature kit; it tests the outbound half of a payments integration: the
dedup / safe-retry contract that makes your own writes safe to retry. Behaviour
follows Stripe's widely-used model (the header is the subject of the IETF draft
*The Idempotency-Key HTTP Header Field*).

- **Replay = exactly once.** Same key + same body must replay the *stored*
  original response — same resource id, no second side effect. The kit fires the
  retry and checks the id didn't change; a new id means you double-charged.
- **Same key, different body = rejected.** Reusing a key with a mismatched
  payload must return 409/422, not silently serve the old result or run again.
- **Different keys = independent.** Two different keys with the same body must
  both execute — collapsing them means you're keying on the body, and dropping
  real requests.
- **Concurrency needs a lock.** Two in-flight requests with the same key must
  produce one side effect. Without an in-flight lock, both pass the "is it
  stored yet?" check and both execute — a retry-storm double charge. The kit
  fires them simultaneously and counts the resources created.
- **Missing key = your documented policy.** No key header → reject (4xx) or
  pass through (2xx). You tell the kit which; it never guesses silently.

## What makes it a *test* kit, not a blog post

It ships **two reference endpoints**: a correct one and a deliberately naive
(no-dedup) one. Run `ikt demo` and watch the harness pass all five against the
correct endpoint — with a side-effect counter proving exactly-once — and *flag*
the naive one on replay, mismatch, concurrency, and missing-key. That correct/
broken pair is the proof the checks actually distinguish good idempotency from
the double-charge bug, not just rubber-stamping a happy path.

Runs in Python or Node, entirely from the standard library. No `pip install`, no
`npm install`, no account required to run any of it.

## What's inside

- The harness in two languages: `ikt.py` (Python) and `ikt.js` (Node), same
  commands (`check`, `replay`, `mismatch`, `distinct-keys`, `concurrent`,
  `missing-key`, `demo`, `list`).
- A **correct** reference endpoint (`stub_handler.py`) you can adapt — an
  in-memory store keyed on `(method, path, Idempotency-Key)` with a request
  fingerprint + the stored response, a per-key in-flight lock, 422 on a
  fingerprint mismatch, a configurable missing-key policy, and a
  `GET /_debug/side_effects` counter.
- A **naive** endpoint (`stub_handler_naive.py`) with no dedup — the bug in the
  flesh, shipped so the suite can prove the harness catches it.
- Three docs-derived request fixtures + `PROVENANCE.md` documenting every
  behaviour's source (Stripe's idempotency docs + the IETF header draft), with a
  pinned sha256 per fixture.
- An HTTP-layer real-path test suite (`test_http_realpath.py`, 20 tests) — every
  request POSTed over real HTTP, with a side-effect counter proving exactly-once.
- A one-page `GOTCHAS.md` checklist and a `QUICKSTART.md`.

## Requirements

- Python 3.8+ or Node 14+.
- No account, no dependencies, no build step.
- No secret values live in the kit; `.env.example` names optional config only.

## What it does NOT do (so you know what you're buying)

- It does **not** verify webhook signatures / HMAC — that's the Webhook Test
  Kits. This is the opposite direction: making your own writes safe to retry.
- It does **not** talk to Stripe or any live API, create an account, or move
  money. The `demo` runs entirely in-process.
- It does **not** validate your business logic — only the idempotency edge
  behaviour of your endpoint.
- It tests the **Stripe-style model.** The IETF draft standardises the header,
  not one mandated status code, so the exact codes (409/422 for a conflict, 400
  for a missing key under `required`) follow Stripe's documented behaviour. If
  your API documents different codes, adjust the expectation — the missing-key
  mode is configurable and the conflict check accepts 409 or 422.
- **Expiry** (stored responses time out — Stripe documents 24h) is documented in
  `GOTCHAS.md` but not asserted against a live endpoint (it would require waiting
  out the TTL). The in-process properties the kit *can* prove, it proves.
- The fixtures are **docs-derived** (cited file-by-file in `PROVENANCE.md`), not
  captures from a live API.

## FAQ

**Isn't idempotency just a dictionary keyed on the header?**
The happy path is. The bugs are in the edges: the fingerprint check (same key,
different body), the in-flight lock (two concurrent retries), and the expiry/
storage model — and the concurrency bug in particular never shows up in a
single-threaded unit test. This kit fires exactly those edges at your endpoint.

**Why not just read Stripe's docs?**
You should — and the correct implementation is a few dozen lines once you know
the contract. What you're paying for is the harness that proves *your* endpoint
honours it (including the concurrency case), plus the correct/naive reference
pair that demonstrates the checks catch a broken implementation. The free
substitute is real; the kit is the done, runnable version.

**Refunds / support / license:** [owner-to-set — storefront defaults;
suggested: 14-day no-questions refund, single-developer license, email support
best-effort.]

---

## PROVENANCE-FOOTER

Every claim above is checkable against the committed source (blob `file@sha`
at build time, branch `claude/idempotency-key-test-kit-2026-07-18`):

- `candidates/idempotency-key-test-kit/ikt.py@4fc4e8bd7ae910f774f26d8cc7df83c57ab4d073`
  — the harness (five properties, demo, list).
- `candidates/idempotency-key-test-kit/stub_handler_naive.py@8252787e8d9694cd18f8372f45e2e983854f3a7e`
  — the deliberately no-dedup reference endpoint (the value proof).
- `candidates/idempotency-key-test-kit/test_http_realpath.py@22c6b35c58a9189cb4c97879b189247876234cf0`
  — the 20-test HTTP real-path suite (correct all-pass + exactly-once counter;
  naive flagged on 4 properties).
- `candidates/idempotency-key-test-kit/GOTCHAS.md@53c16ec8e7f0432e3956591d5c61cd61053e0b52`
  — the five failure modes, each mapped to a kit command.
- `candidates/idempotency-key-test-kit/fixtures/PROVENANCE.md@bee05936a6fa10e76c3cada86718a549b51869f2`
  — the honest source statement (Stripe model vs IETF draft) + per-fixture
  sha256.
- `candidates/idempotency-key-test-kit/dist/idempotency-key-test-kit-v0.1.zip@861368173920e0e23a9455e041745c80c3db2440`
  — the buyer bundle (sha256
  `8607803d5fd7286e9f86f1515981ea1ca6052ae06d7a8d417526dd85a796f6e1`,
  32,925 bytes, 14 content files; byte-reproducible via `package.sh`).
