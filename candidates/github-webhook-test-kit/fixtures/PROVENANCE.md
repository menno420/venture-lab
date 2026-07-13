# Fixture provenance

The event payloads in this directory are **vendored byte-for-byte** from
GitHub's own machine-readable webhook example set — the
[`octokit/webhooks`](https://github.com/octokit/webhooks) repository
(MIT-licensed), which is the payload-example source GitHub's octokit tooling
and webhook schemas are built from. Nothing here was synthesized from memory:
the whole point of the kit is to test handlers against payload shapes GitHub
actually documents, because a hand-simplified stand-in hides exactly the
gotchas the kit exists to catch (the discipline this lane learned on the
Stripe Webhook Test Kit — see that kit's D1 lesson).

> `docs.github.com` is not fetchable through the agent proxy used to build
> this kit, so all citations below point at the **source files behind those
> docs pages** on `raw.githubusercontent.com` (`github/docs` markdown and
> `octokit/webhooks` payload examples), fetched 2026-07-13 (UTC) from branch
> `main`.

## Files (vendored verbatim, fetch date 2026-07-13)

| File | X-Hub event (`X-GitHub-Event`) | Source (octokit/webhooks @ main, `payload-examples/api.github.com/…`) | sha256 of the vendored file |
|---|---|---|---|
| `ping.json` | `ping` | `ping/payload.json` | `99c1656b2a959bedc162ec8881ececbd96b281059f43862dfde6a9939aa7decc` |
| `push.json` | `push` | `push/payload.json` | `909b4665b3d1ee7c6c0430f0d4d25167169954e57bfb0c80c9f70152b5fed288` |
| `pull_request_opened.json` | `pull_request` | `pull_request/opened.payload.json` | `d34772e6b4b912586626b71101fd7e9f529943866c895dcb3381ec476003e834` |
| `issue_comment_created.json` | `issue_comment` | `issue_comment/created.payload.json` | `d68665d981f7bcbdaf1d9475a192926a541fdfcb0f371e0cac21dee6cf61e992` |
| `check_run_completed.json` | `check_run` | `check_run/completed.payload.json` | `0c8bef19e50e4c66848fe3c109efdf1ccc70429ce9d866beb7c2898af0950aae` |

`EVENTS.json` (kit-authored, not vendored) maps each fixture to the
`X-GitHub-Event` header value a real delivery of that payload carries —
the event name is **not** in the payload body, which is gotcha #1.

The example payloads contain only GitHub's own illustrative values
(octocat-style demo users/repos); no fixture contains real customer data or
any secret.

## The signature scheme (verified against GitHub's own docs source)

Source: `github/docs @ main` —
`content/webhooks/using-webhooks/validating-webhook-deliveries.md`
(fetched 2026-07-13):

- Header: `X-Hub-Signature-256: sha256=<hex>` where `<hex>` is the lowercase
  hex **HMAC-SHA256** digest of the **raw request body**, keyed with the
  webhook's secret token. ("GitHub uses an HMAC hex digest to compute the
  hash. The hash signature always starts with `sha256=`.")
- A legacy `X-Hub-Signature: sha1=<hex>` (HMAC-SHA1) is also sent, "provided
  for compatibility with existing integrations"; GitHub recommends verifying
  the SHA-256 header instead
  (`content/webhooks/webhook-events-and-payloads.md`, "Delivery headers").
- Comparison must be constant-time: "Never use a plain `==` operator.
  Instead consider using a method like … `crypto.timingSafeEqual`" (same
  validating-webhook-deliveries source).
- **There is no timestamp in the scheme** (unlike Stripe's `t=` component):
  replay protection is delivery-GUID hygiene, not signature freshness. The
  docs' best-practices source
  (`content/webhooks/using-webhooks/best-practices-for-using-webhooks.md`)
  says verbatim: "In a replay attack, a bad actor intercepts a webhook
  delivery and re-sends the delivery. To protect against replay attacks, you
  can use the `X-GitHub-Delivery` header to ensure that each delivery is
  unique per event." and "If you request a redelivery, the
  `X-GitHub-Delivery` header will be the same as in the original delivery."

### GitHub's official test vector (shipped as the kit's `vector` command)

The same validating-webhook-deliveries source publishes a known-answer test:

- secret: `It's a Secret to Everybody`
- payload: `Hello, World!`
- expected header:
  `X-Hub-Signature-256: sha256=757107ea0eb2509fc211221cce984b8a37570b6d7586c22c46f4379c8b043e17`

`gwtk.py vector` / `gwtk.js vector` recompute this locally and compare —
so a buyer can prove the kit's HMAC implementation against GitHub's own
published constant in one command, offline.

## Delivery headers (verified against the docs source)

Source: `github/docs @ main` —
`content/webhooks/webhook-events-and-payloads.md`, "Delivery headers"
(fetched 2026-07-13). Real deliveries carry: `X-GitHub-Event` (the event
name), `X-GitHub-Delivery` (a GUID unique per event), `X-Hub-Signature`
(legacy SHA-1, only when a secret is set), `X-Hub-Signature-256` (SHA-256,
only when a secret is set), and a `User-Agent` that "will always have the
prefix `GitHub-Hookshot/`". The kit's `fire` sends this same header set
(User-Agent `GitHub-Hookshot/gwtk` so test traffic is honest about its
origin in your logs).

## Content types (verified against the docs source)

Source: `github/docs @ main` —
`data/reusables/webhooks/content_type_and_secret.md` (fetched 2026-07-13):

- `application/json` — "will deliver the JSON payload directly as the body
  of the `POST` request."
- `application/x-www-form-urlencoded` — "will send the JSON payload as a
  form parameter called `payload`."

In BOTH cases the signature is the HMAC of the **raw request body as sent**
— for form deliveries that is the urlencoded `payload=…` bytes, NOT the JSON
inside. `fire --form` exercises exactly this (gotcha #4).

## What is illustrative, not verified

Payload field names, structure, and values are vendored verbatim from
GitHub's published examples (above); they were NOT captured from a live
webhook delivery in this build, and no live GitHub App or webhook was
created to produce them (this repo's no-new-accounts rule). The
`X-GitHub-Delivery` GUIDs the kit generates when firing are random UUIDs,
not GitHub-issued ones — real GUIDs only exist on real deliveries.
