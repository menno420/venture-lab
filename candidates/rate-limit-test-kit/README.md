# Rate-Limit Test Kit v0.1

Prove your API's rate limiter behaves correctly — that it returns **429** at the
limit (not one request late), emits a valid **`Retry-After`** so clients know when
to come back, keeps its **`RateLimit-*` headers** honest, and actually **resets**
its window when it says it will. Point it at your endpoint, fire a burst, get
PASS/FAIL per property. Stdlib only, no dependencies, no vendor account, no live
API.

This is **not** a webhook signature kit and **not** the Idempotency Key Test Kit.
It tests a different problem class: **throttling correctness**. The 429 +
`Retry-After` semantics follow RFC 6585 §4 and RFC 9110 §10.2.3; the
`RateLimit-Limit`/`Remaining`/`Reset` header fields follow the IETF draft
*RateLimit header fields for HTTP* (and the legacy `X-RateLimit-*` convention) —
which is a **draft, not yet an RFC**, and the kit is explicit about that. See
`fixtures/PROVENANCE.md`.

## The six properties it checks

Point `rltk` at your endpoint and it reports PASS/FAIL for each:

1. **under-limit** — the first `limit` requests inside a window return **2xx**.
   Throttling *before* the limit means your limit is effectively lower than you
   advertise.
2. **over-limit** — request number `limit`+1 within the window returns **429**. A
   2xx there is an **off-by-one quota leak**: your "100/hour" actually lets 101
   through.
3. **retry-after** — that 429 carries a `Retry-After` that is a **positive, sane**
   delay-seconds *or* a future HTTP-date. Missing / `0` / negative / absurd means
   a client can't know when to retry — it hammers you or gives up.
4. **headers** — `RateLimit-*` / `X-RateLimit-*` headers, **when present**, are
   consistent: `Limit` is a positive integer, `Remaining` decrements and hits
   **0 exactly at the 429 boundary**, `Reset` points into the **future**. (No
   such headers at all → passes with a note; they're optional per the draft.)
5. **window-reset** — after the advertised reset elapses, requests **succeed
   again**. A limiter that never resets is a FAIL.
6. **retry-after-honored** — the advertised `Retry-After` **matches when the
   service actually resumes**: still 429 just before it, 2xx just after it
   (within tolerance). A `Retry-After` that lies is worse than none.

## Quickstart

Zero setup — run the built-in demo first (no accounts, no endpoint of your own):

```
python3 rltk.py demo        # or: node rltk.js demo
```

It spins up two bundled reference limiters in-process — a **correct** fixed-window
one (all six properties PASS) and a deliberately **naive** one (off-by-one, a 429
with no `Retry-After`, and stale/stuck `X-RateLimit-*` headers, which the kit
FLAGS) — and prints the verdicts side by side. This is the kit's value proof: it
distinguishes a correct limiter from a broken one.

Then point it at your own endpoint:

```
# start your app (or the bundled correct reference limiter) listening locally:
python3 stub_handler.py 8000        # limit 5 / 1000ms window by default

# run all six properties against it (tell it your per-window budget):
python3 rltk.py check --url http://localhost:8000 --limit 5
```

Run a single property:

```
python3 rltk.py under-limit          --url http://localhost:8000 --limit 5
python3 rltk.py over-limit           --url http://localhost:8000 --limit 5
python3 rltk.py retry-after          --url http://localhost:8000 --limit 5
python3 rltk.py headers              --url http://localhost:8000 --limit 5
python3 rltk.py window-reset         --url http://localhost:8000 --limit 5 --window 1
python3 rltk.py retry-after-honored  --url http://localhost:8000 --limit 5
python3 rltk.py list
```

`rltk.js` mirrors every command via Node (stdlib only, Node 14+):

```
node rltk.js check --url http://localhost:8000 --limit 5
node rltk.js demo
```

## Pointing it at a REAL endpoint

- **`--limit N`** — your per-window budget. If you don't know it, the kit reads it
  from a `RateLimit-Limit` header when your endpoint sends one.
- **`--fixture`** — which request template to replay (`api_ping` GET by default,
  or `api_write` POST). Edit `fixtures/MANIFEST.json` to point the path at your
  own route, or add your own fixture.
- **`--window S`** — the reset-wait fallback (seconds) used by `window-reset` when
  there's no `Retry-After` to read.
- **`--settle S`** — the bundled stubs expose `POST /_debug/reset`, so each check
  starts in a fresh window automatically. A real endpoint has no such route, so
  pass `--settle <window-seconds>` to sleep one window before each burst and start
  clean.
- **Use a route where a burst is safe.** The harness sends real requests; point it
  at a cheap idempotent probe (a health/ping route behind the same limiter), not
  a route that charges money or mutates state.

## What's inside

- The harness in two languages: `rltk.py` (Python) and `rltk.js` (Node), same
  commands (`check`, the six single-property checks, `demo`, `list`).
- A **correct** reference limiter (`stub_handler.py`) you can read — a thread-safe
  fixed-window counter with a short configurable window, emitting `429` +
  `Retry-After` + consistent `RateLimit-*` **and** legacy `X-RateLimit-*` headers.
- A deliberately **naive** limiter (`stub_handler_naive.py`) with the three
  classic bugs — off-by-one, a 429 with no `Retry-After`, and stuck/stale
  `X-RateLimit-*` headers — shipped so the test suite can prove the harness
  catches them.
- Two docs-derived request templates (`api_ping`, `api_write`) +
  `fixtures/PROVENANCE.md` citing every property to its source (RFC 6585 / RFC
  9110 / the RateLimit draft) and pinning a sha256 per fixture.
- An HTTP-layer real-path test suite (`test_http_realpath.py`, 27 tests) — every
  request fired over real HTTP against a reference limiter on an ephemeral port,
  with a short 800 ms window so the timed checks stay fast.
- A one-page `GOTCHAS.md` checklist and a `QUICKSTART.md`.

## Run the kit's own tests

```
python3 -m unittest -v
```

Every request is fired over actual HTTP to a reference limiter on an ephemeral
port. All green = the kit is intact on your machine (takes a few seconds — two of
the properties wait out a real window).

## What it does NOT do (so you know what you're buying)

- It does **not** verify webhook signatures / HMAC — that's the Webhook Test Kits
  — and it does **not** test idempotency / safe-retry — that's the Idempotency Key
  Test Kit. This is a distinct problem class: throttling correctness.
- It does **not** talk to any live API, create an account, or move money. The
  `demo` runs entirely in-process against bundled stubs.
- It tests the **separate-header** `RateLimit-*` / `X-RateLimit-*` convention —
  the one most deployed APIs emit. The RateLimit header spec is an **IETF draft,
  not an RFC**, and its newest revisions favour a single combined structured
  `RateLimit:` field, which the kit does **not** assert. The 429 + `Retry-After`
  behaviour it *does* assert rests on stable RFCs (6585, 9110).
- The `RateLimit-*` headers are **optional**: an endpoint that emits none passes
  the `headers` check with a note. What's non-negotiable is the 429 at the limit
  and a usable `Retry-After`.
- It tests the limiter's behaviour **for the caller it is** (a single bucket from
  one client). It does not test per-user/per-IP fairness, distributed-limiter
  consistency across nodes, or your choice of algorithm (fixed-window vs token
  bucket vs sliding log) — only that the externally-visible contract holds.
- The fixtures are **docs-derived** request templates (cited in
  `PROVENANCE.md`), not captures from a live API.

## Requirements

- Python 3.8+ (for `rltk.py`, the stubs, the tests) or Node 14+ (for `rltk.js`).
- No account, no `pip install`, no `npm install`.
- No secret values live in this kit; `.env.example` names optional config only.
