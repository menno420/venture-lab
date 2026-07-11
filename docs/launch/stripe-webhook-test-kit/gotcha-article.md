# Your Stripe webhook says customer_email is null — here's why (and the fix)

> **Status:** `reference`

*Draft — free top-of-funnel article. Not published.*

You wired up a Stripe Checkout, added a `checkout.session.completed` webhook, and
pulled the buyer's email out of the event so you could send them their product.
It worked in your head. Then a real order came in and your logs showed:

```
buyer email: None
```

The payment went through. The customer was charged. And your handler has no idea
who to deliver to. Here's what's actually happening.

## The symptom

On a real `checkout.session.completed` event, this is `null`:

```
event.data.object.customer_email   ->   null
```

So the obvious line of code — read `customer_email` off the session — gets nothing,
and the order silently falls on the floor.

## Why it's null

Stripe Checkout does **not** put the buyer's email in the top-level
`customer_email` field on a normal completion. It collects the email during
checkout and puts it in the customer details object instead:

```
event.data.object.customer_details.email   ->   "buyer@example.com"
```

The top-level `customer_email` is only populated when *you* set it yourself when
creating the session (e.g. you pre-filled it from a logged-in user), or on some
older/legacy integrations. So for the common case — a guest buyer typing their
email into Stripe's form — `customer_email` is `null` and the real address is one
level down.

## The fix

Read `customer_details.email` first, and fall back to the top-level
`customer_email` for the pre-filled/legacy case:

```python
def resolve_buyer_email(session_obj):
    details = session_obj.get("customer_details") or {}
    email = details.get("email")
    if email:
        return email
    # Fallback: populated only when you pre-set it, or on legacy integrations.
    return session_obj.get("customer_email")

# in your webhook handler:
obj = event["data"]["object"]
buyer_email = resolve_buyer_email(obj)
if not buyer_email:
    # don't 200-and-forget: log/flag so no paid order is silently lost
    ...
```

That's it. Once you know the field, it's a few lines — but it costs you real
orders until you do.

## One more that bites right after this one

While you're in here: your `success_url`. Stripe only expands one placeholder,
`{CHECKOUT_SESSION_ID}`. People reach for something like:

```
https://yoursite.com/success?email={CHECKOUT_EMAIL}
```

...expecting Stripe to fill in the buyer's email. It doesn't. `{CHECKOUT_EMAIL}`
is not a real placeholder, so Stripe passes it through **literally** — your buyer
lands on a page with a raw `{CHECKOUT_EMAIL}` in the URL. Use
`{CHECKOUT_SESSION_ID}` and resolve the buyer server-side from the session id.

## Test it before it costs you

The reason these bugs survive to production is that they don't show up unless you
test against the *actual shape* Stripe sends — a payload you typed from memory
won't have the null `customer_email`, so your test passes and production doesn't.
There's a small stdlib-only test kit that fires real-shape, correctly-signed
Stripe events at your local webhook endpoint and checks exactly these traps, if
you'd rather not assemble the fixtures yourself.
