# Session — The Idempotency & Retry Cookbook $19 (new sellable → owner-click-ready)

> **Status:** `complete`

- **📊 Model:** claude-opus-4-8 family · high effort · new-sellable build (guide)
- **started (date -u):** Sat Jul 18 19:38 UTC 2026
- **branch:** `claude/idempotency-retry-cookbook-2026-07-18`
- **base:** `main@f28465e`
- **purpose:** build **The Idempotency & Retry Cookbook ($19)** to owner-click-
  ready and land it as ONE PR — a NEW guide-shaped sellable that TEACHES the
  safe-retry patterns for APIs (idempotency keys, retryable-vs-non-retryable
  classification, exponential backoff + jitter, retry budgets + circuit
  breakers, honoring `Retry-After`, at-least-once vs exactly-once + consumer
  dedup). It COMPLEMENTS, does not duplicate, the Idempotency Key Test Kit and
  the Rate-Limit Test Kit: those TEST an implementation over HTTP; this TEACHES
  the patterns and ships small, runnable, self-tested reference recipes — the
  same relationship the Merge-Wall / Auto-Merge Enabler cookbooks have to their
  kits. Guide-shaped scaffold mirrors the Auto-Merge Enabler Cookbook
  (guide/ chapters + recipes/ + INCLUDED/README/QUICKSTART/PROVENANCE +
  PROVENANCE-FOOTER `file@sha` / spec citations + allow-list byte-reproducible
  `package.sh` + dist zip). Grounded + cited to the IETF *Idempotency-Key HTTP
  Header Field* draft, RFC 9110 (retry semantics + `Retry-After`), RFC 6585
  (429), and public engineering retry guidance (AWS/Google/Stripe), no
  fabricated quotes. The build ENDS at a queued owner ⚑ publish click (rail 13
  / CONSTITUTION §13) — no publish, no spend, no accounts by the seat.
- **session:** Mirrors the Auto-Merge Enabler / Merge-Wall cookbook scaffold
  (guide-shaped, PROVENANCE-FOOTER convention) but is a genuinely different
  product: it teaches the safe-retry PATTERNS rather than shipping workflow
  YAML or an HTTP test kit. Evidence class is a hybrid: the recipes/ dir ships
  runnable stdlib snippets (backoff-with-jitter, an idempotency-store sketch, a
  retry loop) with a real `unittest` self-test that runs from source, from the
  extracted bundle, and in CI (a wired `idempotency-retry-cookbook-tests` job);
  the prose is verified-by-citation (honest-null inventory substitute for the
  zero-runtime chapters). Cross-sells the two companion kits without copying
  their content. Born-red card holds the substrate-gate red until the
  deliberate completion flip.

## 💡 Session idea

💡 **Ship a cross-lane "Safe Retries Bundle" that pairs THIS teaching cookbook
with the two test kits it teaches — the guide lane's first teach+test bundle —
and, above it, an "API Reliability Handbook" mega-guide that binds all the
own-endpoint cookbooks into one anchor.** The catalog now has a clean
teach-vs-test pair on the exact same subject: this cookbook TEACHES safe retries
(idempotency keys, backoff+jitter, budgets, breakers, Retry-After, dedup), and
the Idempotency Key Test Kit ($29) + Rate-Limit Test Kit ($29) TEST a buyer's
endpoint for exactly those properties. That is the strongest cross-sell shape in
the catalog — a buyer who fails a kit's assertion has, in the cookbook, the cited
fix, and a buyer who reads the cookbook wants the kits to prove their own code.
So the obvious higher-AOV move is a **Safe Retries Bundle** (cookbook $19 +
Idempotency kit $29 + Rate-Limit kit $29 → a ~$59 anchor vs $77 singles), the
guide-lane analog of the Webhook Verifier / API Robustness four-packs — but it is
a *teach + test* bundle, not test-only, which is a genuinely new bundle template
(the existing two bundles are all-kits). It composes with the api-robustness-bundle
card's #239 `_api-hardening-core/` idea: once the kits share a core, the bundle's
`package.sh`/MANIFEST is the same zip-of-zips assembly, just spanning a guide + two
kits. Move two, once several cookbooks exist (Merge-Wall, Auto-Merge Enabler,
False-Green, this one, the Field Manual): an **"API Reliability Handbook"**
mega-guide — one storefront SKU that binds the own-endpoint teaching cookbooks at
a deeper anchor (e.g. $49 vs the ~$91 singles), the guide-lane's highest-AOV reach
at near-zero new build cost since the chapters already exist. Both moves turn the
catalog's growing teach/test symmetry into revenue instead of leaving it implicit
in cross-sell footers. The bundle is the higher-confidence first step — it needs
only the three existing SKUs published, and its discount math is the same play the
two live-drafted bundles already prove.

## previous-session review

previous-session review: `.sessions/2026-07-18-api-robustness-bundle.md` (PR #239,
the R7 slice — the API Robustness Bundle $79, a hard-gated four-kit own-endpoint
SKU). A disciplined, honestly-scoped bundle build: it mirrored the Webhook
Verifier hard-gate precedent exactly (numbered §7 steps carry no ⚑ so the queue
derives zero D-items; the blocking component-publish checkboxes come first and
name the real D-numbers), shipped a real byte-reproducible zip-of-zips assembly
with an 8-test inventory check wired into CI rather than an N/A-artifact hand-wave,
and re-verified all 125 component tests green — the right instinct that a bundle's
honesty is that its pins are asserted both on disk and inside the built zip. Its 💡
converged (a third independent time, with the Shopify #227 and bundle #231 cards)
on extracting `_api-hardening-core/` before the eight near-copy kits drift, plus an
"API Reliability Suite" mega-bundle — the strongest signal yet that the scaffold
dedup is the next slice. This cookbook is the guide-lane complement to that R7
bundle: where #239 bundles the kits that TEST the own-endpoint properties, this
teaches the patterns behind them, and this card's 💡 carries the convergence into
the guide lane (a teach+test "Safe Retries Bundle"). One nit for that lane: the
bundle correctly parks HARD-GATED on four unpublished components, so its revenue is
doubly downstream of the same single concentrated channel — the bundle can't earn
until the components publish, and the components can't earn without distribution;
worth stating in the bundle's own kill-clock that the gate is distribution, not
build.

## Work log

- 2026-07-18T19:38Z — Branch `claude/idempotency-retry-cookbook-2026-07-18`
  from origin/main (`f28465e`); collision check clean (no `control/claims/`
  idempotency-retry claim, no `candidates/idempotency-retry-cookbook/`, no open
  PR covering it). Born-red card committed (first commit), pushed. Build begins.
- 2026-07-18T19:5xZ — Built `candidates/idempotency-retry-cookbook/`: 8 guide
  chapters (each with a Sources footer citing RFC 9110 / RFC 6585 / the IETF
  Idempotency-Key + RateLimit drafts / AWS backoff-and-jitter / Google SRE / gRPC
  retry throttling / Nygard Circuit Breaker / Stripe idempotency docs), 4 stdlib
  recipes (`backoff.py`, `idempotency_store.py`, `retry.py`) + a 26-test
  `test_recipes.py` self-test, README/QUICKSTART/INCLUDED/PROVENANCE, allow-list
  `package.sh`, dist zip. Self-test 26/26 green from source AND from the extracted
  bundle; `package.sh` double-rebuild byte-identical (sha256
  `9579f98ae0ffbb5e670e03aa48673ad45d070632ac657aef98dde4bbfc8a8981`, 43,177
  bytes, 16 content files); inventory 16/16 vs INCLUDED.md; 12 markdown files
  valid UTF-8 H1-headed balanced-fenced; secret-shape scan 0 hits; no junk in the
  archive. Wired the `idempotency-retry-cookbook-tests` CI job. Landed the launch
  dir, the §7 vetting packet (backticked filenames in §7 checkboxes), and the
  regenerated OWNER-QUEUE (idempotency-retry-cookbook = new decision D7; every
  alphabetically-later decision +1 — JWT D7→D8 … keyword-map C1 D26→D27; derive
  manual-review none). Reconciled `docs/launch/CATALOG.md` (new row + positioning
  block + every shifted D-number, incl. the API Robustness Bundle gate
  D6+D8+D14+D17 and provenance D1→D27). `bootstrap.py check --strict`: only the
  born-red HOLD red (by design). PR #240 opened READY. Card flipped `complete`
  (this commit).
