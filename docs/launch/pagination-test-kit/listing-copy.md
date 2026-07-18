# Marketplace listing copy — Pagination Test Kit v0.1

> **Status:** `reference`

**Title:** Pagination Test Kit — prove your cursor pagination doesn't skip or duplicate rows

**Short description (≤200 chars, 197):** Point it at your endpoint and prove your
pagination: no skipped/duplicated rows, stable when rows change mid-traversal
(where OFFSET fails), a consistent order, a clamped page size, a terminal signal,
a forged cursor rejected. Stdlib. No account.

**Price:** $29 (one-time)

## Description

Pagination is easy to write and easy to get subtly wrong. `LIMIT n OFFSET k` looks
fine in every test — until a row is inserted or deleted between page fetches and
the offset window shifts, silently **skipping** or **duplicating** rows in every
export, sync, and "load more" scroll. The cursor is a raw offset or id the client
can forge; a garbage cursor gets coerced to page 1 instead of a 400; `?limit=100000`
returns the whole table. None of these show up in a green unit-test suite, because
a single static-fixture test never mutates the dataset mid-traversal or crosses the
boundary.

The Pagination Test Kit points at your own paginated endpoint and proves the six
properties correct cursor/keyset pagination must satisfy — runnable in seconds, no
vendor account, no live API, stdlib only. It is **not** a webhook-signature kit,
**not** the Idempotency Key Test Kit, and **not** the Rate-Limit Test Kit; it tests
a fourth problem class: **result-set integrity**. There is no single RFC for cursor
pagination — it's a widely-deployed pattern — so the kit tests the keyset/cursor
model (Stripe/Slack/GitHub cursor pagination + the keyset-vs-offset literature) and
says so honestly.

- **No overlap, no gap.** Following `next_cursor` from page 1 yields every item
  exactly once — concatenating all pages reproduces the full ordered set.
- **Stable under mutation.** Inserting/deleting rows *between* page fetches must not
  skip or duplicate items present throughout. This is the headline: OFFSET
  pagination fails it; keyset pagination passes.
- **A consistent order.** A stable sort key plus a **unique tiebreaker** (order by
  `(created_at, id)`), so tied sort values don't scramble page boundaries.
- **A clamped page size.** `limit` is honored up to a documented max and anything
  larger is clamped (`X-Page-Size-Max`) — an unbounded page is a cheap DoS.
- **A terminal signal.** The last page returns a null/absent cursor; the loop
  terminates instead of spinning forever.
- **A rejected forged cursor.** A malformed or tampered cursor returns **4xx**, not
  a silently-wrong page 1.

## What makes it a *test* kit, not a blog post

It ships **two reference pagers**: a correct keyset one and a deliberately naive
OFFSET one (skips under mutation, no clamp, forged cursor served as page 1). Run
`pgtk demo` and watch the harness pass all six against the correct pager and *flag*
the naive one on `stable-under-mutation`, `page-size`, and `cursor-tamper`. That
correct/broken pair is the proof the checks actually distinguish a good pager from a
broken one — and the kit is honest that three of the six properties (`traversal`,
`ordering`, `terminal`) don't distinguish the two in a static dataset, so it never
overclaims.

Runs in Python or Node, entirely from the standard library. No `pip install`, no
`npm install`, no account required to run any of it.

## What's inside

- The harness in two languages: `pgtk.py` (Python) and `pgtk.js` (Node), same
  commands (`check`, `traversal`, `stable-under-mutation`, `ordering`, `page-size`,
  `terminal`, `cursor-tamper`, `demo`, `list`).
- A **correct** reference pager (`stub_handler.py`) you can read — keyset pagination
  over a 12-row dataset on `(created_at, id)`, an opaque **HMAC-signed** cursor, an
  `X-Page-Size-Max` clamp, and `/_debug/*` hooks for the mutation test.
- A **naive** pager (`stub_handler_naive.py`) with the classic bugs, shipped so the
  suite can prove the harness catches them.
- Two docs-derived request/response templates + `PROVENANCE.md` grounding every
  property in its source (the keyset/cursor pattern, Stripe/Slack/GitHub cursor
  docs, the keyset-vs-offset literature), with a pinned sha256 per fixture.
- An HTTP-layer real-path test suite (`test_http_realpath.py`, 31 tests) — every
  request fired over real HTTP against a reference pager; no timed waits, so it runs
  fast.
- A one-page `GOTCHAS.md` checklist and a `QUICKSTART.md`.

## Requirements

- Python 3.8+ or Node 14+.
- No account, no dependencies, no build step.
- No secret values live in the kit; `.env.example` names optional config only.

## What it does NOT do (so you know what you're buying)

- It does **not** verify webhook signatures / HMAC (that's the Webhook Test Kits),
  test idempotency / safe-retry (the Idempotency Key Test Kit), or test throttling /
  rate limits (the Rate-Limit Test Kit). This is a distinct problem class: result-set
  integrity across pages.
- It does **not** talk to any live API, create an account, or move money. The `demo`
  runs entirely in-process.
- It tests the **keyset/cursor** model. There is **no single RFC** for cursor
  pagination — the sources are the common pattern and named vendor docs, cited
  honestly in `PROVENANCE.md`. It does not prescribe *how* your cursor is encoded
  (signed token, stored cursor, encoded position) — only the externally-visible
  behaviour.
- The `stable-under-mutation` property needs a test-mutation hook (the bundled stubs
  have one). Against a read-only real endpoint it **SKIPs** rather than falsely
  passing or failing — run it against a seeded, mutable test dataset.
- It tests the collection **as one ordered set from one caller** — not per-user
  visibility filtering, cross-shard cursor consistency, or your storage choice.
- The fixtures are **docs-derived** templates (cited in `PROVENANCE.md`), not
  captures from a live API.

## FAQ

**Isn't pagination just `LIMIT` and `OFFSET`?**
That's exactly the bug. Offset pagination is a position *by count*, so it skips or
duplicates rows the moment the dataset changes under it — invisible until a real
insert/delete lands mid-traversal. Keyset (cursor) pagination names a *row position*
and is stable. This kit reproduces the exact mutation that exposes the offset bug and
proves your endpoint is on the right side of it.

**Why not just read a keyset-pagination blog post?**
You should — and correct keyset pagination is a few dozen lines once you know to use
a composite key. What you're paying for is the harness that proves *your* endpoint
honours it (including the mid-traversal mutation and the forged-cursor rejection a
from-memory test skips), plus the correct/naive reference pair that demonstrates the
checks catch a broken pager. The free substitute is real; the kit is the done,
runnable version.

**Refunds / support / license:** [owner-to-set — storefront defaults; suggested:
14-day no-questions refund, single-developer license, email support best-effort.]

---

## PROVENANCE-FOOTER

Every claim above is checkable against the committed source (blob `file@sha` at
build time, branch `claude/pagination-test-kit-2026-07-18`):

- `candidates/pagination-test-kit/pgtk.py@3d09b5c64be00d8dc2f29bd8f1c789eb40cb0d70`
  — the harness (six properties, demo, list).
- `candidates/pagination-test-kit/pgtk.js@33895f364cc01d005d5b6db61ce4fe740e38a754`
  — the Node parity port (same six properties + demo).
- `candidates/pagination-test-kit/stub_handler_naive.py@85255b9b7f63f787fa134a37c67e0b0d17e97ee9`
  — the deliberately broken reference pager (OFFSET skip under mutation, no clamp,
  forged cursor served as page 1 — the value proof).
- `candidates/pagination-test-kit/test_http_realpath.py@a85612efd5450c75d63f7bdfe16f9f5c126a3613`
  — the 31-test HTTP real-path suite (correct all-pass; naive flagged on 3
  properties; traversal + ordering + terminal honestly non-distinguishing; the
  SKIP path for stability without mutation hooks; cursor sign/verify units).
- `candidates/pagination-test-kit/GOTCHAS.md@b2c2d356480fc7917e89d0cc63826445b19b695e`
  — the failure modes, each mapped to a kit command.
- `candidates/pagination-test-kit/fixtures/PROVENANCE.md@6f2a71835d07d462bcf6ce608bfde048c23d894b`
  — the honest source statement (no single RFC; the keyset/cursor pattern + named
  vendor docs) + per-fixture sha256.
- `candidates/pagination-test-kit/dist/pagination-test-kit-v0.1.zip@960f1caf879d61fb6c4c63f3384f5a4d2ef44449`
  — the buyer bundle (sha256
  `ae189fe9465dc7a27204c84b5e187e475fb25158c0f6c31033701fc2e970a118`, 42,827
  bytes, 13 content files; byte-reproducible via `package.sh`).
