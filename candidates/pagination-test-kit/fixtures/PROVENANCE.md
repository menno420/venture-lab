# Fixture provenance

**Honest statement up front:** the templates in this directory are
**docs-derived** — representative request/response shapes (a page of items with a
`next_cursor`), not captures from a live API. A pagination test is about
**result-set integrity across pages**, not the body shape, so these fixtures exist
to describe the request/response contract the harness traverses; they carry
clearly-fake demo markers. No account was created, no API key was used, and no
real service was called to build this kit (this repo's no-new-accounts rule).
Every pagination behaviour this kit checks is grounded in the public sources
below, so a buyer can audit each claim.

> Reconstructed 2026-07-18 (UTC). Payload shapes are illustrative; they are
> REQUEST/RESPONSE templates (path + param names + item/cursor fields), not real
> records.

## Honest scope: which model does this kit test?

Unlike the 429 + `Retry-After` behaviour the sibling Rate-Limit kit tests, there
is **no single RFC for cursor pagination**. It is a widely-deployed *pattern*, not
a ratified standard, and this kit is explicit about that. The model the kit tests
is **keyset (a.k.a. cursor / seek) pagination**: rows are totally ordered by a
stable sort key plus a **unique tiebreaker**, and a page is "the next N rows
strictly after the position named by an opaque cursor," rather than
**offset/limit** pagination ("skip N rows, take the next M"). The sources:

- **Keyset vs. offset pagination (the general literature).** The well-documented
  problem with `OFFSET`/`LIMIT` pagination is that the offset window is a
  *position by count*, so when rows are inserted or deleted between page fetches
  the window shifts and items are **skipped or duplicated**. Keyset pagination
  names a *row position* (a value in the ordered space), so it is stable under
  those mutations. This is the backbone of the `stable-under-mutation` property —
  the kit's headline — and the reason the bundled naive stub (offset) fails it
  while the correct stub (keyset) passes. (See e.g. Markus Winand's
  *use-the-index-luke* "No Offset" writing and the broad "keyset pagination"
  literature; the kit does not depend on any one author — the skip/dupe behaviour
  is reproduced directly by the bundled stubs.)

- **Opaque cursor tokens (vendor cursor-pagination docs).** Major APIs expose the
  cursor as an **opaque token** the client must pass back unmodified rather than
  construct or edit: **Stripe** (list pagination via `starting_after`/`ending_before`
  object ids and `has_more`), **Slack** (`response_metadata.next_cursor` + a
  `limit`), and **GitHub** (Link-header `rel="next"` cursors on many endpoints).
  The common contract across them: follow the server-provided cursor to page, and
  a cursor is not something the client fabricates. This kit's correct stub models
  that with an **HMAC-signed** opaque cursor so a **forged or tampered** cursor is
  **tamper-evident and rejected (400)** — the `cursor-tamper` property. (Signing
  the cursor is one honest implementation of "opaque"; a server may instead store
  cursors, or encode an un-signed but validated position — the kit asserts the
  *externally-visible* behaviour "a bad cursor is rejected, not coerced to page
  1," which any of those achieve.)

- **Total order needs a unique tiebreaker.** If the sort key is not unique (two
  rows share a `created_at`), pagination on the sort key alone is unstable —
  rows can be skipped or repeated at page boundaries. The standard fix, which
  this kit asserts in the `ordering` property, is a composite key of the sort
  column plus a **unique tiebreaker** (here the row `id`): order by
  `(created_at, id)`. The bundled dataset deliberately contains tied `created_at`
  values so this matters.

**What the kit asserts vs. what is a modelling choice.** The behaviours the kit
asserts are all *externally visible*: a cursor traversal with no overlap/gap
(`traversal`), no skip/dupe under a controlled mid-traversal mutation
(`stable-under-mutation`), a consistent total order (`ordering`), a page size that
is honored and clamped to a documented max (`page-size`), a terminal signal
(`terminal`), and a rejected forged cursor (`cursor-tamper`). The *implementation*
the reference stub uses (keyset on `(created_at, id)` with an HMAC-signed cursor)
is one honest way to satisfy them; a buyer's API may satisfy the same contract
with SQL keyset queries, stored cursors, or a vendor pager. The kit tests the
contract, not the implementation.

## The properties this kit checks (and their basis)

| Property | What the kit asserts | Basis |
|---|---|---|
| **traversal** | following `next_cursor` yields every item with no overlap and no gap; all pages concatenated reproduce the full ordered set exactly once | the cursor-pagination contract (follow the server cursor to page through the set) |
| **stable-under-mutation** | inserting + deleting rows BETWEEN page fetches does not skip or duplicate items present throughout | keyset-vs-offset literature (offset shifts under mutation; keyset does not) — the headline |
| **ordering** | a consistent total order: a stable sort key + a UNIQUE tiebreaker, no duplicate ids | the "tiebreaker required for a stable order" result |
| **page-size** | `limit` honored on full pages; an over-max `limit` is CLAMPED to a documented max (`X-Page-Size-Max`), not served unbounded | vendor pagers cap page size (e.g. Slack/GitHub per-page maxima); an unbounded page is a DoS |
| **terminal** | the last page signals the end (null/absent `next_cursor`); the loop terminates | the cursor contract (`has_more:false` / absent cursor ends the walk) |
| **cursor-tamper** | a malformed or forged/opaque cursor is rejected (4xx), not silently coerced to page 1 | opaque-cursor convention (the client passes back the server's token unmodified) |

## The fixtures (docs-derived templates)

| File | Role | sha256 of the vendored file |
|---|---|---|
| `items_keyset.json` | primary — a page response matching the bundled stubs (`/items`, `items[].id`, `next_cursor`) | `31ee8745a27da7d13a49e93476073d823d5babccbe4f83b834738c1237413c7b` |
| `items_pagetoken.json` | a differently-named cursor API (`page_size`/`page_token`/`data`/`next_page_token`) — a template to adapt to your own endpoint | `ef235df69da875a15cce7cdc31b72988e73ddd2e46397f026604275b1dbc2ec5` |

`MANIFEST.json` (kit-authored, not vendored — sha256
`462877dd0d7d59669763a7ca151fed34e445456968faa782b699f0e9236304ac`) maps each
fixture stem to the collection path, the page-size and cursor query-param names,
and the response fields carrying the item list, the next cursor, the id, and the
sort key — so `--fixture` (or an edited manifest) can point the harness at your
own API's naming.

## What is illustrative, not wire-captured

The row bodies are reconstructed representative shapes with clearly-fake demo
markers (`pgtk_demo_row_0001`, `PGTK-DEMO-OPAQUE-CURSOR-01`,
`pgtk-demo-record-1`) — none is a real record or captured payload, and no
account, key, or service call was made to produce them. The reference stubs
(`stub_handler.py` / `stub_handler_naive.py` and their Node equivalents inside
`pgtk.js`'s `demo`) are the kit's own code, not vendor code; the naive stub
exists specifically so the test suite can prove the harness catches a broken pager
(the offset skip under mutation, an unbounded over-max page, and a forged cursor
served as page 1). The `.env.example` names optional configuration only; no secret
value ships in this kit (the demo cursor-signing key is a clearly-labelled
non-secret default).
