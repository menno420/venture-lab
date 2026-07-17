# Marketplace listing copy — Slack Webhook Test Kit v0.1

> **Status:** `reference`

**Title:** Slack Webhook Test Kit — prove your handler before you ship

**Short description (≤200 chars, 188):** Fire real-shape signed Slack requests
at your local endpoint — forged, unsigned, stale-timestamp, tampered,
form-encoded, challenge. Stdlib only. No Slack app, no workspace, no
dependencies.

**Price:** $29 (one-time)

## Description

Most Slack integration bugs don't show up while you're building — they show up
on the first real request: the `url_verification` challenge your endpoint
never answers (so Slack silently delivers nothing), the signature that "never
validates" because your request is form-encoded, the replayed request your
endpoint happily re-processes because you verified the signature but never
checked the clock.

The Slack Webhook Test Kit signs real-shape Slack request bodies with the
actual `X-Slack-Signature` `v0=` scheme (`HMAC-SHA256` over
`v0:{timestamp}:{raw_body}`, with the `X-Slack-Request-Timestamp` header
exactly like a real request) and fires them over HTTP at your local endpoint —
no Slack app, no workspace, no tunnel. It checks the gotchas that repeatedly
break first Slack integrations:

- **Forged requests accepted.** If your handler skips or fumbles signature
  verification, anyone who knows your endpoint URL can post fake requests. The
  kit fires a wrong-secret request and checks you reject it.
- **Missing signature ≠ skip verification.** `--unsigned` sends no signature
  headers at all — the classic `if header: verify()` bug silently accepts it.
- **The timestamp window is on YOU.** `--stale` sends a request with a
  perfectly VALID signature but an out-of-window `X-Slack-Request-Timestamp`.
  Slack bakes the timestamp into the signature, so a captured request stays
  "correctly signed" forever — you must reject anything older than 5 minutes.
- **Tampered bodies.** `--tamper` signs the real body, then mutates it before
  sending — a handler that hashes a re-parsed copy instead of the raw bytes
  accepts it.
- **Form-encoded signatures.** Slash commands (flat form fields) and
  interactivity (`payload=<json>`) arrive as
  `application/x-www-form-urlencoded`; the signature covers the raw form body,
  NOT the JSON inside. The kit fires both.
- **The challenge handshake.** `check-challenge` proves your endpoint answers
  the `url_verification` request by echoing its `challenge` — miss it and
  Slack never verifies your Events API URL.

Plus a built-in honesty check on the kit itself: the `vector` command
recomputes Slack's OWN published worked example (signing secret
`8f742231…`, timestamp `1531420618` → `v0=a2114d57…`) so you can prove the
kit's HMAC implementation against Slack's documentation in one offline
command.

Runs in Python or Node, entirely from the standard library. No `pip install`,
no `npm install`, no Slack account required to run the tests.

## What's inside

- The harness in two languages: `swtk.py` (Python) and `swtk.js` (Node), same
  four commands (`fire` with 4 hostile/variant modes, `check-challenge`,
  `vector`, `list`).
- An example CORRECT handler (`stub_handler.py`) you can adapt —
  timestamp-window check first, constant-time `v0=` verification, fail-closed
  on missing signature/timestamp, raw-body form support, `url_verification`
  challenge echo, `event_id` returned for your own dedupe.
- Four real-shape Slack request fixtures (`url_verification`,
  `event_callback` / `app_mention`, a slash command, a `block_actions`
  interactivity payload) + `PROVENANCE.md` documenting where every payload and
  every scheme fact comes from, with a pinned sha256 per fixture.
- An HTTP-layer real-path test suite (`test_http_realpath.py`, 18 tests) —
  every request is signed and POSTed over real HTTP.
- A one-page `GOTCHAS.md` checklist and a `QUICKSTART.md`.

## Requirements

- Python 3.8+ or Node 14+.
- No Slack account, no dependencies, no build step.
- Your signing secret is read from an environment variable — no secret values
  are stored in the kit.

## What it does NOT do (so you know what you're buying)

- It does not talk to the real Slack API, create an app, or touch any live
  workspace.
- It does not validate your business logic — only the request edge behaviour
  (signatures, the timestamp window, the challenge, content types).
- It is not a substitute for Slack's own request-URL tester or Socket Mode,
  which forward REAL requests from a live app; this kit tests your handler
  locally before (and without) wiring one.
- If you use Slack's official **Bolt** SDK, it verifies signatures for you —
  this kit is for handlers you hand-roll outside Bolt.
- The fixtures are **reconstructed from Slack's own documentation** (cited
  file-by-file in `PROVENANCE.md`), not captures from a live workspace. Four
  request shapes ship in v0.1.
- Claims are verified by citation: every signature/timestamp/content-type fact
  in `GOTCHAS.md` and `PROVENANCE.md` names the Slack docs page it was checked
  against — audit them yourself, and run `vector` to check the HMAC.

## FAQ

**Why not just use Slack's request-URL tester or ngrok + a real app?**
Those need a live app, a configured Request URL, and a reachable endpoint —
and they only send well-formed requests. This kit runs against `localhost`
with zero setup and also sends the hostile ones (forged, unsigned, stale,
tampered) that Slack will never helpfully send you.

**Isn't the signing code just a few lines?**
Yes — and Slack documents it. What you're paying for is the harness + the
real-shape fixtures + the hostile modes (especially the stale-timestamp replay
check, the one people forget) + the challenge-echo test, all runnable against
your own endpoint in seconds. The free substitute is real; the kit is the
done version.

**Refunds / support / license:** [owner-to-set — storefront defaults;
suggested: 14-day no-questions refund, single-developer license, email support
best-effort.]

---

## PROVENANCE-FOOTER

Every claim above is checkable against the committed source (blob `file@sha`
at build time, branch `claude/slack-webhook-test-kit-2026-07-17`):

- `candidates/slack-webhook-test-kit/swtk.py@2d60c6cdd82207dd9b8663d80f6d29c6147e3f7f`
  — the harness (signature scheme, fire modes, vector, challenge check).
- `candidates/slack-webhook-test-kit/fixtures/PROVENANCE.md@3af20594f4e34a6b6d1eb4df41d0a63c840f57a2`
  — the honest fixture-provenance statement + per-fixture sha256 + docs
  citations for the signing algorithm and each payload type.
- `candidates/slack-webhook-test-kit/GOTCHAS.md@7f476fae9460ac4b8e54181993f90d9b182c65ce`
  — the six failure modes, each mapped to a kit command.
- `candidates/slack-webhook-test-kit/test_http_realpath.py@1150627c075d6391538a1b0a55f263281541f20f`
  — the 18-test HTTP real-path suite (true-pass + forge/unsigned/stale/tamper
  fail).
- `candidates/slack-webhook-test-kit/dist/slack-webhook-test-kit-v0.1.zip@66f429b20f65f9c3dc6b574607b8725784b97931`
  — the buyer bundle (sha256
  `9ea865735de0402a534f872f816c8cc1eea68fcecfb114b3a1499114abd755e8`,
  29,290 bytes, 14 content files; byte-reproducible via `package.sh`).
