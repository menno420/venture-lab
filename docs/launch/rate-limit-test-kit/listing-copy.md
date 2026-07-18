# Marketplace listing copy — Rate-Limit Test Kit v0.1

> **Status:** `reference`

**Title:** Rate-Limit Test Kit — prove your 429s and Retry-After are correct

**Short description (≤200 chars, 188):** Point it at your endpoint and prove your
rate limiter: 429 at the limit (no off-by-one), a valid Retry-After, consistent
RateLimit-* headers, and a window that really resets. Stdlib only. No account.

**Price:** $29 (one-time)

## Description

A rate limiter is easy to write and easy to get subtly wrong. The `count <= limit
+ 1` off-by-one lets your "100/hour" quota pass 101. The 429 goes out with no
`Retry-After`, so clients hammer you or give up. The `X-RateLimit-Remaining`
header sits stuck at the limit, or `Reset` is a stale timestamp already in the
past. And the window that's supposed to reopen after 60 seconds quietly doesn't.
None of these show up in a green unit-test suite, because a single-request test
never crosses the boundary or waits out a window.

The Rate-Limit Test Kit points at your own API endpoint and proves the six
properties a correct server-side rate limiter must satisfy — runnable in seconds,
no vendor account, no live API, stdlib only. It is **not** a webhook-signature kit
and **not** the Idempotency Key Test Kit; it tests a third problem class:
throttling correctness. The 429 + `Retry-After` behaviour follows RFC 6585 §4 and
RFC 9110 §10.2.3; the `RateLimit-*` header fields follow the IETF draft *RateLimit
header fields for HTTP* (and the legacy `X-RateLimit-*` convention).

- **Under the limit → 2xx.** The first `limit` requests in a window succeed —
  throttling before the limit means your budget is smaller than you advertise.
- **Over the limit → 429.** Request `limit`+1 must return **429 Too Many
  Requests**. A 2xx there is the classic off-by-one quota leak.
- **A valid Retry-After.** The 429 must carry a positive, sane `Retry-After`
  (delay-seconds or a future HTTP-date) — not missing, not `0`, not a past date.
- **Honest RateLimit-* headers.** When present, `Limit`/`Remaining`/`Reset` must
  be consistent: Remaining decrements to 0 at the boundary, Reset points to the
  future. (No headers at all → fine; they're optional per the draft.)
- **The window resets.** After the advertised reset elapses, requests succeed
  again — and the advertised `Retry-After` matches when the service *actually*
  resumes, still 429 before it and 2xx after it.

## What makes it a *test* kit, not a blog post

It ships **two reference limiters**: a correct fixed-window one and a deliberately
naive one (off-by-one, a 429 with no `Retry-After`, stuck/stale headers). Run
`rltk demo` and watch the harness pass all six against the correct limiter and
*flag* the naive one on `over-limit`, `retry-after`, `headers`, and
`retry-after-honored`. That correct/broken pair is the proof the checks actually
distinguish a good limiter from a broken one — and the kit is honest that two of
the six properties (`under-limit`, `window-reset`) don't distinguish the two, so
it never overclaims.

Runs in Python or Node, entirely from the standard library. No `pip install`, no
`npm install`, no account required to run any of it.

## What's inside

- The harness in two languages: `rltk.py` (Python) and `rltk.js` (Node), same
  commands (`check`, `under-limit`, `over-limit`, `retry-after`, `headers`,
  `window-reset`, `retry-after-honored`, `demo`, `list`).
- A **correct** reference limiter (`stub_handler.py`) you can read — a thread-safe
  fixed-window counter with a short configurable window, emitting `429` +
  `Retry-After` + consistent `RateLimit-*` and legacy `X-RateLimit-*` headers.
- A **naive** limiter (`stub_handler_naive.py`) with the three classic bugs,
  shipped so the suite can prove the harness catches them.
- Two docs-derived request templates + `PROVENANCE.md` documenting every
  property's source (RFC 6585 §4, RFC 9110 §10.2.3, the RateLimit IETF draft),
  with a pinned sha256 per fixture.
- An HTTP-layer real-path test suite (`test_http_realpath.py`, 27 tests) — every
  request fired over real HTTP against a reference limiter, with a short 800 ms
  window so the timed checks stay fast.
- A one-page `GOTCHAS.md` checklist and a `QUICKSTART.md`.

## Requirements

- Python 3.8+ or Node 14+.
- No account, no dependencies, no build step.
- No secret values live in the kit; `.env.example` names optional config only.

## What it does NOT do (so you know what you're buying)

- It does **not** verify webhook signatures / HMAC (that's the Webhook Test Kits)
  and does **not** test idempotency / safe-retry (that's the Idempotency Key Test
  Kit). This is a distinct problem class: throttling correctness.
- It does **not** talk to any live API, create an account, or move money. The
  `demo` runs entirely in-process.
- It tests the **separate-header** `RateLimit-*` / `X-RateLimit-*` convention that
  most deployed APIs emit. That spec is an **IETF draft, not an RFC**, and its
  newest revisions favour a single combined structured `RateLimit:` field, which
  the kit does **not** assert. The 429 + `Retry-After` behaviour it *does* assert
  rests on stable RFCs.
- The `RateLimit-*` headers are **optional** — an endpoint that emits none passes
  the `headers` check with a note. What's non-negotiable is the 429 at the limit
  and a usable `Retry-After`.
- It tests the limiter's behaviour for the **caller it is** (one bucket, one
  client). It does not test per-user/per-IP fairness, distributed-limiter
  consistency across nodes, or your choice of algorithm — only that the
  externally-visible contract holds.
- The fixtures are **docs-derived** request templates (cited in `PROVENANCE.md`),
  not captures from a live API.

## FAQ

**Isn't a rate limiter just a counter with a TTL?**
The happy path is. The bugs are at the edges: the exact boundary (off-by-one), the
429's `Retry-After` (missing or lying), the advertised `RateLimit-*` headers
(stuck/stale), and whether the window actually reopens on schedule — none of which
a single-request unit test exercises. This kit fires exactly those edges at your
endpoint.

**Why not just read the RFCs?**
You should — and the correct behaviour is a few dozen lines once you know the
contract. What you're paying for is the harness that proves *your* endpoint
honours it (including the boundary and the reset, which take a burst and a wait),
plus the correct/naive reference pair that demonstrates the checks catch a broken
limiter. The free substitute is real; the kit is the done, runnable version.

**Refunds / support / license:** [owner-to-set — storefront defaults; suggested:
14-day no-questions refund, single-developer license, email support best-effort.]

---

## PROVENANCE-FOOTER

Every claim above is checkable against the committed source (blob `file@sha` at
build time, branch `claude/rate-limit-test-kit-2026-07-18`):

- `candidates/rate-limit-test-kit/rltk.py@cdc5293310ae1a8490caa0073777164d599d5331`
  — the harness (six properties, demo, list).
- `candidates/rate-limit-test-kit/rltk.js@722e198d81f4efbad739805583e8b56470442a55`
  — the Node parity port (same six properties + demo).
- `candidates/rate-limit-test-kit/stub_handler_naive.py@f6a70d06540ac66cc6858458e2b7ea789dc4971a`
  — the deliberately broken reference limiter (off-by-one, no Retry-After, stale
  headers — the value proof).
- `candidates/rate-limit-test-kit/test_http_realpath.py@7528352701059f2525a1789ce3d9a687668486e3`
  — the 27-test HTTP real-path suite (correct all-pass; naive flagged on 4
  properties; under-limit + window-reset honestly non-distinguishing).
- `candidates/rate-limit-test-kit/GOTCHAS.md@e84761054f069c0e84a9a97a87f83891ec2ffd10`
  — the failure modes, each mapped to a kit command.
- `candidates/rate-limit-test-kit/fixtures/PROVENANCE.md@82e3f5489d876cf6bfabe1d20009413a3ebd60d8`
  — the honest source statement (stable RFCs vs the RateLimit draft) + per-fixture
  sha256.
- `candidates/rate-limit-test-kit/dist/rate-limit-test-kit-v0.1.zip@282e1c49393f8c71e356df0aad35e5aa7bd50bf7`
  — the buyer bundle (sha256
  `908dc84be5a3e6a5be6ee72123c80cac137f1b2338018e39c6af51ef767ecd45`, 35,991
  bytes, 13 content files; byte-reproducible via `package.sh`).
