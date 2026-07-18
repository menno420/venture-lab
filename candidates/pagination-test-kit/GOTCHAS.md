# Pagination gotchas — the one-page checklist

The failure modes that repeatedly break first pagination implementations. Each
maps to a `pgtk` command that proves your endpoint is not making the mistake.
There is no single RFC for cursor pagination — the model is the keyset/cursor
pattern (sources cited in `fixtures/PROVENANCE.md`).

## 1. Offset pagination skips or duplicates rows under mutation

The classic bug: paginate with `LIMIT n OFFSET k`. The offset is a position **by
count**, so if a row *before* your current offset is **deleted** between page
fetches, every later row shifts down one and the next `OFFSET` **skips** a row; if
a row is **inserted** before the offset, a row is **duplicated** onto the next
page. On a busy collection this silently drops or repeats items in every export,
sync, or "load more" scroll. The fix is **keyset (cursor) pagination**: the cursor
names a **row position** in the ordered space (`WHERE (created_at, id) >
(last_created_at, last_id)`), which does not move when other rows change.

**Check it:** `pgtk stable-under-mutation --limit N` — deletes an already-returned
row and inserts a tail row BETWEEN page fetches, then asserts every item present
throughout still appears exactly once. (Needs a test-mutation hook; SKIPs on a
read-only endpoint — run it against a seeded, mutable test dataset.)

## 2. No unique tiebreaker → an unstable order at page boundaries

If you `ORDER BY created_at` and two rows share a `created_at`, their relative
order is undefined and can differ between queries — so a row can be skipped or
repeated right at a page boundary even without any mutation. Always order by the
sort column **plus a unique tiebreaker** (the primary key): `ORDER BY (created_at,
id)`. The cursor must encode **both** parts.

**Check it:** `pgtk ordering --limit N` — traverses and asserts a consistent total
order by `(sort_key, id)` with the tiebreaker unique across rows (no duplicate
ids).

## 3. A cursor the client can forge (or that isn't rejected when garbage)

A cursor is meant to be **opaque** — the client passes back exactly what the
server gave it. Two failures: (a) the cursor is a **raw offset or raw id** the
client can guess/edit to jump anywhere or desync the walk; (b) a **malformed or
forged** cursor is **silently coerced to page 1** (a common `int(cursor)` →
fallback-to-0 bug) instead of returning **400**. Both mean a bad cursor produces a
plausible-looking wrong result. Make the cursor opaque and **validate it** — sign
it (HMAC), or store/whitelist issued cursors — and **reject** anything that
doesn't verify.

**Check it:** `pgtk cursor-tamper --limit N` — fires several malformed and
tampered cursors and asserts each is rejected with a 4xx, not served as page 1.

## 4. An unbounded page size

If you honor whatever `limit` the client sends, `?limit=1000000` returns your
whole table in one response — a cheap denial-of-service and a memory spike. Honor
`limit` **up to a documented maximum** and **clamp** anything larger (advertise it
with `X-Page-Size-Max` so clients know). A `limit` of `0` or a negative should
clamp to a sane minimum, not return everything or crash.

**Check it:** `pgtk page-size --limit N --max M` — confirms a normal `limit` is
honored on full pages and an over-max `limit` is clamped to the documented max
(read from `X-Page-Size-Max` when present).

## 5. A walk that never ends (or ends without saying so)

The last page must signal the end — `next_cursor: null` (or `has_more: false`, or
an absent cursor) — so a client loop stops. Two bugs: a cursor that **keeps
returning itself** (an infinite loop, often an off-by-one in the "is there a next
page?" check), or a last page that returns a **non-null cursor pointing past the
end** so the client fetches an empty page forever.

**Check it:** `pgtk terminal --limit N` — traverses to the end under a hard page
cap and a repeated-cursor guard, and asserts the walk terminates with a
null/absent next-cursor.

## 6. Two honest non-signals (and the scope of the test)

- **`traversal`, `ordering`, and `terminal` don't distinguish a broken pager from
  a correct one on their own.** Offset pagination traverses a **static** dataset
  correctly (no overlap, no gap), orders rows consistently, and signals the
  terminal page — so those three pass on both the correct and the naive reference
  stub. The distinguishing failures are `stable-under-mutation`, `page-size`, and
  `cursor-tamper`. The kit says this out loud rather than overclaiming
  (`stub_handler_naive.py` documents which bugs each property does and doesn't
  catch).
- **Scope.** This kit tests the externally-visible pagination contract for the
  collection **as one ordered set from one caller**. It does not test per-user
  visibility filtering, cross-shard/parallel cursor consistency, or which storage
  you chose. Those are design decisions; the kit checks that whatever you built
  traverses without skip/dupe, orders stably, clamps the page size, terminates,
  and rejects a forged cursor.

---

Run all six at once with `pgtk check --url … --limit N`, and see them distinguish
correct keyset pagination from a broken offset one with `pgtk demo`.
