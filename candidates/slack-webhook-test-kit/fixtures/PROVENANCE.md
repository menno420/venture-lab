# Fixture provenance

**Honest statement up front:** the request bodies in this directory were
**reconstructed from Slack's official published documentation**, not captured
from a live Slack workspace. No Slack app was created and no live workspace
was connected to build this kit (this repo's no-new-accounts rule). Every
field name, shape, and signing fact below is cited to the Slack docs page it
was taken from, so a buyer can audit each claim against Slack's own
documentation. Where a value is illustrative (a demo user id, a demo
challenge string), it carries Slack's own documented example value or a
clearly-fake test value — never a real token or secret.

> Fetched/reconstructed 2026-07-17 (UTC). Citations are to `api.slack.com`
> documentation pages by title + path; the values reproduced here are the
> ones Slack publishes as worked examples on those pages.

## The signature scheme (from Slack's docs)

Source: **api.slack.com — "Verifying requests from Slack"**
(`https://api.slack.com/authentication/verifying-requests-from-slack`):

- Header: `X-Slack-Signature: v0=<hex>` where `<hex>` is the lowercase hex
  **HMAC-SHA256** digest, keyed with your app's **Signing Secret**, of a
  **base string**.
- Base string: `"v0:" + X-Slack-Request-Timestamp + ":" + <raw request body>`
  — colon-joined, and the body is the **raw bytes of the request** taken
  **before any parsing**. (Slack: "Concatenate the version number, the
  timestamp, and the body of the request, using a colon as the delimiter.")
- The version prefix is `v0` today; Slack signs and expects the same `v0`
  string, and reserves higher versions for future schemes.
- **Replay protection is a separate, mandatory check:** Slack sends
  `X-Slack-Request-Timestamp`, and the docs instruct you to **reject any
  request whose timestamp is more than five minutes (300 seconds) from local
  time** before trusting the signature — "it could be a replay attack, so you
  should ignore it." This is the key difference from GitHub (no timestamp at
  all) and the same 300s window as Stripe (but signed differently).
- **Constant-time compare:** the docs' reference snippets compare with
  `hmac.compare` / `hash_equals`-style constant-time equality, never `==`.

### Slack's published worked example (shipped as the kit's `vector` command)

The same "Verifying requests from Slack" page publishes a fully worked
known-answer example:

- signing secret: `8f742231b10e8888abcd99yyyzzz85a5`
- `X-Slack-Request-Timestamp`: `1531420618`
- request body: the slash-command form body vendored here as
  `slash_command.txt` (byte-for-byte the docs' example body).
- expected signature:
  `v0=a2114d57b48eac39b9ad189dd8316235a7b4a8d21a10bd27519666489c69b503`

`swtk.py vector` / `swtk.js vector` recompute this locally and compare — so a
buyer can prove the kit's HMAC implementation against Slack's own published
constant in one command, offline. (Reproduced and verified during this build.)

## The fixtures (reconstructed from documented example shapes)

| File | Content-Type of a real request | Reconstructed from (api.slack.com) | sha256 of the vendored file |
|---|---|---|---|
| `url_verification.json` | `application/json` | "Events API — Request URL configuration / responding to the `url_verification` challenge" — the documented `{token, challenge, type}` handshake body (challenge value is Slack's own example string) | `9a69dea0924095e441ad77c86c3de2d792b7c317d527226b61e751fae8b7ac0c` |
| `event_callback_app_mention.json` | `application/json` | "Events API — event delivery / the `event_callback` wrapper" + "the `app_mention` event type" — the documented outer wrapper (`type: event_callback`, `event_id`, `event_time`, `authorizations`) around an `app_mention` inner event | `b0733f73fa10b13d76e73e0ce8f078ec4cee08de4a0dc2bb791864d66d5feb11` |
| `slash_command.txt` | `application/x-www-form-urlencoded` | "Verifying requests from Slack" worked example — the exact form body Slack publishes; also "Slash commands — the request payload" (flat form fields: `command`, `text`, `user_id`, `response_url`, `trigger_id`, …) | `390eeeff8d0cb7c9f6ecf8a88c3df6452fea0914eb02f64844369f3758d8d330` |
| `interactive_block_actions.txt` | `application/x-www-form-urlencoded` | "Handling user interaction — interactivity payloads" — a `block_actions` payload delivered as `payload=<urlencoded JSON>`; the inner JSON uses the documented `block_actions` shape (`type`, `user`, `actions[]`, `response_url`, `trigger_id`) | `b4c81a2c5c2dcfd64f46f691802382cb635f956bc8fb666af60c212fde94d0e1` |

`MANIFEST.json` (kit-authored, not vendored) maps each fixture stem to the
`Content-Type` a real Slack request of that shape carries — Slack does **not**
put the content type in the body, and the signature covers the **raw body as
sent**, so the kit needs this manifest to fire each fixture the way Slack
would deliver it.

## Content types (from Slack's docs)

Slack delivers different product surfaces with different content types, and
the signature always covers the **raw request body as sent**:

- **Events API** (`url_verification`, `event_callback`) → `application/json`;
  the body IS the JSON document.
- **Slash commands** → `application/x-www-form-urlencoded`; flat form fields
  (`command=…&text=…&user_id=…`).
- **Interactivity** (block actions, shortcuts, modals) →
  `application/x-www-form-urlencoded` with the JSON nested in a single
  `payload` field (`payload=%7B…%7D`).

For the two form surfaces, the signature is the HMAC of those **raw
urlencoded bytes** — NOT the JSON inside the `payload` field. `fire`
reproduces exactly this by signing the stored raw body verbatim (gotcha #2).

## What is illustrative, not wire-captured

Payload field names, structure, and values are reconstructed from Slack's
published example shapes (cited above); they were **not** captured from a live
Slack delivery in this build, and no live Slack app or workspace was created
to produce them. The signing secret, tokens, user/team ids, `challenge`, and
`trigger_id` values are Slack's own documented example values or clearly-fake
test values — none is a real credential. The `X-Slack-Request-Timestamp` the
kit sends when firing is the current clock (or a deliberately stale value for
`--stale`), not a Slack-issued one; real timestamps only exist on real
requests.
