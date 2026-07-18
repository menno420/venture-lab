# Fixture provenance

**Honest statement up front:** the request templates in this directory are
**docs-derived** — representative request shapes (a cheap GET probe and a POST
write body), not captures from a live API. A rate-limit test is about the request
**count within a window**, not the body shape, so these fixtures exist to be
replayed in a burst against an endpoint you name; they carry clearly-fake demo
markers. No account was created, no API key was used, and no real service was
called to build this kit (this repo's no-new-accounts rule). Every rate-limit
behaviour this kit checks is cited below to a public source, so a buyer can audit
each claim.

> Reconstructed 2026-07-18 (UTC). Payload shapes are illustrative; they are
> REQUEST templates (method + path + optional body), not webhook deliveries.

## Honest scope: which model does this kit test?

There are three relevant sources, and they cover different, complementary things.
This matters because part of what the kit tests is a **stable RFC** and part is a
**not-yet-ratified IETF draft** — the kit is explicit about which is which.

- **RFC 6585 §4 — "429 Too Many Requests"** (Additional HTTP Status Codes,
  IETF, Proposed Standard). Defines the **429** status code a server returns when
  a client has sent too many requests in a given time, and states that the
  response **MAY** include a `Retry-After` header indicating how long to wait.
  This is a **stable standard** and is the backbone of properties `over-limit`
  and `retry-after`.

- **RFC 9110 §10.2.3 — `Retry-After`** (HTTP Semantics, IETF, Internet
  Standard). Defines the two valid **forms** of `Retry-After`: an **HTTP-date**,
  or a non-negative **delay in seconds**. The kit's `retry-after` check accepts
  either form and rejects the rest (missing, zero/negative, non-numeric junk, a
  past date, or an absurdly large value). Stable standard.

- **The IETF draft — "RateLimit header fields for HTTP"**
  (`draft-ietf-httpapi-ratelimit-headers`, IETF HTTP APIs working group). This
  specifies the **`RateLimit-Limit` / `RateLimit-Remaining` / `RateLimit-Reset`**
  header fields (an evolution of the widely-deployed legacy **`X-RateLimit-*`**
  convention) that advertise a client's remaining budget and when the window
  resets. Crucially, this is a **DRAFT, not yet an RFC**, and its exact shape has
  changed across revisions (recent revisions favour a single structured
  `RateLimit` field). **This kit tests the separate-header convention**
  (`RateLimit-*` and the legacy `X-RateLimit-*` aliases), which is what the large
  majority of deployed APIs emit today, and it says so. The combined structured
  `RateLimit:` field is a known variation the kit does **not** assert.

**What the kit asserts vs. what is optional.** The 429 + `Retry-After` behaviour
(properties `over-limit`, `retry-after`, `window-reset`, `retry-after-honored`)
rests on the stable RFCs. The `RateLimit-*` header consistency (property
`headers`) rests on the **draft** and is treated as **optional**: if your
endpoint emits **no** such headers, the `headers` check passes with a note
(they're not mandatory); if it **does** emit them, they must be internally
consistent (Limit a positive integer, Remaining decrementing to 0 at the
boundary, Reset pointing into the future). A buyer whose API uses a different
convention should adjust the expectation — the harness reads both the draft and
legacy header names and the limit is configurable (`--limit`).

## The properties this kit checks (and their sources)

| Property | What the kit asserts | Source |
|---|---|---|
| **under-limit** | the first `limit` requests in a window return **2xx** | the limit contract itself (429 only applies past the limit — RFC 6585 §4) |
| **over-limit** | request `limit`+1 in the window returns **429** (no off-by-one) | RFC 6585 §4 (429 Too Many Requests) |
| **retry-after** | the 429 carries a **positive, sane** `Retry-After` (delay-seconds or a future HTTP-date) | RFC 6585 §4 (MAY send Retry-After) + RFC 9110 §10.2.3 (the two valid forms) |
| **headers** | `RateLimit-*`/`X-RateLimit-*`, **when present**, are consistent (Limit positive; Remaining decrements to 0 at the boundary; Reset in the future) | the RateLimit-header IETF **draft** + the legacy X-RateLimit-* convention |
| **window-reset** | after the advertised reset elapses, requests **succeed again** | the fixed-window/token-bucket model — a window that resets (RFC 6585 §4 Retry-After semantics) |
| **retry-after-honored** | the advertised `Retry-After` matches when the service **actually resumes** (still 429 before, 2xx after, within tolerance) | RFC 9110 §10.2.3 (Retry-After is a promise about when to retry) |

## The fixtures (docs-derived request templates)

| File | Method · path | Role | sha256 of the vendored file |
|---|---|---|---|
| `api_ping.json` | `GET /api/ping` | primary — a cheap GET probe fired in a burst (the default; its body is not sent on a GET) | `a41f74cd702a7f2bfd1f0b419eb15d4af5043e019d38e90e5f0dbfaf0fe0ad2b` |
| `api_write.json` | `POST /api/items` | a write-side POST burst — for limiters that scope by method/route | `d59a873137f3f61bf6872db8df607cc473019b42356ab8b31859d7282ac58ceb` |

`MANIFEST.json` (kit-authored, not vendored — sha256
`bc60a8fac2bde4a57c3b1bc2cc9ed4559cca47d74f0c8e8f2060fdd6ea27dc87`) maps each
fixture stem to the HTTP method, path, and Content-Type the harness replays in a
burst. Point `--fixture` (or edit the manifest path) at the route on your own API
you want to throttle-test.

## What is illustrative, not wire-captured

The fixture bodies are reconstructed representative shapes with clearly-fake demo
markers (`rltk_demo_client_0001`, `RLTK-DEMO-01`) — none is a real credential,
record, or captured payload, and no account, key, or service call was made to
produce them. The reference stubs (`stub_handler.py` / `stub_handler_naive.py`
and their Node equivalents inside `rltk.js`'s `demo`) are the kit's own code, not
vendor code; the naive stub exists specifically so the test suite can prove the
harness catches a broken limiter (off-by-one, a 429 with no `Retry-After`, and
stale/stuck `X-RateLimit-*` headers). The `.env.example` names optional
configuration only; no secret value ships in this kit.
