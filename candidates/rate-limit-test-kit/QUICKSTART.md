# Quickstart — Rate-Limit Test Kit v0.1

Three minutes from unzip to a green check on your own endpoint. Stdlib only — no
`pip install`, no `npm install`, no account.

## 0. See the kit work (offline, no endpoint of your own)

```
python3 rltk.py demo      # or: node rltk.js demo
```

This spins up two bundled reference limiters in-process — a **correct**
fixed-window one and a deliberately **naive** one — runs all six properties
against each, and prints the verdicts. Expect: the correct limiter PASSES all six;
the naive one is FLAGGED on `over-limit` (off-by-one), `retry-after` (429 with no
`Retry-After`), `headers` (stuck/stale `X-RateLimit-*`), and
`retry-after-honored`. It is honestly NOT flagged on `under-limit` or
`window-reset` — those two properties don't distinguish the two limiters, and the
kit says so. No accounts, no network, no money.

## 1. Start an endpoint

Either your own app, or the bundled correct reference limiter:

```
python3 stub_handler.py 8000
```

It listens on `http://127.0.0.1:8000`, limits **5 requests per 1000 ms** by
default (set `RLTK_LIMIT` / `RLTK_WINDOW_MS`), and exposes `POST /_debug/reset`
and `GET /_debug/state`.

## 2. Tell the kit your limit

The kit needs to know your per-window budget to find the boundary:

- `--limit 5` — you allow 5 requests per window.
- If you don't know it, the kit reads it from a `RateLimit-Limit` header when your
  endpoint sends one.

## 3. Run the full check

```
python3 rltk.py check --url http://localhost:8000 --limit 5
```

Expect all six properties `PASS`. Each `FAIL` line names the exact bug and points
at `GOTCHAS.md`.

## 4. Run one property at a time

```
python3 rltk.py under-limit          --url http://localhost:8000 --limit 5   # first 5 → 2xx
python3 rltk.py over-limit           --url http://localhost:8000 --limit 5   # 6th → 429 (no off-by-one)
python3 rltk.py retry-after          --url http://localhost:8000 --limit 5   # 429 carries a sane Retry-After
python3 rltk.py headers              --url http://localhost:8000 --limit 5   # RateLimit-* consistent
python3 rltk.py window-reset         --url http://localhost:8000 --limit 5 --window 1
python3 rltk.py retry-after-honored  --url http://localhost:8000 --limit 5
```

The Node port is identical: `node rltk.js check --url http://localhost:8000 --limit 5`.

## 5. Against a real endpoint without a debug-reset route

The bundled stubs reset cleanly between checks. A real endpoint won't have a
`/_debug/reset` route, so start each burst in a fresh window by sleeping one
window first:

```
python3 rltk.py check --url https://api.example.com --limit 100 --settle 60 --window 60
```

Point `--fixture` (or the path in `fixtures/MANIFEST.json`) at a **cheap,
burst-safe** route behind the same limiter — a health/ping endpoint — never one
that charges money or mutates state.

## 6. Run the kit's own test suite

```
python3 -m unittest -v
```

Every request is fired over actual HTTP to a reference limiter on an ephemeral
port; a short 800 ms window keeps the timed checks fast. All green = the kit is
intact on your machine.

---

Next: read `GOTCHAS.md` (one page, the failure modes) and adapt `stub_handler.py`
into your framework of choice.
