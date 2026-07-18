# Quickstart — Pagination Test Kit v0.1

Three minutes from unzip to a green check on your own endpoint. Stdlib only — no
`pip install`, no `npm install`, no account.

## 0. See the kit work (offline, no endpoint of your own)

```
python3 pgtk.py demo      # or: node pgtk.js demo
```

This spins up two bundled reference pagers in-process — a **correct** keyset one
and a deliberately **naive** `OFFSET` one — runs all six properties against each,
and prints the verdicts. Expect: the correct pager PASSES all six; the naive one
is FLAGGED on `stable-under-mutation` (the offset skip when a prior row is deleted
mid-walk), `page-size` (an over-max `limit` served unbounded), and `cursor-tamper`
(a forged cursor served as page 1). It is honestly NOT flagged on `traversal`,
`ordering`, or `terminal` — those three don't distinguish the two pagers in a
static dataset, and the kit says so. No accounts, no network, no money.

## 1. Start an endpoint

Either your own app, or the bundled correct reference pager:

```
python3 stub_handler.py 8000
```

It listens on `http://127.0.0.1:8000`, serves a 12-row demo set ordered by
`(created_at, id)` at `GET /items?limit=N&cursor=<opaque>`, clamps `limit` to a
documented max of 5 (`X-Page-Size-Max`; set `PGTK_MAX`), and exposes
`GET /_debug/all`, `POST /_debug/reset`, `POST /_debug/insert`, and
`POST /_debug/delete` for the mutation test.

## 2. Run the full check

```
python3 pgtk.py check --url http://localhost:8000 --limit 3
```

Expect all six properties `PASS` (or `SKIP` for `stable-under-mutation` against an
endpoint without the mutation hooks). Each `FAIL` line names the exact bug and
points at `GOTCHAS.md`.

## 3. Run one property at a time

```
python3 pgtk.py traversal              --url http://localhost:8000 --limit 3   # no overlap / no gap
python3 pgtk.py stable-under-mutation  --url http://localhost:8000 --limit 3   # no skip/dupe mid-walk
python3 pgtk.py ordering               --url http://localhost:8000 --limit 3   # total order + tiebreaker
python3 pgtk.py page-size              --url http://localhost:8000 --limit 3 --max 5
python3 pgtk.py terminal               --url http://localhost:8000 --limit 3   # last page ends the walk
python3 pgtk.py cursor-tamper          --url http://localhost:8000 --limit 3   # forged cursor -> 4xx
```

The Node port is identical: `node pgtk.js check --url http://localhost:8000 --limit 3`.

## 4. Against your own API

- Point `--fixture` (or edit the entry in `fixtures/MANIFEST.json`) at your route
  and field names: the collection `path`, the `limit_param` / `cursor_param` query
  names, and the `items_field` / `next_cursor_field` / `id_field` / `sort_field`
  response fields. The bundled `items_pagetoken` fixture shows a
  `page_size`/`page_token`/`data`/`next_page_token` API for reference.
- Set `--max` to your documented maximum page size if your endpoint sends no
  `X-Page-Size-Max` header.
- `stable-under-mutation` needs a way to insert/delete rows mid-traversal. On a
  read-only endpoint it **SKIPs** (neither pass nor fail). To exercise it, run
  against a **seeded test dataset** with equivalent test hooks — that is exactly
  where offset pagination breaks and keyset holds.

## 5. Run the kit's own test suite

```
python3 -m unittest -v
```

Every request is fired over actual HTTP to a reference pager on an ephemeral port;
no timed waits, so it finishes fast. All green = the kit is intact on your machine.

---

Next: read `GOTCHAS.md` (one page, the failure modes) and adapt `stub_handler.py`
into your framework of choice.
