# GitHub webhook gotchas — the one-page checklist

The six failure modes that repeatedly break first GitHub webhook
integrations. Each maps to a kit command that proves your handler is not
making the mistake. Sources: GitHub's own docs sources, cited in
`fixtures/PROVENANCE.md` (fetched 2026-07-13).

## 1. The event name is NOT in the payload

The event type (`push`, `pull_request`, `issue_comment`, …) travels **only**
in the `X-GitHub-Event` request header. The payload's `action` field is not
a substitute: `push` and `ping` deliveries have **no** `action` at all, and
action values collide across event types (`created` is an action of
issue_comment, release, repository, …; `completed` of check_run,
check_suite, workflow_run, …). A handler that switches on `payload["action"]`
alone conflates event types or crashes on push.

**Check it:** `gwtk check-event --fixture push` ·
`gwtk check-event --fixture check_run_completed`

## 2. Verify the RAW body bytes — sha256, hex, constant-time

`X-Hub-Signature-256` is `sha256=` + the lowercase hex **HMAC-SHA256 of the
raw request body**, keyed with your webhook secret. The three classic
implementation bugs:

- **Re-serialized JSON.** Parsing the body and re-`json.dumps()`-ing it
  before hashing produces different bytes (key order, whitespace, unicode
  escaping) — signature never matches, or worse, someone "fixes" it by
  disabling verification. Hash the bytes you received.
- **`==` comparison.** GitHub's docs say verbatim: "Never use a plain `==`
  operator" — use a constant-time compare (`hmac.compare_digest`,
  `crypto.timingSafeEqual`).
- **Digest-vs-header confusion.** The header value includes the `sha256=`
  prefix; compare like against like.

**Check it:** `gwtk fire --forge` (must be rejected) and `gwtk vector`
(proves the kit's own HMAC against GitHub's published test vector).

## 3. There is NO timestamp — replays verify forever

Unlike Stripe's scheme (`t=…` + tolerance window), GitHub's signature has
**no timestamp component**. A captured delivery replays and verifies
indefinitely. GitHub's own best-practices doc: protect against replay
attacks with the `X-GitHub-Delivery` GUID — it is unique per event, and a
requested redelivery **reuses the original GUID**, so GUID dedupe also makes
redeliveries safe.

**Check it:** `gwtk fire --replay` (fires the identical delivery twice; the
bundled `stub_handler.py` shows the dedupe pattern).

## 4. Form-encoded deliveries sign the FORM body, not the JSON

A webhook created with content type `application/x-www-form-urlencoded`
(a one-click choice in the UI) delivers the JSON **inside a form field**:
`payload=%7B…%7D`. The signature covers those raw urlencoded bytes — NOT the
JSON inside. Handlers that decode first and verify the JSON see permanent
signature failures.

**Check it:** `gwtk fire --form` (signed over the raw form body, exactly as
GitHub signs it).

## 5. Fail CLOSED on missing/downgraded signatures

If your webhook has a secret configured, GitHub sends `X-Hub-Signature-256`
on **every** delivery. So:

- A delivery with **no** signature header did not come from your webhook —
  reject it. The common bug is `if header: verify()` — which silently
  accepts anything unsigned.
- A delivery carrying **only** the legacy `X-Hub-Signature` (SHA-1) header
  is a downgrade: an attacker who strips the sha256 header must not be able
  to route you onto the weaker check. GitHub keeps SHA-1 only "for
  compatibility with existing integrations" and recommends SHA-256.

**Check it:** `gwtk fire --unsigned` and `gwtk fire --sha1-only` (both must
be rejected with 4xx).

## 6. Answer `ping` — it is the first delivery you will ever get

Creating a webhook immediately sends a `ping` event (`zen`, `hook_id`,
`hook` — no `action`, no event resource). A handler that assumes
`payload["pull_request"]` exists 500s on it, and the very first thing you
see in the deliveries UI is a red X. Return 2xx on ping. Also respond fast
on everything: GitHub terminates deliveries not answered within 10 seconds
(github.com) — ack first, process async.

**Check it:** `gwtk fire --fixture ping` ·
`gwtk check-event --fixture ping`
