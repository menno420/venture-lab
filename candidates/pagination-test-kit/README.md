# Pagination Test Kit v0.1

Prove your API's pagination is correct — that following the next-cursor walks the
whole result set with **no skipped and no duplicated** items, stays **stable when
rows are inserted/deleted mid-traversal** (the property naive `OFFSET` pagination
fails), keeps a **consistent order**, **honors the page-size limit** and clamps an
over-max request, **signals the last page**, and **rejects a forged cursor**.
Point it at your endpoint, traverse, get PASS/FAIL per property. Stdlib only, no
dependencies, no vendor account, no live API.

This is **not** a webhook signature kit, **not** the Idempotency Key Test Kit, and
**not** the Rate-Limit Test Kit. It tests a different problem class: **result-set
integrity** of a paginated collection. There is no single RFC for cursor
pagination — it is a widely-deployed *pattern* — so the kit tests the
keyset/cursor model (Stripe/Slack/GitHub cursor pagination + the keyset-vs-offset
literature) and says so honestly. See `fixtures/PROVENANCE.md`.

## The six properties it checks

Point `pgtk` at your endpoint and it reports PASS / FAIL / SKIP for each:

1. **traversal** — following `next_cursor` from page 1 yields every item with
   **no overlap and no gap**; concatenating all pages reproduces the full ordered
   set **exactly once**.
2. **stable-under-mutation** — inserting and deleting rows **between page fetches**
   must not skip or duplicate items present throughout. This is the headline: a
   naive `OFFSET`/`LIMIT` pager skips a row when a prior row is deleted mid-walk,
   because the offset window shifts. (SKIPs cleanly if your endpoint exposes no
   test-mutation hook — see below.)
3. **ordering** — a **consistent total order**: a stable sort key plus a
   **unique tiebreaker** (e.g. `ORDER BY (created_at, id)`), no duplicate ids.
   Without a tiebreaker, tied sort values make page boundaries unstable.
4. **page-size** — the `limit` is **honored** on full pages, and a request **over
   the documented max** is **clamped** to that max (read from `X-Page-Size-Max`),
   never served unbounded — an unbounded page is a cheap DoS.
5. **terminal** — the last page **signals the end** (null/absent `next_cursor`)
   and the loop terminates — no infinite cursor loop.
6. **cursor-tamper** — a malformed or forged/opaque cursor is **rejected (4xx)**,
   not silently coerced to page 1. The correct reference stub signs its cursor so
   any tampering is detectable.

## Quickstart

Zero setup — run the built-in demo first (no accounts, no endpoint of your own):

```
python3 pgtk.py demo        # or: node pgtk.js demo
```

It spins up two bundled reference stubs in-process — a **correct** keyset pager
(all six properties PASS) and a deliberately **naive** `OFFSET` pager (which the
kit FLAGS on `stable-under-mutation`, `page-size`, and `cursor-tamper`) — and
prints the verdicts side by side. This is the kit's value proof: it distinguishes
correct keyset pagination from a broken offset one.

Then point it at your own endpoint:

```
# start your app (or the bundled correct reference pager) listening locally:
python3 stub_handler.py 8000        # keyset on (created_at, id), 12-row demo set

# run all six properties against it (tell it the page size to traverse with):
python3 pgtk.py check --url http://localhost:8000 --limit 3
```

Run a single property:

```
python3 pgtk.py traversal              --url http://localhost:8000 --limit 3
python3 pgtk.py stable-under-mutation  --url http://localhost:8000 --limit 3
python3 pgtk.py ordering               --url http://localhost:8000 --limit 3
python3 pgtk.py page-size              --url http://localhost:8000 --limit 3 --max 5
python3 pgtk.py terminal               --url http://localhost:8000 --limit 3
python3 pgtk.py cursor-tamper          --url http://localhost:8000 --limit 3
python3 pgtk.py list
```

`pgtk.js` mirrors every command via Node (stdlib only, Node 14+):

```
node pgtk.js check --url http://localhost:8000 --limit 3
node pgtk.js demo
```

## Pointing it at a REAL endpoint

- **`--limit N`** — the page size to traverse with (default 3). Use a small value
  so the dataset spans several pages.
- **`--fixture`** — which request/response template to use. `items_keyset` (the
  default) matches the bundled stubs (`/items`, `items[].id`, `next_cursor`);
  `items_pagetoken` shows a differently-named API (`page_size`/`page_token`/
  `data`/`next_page_token`). Edit `fixtures/MANIFEST.json` to match your own
  route and field names, or add your own fixture.
- **`--max N`** — your documented maximum page size, used by `page-size` when your
  endpoint sends no `X-Page-Size-Max` header.
- **The `stable-under-mutation` check needs a way to mutate the dataset
  mid-traversal.** The bundled stubs expose `POST /_debug/insert`,
  `POST /_debug/delete`, `POST /_debug/reset`, and `GET /_debug/all` (ground
  truth) so the harness can drive a controlled insert+delete between page fetches.
  A real endpoint usually has no such routes — so this one property **SKIPs** (it
  is neither passed nor failed) with a note. To exercise it against your API, run
  it against a **seeded test dataset you can mutate** (a test DB with equivalent
  test hooks), which is exactly where the offset-vs-keyset difference bites. The
  other five properties run against any read-only paginated endpoint.
- **Use a read-safe collection.** The harness sends real GET requests; point it at
  a listing route, not one that charges money or mutates state.

## What's inside

- The harness in two languages: `pgtk.py` (Python) and `pgtk.js` (Node), same
  commands (`check`, the six single-property checks, `demo`, `list`).
- A **correct** reference pager (`stub_handler.py`) you can read — keyset
  pagination over a sortable 12-row dataset on `(created_at, id)`, an opaque
  **HMAC-signed** cursor, an `X-Page-Size-Max` clamp, and `/_debug/*` hooks for
  the mutation test.
- A deliberately **naive** pager (`stub_handler_naive.py`) with the classic bugs —
  `OFFSET`/`LIMIT` pagination that skips under mutation, no over-max clamp, and a
  forged cursor served as page 1 — shipped so the test suite can prove the harness
  catches them.
- Two docs-derived request/response templates (`items_keyset`, `items_pagetoken`)
  + `fixtures/PROVENANCE.md` grounding every property in its source (the
  keyset/cursor pattern, Stripe/Slack/GitHub cursor docs, the keyset-vs-offset
  literature) and pinning a sha256 per fixture.
- An HTTP-layer real-path test suite (`test_http_realpath.py`, 31 tests) — every
  request fired over real HTTP against a reference pager on an ephemeral port; no
  timed waits, so it runs fast.
- A one-page `GOTCHAS.md` checklist and a `QUICKSTART.md`.

## Run the kit's own tests

```
python3 -m unittest -v
```

Every request is fired over actual HTTP to a reference pager on an ephemeral port.
All green = the kit is intact on your machine.

## What it does NOT do (so you know what you're buying)

- It does **not** verify webhook signatures / HMAC (the Webhook Test Kits), test
  idempotency / safe-retry (the Idempotency Key Test Kit), or test throttling /
  rate limits (the Rate-Limit Test Kit). This is a distinct problem class:
  result-set integrity across pages.
- It does **not** talk to any live API, create an account, or move money. The
  `demo` runs entirely in-process against bundled stubs.
- It tests the **keyset/cursor** model (an opaque cursor over a
  `(sort_key, unique_id)` order). There is **no single RFC** for cursor
  pagination — the kit's sources are the common pattern and named vendor docs,
  cited honestly in `PROVENANCE.md`. It does not prescribe *how* your cursor is
  encoded (signed token, stored cursor, encoded position) — only the
  externally-visible behaviour (no skip/dupe, a bad cursor rejected, a clamp, a
  terminal signal).
- The `stable-under-mutation` property needs a test-mutation hook (the bundled
  stubs have one). Against a read-only real endpoint it **SKIPs** rather than
  falsely passing or failing — run it against a seeded, mutable test dataset.
- It tests the collection **as one ordered set from one caller**. It does not test
  per-user visibility filtering, sharded/parallel cursor consistency, or your
  choice of storage — only that the externally-visible pagination contract holds.
- The fixtures are **docs-derived** templates (cited in `PROVENANCE.md`), not
  captures from a live API.

## Requirements

- Python 3.8+ (for `pgtk.py`, the stubs, the tests) or Node 14+ (for `pgtk.js`).
- No account, no `pip install`, no `npm install`.
- No secret values live in this kit; `.env.example` names optional config only.
