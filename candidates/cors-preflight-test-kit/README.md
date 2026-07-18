# CORS Preflight Test Kit v0.1

Prove your API's **CORS configuration** behaves correctly for a browser — that the
cross-origin `OPTIONS` preflight returns an ok status, that
`Access-Control-Allow-Origin` matches the request `Origin` (with `Vary: Origin`
when it echoes a specific origin), that the preflight advertises the **method** and
**headers** the browser asked for, that credentials are never paired with a `*`
origin, and that your server does **not** reflect an arbitrary `Origin` back (the
open-CORS security hole). Point it at your endpoint with your app's origin, get
PASS/FAIL per property. Stdlib only, no dependencies, no vendor account, no live
API, no real browser required.

This is **not** a webhook signature kit, **not** the Idempotency Key Test Kit,
**not** the Rate-Limit Test Kit, **not** the Pagination Test Kit, and **not** the
JWT Auth Test Kit. It tests a different problem class: the **browser cross-origin
(CORS) contract** your server emits. The behaviour it checks follows the WHATWG
Fetch Standard "CORS protocol" and MDN's CORS documentation. See
`fixtures/PROVENANCE.md`.

## Why this exists

CORS bugs are invisible to `curl` and to a same-origin unit test, and they fail in
two equally bad ways:

- **Nothing works in the browser.** *"Access to fetch has been blocked by CORS
  policy: No 'Access-Control-Allow-Origin' header is present."* Or the preflight
  404s because your framework doesn't answer `OPTIONS`. Or you set
  `Access-Control-Allow-Origin` but forgot `Access-Control-Allow-Methods` /
  `-Allow-Headers`, so the JSON POST with an `Authorization` header is blocked.
- **Everything is wide open.** Your server echoes back whatever `Origin` it's given
  and sets `Access-Control-Allow-Credentials: true`, so **any website on the
  internet** can make a credentialed request and read the authenticated response.

Both are one-line mistakes. This kit fires exactly the cross-origin requests a
browser would and reports which of the six properties your endpoint gets right.

## The six properties it checks

Point `cptk` at your endpoint (`--url`) and tell it your app's browser origin
(`--origin`); it reports PASS/FAIL for each:

1. **preflight-status** — the cross-origin `OPTIONS` preflight returns an **ok
   status** (200 or 204). A 404/405/500 preflight means the browser never sends
   the real request. Many frameworks 404/405 `OPTIONS` by default until CORS is
   wired.
2. **allow-origin** — both the preflight **and** the actual response carry
   `Access-Control-Allow-Origin` matching the request `Origin` (or `*`). When it
   echoes the **specific** origin (not `*`), `Vary: Origin` must be present — or a
   shared cache can serve one origin's `Allow-Origin` header to a **different**
   origin, breaking CORS for everyone behind the cache.
3. **allow-methods** — the preflight's `Access-Control-Allow-Methods` covers the
   method the client asked for (`Access-Control-Request-Method`). A method that
   isn't listed is blocked.
4. **allow-headers** — the preflight's `Access-Control-Allow-Headers` covers every
   header the client asked for (`Access-Control-Request-Headers`),
   case-insensitively — and it flags the Fetch-spec gotcha that a literal `*` does
   **not** cover `Authorization` (it must be named explicitly).
5. **credentials** — if `Access-Control-Allow-Credentials: true` is present, the
   `Allow-Origin` must be a **specific origin, not `*`** (browsers reject
   `*`+credentials), and the methods/headers lists must not be the literal `*`.
6. **reflect-guard** — a **disallowed** probe origin must **not** be reflected into
   `Access-Control-Allow-Origin`. Blindly echoing any `Origin` is open CORS: any
   website can read authenticated responses. `*`+credentials is flagged too.

## Quickstart

Zero setup — run the built-in demo first (no accounts, no endpoint of your own):

```
python3 cptk.py demo        # or: node cptk.js demo
```

It spins up two bundled reference endpoints in-process — a **correct** one
(allowlist-based, all six properties PASS) and a deliberately **naive** one
(reflects any origin, no `Vary`, no `Allow-Methods`/`Allow-Headers` on the
preflight, which the kit FLAGS) — and prints the verdicts side by side. This is the
kit's value proof: it distinguishes a correct CORS config from a broken one.

Then point it at your own endpoint:

```
# start your app (or the bundled correct reference endpoint):
python3 stub_handler.py 8000        # allowlist = https://app.example.com by default

# run all six properties against it, naming your browser origin:
python3 cptk.py check --url http://localhost:8000 --origin https://app.example.com
```

Run a single property:

```
python3 cptk.py preflight-status --url http://localhost:8000 --origin https://app.example.com
python3 cptk.py allow-origin     --url http://localhost:8000 --origin https://app.example.com
python3 cptk.py allow-methods    --url http://localhost:8000 --origin https://app.example.com
python3 cptk.py allow-headers    --url http://localhost:8000 --origin https://app.example.com
python3 cptk.py credentials      --url http://localhost:8000 --origin https://app.example.com
python3 cptk.py reflect-guard    --url http://localhost:8000 --origin https://app.example.com
python3 cptk.py list
```

`cptk.js` mirrors every command via Node (stdlib only, Node 14+):

```
node cptk.js check --url http://localhost:8000 --origin https://app.example.com
node cptk.js demo
```

## Pointing it at a REAL endpoint

- **`--origin`** (required) — the browser origin your front-end is served from,
  e.g. `https://app.example.com`. This is the `Origin` the kit sends; it must be an
  origin your server is supposed to allow.
- **`--fixture`** — which request template to replay: `api_json_post` (an
  authenticated JSON POST, the default) or `api_get_authed` (a GET carrying
  Authorization). Both are **non-simple** requests, so the browser preflights them.
  Edit `fixtures/MANIFEST.json` to point the path/headers at your own route, or add
  your own fixture.
- **`--bad-origin`** — the disallowed probe origin the `reflect-guard` check sends
  (default `https://cptk-probe.invalid`). It must be an origin your server should
  **reject** — the check fails if your server echoes it back.
- **Safe to run against a real endpoint.** The kit sends one preflight and one real
  request per property; point `--fixture` at a route that's cheap and safe to hit.

## What's inside

- The harness in two languages: `cptk.py` (Python) and `cptk.js` (Node), same
  commands (`check`, the six single-property checks, `demo`, `list`).
- A **correct** reference endpoint (`stub_handler.py`) you can read — an
  allowlist-based CORS handler that answers the preflight with `204` +
  `Access-Control-Allow-Origin` (echoed) + `Vary: Origin` +
  `Access-Control-Allow-Methods` + `-Allow-Headers` + `-Allow-Credentials`, and
  returns **no** CORS headers for an origin off its allowlist.
- A deliberately **naive** endpoint (`stub_handler_naive.py`) with the classic
  bugs — reflects any origin, no `Vary`, no `Allow-Methods`/`Allow-Headers` on the
  preflight — shipped so the test suite can prove the harness catches them.
- Two docs-derived request templates (`api_json_post`, `api_get_authed`) +
  `fixtures/PROVENANCE.md` citing every property to its source (the WHATWG Fetch
  Standard CORS protocol + MDN CORS) and pinning a sha256 per fixture.
- An HTTP-layer real-path test suite (`test_http_realpath.py`, 37 tests) — every
  request fired over real HTTP against a reference endpoint on an ephemeral port,
  no timed waits.
- A one-page `GOTCHAS.md` checklist and a `QUICKSTART.md`.

## Run the kit's own tests

```
python3 -m unittest -v
```

Every request is fired over actual HTTP to a reference endpoint on an ephemeral
port. All green = the kit is intact on your machine.

## What it does NOT do (so you know what you're buying)

- It does **not** verify webhook signatures / HMAC (that's the Webhook Test Kits),
  does **not** test idempotency / safe-retry (the Idempotency Key Test Kit),
  throttling (the Rate-Limit Test Kit), result-set integrity (the Pagination Test
  Kit), or token security (the JWT Auth Test Kit). This is a distinct problem
  class: the browser CORS contract.
- It does **not** drive a real browser. It fires the exact cross-origin preflight
  and request a browser would (`OPTIONS` + the real method with `Origin`) and
  checks the response headers against the rules a browser enforces — at the HTTP
  layer, in milliseconds, with no headless-browser dependency.
- It does **not** cover Private Network Access
  (`Access-Control-Allow-Private-Network`) — a separate, newer mechanism left out
  of scope. It asserts the core CORS protocol every browser has enforced for years.
- It tests CORS **for the origin you name** (`--origin`) plus one disallowed probe
  (`--bad-origin`). It does not enumerate your entire allowlist or your per-route
  policy matrix — run it once per origin/route you care about.
- The `credentials` property only asserts something when your endpoint sets
  `Access-Control-Allow-Credentials: true`; a non-credentialed public API that uses
  `Access-Control-Allow-Origin: *` passes `credentials` and `reflect-guard` with a
  note. Two properties (`preflight-status`, `credentials`) honestly do **not**
  distinguish the bundled correct config from the naive one — the kit says so.
- The fixtures are **docs-derived** request templates (cited in `PROVENANCE.md`),
  not captures from a live API. The `demo` runs entirely in-process against bundled
  stubs — no account, no network beyond localhost, no money.

## Requirements

- Python 3.8+ (for `cptk.py`, the stubs, the tests) or Node 14+ (for `cptk.js`).
- No account, no `pip install`, no `npm install`.
- No secret values live in this kit; `.env.example` names optional config only.
