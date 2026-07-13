# 4 · PROVENANCE.md: the file that keeps fixtures honest

A vendored fixture is only as trustworthy as its paper trail. The lane's
convention is a `PROVENANCE.md` committed **next to the fixtures**, and it
has earned its keep twice (both shipped kits carry one). This chapter is
that pattern, generalized.

## The sections that matter

**1. The claim, up front.** One paragraph stating what these fixtures are —
"real-shape: every field NAME and type was verified against the provider's
own SDK source, not written from memory" — and why a hand-simplified
stand-in would defeat the purpose.

**2. Constraints, written down.** If you could not reach the primary source,
say so and name the substitute. The lane's version reads:

> `docs.stripe.com` returns **HTTP 403** through the agent proxy used to
> build this kit, so the authoritative reference is the `stripe-go` SDK
> source (generated from the same OpenAPI spec Stripe publishes) …
> Field names are copied from the Go struct `json:"..."` tags.

That paragraph converts a limitation into evidence: a reader can re-verify
every field against the named source.

**3. A file table.** Each fixture, its event type, and *which gotcha it
exercises*. Fixtures are teaching artifacts; the table is their syllabus.

**4. The real-shape facts your suite depends on.** Spell out the trap each
fixture guards, in prose. For the checkout pair: top-level `customer_email`
is null on a normal completion; the address lives at
`customer_details.email`; the legacy fixture covers the guest-prefill case
where the top-level field IS set. When a future maintainer wonders why a
test asserts a field is null, this section is the answer.

**5. Field-name verification, with URLs.** The load-bearing section: every
field your handler reads, mapped to the SDK struct / OpenAPI schema where
its wire name was checked — verbatim `json:` tags listed, so re-verification
is mechanical.

**6. Verified vs illustrative.** State plainly which parts are verified
(names, types, signature scheme) and which are realistic examples (ids,
addresses, amounts, timestamps) — and that no fixture contains real customer
data or secrets.

**7. The auth scheme, if you test it.** The lane's provenance records the
signature scheme against SDK source too: header format
`t=<unix_ts>,v1=<hex>`, HMAC-SHA256 over `f"{t}." + raw_body` with the
endpoint secret, default tolerance 300 seconds, constant-time compare,
multiple `v1=` entries during rotation. Signature bugs are byte-level bugs;
provenance at byte-level precision is what makes chapter 5's forged/stale
tests meaningful.

## Why a stub generator helps

Nobody writes this file from scratch on a Tuesday under deadline. The
`vendor_fixture.py` script this guide ships (chapter 7) writes the skeleton
for you at vendoring time — fixture sha256, every null field enumerated,
volatile fields flagged, `[[fill]]` slots for the source URL and the
verification table — so the honest path is also the lazy path. The slots it
cannot fill are exactly the ones only you can: where the sample came from,
and which sources you checked the names against.

---

*Provenance of this chapter: every quoted passage and section element is
from the two committed provenance files —
`candidates/stripe-webhook-test-kit/fixtures/PROVENANCE.md` @ `dfe3332`
(the 403 constraint note, file table, real-shape facts, verified `json:`
tags, signature scheme) and
`candidates/membership-kit/server/fixtures/PROVENANCE.md` @ `dfe3332`.*
