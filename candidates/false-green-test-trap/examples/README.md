# Examples — provenance

`checkout_session_completed.sample.json` is a verbatim copy of the
real-shape `checkout.session.completed` fixture vendored by the Stripe
Webhook Test Kit built in the same lane as this guide
(`candidates/stripe-webhook-test-kit/fixtures/checkout_session_completed.json`
in the public `menno420/venture-lab` repo). Its field names and types were
verified against Stripe's `stripe-go` SDK source and published OpenAPI spec
— the full verification record is that kit's `fixtures/PROVENANCE.md`. Its
values (ids, the `example.com` address, amounts, timestamps) are realistic
illustrative examples, not captured from a live account; it contains no real
customer data and no secrets.

It is here so you can reproduce chapter 7's worked run immediately:

```
python3 vendor_fixture.py examples/checkout_session_completed.sample.json \
        --name checkout_session_completed --out fixtures
```

Expected: exit 0, a fixture + provenance stub in `fixtures/`, and
`data.object.customer_email` listed among the 7 null fields — the exact
field from chapter 1's war story.
