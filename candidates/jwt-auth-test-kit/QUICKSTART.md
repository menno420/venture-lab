# Quickstart — JWT Auth Test Kit v0.1

Three minutes from unzip to a green check on your own endpoint. Stdlib only — no
`pip install`, no `npm install`, no account.

## 0. See the kit work (offline, no endpoint of your own)

```
python3 jatk.py demo      # or: node jatk.js demo
```

This spins up two bundled reference verifiers in-process — a **correct** one and a
deliberately **naive** one — runs all nine properties against each, and prints the
verdicts. Expect: the correct verifier PASSES all nine; the naive one is FLAGGED on
`alg-none-rejected` (accepts an unsigned token), `alg-confusion-rejected` (HMACs a
token against a public key it holds), `expired-rejected`, `not-yet-valid-rejected`,
`audience-enforced`, and `issuer-enforced`. It is honestly NOT flagged on
`valid-accepted`, `signature-rejected`, or `malformed-rejected` — those three don't
distinguish the two verifiers, and the kit says so. No accounts, no network, no money.

## 1. Start an endpoint

Either your own app, or the bundled correct reference verifier:

```
python3 stub_handler.py 8000
```

It listens on `http://127.0.0.1:8000`, protects `GET /protected` behind an
`Authorization: Bearer <jwt>` header, pins the algorithm allowlist to `HS256`,
verifies the signature with a demo secret, and enforces `exp`/`nbf`/`aud`
(`jatk-demo-api`)/`iss` (`jatk-demo-issuer`). Override with `JATK_SECRET`,
`JATK_AUD`, `JATK_ISS`.

## 2. Run the full check

```
python3 jatk.py check --url http://localhost:8000 \
    --secret jatk-demo-hs256-secret-not-a-real-secret \
    --aud jatk-demo-api --iss jatk-demo-issuer
```

Expect all nine properties `PASS` (or `SKIP` for `audience`/`issuer` if you don't
configure them). Each `FAIL` line names the exact bypass and points at `GOTCHAS.md`.

## 3. Run one property at a time

```
python3 jatk.py valid-accepted          --url http://localhost:8000 --secret ... --aud ... --iss ...
python3 jatk.py alg-none-rejected       --url http://localhost:8000 --secret ...
python3 jatk.py signature-rejected      --url http://localhost:8000 --secret ...
python3 jatk.py alg-confusion-rejected  --url http://localhost:8000 --secret ... --pubkey fixtures/test_public_key.pem
python3 jatk.py expired-rejected        --url http://localhost:8000 --secret ...
python3 jatk.py not-yet-valid-rejected  --url http://localhost:8000 --secret ...
python3 jatk.py audience-enforced       --url http://localhost:8000 --secret ... --aud jatk-demo-api
python3 jatk.py issuer-enforced         --url http://localhost:8000 --secret ... --iss jatk-demo-issuer
python3 jatk.py malformed-rejected      --url http://localhost:8000 --secret ...
```

The Node port is identical: `node jatk.js check --url http://localhost:8000 --secret ... --aud ... --iss ...`.

## 4. Against your own API

- Pass **`--secret`** = your server's HS256 signing key, so the kit can mint a valid
  token and otherwise-valid attack tokens (an expired token still carries a real
  signature, so only the `exp` check can reject it — that is the point).
- Pass **`--aud` / `--iss`** = what your server enforces. Leave a value empty to
  **SKIP** that property.
- Pass **`--pubkey`** = the public key your service also trusts (if any), to make
  the algorithm-confusion token faithful to your deployment. Defaults to the bundled
  `fixtures/test_public_key.pem`.
- Point **`--path`** (or edit `fixtures/MANIFEST.json`) at your protected route.

## 5. Run the kit's own test suite

```
python3 -m unittest -v
```

Every request is fired over actual HTTP to a reference verifier on an ephemeral
port; time claims are fixed ±1h offsets, so it finishes fast. All green = the kit is
intact on your machine.

---

Next: read `GOTCHAS.md` (one page, the bypass classes) and adapt `stub_handler.py`
into your framework of choice.
