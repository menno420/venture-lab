# Quickstart — CORS Preflight Test Kit v0.1

Three minutes from unzip to a green check on your own endpoint. Stdlib only — no
`pip install`, no `npm install`, no account, no browser.

## 0. See the kit work (offline, no endpoint of your own)

```
python3 cptk.py demo      # or: node cptk.js demo
```

This spins up two bundled reference endpoints in-process — a **correct**
allowlist-based one and a deliberately **naive** one — runs all six properties
against each, and prints the verdicts. Expect: the correct config PASSES all six;
the naive one is FLAGGED on `allow-origin` (echoes the origin with no `Vary`),
`allow-methods` (preflight has no `Access-Control-Allow-Methods`), `allow-headers`
(no `Access-Control-Allow-Headers`), and `reflect-guard` (it reflects an arbitrary
origin). It is honestly NOT flagged on `preflight-status` or `credentials` — those
two properties don't distinguish the two configs, and the kit says so. No accounts,
no network beyond localhost, no money.

## 1. Start an endpoint

Either your own app, or the bundled correct reference endpoint:

```
python3 stub_handler.py 8000
```

It listens on `http://127.0.0.1:8000`, allowlists `https://app.example.com` by
default (set `CPTK_ALLOWED_ORIGINS=https://a.example,https://b.example`), answers
the preflight with `204` + the full `Access-Control-*` set for an allowed origin,
and returns **no** CORS headers for a disallowed one.

## 2. Tell the kit your browser origin

The kit needs the `Origin` your front-end is served from — the one your server is
supposed to allow:

- `--origin https://app.example.com`

## 3. Run the full check

```
python3 cptk.py check --url http://localhost:8000 --origin https://app.example.com
```

Expect all six properties `PASS`. Each `FAIL` line names the exact bug and points
at `GOTCHAS.md`.

## 4. Run one property at a time

```
python3 cptk.py preflight-status --url http://localhost:8000 --origin https://app.example.com  # OPTIONS → 200/204
python3 cptk.py allow-origin     --url http://localhost:8000 --origin https://app.example.com  # Allow-Origin + Vary
python3 cptk.py allow-methods    --url http://localhost:8000 --origin https://app.example.com  # Allow-Methods covers the method
python3 cptk.py allow-headers    --url http://localhost:8000 --origin https://app.example.com  # Allow-Headers covers the headers
python3 cptk.py credentials      --url http://localhost:8000 --origin https://app.example.com  # credentials never with `*`
python3 cptk.py reflect-guard    --url http://localhost:8000 --origin https://app.example.com  # no open reflection
```

The Node port is identical: `node cptk.js check --url http://localhost:8000 --origin https://app.example.com`.

## 5. Point it at YOUR route and headers

The bundled fixtures preflight a JSON `POST /api/data` with `Content-Type` +
`Authorization` (`api_json_post`, the default) and a GET carrying `Authorization`
(`api_get_authed`). To test your own route, edit `fixtures/MANIFEST.json` — set the
`path`, `method`, and `request_headers` (the headers your front-end actually sends)
— or add a new fixture and pass `--fixture <name>`. Check the reflect-guard probe
with `--bad-origin https://some-origin-you-reject.example`.

## 6. Run the kit's own test suite

```
python3 -m unittest -v
```

Every request is fired over actual HTTP to a reference endpoint on an ephemeral
port; no timed waits. All green = the kit is intact on your machine.

---

Next: read `GOTCHAS.md` (one page, the seven failure modes) and adapt
`stub_handler.py` into your framework of choice.
