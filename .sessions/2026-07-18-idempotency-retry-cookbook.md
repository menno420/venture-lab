# Session — The Idempotency & Retry Cookbook $19 (new sellable → owner-click-ready)

> **Status:** `in-progress`

- **📊 Model:** [[fill:model]]
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

[[fill:idea]]

## previous-session review

[[fill:prev-review]]

## Work log

- 2026-07-18T19:38Z — Branch `claude/idempotency-retry-cookbook-2026-07-18`
  from origin/main (`f28465e`); collision check clean (no `control/claims/`
  idempotency-retry claim, no `candidates/idempotency-retry-cookbook/`, no open
  PR covering it). Born-red card committed (first commit), pushed. Build begins.
