# Marketplace listing copy — GitHub Webhook Test Kit v0.1

> **Status:** `reference`

**Title:** GitHub Webhook Test Kit — prove your handler before you ship

**Short description (≤200 chars, 183):** Fire real-shape signed GitHub
webhook deliveries at your local endpoint — forged, unsigned, downgraded,
form-encoded, replayed. Stdlib only. No GitHub App, no tunnel, no
dependencies.

**Price:** $29 (one-time)

## Description

Most GitHub webhook bugs don't show up while you're building — they show up
on the first real delivery: the `ping` your handler 500s on, the signature
that "never validates" because your webhook is form-encoded, the forged POST
your endpoint silently accepts because the verification path was never
actually exercised.

The GitHub Webhook Test Kit signs vendored, real-shape GitHub event payloads
with the actual `X-Hub-Signature-256` scheme (plus the legacy SHA-1 header,
exactly like a real delivery, with the full `X-GitHub-Event` /
`X-GitHub-Delivery` header set) and fires them over HTTP at your local
endpoint — no GitHub App, no live webhook, no tunnel. It checks the six
gotchas that repeatedly break first GitHub integrations:

- **Forged deliveries accepted.** If your handler skips or fumbles signature
  verification, anyone who knows your endpoint URL can post fake events. The
  kit fires a wrong-secret delivery and checks you reject it.
- **Missing signature ≠ skip verification.** `--unsigned` sends no signature
  headers at all — the classic `if header: verify()` bug silently accepts it.
- **SHA-1 downgrade.** `--sha1-only` strips the sha256 header and offers only
  the legacy `X-Hub-Signature` — a correct handler refuses the downgrade.
- **Form-encoded signatures.** Webhooks created with content type
  `application/x-www-form-urlencoded` sign the raw `payload=…` form bytes,
  NOT the JSON inside. `--form` reproduces exactly that.
- **Replays verify forever.** GitHub's scheme has NO timestamp (unlike
  Stripe). `--replay` fires the identical delivery twice, same
  `X-GitHub-Delivery` GUID, and shows you the dedupe pattern to copy.
- **The event name is not in the payload.** `push` and `ping` have no
  `action` field; action values collide across event types. `check-event`
  shows why routing must start from the `X-GitHub-Event` header.

Plus a built-in honesty check on the kit itself: the `vector` command
recomputes GitHub's OWN published known-answer test (secret
`It's a Secret to Everybody`, payload `Hello, World!` →
`sha256=757107ea…`) so you can prove the kit's HMAC implementation against
GitHub's documentation in one offline command.

Runs in Python or Node, entirely from the standard library. No `pip
install`, no `npm install`, no GitHub account required to run the tests.

## What's inside

- The harness in two languages: `gwtk.py` (Python) and `gwtk.js` (Node),
  same four commands (`fire` with 5 hostile/variant modes, `check-event`,
  `vector`, `list`).
- An example CORRECT webhook handler (`stub_handler.py`) you can adapt —
  constant-time sha256 verification, fail-closed on missing/downgraded
  signatures, raw-body form support, ping handling, delivery-GUID dedupe.
- Five vendored real-shape GitHub payloads (`ping`, `push`,
  `pull_request` opened, `issue_comment` created, `check_run` completed) +
  `PROVENANCE.md` documenting byte-for-byte where every payload and every
  scheme fact comes from.
- An HTTP-layer real-path test suite (`test_http_realpath.py`, 18 tests) —
  every delivery is signed and POSTed over real HTTP.
- A one-page `GOTCHAS.md` checklist with the six failure modes.

## Requirements

- Python 3.8+ or Node 14+.
- No GitHub account, no dependencies, no build step.
- Your webhook secret is read from an environment variable — no secret
  values are stored in the kit.

## What it does NOT do (so you know what you're buying)

- It does not talk to the real GitHub API, create webhooks, or touch any
  live account.
- It does not validate your business logic — only the webhook edge
  behaviour.
- It is not a substitute for `gh webhook forward` or smee.io, which forward
  REAL deliveries from a live repo; this kit tests your handler locally
  before (and without) wiring one.
- The fixtures are GitHub's own documented example payloads, vendored
  byte-for-byte and cited in `PROVENANCE.md` — not captures from a live
  delivery. Five event types ship in v0.1.
- Claims are verified by citation: every signature/header/content-type fact
  in `GOTCHAS.md` and `PROVENANCE.md` names the GitHub docs source file it
  was checked against — audit them yourself.

## FAQ

**Why not just use GitHub's redeliver button or `gh webhook forward`?**
Those need a live repo, a configured webhook, and a reachable endpoint —
and they only send well-formed deliveries. This kit runs against
`localhost` with zero setup and also sends the hostile ones (forged,
unsigned, downgraded, replayed) that GitHub will never helpfully send you.

**Refunds / support / license:** [owner-to-set — storefront defaults;
suggested: 14-day no-questions refund, single-developer license, email
support best-effort.]
