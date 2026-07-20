# membership cluster → Reddit submission (paste-ready)

> **Status:** `reference`

- **Suggested subreddit:** **r/SaaS** — founders and builders running paid products; tolerant of substantive build/ops write-ups that teach first. (r/stripe also fits and is smaller/more technical; r/SaaS is the higher-reach honest home.)
- **Where to click:** https://www.reddit.com/r/SaaS/submit
- **CTA reminder:** value-first. The teaching IS the post; the single soft product line sits at the very end. No links in the body. Replace `⟨owner: …⟩` before posting, or drop that last line entirely if the sub's rules are strict.

**How to post:** open the submit link, choose a **Text** post, paste the **Title**, then paste the **Body** into the text field (Reddit renders Markdown).

**Title:**

```
Seven things paid-membership sites get wrong about Stripe webhooks and access control (and the fix for each)
```

**Body:**

````markdown
A paid-membership site is a deceptively simple loop: someone pays, they get access, and when they stop paying, access goes away. Stripe Checkout makes the first half feel done in an afternoon. The trouble is that "who is allowed in right now" is not a fact you own — it lives in Stripe and reaches you through **webhooks**: asynchronous, retried, occasionally out of order, sometimes never delivered. Almost every membership bug is a place where the site treated that fragile signal as reliable. Seven that pass a happy-path demo and still leak access, double-charge, or lock out a paying customer.

**1. You grant membership straight from the webhook, without verifying it.** A webhook URL is a public, unauthenticated endpoint; anyone who learns it can POST a body that looks exactly like a real Stripe event and mint themselves a free membership. Your happy path never sends a forged event, so the reject path is never exercised. *Fix:* verify the `Stripe-Signature` header with your `whsec_…` secret **before** trusting a byte — hash the **raw** body byte-for-byte (not a re-serialized copy), and **fail closed** on a missing secret/header or a stale timestamp.

**2. A retried webhook grants (or charges) twice.** Stripe retries on non-2xx *or timeout*; the timeout is the trap — you already granted access and *then* were slow to return 200, so Stripe retries and you grant twice. The test fires each event once, so it never sees the double. *Fix:* make the handler idempotent on Stripe's `event.id` — record processed IDs, return 200 on a duplicate without re-running the grant, and do the check + grant in one transaction. Return 200 fast; push emails/provisioning to a background job.

**3. A failed payment revokes access instantly — no grace period.** A card expires, Stripe sends `invoice.payment_failed`, and you lock the member out on the spot — but Stripe is about to run *dunning* (days of retries + recovery emails that save most of these customers). You just churned a paying subscriber over a temporary decline. *Fix:* gate access on **subscription status**, not the last payment's outcome. `past_due`/`unpaid` keep access through your configured grace window; revoke only at `canceled`.

**4. Access is a boolean you set once, instead of a fact you derive.** `user.is_member = true` on first payment, never correctly reset — so a canceled member keeps access forever, or you flip it off at cancel-click and kick out someone paid through the period end. A boolean can't represent "a member until March 14." *Fix:* store the *facts* (`status`, `current_period_end`, `cancel_at_period_end`) and **derive** access at check time — active/trialing (or past_due within grace) *and* period end in the future.

**5. Revocation rides on a single webhook you might never receive.** Your whole "remove access" path depends on one `customer.subscription.deleted` event — and webhooks are best-effort (a deploy, a 500, a signature reject during secret rotation, and it's gone). The result is ghost members who cancelled months ago and are still inside, which no error log flags because nothing errored. *Fix:* treat webhooks as an optimization, not the source of truth — **reconcile on a schedule** (or lazily at access time) by asking Stripe for current status via the API. Listen *and* poll; never listen alone.

**6. Out-of-order webhooks re-grant access you just revoked.** Stripe doesn't guarantee order. You can get `...deleted` and then an older `...updated` that still says `active`, and a handler that applies the latest webhook re-grants a subscription you correctly revoked. Locally every event arrives in order because you fire it that way. *Fix:* don't trust the event payload as current state — refetch the subscription from the API by ID, or record each subscription's freshest timestamp and ignore any event older than what you've applied.

**7. Membership is keyed off the email, not a stable Stripe ID.** Match webhooks by `customer_email` and reality breaks it: a customer pays with one email and signed up with another, changes it in your app but not Stripe, or shares a checkout — and the grant lands on the wrong account or no account. *Fix:* key membership off the stable Stripe IDs (`cus_…`, `sub_…`), store the customer ID on the user record the first time you see it, and match every later webhook by that ID. Email is a display field that can change without moving an entitlement.

**The pattern under all seven:** treating a webhook as the truth instead of a *notification about* the truth. The truth lives in Stripe's subscription objects; webhooks are an at-least-once, unordered, occasionally-dropped stream of hints. The fix is always the same shape — **verify the hint, make handling it idempotent, store the facts it carries, and derive access from those facts with a reconcile behind you** — so no single webhook is load-bearing.

Cheapest place to start today: fire the same `checkout.session.completed` at your endpoint twice and confirm you granted membership exactly once. Ten minutes, catches the double-grant that costs you the most.

---

*(One line of disclosure: I build small stdlib-first membership starters + a Stripe webhook test kit that fire exactly these cases, each with a correct/broken reference. Entirely optional; everything above stands on its own. ⟨owner: your Gumroad link⟩)*
````
