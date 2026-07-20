# api-robustness cluster → Reddit submission (paste-ready)

> **Status:** `reference`

> **⚑ EDITORIAL NOTE — removal risk on r/webdev (read before posting).** r/webdev
> enforces self-promotion limits, and moderators there routinely remove a *first*
> text post that ends in a product/store link — even a soft, single disclosure
> line like the one at the foot of this body — as self-promo, regardless of how
> much the post teaches first. The teaching content here is genuinely value-first,
> which mitigates but does **not** eliminate that risk. Honest options, safest first:
> **(a)** post the body with the final disclosure line **removed entirely** — no
> store link anywhere in the post (the write-up stands on its own); put any link
> only in a **reply/comment if asked** or in your **profile**; **(b)** read the
> subreddit's current rules/wiki and any "self-promo Saturday" or ratio rule and
> follow it exactly; or **(c)** retarget to a **link-tolerant channel** (e.g.
> r/webhooks, r/SaaS, r/LLMDevs, or your own blog/dev.to cross-post) where a
> single end-of-post link is within norms. Do not add the link back into the body
> just because a placeholder exists. This note is advisory; the file is kept intact.

- **Suggested subreddit:** **r/webdev** — large, tolerant of substantive technical write-ups that teach first. (r/programming is a poor fit: it removes self-posts and self-promo; r/webdev and r/webhooks are the honest homes for this.)
- **Where to click:** https://www.reddit.com/r/webdev/submit
- **CTA reminder:** value-first. The teaching IS the post; the single soft product line sits at the very end. No links in the body. Replace `⟨owner: …⟩` before posting, or drop that last line entirely if the sub's rules are strict.

**How to post:** open the submit link, choose a **Text** post, paste the **Title**, then paste the **Body** into the text field (Reddit renders Markdown).

**Title:**

```
Your tests pass. Your API still breaks in production. Six failure modes that pass every test and still drop real traffic.
```

**Body:**

````markdown
A green test suite proves your code does what your *tests* say. It does not prove your code does what *production* does — and that gap is systematic, not bad luck. Unit tests fire one well-formed request, in order, against a fresh data set. Production fires the same request twice (a client timed out), out of order (two raced), with a forged body (your URL is public), against a data set that changed between page one and page two. All of it is invisible to a suite that only exercises the happy path. Six failure modes, why the test misses each, and the fix.

**1. Your webhook handler isn't replay-safe.** Providers retry on non-2xx *or timeout*. The timeout is the trap: your handler already committed the side effect and *then* was slow to return 200, so the provider retries and you grant/charge/email twice. The test fires each event once, so it never sees the double. *Fix:* make the handler idempotent on the provider's event ID — record processed IDs, return 200 on a duplicate without re-running the effect, and do the "seen this ID?" check and the side effect in one transaction (or two concurrent retries both pass the check first).

**2. Your endpoint accepts forged events.** A webhook URL is a public, unauthenticated endpoint; anyone who learns it can POST a body that looks real. If you act on it without verifying the signature, you've built an open API for fake events. The test's fixtures are all legitimate, so the reject path is never exercised — and "never exercised" looks identical to "works." *Fix:* verify the signature on every request, and get the three details right — hash the **raw** body byte-for-byte (not a re-serialized copy), use a **constant-time** compare (`hmac.compare_digest`, not `==`), and match the provider's exact scheme (Shopify is base64 not hex; Slack signs `v0:{timestamp}:{body}` with a replay window; GitHub is `sha256=` over the raw body). Fail **closed**: a missing secret/header is a rejection, never a skip.

**3. Your retries turn a blip into an outage.** Retry without guard rails and a brief hiccup becomes self-inflicted: every client retries at the same instant (thundering herd), the retries *are* the load keeping the dependency down, and a timed-out POST gets retried into a double write. A failed *response* isn't a failed *operation*. *Fix:* retry only retryable statuses (429, 408, 425, 5xx, transport) and only idempotent operations; back off exponentially **with jitter**; cap the blast radius with a retry budget + circuit breaker; honor `Retry-After` as a floor.

**4. Your pagination silently skips or duplicates rows.** `LIMIT n OFFSET k` is correct in every test and wrong the moment the data set changes between page fetches — delete a row and the window slides (one row skipped forever); insert one and a returned row comes back. The test never mutates the collection mid-traversal, which is the one condition that breaks offset paging. *Fix:* paginate by **keyset/cursor** on a stable ordered key (`WHERE (created_at, id) > (:last_ts, :last_id) ORDER BY created_at, id LIMIT n`); clamp the page size server-side; make cursors opaque and tamper-evident; emit an explicit terminal signal (`next_cursor: null`).

**5. Your 429 tells clients nothing, so they hammer you.** A limiter that returns `429` with no `Retry-After` makes throttled clients either hammer you harder or give up entirely. The companion bug is the off-by-one (`count <= limit + 1` passes 101 on a "100/hour"). The test asserts "over the limit returns 429" and stops. *Fix:* a correct 429 is a *contract* — ship a valid `Retry-After` and honor it, get the boundary exact (`limit` passes, `limit + 1` is the first rejection), prove the window resets, and consider `RateLimit-*` headers (note honestly: those are an IETF draft; the `429 + Retry-After` half rests on stable RFCs 6585 and 9110).

**6. Your CORS config is either broken or a security hole.** Two opposite failures. Broken: `Authorization` isn't a "simple" header, so an authenticated cross-origin request triggers a preflight `OPTIONS` first — miss the handler and the browser never sends the real request. Dangerous: to make the error go away someone sets `Allow-Origin: *`, can't pair it with `Allow-Credentials: true`, so they reflect the request's `Origin` **plus** allow credentials — now any site your logged-in user visits can hit your API with their cookies. CORS is enforced by the *browser*, so `curl`/server-side tests never see either bug. *Fix:* keep an explicit origin **allowlist** and echo back only listed origins (never blind-reflect); never pair `*` with credentials; answer the preflight deliberately.

**The pattern under all six:** the test author writes fixtures from their mental model of the system, and the bug lives in the gap between that model and reality. You don't close it by writing more tests from the same memory — you close it by testing the *adversarial* cases: the replayed event, the forged signature, the concurrent retry, the mutated data set, the boundary request, the browser preflight.

The cheapest place to start: add the replay test to your webhook handler today — fire the same event ID twice, assert the side effect happened once. Ten minutes, catches the most expensive bug on the list.

---

*(One line of disclosure: I make small stdlib-only test kits that fire exactly these cases at your endpoint, each with a correct/broken reference pair. Entirely optional; everything above stands on its own. ⟨owner: your Gumroad link⟩)*
````
