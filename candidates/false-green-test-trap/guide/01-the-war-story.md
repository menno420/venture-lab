# 1 · The war story: thirteen green tests and a dropped sale

A working autonomous-agent revenue lane shipped a $49 membership-site kit
whose headline claim was "Stripe Checkout + webhook, pre-wired." It had a
test suite. The suite was green — **thirteen passing tests** covering the
webhook grant path. And the product's first real purchase would have failed
anyway, silently, with every test still green.

Here is the defect, in full:

- The webhook handler read the buyer's address from
  `event.data.object.customer_email`.
- The tests injected `checkout.session.completed` events **written from
  memory** by the same author — and in the author's memory, of course,
  `customer_email` carried the buyer's email. The tests passed.
- On a **real** live completion, Stripe sends `customer_email: null`; the
  buyer's address arrives in `customer_details.email`. The handler would
  have read `null`, granted nothing, and returned 200 — an order accepted
  and dropped, with no error anywhere.

A second bug hid in the same shadow: the success URL used a
`{CHECKOUT_EMAIL}` placeholder that does not exist (Stripe substitutes
`{CHECKOUT_SESSION_ID}` and nothing else), so even a granted buyer would
have landed on a broken page. No memory-authored test caught that either,
because the same wrong belief wrote both the code and the test.

The lane's own remediation order put the diagnosis in one sentence worth
keeping:

> The 13 green tests inject synthetic events authored from memory, which
> cannot catch a wrong belief about what Stripe actually sends.

The fix was not "write more tests." It was a change of **discipline**: vendor
a real sample payload with written provenance, and exercise the handler over
actual HTTP with that payload. When that suite went in, it asserted the
uncomfortable facts directly — `customer_email` **is** null, the email
**must** come from `customer_details.email` with a legacy fallback — and the
handler was fixed to match reality:

```python
details = obj.get("customer_details") or {}
email = details.get("email") or obj.get("customer_email")
```

That two-line read order is the entire difference between a sale granted and
a sale silently dropped. The rest of this guide turns that incident into a
method you can apply to any webhook or integration — Stripe, GitHub, or
anything else that POSTs JSON at you.

---

*Provenance of this chapter (all claims trace to committed material in the
lane's public repo, `menno420/venture-lab`): the remediation order quoting
the 13-green-tests diagnosis and the D1a/D1b defects — `control/inbox.md`
(ORDER 003) @ `c99caa4`; the fix history and its verification —
`.sessions/2026-07-13-order-003-stripe-path.md` @ `d058c4d` (fix landed in
PR #16, squash `912da3e`, 2026-07-11; re-verified green 2026-07-13); the
corrected read-order code — `candidates/membership-kit/server/app.py`
@ `dfe3332` (lines 404–414). Nothing in this story is invented.*
