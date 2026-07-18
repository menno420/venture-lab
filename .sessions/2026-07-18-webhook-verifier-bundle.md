# Session — Webhook Verifier Bundle $79 (hard-gated bundle → ready-pending component publishes)

> **Status:** `complete`

- **📊 Model:** claude-opus-4-8 family · high effort · bundle build
- **started (date -u):** Sat Jul 18 16:29:20 UTC 2026
- **branch:** `claude/webhook-verifier-bundle-2026-07-18`
- **base:** `main@ae36afb`
- **purpose:** bundle the FOUR webhook test kits (Stripe + GitHub + Slack +
  Shopify, $29 each) into ONE discounted storefront SKU — the **Webhook Verifier
  Bundle** — and land it as ONE PR. Unlike the individual kits this lands
  **HARD-GATED (ready-pending-publish):** a storefront bundle references its
  component products, so it cannot be created (owner-click-ready) until the
  not-yet-published component kits are live. Stripe is already LIVE; the gate is
  on the GitHub (D5) / Slack (D14) / Shopify (D13) publish clicks. Mirrors the
  existing hard-gated **Ship-It Bundle** precedent exactly. The build ENDS at
  the queued owner ⚑ publish sequence (rail 13 / CONSTITUTION §13) — no publish,
  no spend, no accounts performed by the seat.
- **session:** Mirrors the Ship-It Bundle hard-gate precedent exactly (N/A→real
  assembly zip aside): numbered §7 steps carry no ⚑ so the queue derives zero
  D-items, the blocking component-publish checkboxes come first and name the real
  D-numbers (GitHub D5 / Slack D14 / Shopify D13), and the price is the cited $79
  vs $116 with the discount math ($37 / 31.9%). Where this bundle goes *beyond*
  Ship-It: it ships a real byte-reproducible assembly zip (four component zips
  verbatim + docs) with an 8-test assembly/inventory check wired into CI, rather
  than the N/A-artifact stance — the pins are asserted both on disk and inside
  the built zip. Born-red card holds substrate-gate red until this completion flip.

## 💡 Session idea

💡 **A manifest-driven, auto-growing bundle** so kit N+5 (SNS / Twilio / Square /
Square) joins the storefront bundle as a one-line edit, not a re-cut by hand.
Today `package.sh` hard-codes the four component zip paths and `MANIFEST.json`
hand-lists the four pins + prices; the moment a fifth webhook kit ships, three
files drift out of sync silently. The fix is a tiny
**`scripts/derive_bundle_manifest.py`** that globs `candidates/*-webhook-test-kit/`,
reads each kit's price from its vetting §3 and its dist sha256 from disk, and
emits `MANIFEST.json` (components + summed price + the chosen-discount bundle
price) deterministically — with `package.sh` copying exactly the kits the
manifest names. Pair it with a **bundle-coverage assertion in `test_bundle.py`**
that FAILS if a `*-webhook-test-kit/` exists on disk but is absent from the
manifest, or if any component's committed sha drifts from its pin — so "the
bundle silently omits a shipped kit" and "a component was revised without
re-cutting the bundle" both become red CI, not a reviewer-trusted eyeball. This
is distinct from (and complementary to) the shopify card's #227 💡 of extracting
a shared `_webhook-kit-core/`: that dedups the kits' *build* scaffold, this
dedups the *bundle's* assembly + honesty bar — the two compose into "add a kit =
drop a fixtures-and-scheme diff, and both the kit and the bundle re-derive
themselves." Bundle price/discount policy (the one genuine judgement call) stays
an explicit constant the derive script reads, never guessed.

## previous-session review

previous-session review: `.sessions/2026-07-18-night-kiln-audio-spec.md`
(PR #228, slice-6 of ORDER 016 — the Night Kiln trilogy audiobook/narration
EDITION-SPEC) — a clean gate-free recombination edition that did the honest
things right: honest per-book AND per-chapter `wc -w` reconciling exactly to the
three EN masters (15,999 / 15,995 / 23,334) with ~150-wpm runtime + ACX
finished-hours, a grep-verified "no real foreign-language terms to translate,
it's invented English cozy-fantasy" pronunciation note (a null stated out loud,
not skipped), an explicit owner-gated NOT-included section, a `file@sha`
provenance footer, and the correct call to add **no** OWNER-QUEUE row (editions
aren't a publish surface — confirmed against the derive script, same as the
large-print/omnibus siblings). Its 💡 — a `scripts/derive_audio_runtime.py` that
`csplit`s a master and machine-emits the per-chapter runtime table — is the same
"machine-derive the one genuinely per-title number so it can't drift" instinct
this bundle card's 💡 applies to `MANIFEST.json`; both lanes independently
converging on "derive the drift-prone table, don't hand-maintain it" is the
strongest signal that mechanical derivation is the next consolidation slice in
each.

## Work log

- 2026-07-18T16:29Z — Branch `claude/webhook-verifier-bundle-2026-07-18` from
  origin/main (`ae36afb`); collision check clean (no `control/claims/` bundle
  claim, no open PR covering it). Born-red card committed (first commit),
  pushed. Build begins.
- 2026-07-18T16:4xZ — Built `candidates/webhook-verifier-bundle/`: README +
  per-kit summaries, QUICKSTART, MANIFEST.json (4 pins + $29×4=$116 → $79 pricing),
  PROVENANCE (discount math + pins), reproducible `package.sh` (zip-of-zips) and
  `test_bundle.py` (8-test assembly/inventory check). Double-rebuild
  byte-identical: bundle sha256
  `28f61d8a33309310640375581ff7a6d2f1320bc03bdecbbc1c08c83d5aaf26c8` (121,689 B,
  10 entries); 8 assembly tests green; 67 component tests re-verified green.
  Wired the `webhook-verifier-bundle-tests` CI job. Landed the launch dir and the
  §7 vetting packet mirroring the Ship-It hard-gate; regenerated OWNER-QUEUE
  (51/51 clean; +0 decisions, +1 HARD-GATED 7-click sequence naming the GitHub
  blocking row). PR #231 opened READY. Card flipped `complete` (this commit).
