# Quickstart — The False-Green Test Trap

Ten minutes to the point, thirty to apply it to your own handler. Python
3.8+ stdlib only; everything runs offline.

## 1. Read chapter 1 (3 minutes)

`guide/01-the-war-story.md` — thirteen green tests, one silently dropped
sale, and the two-line fix. Everything else in the guide exists because of
this incident.

## 2. Reproduce the worked run (1 minute)

```
python3 vendor_fixture.py examples/checkout_session_completed.sample.json \
        --name checkout_session_completed --out fixtures
```

Read the output: 7 null fields, including `data.object.customer_email` —
the exact field from the war story, surfaced before you write any test.
Open `fixtures/checkout_session_completed.PROVENANCE.md` and look at the
`[[fill]]` slots: that is the homework the tool cannot do for you.

Optional: `python3 -m unittest test_vendor_fixture -v` (8 tests, offline).

## 3. Vendor YOUR provider's payload (10 minutes)

Get a real sample per chapter 3's source hierarchy — provider CLI/webhook
delivery log first, dashboard event log second, documented full samples
third — paste it into a file, and run the tool on it. Use
`--redact-emails` if the sample came from real traffic. Then fill the
provenance stub: source URL, field-name verification against SDK/OpenAPI
source (chapter 4 shows a filled example's anatomy).

## 4. Put the fixture on the real path (15 minutes)

Chapter 5: ephemeral-port HTTP server, fixture read as raw bytes, real
signature scheme, forged + stale rejections, and the insecure-handler
canary. The skeleton is ~15 lines of stdlib.

## 5. Install the checklist

Copy `guide/06-pre-merge-checklist.md` into your PR template. The
one-sentence version: *a green suite proves your code matches your model;
only a vendored payload on the real path proves your model matches the
provider.*
