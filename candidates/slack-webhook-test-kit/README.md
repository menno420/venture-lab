# Slack Webhook Test Kit v0.1

Test your Slack request handler against the requests Slack really sends —
stdlib only, no dependencies, no Slack app, no workspace, no tunnel.

The kit signs real-shape Slack request bodies with the actual
`X-Slack-Signature` `v0=` scheme (`HMAC-SHA256` over
`v0:{timestamp}:{raw_body}`, plus the `X-Slack-Request-Timestamp` header
exactly like a real request) and fires them over HTTP at your local endpoint,
then checks your handler the way Slack actually behaves: forged, unsigned,
stale-timestamp (replay), tampered-body, form-encoded, and the
`url_verification` challenge included. It catches the specific gotchas that
repeatedly break first Slack integrations — not toy payloads written from
memory.

## Quickstart

1. Start your handler (or the bundled example) listening locally. To run the
   bundled example handler:

   ```
   SLACK_SIGNING_SECRET=your_signing_secret python3 stub_handler.py 8000
   ```

   The signing secret is read from the environment — never hardcode it.

2. Prove the kit's own HMAC implementation against Slack's published worked
   example (offline, no server needed):

   ```
   python3 swtk.py vector
   ```

3. List the bundled fixtures:

   ```
   python3 swtk.py list
   ```

4. Fire a correctly-signed request at your endpoint (PASS = handler returns
   2xx):

   ```
   SLACK_SIGNING_SECRET=your_signing_secret \
     python3 swtk.py fire --url http://localhost:8000/slack/events --fixture event_callback_app_mention
   ```

5. Fire the hostile variants (PASS = handler REJECTS each with 4xx — proves
   verification is actually running and fails closed):

   ```
   python3 swtk.py fire --url http://localhost:8000/slack/events --fixture event_callback_app_mention --forge
   python3 swtk.py fire --url http://localhost:8000/slack/events --fixture event_callback_app_mention --unsigned
   python3 swtk.py fire --url http://localhost:8000/slack/events --fixture event_callback_app_mention --stale
   python3 swtk.py fire --url http://localhost:8000/slack/events --fixture event_callback_app_mention --tamper
   ```

6. Fire the form-encoded surfaces (slash commands are flat form fields;
   interactivity nests the JSON in a `payload=` field — the signature covers
   the raw form body, not the JSON inside):

   ```
   python3 swtk.py fire --url http://localhost:8000/slack/events --fixture slash_command
   python3 swtk.py fire --url http://localhost:8000/slack/events --fixture interactive_block_actions
   ```

7. Check the `url_verification` challenge handshake (the first request Slack
   ever sends; your endpoint must echo the challenge back):

   ```
   python3 swtk.py check-challenge --url http://localhost:8000/slack/events
   ```

### Node port

`swtk.js` mirrors the same four commands via Node (stdlib only, Node 14+):

```
node swtk.js vector
node swtk.js list
node swtk.js fire --url http://localhost:8000/slack/events --fixture slash_command
node swtk.js check-challenge --url http://localhost:8000/slack/events
```

## What it checks

1. **fire** — your handler ACCEPTS a correctly-signed real request (HTTP 2xx),
   with the real header set (`X-Slack-Signature`, `X-Slack-Request-Timestamp`,
   a `Slackbot` User-Agent).
2. **fire --forge** — your handler REJECTS a wrong-secret request (4xx)
   instead of silently accepting it. A 2xx here means anyone who knows your
   URL can post fake requests.
3. **fire --unsigned** — your handler REJECTS a request with no signature
   headers: missing signature must fail closed.
4. **fire --stale** — your handler REJECTS a request whose timestamp is
   outside the ±300s window, **even though its signature is valid**. This is
   Slack's replay defence, and it is on you — the timestamp is baked into the
   signature, so a captured request stays "correctly signed" forever.
5. **fire --tamper** — signs the real body, then mutates it before sending:
   your handler REJECTS it because it hashes the RAW bytes it received, not a
   re-parsed copy.
6. **fire --fixture slash_command / interactive_block_actions** — the
   `application/x-www-form-urlencoded` surfaces, signed over the raw form body
   exactly as Slack signs them (the #1 "my signature never validates" cause).
7. **check-challenge** — the `url_verification` handshake: your endpoint must
   answer 200 and echo the `challenge` value, or Slack never verifies the URL
   and delivers no events.
8. **vector** — recomputes Slack's own published worked example (signing
   secret `8f742231…`, timestamp `1531420618`) and compares against the
   documented `v0=a2114d57…` constant.

## Run the kit's own tests

The kit ships with an HTTP-layer real-path test suite (every request is signed
and POSTed over real HTTP to a handler on an ephemeral port):

```
python3 -m unittest -v
```

## What it does NOT do

Be clear about the boundaries:

- It does **not** talk to the real Slack API, create an app, or touch any live
  workspace.
- It does **not** validate your business logic — only the request edge
  behaviour (signatures, timestamp window, challenge, content types).
- It is **not** a substitute for Slack's own request-URL tester or a tunnel
  (ngrok / Socket Mode), which forward REAL requests from a live app — this
  kit is for testing your handler locally *before* (and without) wiring one.
- The bundled fixtures are **reconstructed from Slack's official
  documentation** (see `fixtures/PROVENANCE.md`), not captures from a live
  workspace; four request shapes ship in v0.1 (`url_verification`,
  `event_callback` / `app_mention`, a slash command, and a `block_actions`
  interactivity payload).

## Where the shapes come from

See `fixtures/PROVENANCE.md` — every request body is reconstructed from
Slack's published example shapes, with the signing algorithm, timestamp
window, and each payload type cited to the Slack docs page it came from, and
the `vector` command proves the HMAC implementation against Slack's own
published constant. No fixture contains a real token or secret.

## Requirements

- Python 3.8+ (for `swtk.py`, `stub_handler.py`, tests) or Node 14+
  (for `swtk.js`).
- No account, no `pip install`, no `npm install`.
- No secret values live in this kit — the signing secret is read from an env
  var (`SLACK_SIGNING_SECRET` by default).
