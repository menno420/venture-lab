# Included — file manifest

Every file in The False-Green Test Trap v0.1 bundle and what it does.

## Top level

| file | what it does |
|---|---|
| `README.md` | What this is, requirements, honesty box |
| `QUICKSTART.md` | Ten-minute path from unzip to applied discipline |
| `INCLUDED.md` | This manifest |
| `vendor_fixture.py` | Offline stdlib tool: pasted sample payload → validated fixture + provenance stub (nulls enumerated, volatile flagged, secrets refused, optional email redaction) |
| `test_vendor_fixture.py` | 8 unittest cases for the tool (offline) |

## guide/ (7 chapters)

| file | what it does |
|---|---|
| `guide/01-the-war-story.md` | The documented incident: 13 green tests, `customer_email: null`, the silent drop |
| `guide/02-why-green-tests-lie.md` | The false-green mechanism and where it bites (nulls, envelopes, shortcuts, placeholders) |
| `guide/03-vendor-a-fixture.md` | Source hierarchy for real payloads; vendored vs pasted-blob; values-vs-names honesty |
| `guide/04-provenance.md` | The PROVENANCE.md pattern, section by section, from two shipped examples |
| `guide/05-http-layer-tests.md` | Real-path testing: ephemeral port, raw bytes, forged/stale, the insecure-handler canary |
| `guide/06-pre-merge-checklist.md` | Copy-paste pre-merge checklist (one page) |
| `guide/07-vendor-fixture-py.md` | Tool docs + a verbatim executed run |

## examples/

| file | what it does |
|---|---|
| `examples/checkout_session_completed.sample.json` | Real-shape SDK-source-verified sample payload for the worked run |
| `examples/README.md` | Provenance of that sample |

**Total: 14 files** (5 top-level + 7 guide chapters + 2 examples, counting
this manifest). Every guide chapter ends with a provenance footer citing
the committed material (file @ commit in `menno420/venture-lab`) it was
assembled from.
