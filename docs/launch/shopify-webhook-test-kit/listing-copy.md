# Marketplace listing copy — Shopify Webhook Test Kit v0.1

> **Status:** `reference`

**Title:** Shopify Webhook Test Kit — prove your handler before you ship

**Short description (≤200 chars, 185):** Fire real-shape signed Shopify webhooks
at your local endpoint — forged, unsigned, tampered, malformed-base64, plus
topic routing. Stdlib only. No store, no app install, no dependencies.

**Price:** $29 (one-time)

## Description

Most Shopify webhook bugs don't show up while you're building — they show up on
the first real delivery: the signature that "never validates" because you hashed
a re-serialised copy instead of the raw body, the hex digest you computed when
Shopify sends base64, the endpoint that 500s the moment someone posts a garbage
signature header, the retry you process twice because you never deduped.

The Shopify Webhook Test Kit signs real-shape Shopify webhook bodies with the
actual `X-Shopify-Hmac-Sha256` scheme (`base64(HMAC-SHA256(client_secret,
raw_body))` — base64, not hex, over the raw request body directly, with the real
`X-Shopify-Topic` / `X-Shopify-Shop-Domain` / `X-Shopify-Webhook-Id` /
`X-Shopify-Api-Version` headers) and fires them over HTTP at your local endpoint
— no store, no app install, no tunnel. It checks the gotchas that repeatedly
break first Shopify integrations:

- **Forged webhooks accepted.** If your handler skips or fumbles HMAC
  verification, anyone who knows your endpoint URL can post fake webhooks. The
  kit fires a wrong-secret webhook and checks you reject it.
- **Missing signature ≠ skip verification.** `--unsigned` sends no
  `X-Shopify-Hmac-Sha256` header — the classic `if header: verify()` bug
  silently accepts it.
- **Tampered bodies.** `--tamper` signs the real body, then mutates it before
  sending — a handler that hashes a re-parsed copy instead of the raw bytes
  accepts it. (Shopify's own docs: capture the raw body *before* it's parsed.)
- **Malformed signature crashes.** `--malformed` sends a header that isn't valid
  base64. A naive `base64_decode(header)` with no error handling 500s or drops
  the connection — a denial-of-service anyone can trigger. The kit checks you
  reject it cleanly with a 4xx.
- **Base64, not hex.** Shopify's digest is base64-encoded, unlike Slack/GitHub's
  hex — the from-memory implementation's #1 mistake. The `vector` command proves
  the kit's own base64 HMAC path so you can compare against yours.
- **Topic routing.** Shopify puts the event type in the `X-Shopify-Topic`
  header, not the body. The kit fires `orders/create`, `products/update`, and
  `app/uninstalled` with the real header so you can prove your router.

Plus a built-in honesty check on the kit itself: the `vector` command recomputes
a pinned known-answer (a fixed secret + body → `uhRiDuW3…`) and confirms the
Python and Node ports agree — offline, in one command.

Runs in Python or Node, entirely from the standard library. No `pip install`,
no `npm install`, no Shopify account required to run the tests.

## What's inside

- The harness in two languages: `shwtk.py` (Python) and `shwtk.js` (Node), same
  three commands (`fire` with 4 hostile/variant modes, `vector`, `list`).
- An example CORRECT handler (`stub_handler.py`) you can adapt — raw-body
  capture before parsing, base64 HMAC-SHA256 verification with constant-time
  compare, fail-closed on a missing header, defensive base64 decode (no crash on
  garbage), topic routing over `X-Shopify-Topic`, and the
  `X-Shopify-Webhook-Id` returned for your own dedupe.
- Three real-shape Shopify webhook fixtures (`orders/create`, `products/update`,
  `app/uninstalled`) + `PROVENANCE.md` documenting where every payload and every
  scheme fact comes from, with a pinned sha256 per fixture.
- An HTTP-layer real-path test suite (`test_http_realpath.py`, 17 tests) — every
  request is signed and POSTed over real HTTP.
- A one-page `GOTCHAS.md` checklist and a `QUICKSTART.md`.

## Requirements

- Python 3.8+ or Node 14+.
- No Shopify account, no dependencies, no build step.
- Your webhook secret is read from an environment variable — no secret values
  are stored in the kit.

## What it does NOT do (so you know what you're buying)

- It does not talk to the real Shopify API, create a store, install an app, or
  touch any live shop.
- It does not validate your business logic — only the request edge behaviour
  (HMAC verification, raw-body handling, malformed-input safety, topic routing).
- It is not a substitute for Shopify's CLI `app dev` webhook forwarding or a
  tunnel, which forward REAL webhooks from a live app; this kit tests your
  handler locally before (and without) wiring one.
- If you use Shopify's official libraries (`@shopify/shopify-api`, the
  `shopify_api` gem), they can verify the HMAC for you — this kit is for
  handlers you hand-roll outside those helpers.
- There is deliberately no replay/timestamp check and no challenge handshake —
  Shopify's HMAC covers the raw body with no timestamp, so those don't exist in
  Shopify's scheme (dedupe on `X-Shopify-Webhook-Id` instead). The kit is honest
  about this rather than inventing a check Shopify doesn't have.
- The fixtures are **reconstructed from Shopify's own documentation** (cited
  file-by-file in `PROVENANCE.md`), not captures from a live store. Three topic
  shapes ship in v0.1.
- Shopify publishes no fixed known-answer HMAC constant, so the `vector` command
  is the kit's own pinned known-answer (a self-consistency + Python/Node parity
  proof), honestly labelled — not a reproduction of a Shopify value.

## FAQ

**Why not just use Shopify's CLI `app dev` or a tunnel + a real app?**
Those need an app, a dev store, and a reachable endpoint — and they only send
well-formed webhooks. This kit runs against `localhost` with zero setup and also
sends the hostile ones (forged, unsigned, tampered, malformed) that Shopify will
never helpfully send you.

**Isn't the signing code just a few lines?**
Yes — and Shopify documents it. What you're paying for is the harness + the
real-shape fixtures + the hostile modes (especially the malformed-base64 crash
check and the base64-not-hex trap, the two things a from-memory implementation
gets wrong) + the topic-routing model, all runnable against your own endpoint in
seconds. The free substitute is real; the kit is the done version.

**Refunds / support / license:** [owner-to-set — storefront defaults;
suggested: 14-day no-questions refund, single-developer license, email support
best-effort.]

---

## PROVENANCE-FOOTER

Every claim above is checkable against the committed source (blob `file@sha`
at build time, branch `claude/shopify-webhook-test-kit-2026-07-17`):

- `candidates/shopify-webhook-test-kit/shwtk.py@670d05beccbb6226de96da144a249ecbf4b84d1a`
  — the harness (base64 HMAC scheme, fire modes, vector).
- `candidates/shopify-webhook-test-kit/fixtures/PROVENANCE.md@355e0a9be666df67e854b62b14d2d4368ba314fa`
  — the honest fixture-provenance statement + per-fixture sha256 + docs
  citations for the signing algorithm and each topic payload.
- `candidates/shopify-webhook-test-kit/GOTCHAS.md@71850eeb820020047b6698e443bb88ba9ad92089`
  — the five failure modes, each mapped to a kit command.
- `candidates/shopify-webhook-test-kit/test_http_realpath.py@338ba530c6437ceb2c51b8d3d1720676c5451e88`
  — the 17-test HTTP real-path suite (true-pass + forge/unsigned/tamper/
  malformed-base64 fail + topic routing).
- `candidates/shopify-webhook-test-kit/dist/shopify-webhook-test-kit-v0.1.zip@a80a7f957908d7b82bba7d3c687ea6d8c23cf2f1`
  — the buyer bundle (sha256
  `8ff06e534187170e3d9622e72f43b7587b7e4f5e63feee4ad3917fd211ee0423`,
  29,142 bytes, 13 content files; byte-reproducible via `package.sh`).
