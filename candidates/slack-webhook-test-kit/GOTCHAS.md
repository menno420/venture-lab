# Slack request-signing gotchas — the one-page checklist

The failure modes that repeatedly break first Slack integrations. Each maps
to a kit command that proves your handler is not making the mistake. Sources:
Slack's own docs, cited in `fixtures/PROVENANCE.md` (reconstructed 2026-07-17).

## 1. Enforce the ±300s timestamp window — BEFORE the signature

Slack signs `"v0:" + X-Slack-Request-Timestamp + ":" + body`, but it also
sends the timestamp as its own header and the docs tell you to **reject any
request more than five minutes (300s) from now** — "it could be a replay
attack, so you should ignore it." A handler that verifies the signature but
never checks the clock accepts a captured request forever: the signature
stays valid because the timestamp is baked into it. Check freshness first,
then trust the signature.

**Check it:** `swtk fire --stale` (a VALID signature on an out-of-window
timestamp — must be rejected).

## 2. Verify the RAW body bytes — sha256, hex, constant-time

`X-Slack-Signature` is `v0=` + the lowercase hex **HMAC-SHA256** of the base
string, keyed with your **Signing Secret** (not a bot token, not the
verification token). The three classic bugs:

- **Re-serialized / re-parsed body.** Parsing the body and re-encoding it
  before hashing produces different bytes — for form requests especially
  (key order, `+` vs `%20`). Hash the exact bytes you received.
- **`==` comparison.** Use a constant-time compare
  (`hmac.compare_digest`, `crypto.timingSafeEqual`), never `==`.
- **Wrong secret.** The Signing Secret (Basic Information → App Credentials)
  is not the legacy Verification Token and not a bot/user OAuth token.

**Check it:** `swtk fire --forge` (wrong secret, must be rejected),
`swtk fire --tamper` (body mutated after signing, must be rejected), and
`swtk vector` (proves the kit's own HMAC against Slack's published example).

## 3. Answer the `url_verification` challenge — it's the FIRST request

The moment you save an Events API Request URL, Slack POSTs a
`url_verification` request: `{"type":"url_verification","challenge":"…"}`.
You must respond 200 and **echo the `challenge` value back** (plain text, or
JSON `{"challenge": "…"}`). Miss it and Slack marks the URL unverified and
delivers **no events at all** — the integration silently never starts.

**Check it:** `swtk check-challenge` (offline explainer, or `--url` to POST
the fixture and confirm your handler echoes the challenge).

## 4. Fail CLOSED on a missing signature or timestamp

If a request arrives with no `X-Slack-Signature` (or no
`X-Slack-Request-Timestamp`), it did not come from Slack — reject it. The
common bug is `if sig_header: verify()`, which silently accepts anything
unsigned. A configured app ALWAYS signs.

**Check it:** `swtk fire --unsigned` (no signature headers — must be
rejected with 4xx).

## 5. Form surfaces sign the FORM body, not the JSON inside

Slash commands and interactivity arrive as
`application/x-www-form-urlencoded`. Slash commands are flat fields
(`command=…&text=…`); interactivity nests the JSON in a single `payload`
field (`payload=%7B…%7D`). In BOTH cases the signature covers the **raw
urlencoded bytes**, not the decoded fields or the inner JSON. Handlers that
`parse_qs` first and hash the reconstructed body see permanent signature
failures.

**Check it:** `swtk fire --fixture slash_command` and
`swtk fire --fixture interactive_block_actions` (both signed over the raw
form body, exactly as Slack sends it).

## 6. Respond within 3 seconds — ack fast, work async

Slack retries any Events API delivery it doesn't get a 2xx for within 3
seconds (and slash commands / interactivity expect a fast response too).
A slow handler gets the same event again — so acknowledge immediately and do
heavy work out-of-band, and dedupe on `event_id` (Events API) since retries
re-send it.

**Check it:** the bundled `stub_handler.py` acks with 2xx before any work and
returns the `event_id` so you can wire your own dedupe.
