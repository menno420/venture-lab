# Chapter 1 — The D1 Lesson: Never Claim a Payment Path Works Without Executing It

**FREE CHAPTER**

The first product this lane built was a $49 membership-site boilerplate kit. Its headline feature, printed at the top of the listing, was "Stripe Checkout + webhook, pre-wired." Under that headline sat thirteen passing tests. The kit shipped. The tests were green. And the payment path was broken in two specific, silent, order-losing ways.

This is the lesson the lane calls **D1**, and it is recorded as binding-forever in the succession brief (`docs/NEXT-SESSION.md`, the section titled THE D1 LESSON): *never claim a payment path works without executing it.*

## The two bugs

Both bugs came from the same root cause, so it is worth seeing them concretely.

**Bug one: the buyer email was read from the wrong field.** The webhook handler grabbed the buyer's address from the top-level `customer_email` field of the `checkout.session.completed` event. On the payloads the tests used, that field was populated, so the tests passed. But on a *real* Checkout completion, `customer_email` is `null` — the buyer's address lives in `customer_details.email`. The grant path, run against a live event, would have read `null` and failed to deliver access to a customer who had just paid.

**Bug two: an invalid success-URL placeholder.** The checkout session's `success_url` used a `{CHECKOUT_EMAIL}` placeholder, on the assumption that Stripe would expand it to the buyer's email. Stripe supports exactly one placeholder in that position — `{CHECKOUT_SESSION_ID}`. `{CHECKOUT_EMAIL}` is never expanded; it lands in the buyer's browser as the literal string `{CHECKOUT_EMAIL}`.

Neither bug was exotic. Both are among the most common first-integration mistakes with Stripe Checkout. And both sailed straight through thirteen green tests.

## Why the tests lied

The tests lied because the payloads they tested were **authored from memory**. Someone (an agent, in this case) wrote out what a `checkout.session.completed` event looks like, from recollection of the shape, and fed those hand-written objects to the handler. The hand-written events had `customer_email` populated, because that is the field a human remembers as "the email field." The tests then confirmed that the handler read the field that the same author had populated. That is a closed loop. It proves the handler agrees with its author's memory. It proves nothing about Stripe.

The general form of the trap: **a test built from a synthesized payload validates your assumptions, not the provider's behavior.** If you and your test author share the same wrong mental model of the event shape, the test will confirm the wrong model with a reassuring green tick.

## The fix, and the discipline it became

The repair (recorded as ORDER 003, the "stripe-real-path" fix; see the session card `.sessions/2026-07-11-order-003-stripe-real-path.md`) had three parts:

1. Read the buyer email from `customer_details.email`, with the legacy top-level `customer_email` only as a fallback — and pass the buyer email into the session at creation so the webhook has it deterministically.
2. Replace `{CHECKOUT_EMAIL}` with `{CHECKOUT_SESSION_ID}` in the success URL.
3. Build a **real-path HTTP-layer test**: sign a *vendored* real-shape Stripe payload with the actual `Stripe-Signature` scheme and POST it over real HTTP to the handler on an ephemeral port.

That third part is the discipline. The fixtures are not written from memory — they are vendored, meaning each field name and type was checked against Stripe's own SDK source and carries a `PROVENANCE.md` recording where it came from. The lane later factored this into a standalone product, the Stripe Webhook Test Kit, whose fixtures directory ships `checkout_session_completed.json` (with the null top-level `customer_email` and the real `customer_details.email`) alongside a legacy-email variant (`checkout_session_completed_legacy_email.json`) so both code paths are exercised against real shapes.

## The rule you take away

Test payment code against **vendored real provider payloads at the HTTP layer** — never against payloads you synthesized from memory. Concretely:

- Get your fixtures from the provider's documented samples or SDK source, and record their provenance. Do not type them from recollection.
- Exercise the handler the way the provider actually calls it: over HTTP, with a real signature, at the route the provider will hit — not by calling an internal function with a dict.
- Include a forged-event case. A handler that returns 2xx to a badly-signed event is one where anyone who knows your endpoint URL can post fake orders. If your test suite never forges a signature, it never checks the lock.

A green test that agrees with its own author's memory is the most dangerous artifact in an agent fleet, because it *looks* exactly like verification. The next chapter is about what to do when a green check contradicts something you can see with your own eyes.

---

*This is a free chapter from the Agent Fleet Field Manual ($39). If it saved you one silently-dropped order, the other nine chapters apply the same discipline across the whole operating surface — merge walls, owner-action money protocol, born-red work tracking, and honest negative ledgering. Every lesson is cited to a real repository artifact.*
