# Fixture provenance

**Honest statement up front:** the request templates in this directory are
**docs-derived** — representative request shapes (an authenticated JSON POST and a
GET carrying Authorization), not captures from a live API. A CORS test is about the
**Origin and the preflight/response headers your server emits**, not the body
shape, so these fixtures exist to be replayed against an endpoint you name; they
carry clearly-fake demo markers. No account was created, no API key was used, and
no real service was called to build this kit (this repo's no-new-accounts rule).
Every CORS behaviour this kit checks is cited below to a public source, so a buyer
can audit each claim.

> Reconstructed 2026-07-18 (UTC). Payload shapes are illustrative; they are
> REQUEST templates (method + path + the request headers that trigger a browser
> preflight), not webhook deliveries or live captures.

## Honest scope: what does this kit test?

This kit tests the **server-emitted CORS contract at the HTTP layer** — exactly
the response headers a browser inspects when it makes a cross-origin request. It
fires a real cross-origin **preflight** (`OPTIONS` with `Origin` +
`Access-Control-Request-Method` + `Access-Control-Request-Headers`) and a real
**actual request** (the method with an `Origin` header), then checks the
`Access-Control-*` response headers against the rules a browser enforces.

It does **not** drive a real browser, and it does **not** cover Private Network
Access (the `Access-Control-Allow-Private-Network` / `Access-Control-Request-Private-Network`
extension) — that is a separate, newer mechanism the kit intentionally leaves out
of scope and says so. What it asserts is the core CORS protocol every browser has
enforced for years.

## The sources

- **WHATWG Fetch Standard — "CORS protocol"** (the living standard that defines
  CORS for the web platform). It defines the `Access-Control-Allow-Origin`,
  `-Allow-Methods`, `-Allow-Headers`, `-Allow-Credentials`, and `-Max-Age`
  response headers; the preflight (`OPTIONS`) request and the
  `Access-Control-Request-Method` / `-Request-Headers` request headers; the rule
  that **`Access-Control-Allow-Origin: *` cannot be combined with credentials**
  (a credentialed request requires the specific origin echoed, not `*`); and the
  rule that the `*` wildcard in `Access-Control-Allow-Headers` does **not** cover
  `Authorization` (it must be listed by name). This is the backbone of all six
  properties.

- **MDN Web Docs — "Cross-Origin Resource Sharing (CORS)"** and the individual
  `Access-Control-*` / `Vary` header pages. MDN documents the preflight flow, the
  `Access-Control-Allow-Credentials` + specific-origin requirement, and the
  guidance to send **`Vary: Origin`** whenever `Access-Control-Allow-Origin` is
  computed per-request (echoed) rather than a static `*`, so a shared cache does
  not serve one origin's `Allow-Origin` to another. This grounds the
  `allow-origin` (Vary) and `credentials` properties.

## The properties this kit checks (and their sources)

| Property | What the kit asserts | Source |
|---|---|---|
| **preflight-status** | the cross-origin `OPTIONS` preflight returns an ok status (200 or 204) | Fetch CORS protocol — a non-ok preflight aborts the request |
| **allow-origin** | preflight AND actual response carry `Access-Control-Allow-Origin` matching the request `Origin` (or `*`); when it echoes the specific origin, `Vary: Origin` is present | Fetch CORS protocol (Allow-Origin) + MDN (Vary: Origin caching guidance) |
| **allow-methods** | the preflight's `Access-Control-Allow-Methods` covers the requested method (`Access-Control-Request-Method`) | Fetch CORS protocol (preflight method check) |
| **allow-headers** | the preflight's `Access-Control-Allow-Headers` covers every requested header (`Access-Control-Request-Headers`), case-insensitively; a literal `*` does NOT cover `Authorization` | Fetch CORS protocol (preflight header check + the Authorization/`*` carve-out) |
| **credentials** | `Access-Control-Allow-Credentials: true` is never paired with `Access-Control-Allow-Origin: *` (nor a `*` methods/headers list) | Fetch CORS protocol (credentials + `*` prohibition) |
| **reflect-guard** | a disallowed probe origin is NOT reflected into `Access-Control-Allow-Origin`, and `*`+credentials is flagged | Fetch CORS protocol + the well-known open-CORS (origin-reflection) misconfiguration |

## What the kit asserts vs. what is optional

The **`allow-origin`** (presence + Vary when echoed), **`allow-methods`**,
**`allow-headers`**, and **`reflect-guard`** properties are the non-negotiable
core: without them a browser blocks the request, or the endpoint is open to any
website. **`credentials`** is conditional — it only asserts anything when the
endpoint sets `Access-Control-Allow-Credentials: true`; a non-credentialed API
(e.g. a public read-only one that legitimately uses `Access-Control-Allow-Origin:
*`) passes `credentials` and `reflect-guard` with a note. The kit is explicit that
two properties (`preflight-status`, `credentials`) do **not** distinguish the
bundled correct stub from the bundled naive one — documented in
`stub_handler_naive.py` and `GOTCHAS.md`.

## The fixtures (docs-derived request templates)

| File | Method · path | Preflight headers | Role | sha256 of the vendored file |
|---|---|---|---|---|
| `api_json_post.json` | `POST /api/data` | `content-type, authorization` | primary — an authenticated JSON POST that triggers a preflight | `e4d8c9f5892ecf8a6023677bd807974c4c29f4afcaa2146e9fd741316b820292` |
| `api_get_authed.json` | `GET /api/data` | `authorization` | a GET carrying Authorization — a non-simple header, so it also preflights | `9888b3e6fba0f77b2992d7b453b7c99a7f6cd907c6ce9777b2e5bd042116b6e7` |

`MANIFEST.json` (kit-authored, not vendored — sha256
`3a318ce7372b3afdb17263637a32236826e77cfbc9965a2c26c1a464bbd868b4`) maps each
fixture stem to the HTTP method, path, Content-Type, and the
`Access-Control-Request-Headers` value the harness replays. Point `--fixture` (or
edit the manifest path/headers) at the route and headers on your own API you want
to CORS-test.

## What is illustrative, not wire-captured

The fixture bodies are reconstructed representative shapes with clearly-fake demo
markers (`cptk_demo_client_0001`, `CPTK-DEMO-01`) — none is a real credential,
record, or captured payload, and no account, key, or service call was made to
produce them. The reference stubs (`stub_handler.py` / `stub_handler_naive.py`
and their Node equivalents inside `cptk.js`'s `demo`) are the kit's own code, not
vendor code; the naive stub exists specifically so the test suite can prove the
harness catches a broken CORS config (arbitrary origin reflection, no `Vary`, and
a preflight missing `Access-Control-Allow-Methods` / `-Allow-Headers`). The
`.env.example` names optional configuration only; no secret value ships in this
kit.
