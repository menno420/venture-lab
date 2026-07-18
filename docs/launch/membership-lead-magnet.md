# The seven things every paid-membership site gets wrong about Stripe webhooks and access control

> **Status:** `reference`
>
> A free, standalone article — written to be posted as-is to dev.to / Hashnode
> or as a Show HN / r/SaaS / r/stripe submission. It teaches the real failure
> modes of wiring Stripe into a paid-membership site; the product mention at the
> end is a soft, honest footer, not the point. Nothing here is published or spent
> by the seat — posting is an **owner** paste-and-post (OWNER-ACTION), same as
> every launch asset. Draft copy; fill `<ARTICLE_TITLE>` / `<PRODUCT_URL>` before
> posting. Channel drafts for this cluster already live in
> [`distribution-drafts.md`](distribution-drafts.md).

---

A paid-membership site is a deceptively simple loop: someone pays, they get
access, and when they stop paying, access goes away. Stripe Checkout makes the
first half feel done in an afternoon — a payment link, a success page, a member
who's now inside. The trouble is that "who is allowed in right now" is not a
fact you own; it's a fact that lives in Stripe and reaches you through
**webhooks** — asynchronous, retried, occasionally out of order, and sometimes
never delivered at all. Almost every membership bug is a place where the site
treated that fragile signal as if it were a reliable one.

Below are seven failure modes that pass a happy-path demo — you pay, you're in,
the video plays — and still leak free access, double-charge, or lock out a
paying customer once real money and real time are involved. For each: what
actually goes wrong, why it bites in production and not in your test, and the
mechanical fix. If you've wired Stripe into a membership site and haven't
deliberately handled these, at least one of them is probably live right now.

---

## 1. You grant membership straight from the webhook, without verifying it

**The failure.** Your `/webhook` endpoint receives `checkout.session.completed`,
reads the customer, and flips them to "member." But a webhook URL is a public,
unauthenticated HTTP endpoint. Anyone who learns it — from a leaked log, a
browser network tab, a former contractor — can POST a body that looks exactly
like a real Stripe event. If you parse the JSON and act on it without checking
the signature, you have built a public API for minting free memberships and fake
`invoice.paid` events.

**Why it bites in production.** Your happy path never sends a *forged* event, so
the code path that should reject one is never exercised — and "never exercised"
looks identical to "works" on a green dashboard. It stays invisible until
someone curls your endpoint, and by then the free grants are already in your
database looking exactly like paid ones.

**The fix.** Verify the `Stripe-Signature` header on every request with your
endpoint's signing secret (`whsec_…`) *before* you trust one byte of the body,
and get the two details people miss right. **Hash the raw request body,
byte-for-byte** — not a parsed-and-re-serialized copy; re-serializing reorders
keys and breaks the digest, and the usual "fix" is to disable verification. And
**fail closed**: a missing secret, a missing header, or a stale timestamp
(Stripe signs a timestamp so you can reject replays outside a tolerance window)
is a rejection, never a skip. Only after the signature checks out do you look at
what the event says.

---

## 2. A retried webhook grants (or charges) twice

**The failure.** Stripe retries a webhook whenever your endpoint returns non-2xx
*or times out*. The timeout is the dangerous case: your handler may have already
granted the membership — or, on the billing side, already triggered the side
effect — and *then* been slow to return 200. Stripe sees no 200, retries, and
your handler runs the whole thing again. The member is granted twice, the
welcome email fires twice, and any per-event action you took happens twice.

**Why it bites in production.** Your test fires each event exactly once and
asserts the grant happened. It never fires the same `event.id` twice, so it
never sees the double. "Handles the event correctly" and "handles the event
*once* under retry" are different properties, and a single-shot test only checks
the first. Real Stripe traffic — slow handlers, at-least-once delivery — checks
the second for you, in front of customers.

**The fix.** Make the handler idempotent on Stripe's `event.id`. Record
processed event IDs; on a duplicate, return 200 *without* re-running the grant.
Do the "have I seen this ID?" check and the grant under **one transaction** (or
an atomic insert-if-absent), or two concurrent retries both pass the check
before either records the ID and you're back to a double. Return 200 *fast* and
push slow work (emails, provisioning) to a background job, so a slow handler
doesn't *cause* the retry it then can't survive.

---

## 3. A failed payment revokes access instantly — no grace period

**The failure.** A member's card expires. Stripe's renewal charge fails and
sends `invoice.payment_failed`. Your handler treats "payment failed" as "not a
member" and locks them out on the spot. But Stripe hasn't given up — it's about
to run *dunning*: several automatic retries over days, plus the emails that
recover most of these customers. You've locked out a paying subscriber over a
temporary card decline, generated a support ticket, and quite possibly a
cancellation you caused yourself.

**Why it bites in production.** In a demo you never sit through a real dunning
cycle, so the difference between `past_due` (still your customer, Stripe is
retrying) and `canceled` (actually gone) never comes up. In production it's a
large share of your churn, and it's the *avoidable* share.

**The fix.** Treat access as a function of **subscription status**, not of the
last payment's outcome. A subscription in `past_due` or `unpaid` still keeps
access through the grace window you configure in Stripe's dunning settings;
you revoke only when the subscription actually reaches `canceled` (via
`customer.subscription.deleted` or a `status` transition), which Stripe emits
after its retries are exhausted. Let Stripe run the retry-and-recover cycle it's
designed for, and gate access on the *status field*, not the failure event.

---

## 4. Access is a boolean you set once, instead of a fact you derive

**The failure.** On the first successful payment you set `user.is_member = true`
and gate the members' area on that flag. Nothing ever sets it back to `false` at
exactly the right moment. So a canceled member keeps access forever; or, if you
*do* flip it off the instant they click cancel, you kick out someone who cancels
mid-month and is paid through the end of the period. Either way the boolean and
the real entitlement have drifted apart, and no test catches drift because the
test only checks the moment you set the flag.

**Why it bites in production.** `cancel_at_period_end = true` is the normal shape
of a cancellation: the member stays entitled until `current_period_end`, then
lapses. A boolean can't represent "a member until March 14." Time passes in
production and never in a unit test, so the flag looks right the day you write it
and is wrong three weeks later.

**The fix.** Store the *facts* Stripe gives you — the subscription `status` and
`current_period_end` (and `cancel_at_period_end`) — and **derive** access at
check time: a member is someone whose subscription is `active` or `trialing`, or
`past_due` within grace, *and* whose `current_period_end` is in the future. Then
"is this person allowed in right now?" is a computed answer from stored facts,
not a stale flag someone forgot to reset. Cancellation at period end just works,
because you never revoked early — the derived check lapses on its own when the
period ends.

---

## 5. Revocation rides on a single webhook you might never receive

**The failure.** Your entire "remove access when they stop paying" path depends
on receiving one event — `customer.subscription.deleted`. But webhooks are
best-effort: an endpoint that's down for a deploy, a handler that 500s on a
malformed-looking body, a signature check that (correctly) rejects during a
secret rotation, and that event is gone. Stripe retries for a while and then
stops. The revocation never happens, and a former customer keeps full access
indefinitely — the single most common way membership sites leak paid content.

**Why it bites in production.** You can't test "the event that never arrived,"
and locally every event arrives. The gap is only visible as a slow accumulation
of ghost members who cancelled months ago and are still inside, which no error
log ever flags because nothing errored — the work simply never ran.

**The fix.** Treat webhooks as an *optimization*, not the source of truth.
**Reconcile on a schedule:** a periodic job (or a lazy check at access time for
stale records) that asks Stripe for the subscription's *current* status via the
API and re-derives access, so a dropped `deleted` event self-heals on the next
pass. Make the webhook handler resilient enough not to drop events it should
process (return 200 for events you don't handle rather than erroring the whole
delivery), and back it with the reconcile so no single missed webhook is
load-bearing. Listen *and* poll; never listen alone.

---

## 6. Out-of-order webhooks re-grant access you just revoked

**The failure.** Stripe does not guarantee delivery order. Under load, or across
retries, you can receive `customer.subscription.deleted` and *then* an older
`customer.subscription.updated` that still says `active`. A handler that blindly
applies whatever the latest webhook says will happily re-grant access to a
subscription you already correctly revoked — a cancelled member flickers back to
life because an event arrived late.

**Why it bites in production.** Events arrive in order every single time you test
locally, because you fire them in order. Reordering is a property of a retrying,
distributed delivery system under real traffic; it shows up as a member who
"came back" with no payment behind it, which nobody thinks to look for.

**The fix.** Don't trust the event's *payload* as current state. Two robust
options: refetch the subscription from Stripe's API by ID when an event arrives
and apply *that* (the API always returns the true current state), or record each
subscription's freshest `updated`/`created` timestamp and **ignore any event
older than what you've already applied**. Either way you make writes
order-independent, so a late event can't overwrite a newer truth. The webhook
becomes a *nudge to go look*, not the state itself.

---

## 7. Membership is keyed off the email, not a stable Stripe ID

**The failure.** You store members by email and match webhooks by
`customer_email`. Then reality: a customer pays with one email and signed up with
another; someone changes their email in your app but not in Stripe; two people
share a checkout. Now the grant lands on the wrong account, or on no account, and
a paying customer can't get in while a stranger's row got upgraded. Email feels
like an identity and isn't one.

**Why it bites in production.** Your fixtures use one tidy email everywhere, so
the identifier is never ambiguous in a test. In production, emails are mutable,
duplicated, mistyped, and occasionally shared, and each mismatch is a customer
who paid and can't get what they paid for — the worst possible support ticket.

**The fix.** Key membership off the **stable Stripe identifiers** — the
`customer` (`cus_…`) and `subscription` (`sub_…`) IDs — and store the Stripe
customer ID on your user record the first time you see them. Match every
subsequent webhook by that ID, not by email. Treat email as a display and
contact field that can change freely without ever moving an entitlement. When you
must reconcile a brand-new checkout to an existing user, do it once, deliberately,
at signup — not implicitly on every event.

---

## The pattern under all seven

Every one of these is the same mistake in a different costume: **treating a
webhook as the truth instead of a notification about the truth.** The truth about
who's allowed in lives in Stripe's subscription objects; webhooks are an
at-least-once, unordered, occasionally-dropped stream of *hints* that it changed.
The moment you grant straight off an unverified hint, or act twice on a retried
hint, or revoke on a single hint that might never come, or trust a stale hint's
payload over current state, you've built your access control on the one thing in
the system that was never promised to be reliable. The fix underneath all of
them is the same shape: **verify the hint, make handling it idempotent, store the
facts it carries, and derive access from those facts with a reconcile behind
you** — so no single webhook is load-bearing and time can pass without your
membership drifting from reality.

That's the whole article, and it's free. The cheapest place to start today: fire
the same `checkout.session.completed` event at your endpoint twice and confirm
you granted membership exactly once. That one adversarial test takes ten minutes
and catches the double-grant that costs you the most.

---

### If you'd rather not wire and test all of this yourself

I build and sell small, honest, stdlib-first starters and test kits for exactly
this loop — no vendor lock-in, no framework to learn, and each ships a
correct/broken reference so you can watch the check catch a real bug. Entirely
optional; the article stands on its own.

If more than one of these hit home, the bundle is the better value:

- **Ship-It Bundle** — the Membership-Site Boilerplate Kit plus the
  Agent-Workflow Template Pack in one purchase: the tested product layer and the
  process that built it. ▸ `<PRODUCT_URL>`

Or pick the single piece that matches the failure you recognized:

- **Membership-Site Boilerplate Kit** — the checkout → membership →
  gated-access loop pre-wired in stdlib-only Python: a signature-verifying
  webhook handler that **fails closed** on a missing secret (§1), idempotent
  grants (§2), and a deny-when-unpaid gate, running in a loud MOCK-MODE with
  **zero accounts** so you can watch the whole loop before connecting Stripe.
  Honest scope: the live-Stripe path is pre-wired but you run the first live
  purchase yourself. ▸ `<PRODUCT_URL>`
- **Stripe Webhook Test Kit** — points at *your* endpoint and fires the
  adversarial webhook cases from above: a forged/missing signature (§1), a
  replayed duplicate `event.id` (§2), and tampered payloads — real-shape signed
  Stripe events, no Stripe account or tunnel required. ▸ `<PRODUCT_URL>`

And the discipline underneath, if you want the *why* rather than the tools:
**The False-Green Test Trap** — how tests written from your memory of Stripe's
payloads (instead of real captured events) stay green while production breaks,
with an offline tool that vendors real payloads instead. Links: `<PRODUCT_URL>`.

No hype, no invented metrics, no "used by N sites" — just the failure modes, and
some optional starters and tools for the operator who'd rather build the gates
than learn each one by getting burned.
