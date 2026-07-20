# api-robustness cluster → Hashnode submission (paste-ready)

> **Status:** `reference`

- **Where to click:** https://hashnode.com/create/story
- **CTA reminder:** soft footer only — funnel to the **Webhook Verifier Bundle** and **API Robustness Bundle** first, then the single test kits. Post it as an article, not a sales post.
- **Canonical rule for this file:** this lab has no live blog and ~0 traffic. If Hashnode is where you publish **first**, leave the Canonical URL field **blank** — Hashnode becomes canonical. If you already published on dev.to (or your own site) first, set Hashnode's **Canonical URL** (post settings → "Canonical URL") to that first URL to credit the original and avoid a duplicate-content penalty.

**How to post:** open https://hashnode.com/create/story. Put the **Title** in the title field, add the **Tags**, set the **Canonical URL** per the rule above, then paste the **Body** block into the editor. Replace each `⟨owner: …⟩` marker with your real link before publishing.

**Title:**

```
Your tests pass. Your API still breaks in production. Here's the gap.
```

**Tags (add up to 4):** `APIs` · `Web Development` · `Testing` · `Webhooks`

**Body (paste into the editor):**

````markdown
A green test suite proves your code does what your tests say. It does not prove
your code does what production does. The gap between those two is where most
API and webhook bugs live — and it's a *systematic* gap, not bad luck. Unit
tests fire one request, in order, with a well-formed payload, against a fresh
data set. Production fires the same request twice because a client timed out,
out of order because two of them raced, with a forged body because your URL is
public, and against a data set that changed between page one and page two.

None of that is exotic. All of it is invisible to a suite that only ever
exercises the happy path. Below are six failure modes that pass every test and
still drop real traffic — with why the test misses them and what the fix
actually is. If you've shipped a webhook receiver or a public API and haven't
deliberately tested these, at least one of them is probably live in your code
right now.

## 1. Your webhook handler isn't replay-safe

**The failure.** Providers (Stripe, GitHub, Slack, Shopify, and every queue you
didn't write) retry a webhook when your endpoint returns non-2xx *or times
out*. A timeout is the dangerous case: your handler may have already committed
the side effect — granted the membership, shipped the order, incremented the
balance — and *then* been slow to return 200. The provider sees no 200, retries,
and your handler runs the whole thing again. The customer is granted twice,
charged twice, emailed twice.

**Why the test passes.** Your test fires each event exactly once and asserts the
side effect happened. It never fires the same event ID twice, so it never sees
the double. "Handles the event correctly" and "handles the event *once* under
retry" are different properties, and the suite only checks the first.

**The fix.** Make the handler idempotent on the provider's event ID (Stripe's
`id`, GitHub's `X-GitHub-Delivery`, etc.). Record processed IDs; on a duplicate,
return 200 *without* re-running the side effect. Do the "have I seen this ID?"
check and the side effect under one transaction (or an atomic
insert-if-absent), or two concurrent retries both pass the check before either
records the ID and you're back to a double. Return 200 fast, do slow work
async, so a slow handler doesn't *cause* the retry it can't survive.

## 2. Your endpoint accepts forged events

**The failure.** A webhook URL is a public, unauthenticated HTTP endpoint.
Anyone who learns it — from a leaked log, a browser extension, a former
employee — can POST a payload that *looks* exactly like a real event. If you
parse the JSON and act on it without verifying the signature, you've built an
open API for minting free memberships and fake "payment succeeded" events.

**Why the test passes.** Your fixtures are all legitimate. The suite never sends
a request with a *wrong* or *missing* signature, so the code path that should
reject one is never exercised — and "never exercised" reads identically to
"works" on a green dashboard.

**The fix.** Verify the provider's signature on every request, and get the three
details right that people miss:

- **Hash the raw request body, byte-for-byte** — not a parsed-and-re-serialized
  copy. Re-serializing reorders keys and changes whitespace, so the digest never
  matches and you "fix" it by disabling verification. Read the raw bytes *before*
  your framework parses them.
- **Use a constant-time comparison** (`hmac.compare_digest`, not `==`). A
  byte-by-byte `==` leaks timing that can be used to forge a signature.
- **Match the provider's exact scheme.** Shopify sends **base64**, not hex.
  Slack signs the string `v0:{timestamp}:{body}` and expects you to reject a
  stale timestamp (replay window). GitHub is `sha256=` over the raw body and
  still ships a legacy SHA-1 header you should ignore. Getting the scheme
  "close" fails closed if you're lucky and open if you're not.

Fail *closed*: a missing secret, a missing header, or an unparseable signature
is a rejection, never a skip.

## 3. Your retries turn a blip into an outage

**The failure.** A downstream call fails, so you retry it. Applied without guard
rails, that one instinct is how a brief hiccup on one dependency becomes a
self-inflicted outage: every client retries at the same instant (a thundering
herd), the retries *are* the load that keeps the dependency down, and a POST
that actually succeeded-but-timed-out gets retried into a double write. A failed
*response* is not a failed *operation* — when a write times out you cannot tell
whether it ran.

**Why the test passes.** The test injects one failure and asserts one retry
succeeds. It never fires the concurrent herd, never measures the total retry
volume under a sustained outage, and never checks that retrying a timed-out POST
is safe. The loop looks correct in isolation and is dangerous in aggregate.

**The fix.** Retries are a small stack of cooperating decisions, not a loop on
error:

- **Retry only what's retryable:** 429, 408, 425, 5xx, and transport failures.
  Never any other 4xx — a 400 or 403 will fail identically forever.
- **Only retry idempotent operations.** A bare POST isn't safe to retry; a POST
  carrying an idempotency key is. Make the write safe *first*, then retry it.
- **Back off exponentially with jitter.** Fixed or un-jittered backoff
  re-synchronizes the herd on the next attempt. Full/equal/decorrelated jitter
  de-correlates clients so they stop colliding.
- **Cap the blast radius** with a retry budget (retries as a small fraction of
  live traffic) and a circuit breaker that fails fast on a dead dependency and
  probes once on recovery.
- **Honor `Retry-After`** as a floor over your own backoff — never retry sooner
  than the server told you to.

## 4. Your pagination silently skips or duplicates rows

**The failure.** `LIMIT n OFFSET k` looks correct in every test and is wrong the
moment the data set changes between page fetches. Delete a row before the reader
asks for page two and the offset window slides — one unread row is skipped
forever. Insert one and a row you already returned comes back on the next page.
Every export, every "sync since last time", every infinite-scroll feed quietly
loses or repeats records, and nobody files a bug because nobody can see the gap.

**Why the test passes.** The test seeds a fixed data set, reads all the pages,
and asserts it got every row. It never *mutates* the collection mid-traversal,
so the one condition that breaks offset pagination is the one condition the test
guarantees never happens.

**The fix.** Paginate by **keyset / cursor**, not offset: page on a stable,
ordered key (`WHERE (created_at, id) > (:last_ts, :last_id) ORDER BY created_at,
id LIMIT n`) so inserts and deletes elsewhere can't shift your window. Then:

- **Clamp the page size.** An unbounded `?limit=100000` is a denial-of-service
  and a memory spike; cap it server-side and document the cap.
- **Make cursors opaque and tamper-evident** (sign them) so a client can't forge
  one into someone else's result set, and coerce a garbage cursor to a `400`,
  not silently to page one.
- **Emit a clear terminal signal** (an explicit `next_cursor: null`) so clients
  know they're done instead of guessing from a short page.

## 5. Your 429 tells clients nothing, so they hammer you

**The failure.** You added a rate limiter, and under load it does return `429 Too
Many Requests` — with no `Retry-After` header. So every throttled client either
hammers you immediately (making the overload worse) or gives up entirely (a
failed request that didn't need to fail). The classic companion bug is the
off-by-one: a `count <= limit + 1` check lets your advertised "100/hour" quietly
pass 101, so the limit you documented isn't the limit you enforce.

**Why the test passes.** The test asserts "over the limit returns 429" and stops
there. It doesn't assert the response carries a *usable* `Retry-After`, doesn't
cross the exact boundary to catch the off-by-one, and doesn't wait out a window
to prove it actually reopens (tests hate waiting). The status code is right and
everything a client needs to behave is missing.

**The fix.** A correct 429 is a *contract*, not a status code:

- Ship a valid **`Retry-After`** (delay-seconds or an HTTP-date) and actually
  honor it — don't advertise 30s and start rejecting again at 5s.
- Get the boundary exact: request number `limit` passes, `limit + 1` is the
  first rejection.
- Prove the window **resets** on schedule rather than quietly never reopening.
- Consider the `RateLimit-*` headers (limit / remaining / reset) so well-behaved
  clients can self-pace before they ever hit a 429. Honest caveat: those headers
  are an **IETF draft** and optional; the `429 + Retry-After` half rests on
  stable RFCs (6585, 9110). Say which half you're relying on.

## 6. Your CORS config is either broken or a security hole

**The failure.** CORS has two opposite failure modes and teams hit both. The
*broken* one: `Authorization` is not a CORS "simple" header, so a cross-origin
authenticated request triggers a **preflight `OPTIONS`** first — and if your
server doesn't answer the preflight (with `Access-Control-Allow-Headers:
Authorization` and the right method list), the browser never sends the real
request, and you spend an afternoon debugging a "CORS error" that's really a
missing `OPTIONS` handler. The *dangerous* one: to make the error go away
someone sets `Access-Control-Allow-Origin: *`. That can't be combined with
`Access-Control-Allow-Credentials: true` (browsers reject the pair), so the fix
becomes "reflect whatever `Origin` the request sent" *plus* allow credentials —
which means **any website your logged-in user visits can make authenticated
requests to your API with their cookies.** That's a cross-site request forgery
hole with a green "CORS works now" checkmark on top.

**Why the test passes.** CORS is enforced by the *browser*, not the server. A
`curl` or a server-side test ignores CORS entirely — every request succeeds — so
a test suite that isn't driving a real browser can't see either the broken
preflight or the wide-open reflection. The header the browser would reject sails
through your integration tests.

**The fix.** Maintain an explicit **allowlist** of origins and echo an origin
back only if it's on the list — never blind-reflect the request's `Origin`.
Never pair `Allow-Origin: *` with `Allow-Credentials: true`. Answer the
preflight `OPTIONS` deliberately: the allowed methods, the allowed headers
(including `Authorization`), and a sane `Access-Control-Max-Age`. Decide on
purpose whether the endpoint needs credentials at all.

## The pattern under all six

Every one of these passes tests for the same reason: **the test author writes
the fixtures from their mental model of the system, and the bug is in the gap
between that model and reality.** The suite that says the webhook carries a
signature you verify, the retry is safe, the page set is stable, and the 429 is
polite is green precisely because it encodes those beliefs — and production
doesn't share them. You don't close that gap by writing more tests from the same
memory. You close it by testing the *adversarial* cases: the replayed event, the
forged signature, the concurrent retry, the mutated data set, the boundary
request, the browser preflight.

That's it — the whole article is above, and it's free. Go add one adversarial
test to your webhook handler today; the replay case (fire the same event ID
twice, assert the side effect happened once) takes ten minutes and catches the
most expensive bug on the list.

---

### If you'd rather not hand-write those adversarial tests

I write and sell small, stdlib-only Python test kits that point at *your* endpoint
and fire exactly the cases above — no vendor account, no app install, no tunnel,
and each ships a correct/broken reference pair so you can see the check actually
catch a bug. Entirely optional; the article stands on its own.

If more than one of these hit home, the two bundles are the better value:

- **Webhook Verifier Bundle** — the Stripe, GitHub, Slack, and Shopify webhook
  test kits in one download, for the inbound edge (§1 and §2 above). ▸ ⟨owner: your Gumroad link⟩
- **API Robustness Bundle** — the idempotency / safe-retry, rate-limit,
  pagination, and JWT-auth test kits in one download, for your own endpoints
  (§3, §4, §5 above, plus auth-bypass). ▸ ⟨owner: your Gumroad link⟩

Or pick the single kit that matches the failure you recognized:

- **Idempotency Key Test Kit** — proves a retried write runs exactly once (§1, §3).
- **Rate-Limit Test Kit** — proves the boundary, the `Retry-After`, and the reset (§5).
- **Pagination Test Kit** — proves no rows skip or duplicate under mutation (§4).
- **JWT Auth Test Kit** — proves the verifier rejects `alg:none`, algorithm
  confusion, and expired/wrong-audience tokens.
- The four **webhook test kits** (Stripe / GitHub / Slack / Shopify) — real-shape
  signed payloads, tamper and replay cases included (§2).

And the *why* under all of it, if you want the discipline rather than the tools:
**The False-Green Test Trap** (how memory-authored fixtures lie) and **The
Idempotency & Retry Cookbook** (the safe-retry pattern stack from §3, taught with
runnable recipes). Links: ⟨owner: your Gumroad link⟩.

No hype, no invented metrics, no "used by N companies" — just the failure modes,
and some optional tools that fire them at your code so you don't have to write
them from memory.
````
