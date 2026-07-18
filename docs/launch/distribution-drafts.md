# Distribution drafts

> **Status:** `reference`

Announcement drafts — honest, low-hype. Nothing here is published; the owner posts these from their own accounts (each is an OWNER-ACTION). Fill `<PRODUCT_URL>` after ⚑B/⚑D.

## "Show HN"-style
```
Show HN: A stdlib-only Python membership-site kit (Stripe pre-wired, honest v0.x)

I built a small paid-membership starter in stdlib-only Python: an http.server backend, a static landing page, and a gated members stub, with the payment → membership → gated-access loop already wired together. It runs in mock mode with zero accounts so you can watch the whole loop before connecting anything. The membership-grant logic, the deny-when-unpaid 402 gate, idempotent purchases, and JSON persistence are unit-tested. Being honest about scope: Stripe Checkout + the webhook handler are included and pre-wired, but the live Stripe path has not been through a live purchase — that last mile is yours. There's also a $19 pay-what-you-want Agent-Workflow Template Pack (session-discipline templates + advisory hooks) if that's more your thing. Links: <PRODUCT_URL>
```

## Newsletter / blog short
```
Two small, honest starters, built in agent sessions and committed in-repo. The first is a Membership-Site Boilerplate Kit ($49): a stdlib-only Python backend with the payment → membership → gated-access loop pre-wired and running in mock mode with zero accounts. Its grant logic, 402 gate, idempotent purchases, and persistence are unit-tested — and, being straight about it, the live Stripe path is pre-wired but not yet live-tested, so the last mile is yours. The second is an Agent-Workflow Template Pack ($19 pay-what-you-want): a constitution template, session-log card, one-page playbook, and three advisory (fail-open) Claude Code hooks. Grab either, or the $59 bundle. No hype, no "$20K in 7 days" — just two starters you can read, own, and finish. <PRODUCT_URL>
```

## Social / X-LinkedIn short (≤ 280 chars)
```
Shipped a stdlib-only Python membership-site kit ($49): payment → membership → gated-access loop, pre-wired, runs in mock mode with zero accounts. Grant logic unit-tested; Stripe path pre-wired but not yet live-tested (honest v0.x). Companion template pack, $19 PWYW. <PRODUCT_URL>
```

---

## Dev cluster — API-robustness lead magnet

These drafts lead with the **free article** ([`api-robustness-lead-magnet.md`](api-robustness-lead-magnet.md)) — the top-of-funnel discovery asset for the webhook + API-robustness test-kit cluster. The article teaches real failure modes and carries its own soft product footer; these blurbs point at the article first, and the two four-pack bundles (higher AOV) before the singles. The article is content, not a sales post — post it as an article, and let its footer do the funnel. Fill `<ARTICLE_URL>` with the posted article's canonical URL and `<PRODUCT_URL>` after ⚑B/⚑D. Every post below is an OWNER-ACTION from the owner's own account.

### "Show HN"-style
```
Show HN: Six ways your API passes tests and still breaks in production

I wrote up the systematic gap between a green test suite and production for webhook receivers and public APIs: the webhook handler that isn't replay-safe (a provider retry double-processes the event), the endpoint that accepts forged events because it skips signature verification, retries that turn a blip into a self-inflicted outage, offset pagination that silently skips or duplicates rows when the data set changes mid-traversal, a 429 with no Retry-After so clients hammer you, and the CORS + Authorization config that's either broken (missing preflight) or a wide-open credentials hole. For each: why the unit test misses it, and the actual fix. No metrics, no hype — just the failure modes and the ten-minute test that catches the most expensive one. I also sell small stdlib-only test kits that fire these at your endpoint, mentioned in a footer, but the article stands alone. <ARTICLE_URL>
```

### r/programming · r/webdev teaser
```
Your tests pass. Your API still breaks in production. Here's the systematic gap.

Unit tests fire one well-formed request, in order, against a fresh data set. Production fires the same request twice (client timeout → provider retry), out of order (two racing), with a forged body (your webhook URL is public), against a data set that changed between page one and page two. I wrote up six failure modes that pass every test and still drop real traffic — non-idempotent webhook handlers, missing signature verification, retry storms, offset-pagination drift, a 429 with no Retry-After, and the CORS/Authorization footgun — with why the test misses each and what the fix is. Free, no signup. (I sell stdlib-only test kits for these too — that's a footer, not the post.) <ARTICLE_URL>
```

### dev.to / Hashnode intro
```
A green test suite proves your code does what your TESTS say — not what PRODUCTION does, and the gap between those two is a systematic one, not bad luck. This post walks six failure modes that pass every test and still break real traffic: a webhook handler that isn't replay-safe, an endpoint that accepts forged events, retries that amplify an outage, pagination that skips or duplicates rows under mutation, a 429 that tells clients nothing, and a CORS config that's either broken or a security hole. Each section is the failure, why the test misses it, and the real fix — the kind of adversarial case you have to write on purpose because your fixtures encode the beliefs the bug lives in the gap of. If you'd rather not hand-write those tests, I make stdlib-only kits that fire them at your endpoint (two bundles: Webhook Verifier and API Robustness, then singles) — but that's the last paragraph, and the article is the point. <ARTICLE_URL> · kits: <PRODUCT_URL>
```
