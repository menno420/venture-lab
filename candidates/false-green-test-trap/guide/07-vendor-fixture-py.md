# 7 · The tool: vendor_fixture.py

The bundle ships `vendor_fixture.py` — a single-file, stdlib-only,
**offline** tool that turns a pasted provider sample into a vendored fixture
plus the provenance stub chapter 4 demands. It fetches nothing: you bring
the payload (chapter 3's source hierarchy), it brings the discipline.

## Usage

```
python3 vendor_fixture.py SAMPLE.json [--name NAME] [--out DIR]
                          [--redact-emails] [--force]
```

Paste your provider's sample payload into `SAMPLE.json`, run the script, and
you get in `--out` (default `fixtures/`):

- `<name>.json` — the fixture: validated UTF-8 JSON, object-at-top-level
  enforced, pretty-printed with key order preserved;
- `<name>.PROVENANCE.md` — the stub: fixture sha256 and byte size, **every
  null field enumerated** (assert them — that's the chapter-1 lesson),
  volatile-by-name fields flagged (`created`, `*_at`, `api_version`,
  `livemode`, `idempotency_key`, …: never assert their literal values),
  provider-id-shaped and email-shaped values listed, and `[[fill]]` slots
  for the source URL and the field-name verification table.

## Fail-closed behavior (by design)

- **Secret-looking material refuses the whole run** — `sk_live_`/`sk_test_`
  keys, `whsec_` signing secrets, PEM private keys, bearer tokens, GitHub
  and AWS key shapes. Exit 2, nothing written. A sample payload never needs
  a real secret; re-paste without it.
- **Invalid JSON, non-UTF-8, or a bare array/scalar at top level** — exit 2,
  nothing written. A provider event is an object envelope; anything else
  means the paste went wrong.
- **Existing outputs are never clobbered** without `--force`.

`--redact-emails` rewrites every email-shaped string value to a stable
`redacted-N@example.com` placeholder — use it whenever the sample came from
a real dashboard event, so a customer address never lands in your repo.

## A real run

Executed against the committed real-shape `checkout.session.completed`
fixture from the lane's Stripe Webhook Test Kit as the pasted sample
(output verbatim, 2026-07-13):

```
$ python3 vendor_fixture.py pasted-sample.json --name checkout_session_completed --out fixtures
vendored: fixtures/checkout_session_completed.json (1157 bytes)
sha256:   4f4b3be1638a26ab3fa4b1dfe96fd1468d7a861ade5708d1d6a7acfeacbb2c55
stub:     fixtures/checkout_session_completed.PROVENANCE.md
null fields (7):     request.id, request.idempotency_key, data.object.customer_details.address, data.object.customer_details.business_name, data.object.customer_details.individual_name, data.object.customer_details.phone, data.object.customer_email
volatile fields (6): api_version, created, livemode, request.idempotency_key, data.object.created, data.object.livemode
provider ids (4):    id, data.object.id, data.object.customer, data.object.payment_intent
email-shaped values (1): data.object.customer_details.email  <- real address? re-run with --redact-emails
NEXT: open the PROVENANCE stub and fill every [[fill]] slot — source URL + field-name verification make it a fixture you can trust.
```

Note the first null field worth reading twice: `data.object.customer_email`.
The tool surfaces the exact field that cost the war story its first sale —
before you have written a single test.

The bundle includes that sample payload at
`examples/checkout_session_completed.sample.json` (provenance in
`examples/README.md`) so you can reproduce this run immediately, and
`test_vendor_fixture.py` (8 stdlib unittest cases: happy path, null
enumeration, volatile flags, secret refusal, invalid-JSON refusal,
bare-array refusal, email redaction, no-clobber) so the tool itself is held
to the bar it preaches:

```
python3 -m unittest test_vendor_fixture -v
```

## What the tool does NOT do

It cannot verify where your sample came from, fetch provider docs, check
field names against SDK source, or bless a memory-typed payload. Those are
the `[[fill]]` slots — deliberately manual, because the provenance is the
part only you can supply.

---

*Provenance of this chapter: the script, its test suite, and the sample
payload ship in this bundle; the run above was executed against
`candidates/stripe-webhook-test-kit/fixtures/checkout_session_completed.json`
@ `dfe3332` as input on 2026-07-13, output pasted verbatim.*
