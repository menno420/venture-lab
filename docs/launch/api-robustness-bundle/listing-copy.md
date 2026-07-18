# API Robustness Bundle ($79) — listing copy

> **Status:** `reference`
>
> Ready-to-paste copy for a **Gumroad bundle** of the four own-endpoint
> robustness test kits (Idempotency Key + Rate-Limit + Pagination + JWT Auth,
> $29 each). **HARD-GATED:** a Gumroad bundle references its component products
> as existing live products — it cannot be created until the not-yet-published
> component kits are live. None of the four is live yet; the gate is on the
> Idempotency ($29, OWNER-QUEUE **D6**), JWT Auth ($29, **D7**), Pagination
> ($29, **D13**), and Rate-Limit ($29, **D16**) publish clicks. The buyer
> artifact is the bundle zip (`api-robustness-bundle-v0.1.zip`, sha256
> `6be74b6d78a77180a133fd09c31c452baaea77497cd8db63461b9ee43dfb560c`) which
> contains the four component buyer zips verbatim; per-component pins are in the
> [§7 packet](../../publishing/vetting/api-robustness-bundle.md) §1 /
> [`candidates/api-robustness-bundle/MANIFEST.json`](../../../candidates/api-robustness-bundle/MANIFEST.json).

## Title
```
API Robustness Bundle — Idempotency + Rate-Limit + Pagination + JWT Auth Test Kits
```

## Short description (≤ 200 chars)
```
All four own-endpoint robustness kits — Idempotency, Rate-Limit, Pagination, JWT Auth — for $79 instead of $116 separately. Stdlib-only, account-free, one command to run each kit's tests. $37 off.
```

## Long description
```
These are the four kits that test an endpoint YOU own for the robustness properties that stay invisible until they fail in production — each a different problem class:

- Idempotency Key — does a safe retry trigger the side effect exactly once, so a network blip never charges a customer twice? (replay / mismatch / distinct-keys / concurrent / missing-key)
- Rate-Limit — does the limiter return 429 at the limit (not one request late), emit a sane Retry-After, keep its RateLimit-* headers honest, and actually reset its window? (the off-by-one quota leak is the headline)
- Pagination — does following the next-cursor walk the whole result set with no skipped and no duplicated items, even when rows are inserted/deleted mid-traversal? (the property naive OFFSET pagination fails)
- JWT Auth — does a protected endpoint accept a valid token and reject the auth-bypass classes: alg:none, tampered/wrong-key, the RS256->HS256 algorithm-confusion attack, expired, not-yet-valid, wrong audience/issuer, malformed?

Each kit points at your endpoint and reports PASS/FAIL per property against real-shape fixtures, and ships an HTTP real-path test suite you run in one command against bundled correct-vs-broken reference stubs. No vendor account, no API key, no network.

Same honest v0.x scope as the individual listings: these are own-endpoint test kits, not frameworks or middleware. They prove your endpoint's behaviour is correct; they don't implement idempotency, rate-limiting, pagination, or JWT verification for you. Nothing here is hype.
```

## Bullets
```
- All four own-endpoint robustness kits — Idempotency, Rate-Limit, Pagination, JWT Auth — one download, $79 vs $116 bought separately ($37 / ~32% off)
- Each kit: real-shape fixtures + a correct/broken reference pair + a one-command HTTP real-path test suite, PASS/FAIL per property
- Four different problem classes: exactly-once on retry, throttling under load, result-set integrity while paging, auth-bypass resistance on a protected route
- Stdlib-only Python (with a JS parity port alongside) — no account, no API key, no network, no dependencies
- Each artifact pinned by sha256; the bundle contains the four kits' own published zips verbatim
```

## FAQ
```
Q: Can I buy just one kit?
Yes — each is sold separately at $29. The bundle is for people hardening more than one property of an API; it saves $37 and three checkouts.

Q: What exactly do I download?
One zip that contains the four component kits' own buyer zips (byte-for-byte, sha256-pinned) plus a README, QUICKSTART, and MANIFEST. Unzip the bundle, then unzip whichever kit you need — each is self-contained.

Q: Do the kits depend on each other?
No. Each kit is standalone and tests a different problem class. They pair only in the sense that a team hardening an API wants a correct-vs-broken reference and a runnable test for each robustness property.

Q: How is this different from the Webhook Verifier Bundle?
That bundle covers the inbound edge — verifying webhook signatures FROM Stripe/GitHub/Slack/Shopify. This one covers YOUR OWN endpoint's robustness. They share no components and are priced identically ($79); a team wiring up and hardening an API may want both.

Q: Are these full frameworks?
No — they're own-endpoint test kits. They prove your endpoint's behaviour is correct against real-shape fixtures. Honest v0.x scope, same as the individual listings.
```
