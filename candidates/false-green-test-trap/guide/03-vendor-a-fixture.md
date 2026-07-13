# 3 · Vendor a fixture: payloads you didn't write

"Vendoring" a fixture means committing, into your own repo, a sample payload
whose bytes trace to the **provider**, not to your memory. The fixture is
your independent witness: when your mental model and the provider disagree,
the fixture takes the provider's side inside your test suite, where the
disagreement turns a test red instead of dropping a production order.

## Acceptable sources, in order of preference

1. **The provider's tooling, fired at you.** Stripe CLI's
   `stripe trigger checkout.session.completed` (or your provider's
   equivalent) delivers a real event to a local listener; GitHub lets you
   copy the delivered payload from a webhook's "Recent Deliveries" tab.
   This is a real wire payload — the gold source.
2. **Your own dashboard's event log.** Providers show the exact JSON of
   events they sent you. Copy it out (then strip real customer data —
   chapter 7's script flags email-shaped values and can redact them).
3. **The provider's documented samples.** Docs pages with full example
   events are acceptable when they show the complete envelope.
4. **The provider's SDK source or OpenAPI spec — for field-name
   verification.** SDKs are generated from the provider's own API
   definitions; a Go struct's `json:"customer_email"` tag is the wire name,
   verbatim. This source built the fixtures this guide ships from: when the
   lane's agent proxy got HTTP 403 from `docs.stripe.com`, the kit's
   fixtures were verified field-by-field against `stripe-go` struct tags
   and Stripe's published OpenAPI spec instead — and the constraint was
   written down in the fixture's provenance rather than worked around from
   memory.

**Never acceptable:** typing the payload yourself, trimming "irrelevant"
fields, or reconstructing one from a blog post. A hand-trimmed payload is a
memory-authored payload with extra steps — the nulls and envelope fields you
trimmed are precisely where the trap lives.

## What makes it a *vendored* fixture and not just a pasted blob

- **Complete envelope.** Keep `data.object`, `api_version`, `request`, the
  wrapper ids — the whole event as delivered. Your parser runs against all
  of it in production, so it should in tests.
- **The nulls stay.** A real `checkout.session.completed` carries
  `customer_email: null` and a populated `customer_details.email`; a
  correct handler must read `customer_details.email` first and fall back to
  `customer_email` for the legacy/guest case. Your fixture set should cover
  **both** shapes — the lane vendors exactly that pair.
- **No secrets, no real PII.** A sample payload never needs a live API key
  or signing secret. Replace real customer emails with `example.com`
  addresses; keep the *shape*.
- **Written provenance.** Where each fixture came from, when, and which
  field names were verified against which source — the subject of the next
  chapter. A fixture without provenance decays into exactly the kind of
  trusted-but-unverifiable blob the trap feeds on.

## Values vs names: an honest distinction

Field **names and types** are what you verify against provider sources —
they are the contract your parser depends on. **Values** (ids, timestamps,
amounts) may legitimately be illustrative, and your provenance should say
which is which. Tests assert on shape and on the fields your handler reads
— never on a volatile value like `created` or an event id.

---

*Provenance of this chapter: the source hierarchy, the SDK-tag verification
method, the 403-fallback story, and the values-vs-names distinction are the
lane's committed practice in
`candidates/stripe-webhook-test-kit/fixtures/PROVENANCE.md` @ `dfe3332` and
`candidates/membership-kit/server/fixtures/PROVENANCE.md` @ `dfe3332`; the
two-shape fixture pair (null + legacy email) ships in both kits' committed
`fixtures/` directories @ `dfe3332`.*
