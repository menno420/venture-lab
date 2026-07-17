# Quickstart — Slack Webhook Test Kit v0.1

Three minutes from unzip to a green check on your own handler. Stdlib only —
no `pip install`, no `npm install`, no Slack app.

## 0. Prove the kit itself (offline, no server)

```
python3 swtk.py vector      # or: node swtk.js vector
```

Expect `PASS` — the kit recomputes Slack's own published worked example
(signing secret `8f742231…`, timestamp `1531420618`) and matches the
documented `v0=a2114d57…` constant. If this fails, re-download the kit.

## 1. Set your signing secret in the environment

Copy `.env.example` to `.env` and fill in your app's **Signing Secret**
(Slack app → *Basic Information* → *App Credentials* → *Signing Secret*). Then
export it — the kit reads the NAME from the env and never stores the value:

```
export SLACK_SIGNING_SECRET=your_signing_secret_here
```

(The Signing Secret is NOT a bot token and NOT the legacy Verification Token.)

## 2. Start a handler

Either your own handler, or the bundled correct example:

```
SLACK_SIGNING_SECRET=$SLACK_SIGNING_SECRET python3 stub_handler.py 8000
```

It listens on `http://127.0.0.1:8000`.

## 3. Fire the happy path

```
python3 swtk.py fire --url http://localhost:8000/slack/events --fixture event_callback_app_mention
```

Expect `PASS` (HTTP 2xx). Try the form surfaces too:

```
python3 swtk.py fire --url http://localhost:8000/slack/events --fixture slash_command
python3 swtk.py fire --url http://localhost:8000/slack/events --fixture interactive_block_actions
```

## 4. Fire the hostile path (this is the point)

Each of these must be REJECTED (4xx) by a correct handler:

```
python3 swtk.py fire --url http://localhost:8000/slack/events --fixture event_callback_app_mention --forge
python3 swtk.py fire --url http://localhost:8000/slack/events --fixture event_callback_app_mention --unsigned
python3 swtk.py fire --url http://localhost:8000/slack/events --fixture event_callback_app_mention --stale
python3 swtk.py fire --url http://localhost:8000/slack/events --fixture event_callback_app_mention --tamper
```

If any of these prints `FAIL`, your handler is accepting requests it should
refuse — see `GOTCHAS.md` for the fix.

## 5. Check the challenge handshake

```
python3 swtk.py check-challenge --url http://localhost:8000/slack/events
```

Expect `PASS` — your endpoint answered 200 AND echoed the `challenge` value.
Without this, Slack never verifies your Events API URL.

## 6. Run the kit's own test suite

```
python3 -m unittest -v
```

Every request is signed with the real scheme and POSTed over actual HTTP to a
handler on an ephemeral port. All green = the kit is intact on your machine.

---

Next: read `GOTCHAS.md` (one page, six failure modes) and adapt
`stub_handler.py` into your framework of choice.
