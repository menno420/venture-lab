# Session — Shopify Webhook Test Kit $29 (new sellable → owner-click-ready)

> **Status:** `complete`

- **📊 Model:** claude-opus-4-8 family · high effort · new-sellable build
- **started (date -u):** Fri Jul 17 23:51:33 UTC 2026
- **branch:** `claude/shopify-webhook-test-kit-2026-07-17` (PR #227)
- **base:** `main@732ae02`
- **purpose:** build the **Shopify Webhook Test Kit ($29)** to owner-click-ready and
  land it as ONE PR — the N+1 analog of the LIVE Stripe Webhook Test Kit and the
  just-shipped Slack Webhook Test Kit. A stdlib-only, account-free verifier for
  Shopify's webhook signing (`X-Shopify-Hmac-Sha256` = base64 of
  `HMAC-SHA256(client_secret, raw_request_body)` — base64, NOT hex, over the raw
  body DIRECTLY with no timestamp basestring, constant-time compare), shipped
  with vendored real-shape fixtures (`orders/create` / `products/update` /
  `app/uninstalled`), a correct example handler, an HTTP-layer real-path test
  suite (true-pass + tamper-fail + wrong-secret-fail + malformed-base64-fail), a
  byte-reproducible buyer bundle, and a §7 owner-gate publish packet. The build
  ENDS at a queued owner ⚑ publish click (rail 13 / CONSTITUTION §13) — no
  publish, no spend, no accounts performed by the seat.
- **session:** Mirrors the proven Stripe/GitHub/Slack kit scaffold exactly (file
  set, evidence bar, packaging, listing/vetting shape) with the Shopify-specific
  differences called out honestly: the digest is base64 (not hex like Slack's
  `v0=`), signed over the raw body with NO timestamp (so there is no
  stale/replay mode and no challenge handshake), and Shopify publishes no fixed
  known-answer HMAC constant (so the `vector` command is an honest kit-internal
  known-answer + cross-language parity proof, not a reproduction of a vendor
  constant). Born-red card holds the substrate-gate red until the deliberate
  completion flip.

## 💡 Session idea

💡 **A "Webhook Verifier Bundle" listing** pairing all four kits (Stripe +
GitHub + Slack + Shopify) as one higher-AOV storefront page — ~$79 vs $116
buying all four — is now the obvious next move: four kits are built, three
queued behind the one LIVE SWTK, and the intakes already name the cross-sell as
first-ten channel 2, so the bundle is a listing-copy + one-zip-of-zips slice,
zero new code. It pairs naturally with the deeper consolidation: the four kits
now share ~80% of their scaffold by copy — the byte-reproducible allow-list
`package.sh`, the `_insecure_handler` HTTP test scaffold, the
`normal_fire_pass`/`rejected_fire_pass` verdict pair, the `build_request`/
`post_request` shape, and the PROVENANCE discipline (pinned per-fixture sha256 +
a docs citation per fact). Extract a tiny `candidates/_webhook-kit-core/` the
kits inherit — plus a `provenance_lint.py` that FAILS a kit whose fixture lacks
a pinned sha256 or a cited source — so kit N+4 (SNS? Twilio? Square?) is a
fixtures-and-scheme diff, not a re-implementation, and the honesty bar is
machine-enforced rather than reviewer-trusted. The Shopify kit already proved
the template stretches to genuinely different schemes (base64 not hex, no
timestamp, no challenge) without breaking the shared shape — exactly the signal
that the core is worth extracting before it drifts four ways.

## previous-session review

previous-session review: `.sessions/2026-07-17-night-kiln-omnibus-spec.md`
(PR #226, slice-4 of ORDER 016 — the EN omnibus/box-set EDITION-SPEC) — a clean
recombination-only edition spec that did the honest things right: an honest
summed `wc -w` from the three per-book counts (15,999 / 15,995 / 23,334 =
55,328), an explicit owner-gated NOT-included section, a `file@sha` provenance
footer, and the correct call to add **no** OWNER-QUEUE row (editions aren't a
publish surface, confirmed against the derive script on the slice-3 audio spec).
Its 💡 — a shared `versions/omnibus/EDITION-SPEC.template.md` generator across
the three gate-free format tiers (large-print / audio / omnibus) — is the exact
same "templatize the proven tier before it drifts" instinct that this Shopify
card's 💡 applies to the four webhook kits; the two cards independently
converging on "extract the shared scaffold now" is the strongest signal that
consolidation is the next high-leverage slice in both lanes.

## Work log

- 2026-07-17T23:51Z — Branch `claude/shopify-webhook-test-kit-2026-07-17` from
  origin/main (732ae02); collision check clean (`control/claims/` has no
  shopify-webhook-test-kit claim, no open PR covering it). Born-red card
  committed (first commit), pushed. Build begins.
- 2026-07-18T00:2xZ — Built the full kit mirroring the Slack scaffold with the
  Shopify-specific scheme (base64 HMAC over raw body, no timestamp/challenge,
  `--malformed` safety check). 17-test real-path suite green from source AND
  from the extracted zip in a clean dir; all fire modes PASS live on both ports;
  `package.sh` double-rebuild byte-identical (sha256
  `8ff06e534187170e3d9622e72f43b7587b7e4f5e63feee4ad3917fd211ee0423`, 29,142
  bytes, 13 content files); secret-shape scan 0 hits. Wired the
  `shopify-webhook-test-kit-tests` CI job. Landed the launch dir, the §7 vetting
  packet, and the regenerated OWNER-QUEUE (derive script, 50/50 clean; +1
  decision D13 + a 5-click Shopify publish sequence). PR #227 opened READY.
  Card flipped `complete` (this commit).
