# JWT Auth Test Kit v0.1

Prove your API's JWT authentication is **secure** — that a protected endpoint
**accepts** a valid, correctly-signed, unexpired token with the right claims and
**rejects** the critical auth-bypass classes: an `alg:none` unsigned token, a
tampered / wrong-signature / wrong-key token, the **RS256→HS256 algorithm-confusion**
attack, an **expired** token, a **not-yet-valid** (`nbf`/`iat` in the future) token,
a wrong/missing **audience** and **issuer**, and a structurally-malformed token.
Point it at your endpoint, fire the attacks, get PASS/FAIL per property. Stdlib
only, no dependencies, no vendor account, no live API.

This is **not** a webhook signature kit, **not** the Idempotency Key Test Kit,
**not** the Rate-Limit Test Kit, and **not** the Pagination Test Kit. It tests the
highest-severity problem class in API robustness: **JWT verifier security — auth
bypass**. Every property is grounded in **RFC 7519** (JWT), **RFC 7515** (JWS), and
**RFC 8725** ("JWT Best Current Practices"), plus the well-known `alg:none` and
RS256→HS256 algorithm-confusion attacks. See `fixtures/PROVENANCE.md`.

## The nine properties it checks

Point `jatk` at your endpoint and it reports PASS / FAIL / SKIP for each:

1. **valid-accepted** — a valid HS256 token (correct signature, unexpired, correct
   `aud`/`iss`) is **accepted** (2xx).
2. **alg-none-rejected** — an `{"alg":"none"}` unsigned token is **rejected**. The
   classic bypass (RFC 8725 §3.1) — accepting it lets anyone mint any token.
3. **signature-rejected** — a **tampered** payload and a **wrong-key** token are
   both rejected; the signature is actually verified (RFC 7515).
4. **alg-confusion-rejected** — an HS256 token signed with the **RSA/EC public-key
   bytes** as the HMAC secret is **rejected**. A verifier that HMACs a token against
   a public key it holds is bypassable, because the public key is public
   (RFC 8725 §2.1). The fix is to **pin the expected algorithm**.
5. **expired-rejected** — a token with `exp` in the past is rejected (RFC 7519 §4.1.4).
6. **not-yet-valid-rejected** — a token with `nbf`/`iat` in the future is rejected
   (RFC 7519 §4.1.5/§4.1.6).
7. **audience-enforced** — a wrong `aud` and a missing `aud` are rejected when an
   audience is configured (RFC 7519 §4.1.3). SKIPs cleanly if none is set.
8. **issuer-enforced** — a wrong `iss` and a missing `iss` are rejected when an
   issuer is configured (RFC 7519 §4.1.1). SKIPs cleanly if none is set.
9. **malformed-rejected** — a token without three valid base64url/JSON segments is
   rejected — the parser **fails closed**.

## Quickstart

Zero setup — run the built-in demo first (no accounts, no endpoint of your own):

```
python3 jatk.py demo        # or: node jatk.js demo
```

It spins up two bundled reference verifiers in-process — a **correct** one (pins an
alg allowlist, verifies the HS256 signature, enforces `exp`/`nbf`/`aud`/`iss`) and a
deliberately **naive** one (accepts `alg:none`, is vulnerable to algorithm-confusion,
skips the time/audience/issuer checks) — and prints the verdicts side by side. This
is the kit's value proof: the correct verifier passes all nine and the naive one is
**FLAGGED** on `alg-none`, `alg-confusion`, `expired`, `not-yet-valid`, `audience`,
and `issuer`.

Then point it at your own endpoint:

```
# start your app (or the bundled correct reference verifier) listening locally:
python3 stub_handler.py 8000        # GET /protected, HS256 Bearer, aud+iss enforced

# run all nine properties against it (tell it your HS256 secret + expected claims):
python3 jatk.py check --url http://localhost:8000 \
    --secret 'your-hs256-secret' --aud 'your-api' --iss 'your-issuer'
```

Run a single property (same flags):

```
python3 jatk.py alg-none-rejected       --url http://localhost:8000 --secret ...
python3 jatk.py alg-confusion-rejected  --url http://localhost:8000 --secret ... --pubkey your_pub.pem
python3 jatk.py expired-rejected        --url http://localhost:8000 --secret ...
python3 jatk.py audience-enforced       --url http://localhost:8000 --secret ... --aud your-api
python3 jatk.py list
```

`jatk.js` mirrors every command via Node (stdlib only, Node 14+):

```
node jatk.js check --url http://localhost:8000 --secret ... --aud your-api --iss your-issuer
node jatk.js demo
```

## Pointing it at a REAL endpoint

- **`--secret S`** — your server's **HS256 signing secret**. The kit needs it to
  mint a valid token *and* the otherwise-valid attack tokens (an expired token must
  carry a real signature so that only the `exp` check rejects it — that is what
  proves your server checks `exp` and not just the signature). This mirrors the
  webhook kits, which are configured with the provider's signing secret.
- **`--aud` / `--iss`** — the audience and issuer your server enforces. Leave a
  value empty to disable that property (it **SKIPs**). Set them to exercise
  `audience-enforced` / `issuer-enforced`.
- **`--pubkey FILE`** — a public-key blob for the algorithm-confusion token. The
  bundled `fixtures/test_public_key.pem` is used by default; point this at the
  actual public key your service also trusts to make the confusion test faithful to
  your deployment.
- **`--path`** — the protected route (default `/protected`, or set it in
  `fixtures/MANIFEST.json`).
- **Use a read-safe protected route.** The harness sends real GET requests with a
  `Bearer` token; point it at a route that returns 200/401, not one that mutates
  state or moves money.

## What's inside

- The harness in two languages: `jatk.py` (Python) and `jatk.js` (Node), same
  commands (`check`, the nine single-property checks, `demo`, `list`).
- A **correct** reference verifier (`stub_handler.py`) you can read — a pinned
  `HS256` allowlist, an `hmac.compare_digest` signature check, and
  `exp`/`nbf`/`aud`/`iss` enforcement over `GET /protected`.
- A deliberately **naive** verifier (`stub_handler_naive.py`) with the classic
  bypasses — accepts `alg:none`, HMACs a token against a public key it holds
  (algorithm-confusion), and checks no time/audience/issuer claims — shipped so the
  test suite can prove the harness catches them.
- Endpoint/claim templates + `fixtures/PROVENANCE.md` grounding every property in
  its RFC / attack source, with a pinned sha256 per vendored fixture, plus a
  throwaway RSA **public** key for the confusion token.
- An HTTP-layer real-path test suite (`test_http_realpath.py`, 47 tests) — every
  request fired over real HTTP against a reference verifier on an ephemeral port;
  time claims are fixed ±1h offsets, so it runs fast with no real waiting.
- A one-page `GOTCHAS.md` checklist and a `QUICKSTART.md`.

## Run the kit's own tests

```
python3 -m unittest -v
```

Every request is fired over actual HTTP to a reference verifier on an ephemeral
port. All green = the kit is intact on your machine.

## What it does NOT do (so you know what you're buying)

- It does **not** perform real **RS256 / ES256 (RSA / ECDSA) signature-math
  verification**. Testing that your endpoint correctly verifies a genuinely
  RSA-signed token is **out of the shipped stdlib scope** — it would need an
  asymmetric-crypto dependency. The kit tests the HS256 signature path and every
  auth-bypass class above (none of which needs RSA verify), which are the
  highest-severity bugs. The algorithm-confusion check needs **no** RSA verify — it
  forges an HS256 token over the public-key bytes.
- It does **not** verify webhook signatures / HMAC (the Webhook Test Kits), test
  idempotency / safe-retry (the Idempotency Key Test Kit), test throttling (the
  Rate-Limit Test Kit), or test pagination (the Pagination Test Kit). This is a
  distinct, higher-severity problem class: **auth bypass**.
- It does **not** talk to any live API, create an account, or move money. The
  `demo` runs entirely in-process against bundled stubs.
- It tests the **externally-visible verifier contract** (which tokens are accepted
  vs. rejected), not your token-issuance flow, key rotation, refresh-token
  handling, revocation lists, or transport security (use HTTPS). Those are separate
  concerns.
- The bundled secret is a clearly-labelled **non-secret** and the bundled key is a
  **public** key; `.env.example` names optional config only. No real credential
  ships in this kit.

## Requirements

- Python 3.8+ (for `jatk.py`, the stubs, the tests) or Node 14+ (for `jatk.js`).
- No account, no `pip install`, no `npm install`.
- No secret values live in this kit; `.env.example` names optional config only.
