# GitHub Webhook Test Kit v0.1

Test your GitHub webhook handler against the deliveries GitHub really sends —
stdlib only, no dependencies, no GitHub App, no tunnel.

The kit signs vendored real-shape GitHub event payloads with the actual
`X-Hub-Signature-256` scheme (plus the legacy SHA-1 header, exactly like a
real delivery) and fires them over HTTP at your local webhook endpoint, then
checks your handler the way GitHub actually behaves: forged, unsigned,
downgraded, form-encoded, and replayed deliveries included. It catches the
specific gotchas that repeatedly break first GitHub integrations — not toy
payloads written from memory.

## Quickstart

1. Start your webhook handler (or the bundled example) listening locally. To
   run the bundled example handler:

   ```
   GWTK_WEBHOOK_SECRET=your_webhook_secret python3 stub_handler.py 8000
   ```

   The webhook secret is read from the environment — never hardcode it.

2. Prove the kit's own HMAC implementation against GitHub's published test
   vector (offline, no server needed):

   ```
   python3 gwtk.py vector
   ```

3. List the bundled fixtures:

   ```
   python3 gwtk.py list
   ```

4. Fire a correctly-signed delivery at your endpoint (PASS = handler
   returns 2xx):

   ```
   GWTK_WEBHOOK_SECRET=your_webhook_secret \
     python3 gwtk.py fire --url http://localhost:8000/webhook --fixture pull_request_opened
   ```

5. Fire the hostile variants (PASS = handler REJECTS each with 4xx — proves
   signature verification is actually running and fails closed):

   ```
   python3 gwtk.py fire --url http://localhost:8000/webhook --fixture push --forge
   python3 gwtk.py fire --url http://localhost:8000/webhook --fixture push --unsigned
   python3 gwtk.py fire --url http://localhost:8000/webhook --fixture push --sha1-only
   ```

6. Fire a form-encoded delivery (webhooks created with content type
   `application/x-www-form-urlencoded` — the signature covers the raw form
   body, not the JSON inside):

   ```
   python3 gwtk.py fire --url http://localhost:8000/webhook --fixture push --form
   ```

7. Replay the identical delivery twice (GitHub's scheme has no timestamp —
   dedupe on `X-GitHub-Delivery`):

   ```
   python3 gwtk.py fire --url http://localhost:8000/webhook --fixture push --replay
   ```

8. See where the event name actually travels (header, not payload):

   ```
   python3 gwtk.py check-event --fixture push
   ```

### Node port

`gwtk.js` mirrors the same four commands via Node (stdlib only, Node 14+):

```
node gwtk.js vector
node gwtk.js list
node gwtk.js fire --url http://localhost:8000/webhook --fixture pull_request_opened
node gwtk.js check-event --fixture ping
```

## What it checks

1. **fire** — your handler ACCEPTS a correctly-signed real delivery
   (HTTP 2xx), with the full real header set (`X-GitHub-Event`,
   `X-GitHub-Delivery`, both signature headers, `GitHub-Hookshot/` UA).
2. **fire --forge** — your handler REJECTS a wrong-secret delivery (4xx)
   instead of silently accepting it. A 2xx here means anyone who knows your
   endpoint URL can post fake events.
3. **fire --unsigned** — your handler REJECTS a delivery with no signature
   headers at all: missing signature must fail closed, not skip verification.
4. **fire --sha1-only** — your handler REJECTS a delivery carrying only the
   legacy SHA-1 header: no downgrade path off `X-Hub-Signature-256`.
5. **fire --form** — the `application/x-www-form-urlencoded` content type,
   signed over the raw form body exactly as GitHub signs it (the #1 "my
   signature never validates" cause).
6. **fire --replay** — the identical delivery, same GUID, fired twice:
   GitHub's scheme has NO timestamp, so replays verify forever; the kit
   shows both responses and the dedupe pattern to copy.
7. **check-event** — the event name lives ONLY in the `X-GitHub-Event`
   header; `push`/`ping` carry no `action` field, and action values collide
   across event types.
8. **vector** — recomputes GitHub's own published known-answer test
   (secret `It's a Secret to Everybody`, payload `Hello, World!`) and
   compares against the documented `sha256=757107ea…` constant.

## Run the kit's own tests

The kit ships with an HTTP-layer real-path test suite (every delivery is
signed and POSTed over real HTTP to a handler on an ephemeral port):

```
python3 -m unittest -v
```

## What it does NOT do

Be clear about the boundaries:

- It does **not** talk to the real GitHub API, create webhooks, or touch any
  live account.
- It does **not** validate your business logic — only the webhook edge
  behaviour (signatures, headers, content types, routing, replays).
- It is **not** a substitute for `gh webhook forward` or smee.io, which
  forward REAL deliveries from a live repo — this kit is for testing your
  handler locally *before* (and without) wiring a live webhook.
- The bundled fixtures are GitHub's own **documented example payloads**
  (vendored byte-for-byte, see `fixtures/PROVENANCE.md`), not captures from
  a live delivery; five event types ship in v0.1 (`ping`, `push`,
  `pull_request`, `issue_comment`, `check_run`).

## Where the shapes come from

See `fixtures/PROVENANCE.md` — every payload is vendored byte-for-byte from
GitHub's own machine-readable example set (`octokit/webhooks`, MIT), the
signature scheme and header facts are cited to the docs sources behind
docs.github.com, and the `vector` command proves the HMAC implementation
against GitHub's own published constant. No fixture contains real customer
data.

## Requirements

- Python 3.8+ (for `gwtk.py`, `stub_handler.py`, tests) or Node 14+
  (for `gwtk.js`).
- No account, no `pip install`, no `npm install`.
- No secret values live in this kit — the webhook secret is read from an
  env var (`GWTK_WEBHOOK_SECRET` by default).
