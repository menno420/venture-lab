# API Robustness Bundle — v0.1

Four small, stdlib-only, account-free **own-endpoint robustness test kits** in
one download — the Idempotency Key, Rate-Limit, Pagination, and JWT Auth test
kits — bundled at a discount. Each kit points at an endpoint *you own* and
reports PASS/FAIL per property against real-shape fixtures, with an HTTP-layer
test suite you can run in one command with no vendor account and no secrets.

**Price:** **$79** for all four — versus **$116** bought separately (4 × $29).
That is **$37 off (~32%)**. See [`PROVENANCE.md`](PROVENANCE.md) for the pricing
math and the per-kit artifact pins.

> **What you download:** one zip that contains the four component kits' own
> buyer bundles (their exact `*-v0.1.zip` files, byte-for-byte — pinned by
> sha256 in [`MANIFEST.json`](MANIFEST.json)) plus this README, the
> [`QUICKSTART.md`](QUICKSTART.md), and [`PROVENANCE.md`](PROVENANCE.md). Unzip,
> then unzip whichever kit you need — each is self-contained and documented.

---

## What's included

### 1. Idempotency Key Test Kit ($29 alone)

Proves your API's `Idempotency-Key` handling is correct — that a safe retry
triggers the side effect **exactly once**, so a network blip never charges a
customer twice. Checks five properties against an endpoint you own: **replay**
(same key + body replays the stored original response), **mismatch** (same key +
different body → 409/422), **distinct-keys** (different keys → independent
resources), **concurrent** (two in-flight requests with the same key → one side
effect), and **missing-key** (your documented required/passthrough policy).
Behaviour follows Stripe's widely-used model / the IETF `Idempotency-Key` draft.
Tests the **dedup / safe-retry contract**, not signatures.

### 2. Rate-Limit Test Kit ($29 alone)

Proves your API's rate limiter behaves correctly — that it returns **429** at
the limit (not one request late), emits a valid **`Retry-After`**, keeps its
**`RateLimit-*` headers** honest, and actually **resets** its window when it
says it will. Fires a burst and reports PASS/FAIL per property: **under-limit**,
**over-limit** (the off-by-one quota leak), **retry-after**, and the header /
reset checks. The 429 + `Retry-After` semantics follow RFC 6585 §4 and RFC 9110
§10.2.3; the `RateLimit-*` fields follow the IETF draft (stated honestly as a
draft, not an RFC). Tests **throttling correctness**.

### 3. Pagination Test Kit ($29 alone)

Proves your API's pagination is correct — that following the next-cursor walks
the whole result set with **no skipped and no duplicated** items, stays
**stable when rows are inserted/deleted mid-traversal** (the property naive
`OFFSET` pagination fails), keeps a **consistent order**, **honors the page-size
limit**, **signals the last page**, and **rejects a forged cursor**. Reports
PASS / FAIL / SKIP per property. There is no single RFC for cursor pagination —
the kit tests the keyset/cursor model (Stripe / Slack / GitHub cursor pagination
+ the keyset-vs-offset literature) and says so. Tests **result-set integrity**.

### 4. JWT Auth Test Kit ($29 alone)

Proves your API's JWT authentication is **secure** — that a protected endpoint
**accepts** a valid, correctly-signed, unexpired token with the right claims and
**rejects** the critical auth-bypass classes: an `alg:none` unsigned token, a
tampered / wrong-signature / wrong-key token, the **RS256→HS256
algorithm-confusion** attack, an **expired** token, a **not-yet-valid**
(`nbf`/`iat` future) token, a wrong/missing **audience** and **issuer**, and a
structurally-malformed token. Nine properties, each grounded in RFC 7519 / RFC
7515 / RFC 8725 plus the well-known `alg:none` and algorithm-confusion attacks.
The highest-severity problem class in the set: **verifier security — auth
bypass**. (Honest scope: HS256 + the attack classes above are fully covered
stdlib-only; real RS256/ES256 signature-math verify is scoped out-of-band, as
the kit's own listing states.)

---

## Why these four together

These are the four kits that test **an endpoint you own** for the robustness
properties that are invisible until they fail in production, each a *different*
problem class: **exactly-once** on retry (idempotency), **throttling** under
load (rate-limit), **result-set integrity** while paging (pagination), and
**auth-bypass resistance** on a protected route (JWT). A team hardening an API
hits all four — a double charge, a quota leak, a skipped row mid-walk, an
`alg:none` bypass — and each has the same shape of bug: the happy path passes,
the edge silently doesn't. Buying the set gives you a correct-vs-broken
reference and a runnable PASS/FAIL suite for each, so "is my endpoint actually
robust?" stops being a guess.

Same honest v0.x scope as the individual listings: these are **own-endpoint test
kits**, not frameworks or middleware. They prove your endpoint's behaviour
against real-shape fixtures; they do not implement idempotency, rate-limiting,
pagination, or JWT verification *for* you.

## Honesty notes

- The four component kits are **not modified** by this bundle. You receive each
  kit's own published buyer zip, pinned by sha256 in `MANIFEST.json`. If a kit
  is later revised, the bundle is re-cut against the new pin.
- **None of the four kits is live today** — all four are queued owner publish
  clicks (Idempotency D7 / JWT Auth D9 / Pagination D15 / Rate-Limit D18 in the
  OWNER-QUEUE). This bundle is a storefront **discount SKU** over the four kits;
  on Gumroad it can only be created once all four component products are
  published (see the owner gate in the vetting packet). The download works
  standalone regardless — the four kits inside it are complete.
- There is **zero new product code** here: the bundle is an assembly of four
  already-built, already-tested kits plus this documentation. The test in this
  directory is an **assembly/inventory check**, not a fifth product test suite —
  each kit's own suite ships inside its zip and runs the same way it always has.
- This is the own-endpoint sibling of the **Webhook Verifier Bundle** (the
  inbound-edge four-pack). The two bundles share no components and are priced
  identically ($79 over four $29 kits); a buyer wiring up *and* hardening an API
  may want both, but neither depends on the other.
