# CORS gotchas — the one-page checklist

The failure modes that repeatedly break first CORS implementations. Each maps to a
kit command that proves your endpoint is not making the mistake. Every rule below
comes from the WHATWG Fetch Standard "CORS protocol" and MDN's CORS docs (sources
cited in `fixtures/PROVENANCE.md`).

## 1. The preflight 404s / 405s (your framework doesn't answer OPTIONS)

Before a non-simple cross-origin request (a JSON POST, or anything with an
`Authorization` header), the browser sends a **preflight**: an `OPTIONS` request
with `Origin` + `Access-Control-Request-Method`. If your framework returns 404 or
405 for `OPTIONS` — the default in a lot of routers until CORS middleware is added
— the browser treats the preflight as a failure and **never sends the real
request**. Correct: the preflight returns an ok status (**200 or 204**).

**Check it:** `cptk preflight-status --url … --origin …`

## 2. No Access-Control-Allow-Origin (the #1 CORS error)

*"No 'Access-Control-Allow-Origin' header is present on the requested resource."*
The single most common CORS error: the response simply doesn't carry the header, so
the browser blocks the read. It must be present on **both** the preflight and the
actual response, and it must **match the request `Origin`** (an exact echo) or be
`*`.

**Check it:** `cptk allow-origin --url … --origin …`

## 3. Echoing the origin without `Vary: Origin` (cache poisoning)

When you compute `Access-Control-Allow-Origin` per-request (echo the caller's
origin) rather than sending a static `*`, you **must** also send `Vary: Origin`.
Without it, a shared cache (CDN, reverse proxy) can store the response for origin A
and serve it — `Access-Control-Allow-Origin: https://a.example` and all — to a
request from origin B, breaking CORS for everyone behind the cache (or leaking A's
CORS grant to B). Correct: any per-origin `Allow-Origin` is accompanied by
`Vary: Origin`.

**Check it:** `cptk allow-origin --url … --origin …` (it flags an echoed origin
with no `Vary: Origin`).

## 4. Allow-Origin set, but no Allow-Methods / Allow-Headers

The "I set `Access-Control-Allow-Origin` and thought that was enough" bug. The
preflight must **also** advertise:

- `Access-Control-Allow-Methods` covering the method the browser asked for
  (`Access-Control-Request-Method`) — else the real `PUT`/`DELETE`/`POST` is
  blocked.
- `Access-Control-Allow-Headers` covering every header the browser asked for
  (`Access-Control-Request-Headers`) — else the request carrying `Content-Type:
  application/json` or `Authorization` is blocked. This is the classic **"works in
  curl, fails in the browser"** bug.

**Check it:** `cptk allow-methods --url … --origin …` and
`cptk allow-headers --url … --origin …`

## 5. `Access-Control-Allow-Headers: *` does NOT cover Authorization

A little-known Fetch-standard carve-out: the `*` wildcard in
`Access-Control-Allow-Headers` matches any header **except `Authorization`**. If
your front-end sends an `Authorization` header and your server answers the preflight
with `Access-Control-Allow-Headers: *`, the browser **still blocks it** — you must
list `Authorization` by name. This one bites teams who "fixed" CORS with a blanket
`*` and can't understand why authenticated requests still fail.

**Check it:** `cptk allow-headers --url … --origin …` (it flags `*` when
`Authorization` is requested).

## 6. `Access-Control-Allow-Origin: *` with credentials (browsers reject it)

If your endpoint sets `Access-Control-Allow-Credentials: true` (so the browser
sends cookies / `Authorization` on cross-origin requests), then
`Access-Control-Allow-Origin` **cannot** be `*` — the browser rejects the
combination outright, and the credentialed request fails. With credentials you must
echo the **specific** origin (and, per gotcha 3, send `Vary: Origin`). The
`Allow-Methods` / `Allow-Headers` lists likewise cannot be the literal `*` under
credentials.

**Check it:** `cptk credentials --url … --origin …`

## 7. Reflecting ANY origin (the open-CORS security hole)

The most **dangerous** mistake: to "make CORS work," a server copies whatever
`Origin` it receives into `Access-Control-Allow-Origin` and sets
`Access-Control-Allow-Credentials: true` — with no allowlist check. Now **any
website on the internet** can make a credentialed request to your API from a
victim's browser and read the authenticated response. Correct: validate `Origin`
against an allowlist and send CORS headers **only** for approved origins; a
disallowed origin gets **no** `Access-Control-Allow-Origin` at all.

**Check it:** `cptk reflect-guard --url … --origin … --bad-origin https://cptk-probe.invalid`
(it sends a disallowed probe origin and fails if your server echoes it back).

## 8. Two honest non-signals (and the scope of the test)

- **`preflight-status` and `credentials` don't distinguish a broken CORS config
  from a correct one on their own.** A server that reflects any origin still
  returns a 204 preflight, and still pairs credentials with a specific (reflected)
  origin — so those two properties pass on both the correct and the naive reference
  stub. The distinguishing failures are `allow-origin` (missing `Vary`),
  `allow-methods`, `allow-headers`, and `reflect-guard`. The kit says this out loud
  rather than overclaiming (`stub_handler_naive.py` documents which bugs each
  property does and doesn't catch).
- **Scope.** This kit tests server-emitted CORS headers at the HTTP layer, for the
  origin you name plus one disallowed probe. It does **not** drive a real browser,
  enumerate your whole allowlist, or cover Private Network Access
  (`Access-Control-Allow-Private-Network`). It checks that whatever CORS policy you
  built returns the right headers a browser enforces.

---

Run all six at once with `cptk check --url … --origin …`, and see them distinguish
a correct CORS config from a broken one with `cptk demo`.
