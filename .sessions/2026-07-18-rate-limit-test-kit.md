# Session — Rate-Limit Test Kit $29 (new sellable → owner-click-ready)

> **Status:** `complete`

- **📊 Model:** claude-opus-4-8 family · high effort · new-sellable build
- **started (date -u):** Sat Jul 18 17:48 UTC 2026
- **branch:** `claude/rate-limit-test-kit-2026-07-18`
- **base:** `main@c728933`
- **purpose:** build the **Rate-Limit Test Kit ($29)** to owner-click-ready and
  land it as ONE PR — a NEW sellable in the API-robustness kit family, a
  DIFFERENT problem class from the webhook signature kits and the idempotency
  kit. Where the webhook kits verify an inbound provider *signature* and the
  idempotency kit verifies a *safe-retry / exactly-once* dedup contract, this
  kit verifies a buyer's OWN endpoint's **throttling correctness**: that
  requests under the limit return 2xx; that at/over the limit within the window
  the endpoint returns **429 Too Many Requests** with a valid, positive,
  sane `Retry-After` (delay-seconds or HTTP-date); that the optional standard
  `RateLimit-Limit`/`RateLimit-Remaining`/`RateLimit-Reset` (or legacy
  `X-RateLimit-*`) headers, when present, are consistent (Remaining decrements,
  hits 0 exactly at the 429 boundary, Reset is in the future); that after the
  advertised `Retry-After`/reset window elapses, requests succeed again; and
  that the advertised delay matches when the service actually resumes. Stdlib-
  only, account-free, runs with a loud DEMO banner against bundled reference
  stubs. Ships: a CORRECT reference stub (a real fixed-window limiter with a
  short configurable window), a deliberately NAIVE/broken stub (off-by-one +
  missing/invalid Retry-After) so the suite can PROVE it catches the bug, an
  `rltk.py` harness (+ `rltk.js` Node parity) a buyer points at their own
  endpoint, an HTTP-layer real-path test suite with a request-counter and a
  short window, real docs-derived fixtures + PROVENANCE (cited to the IETF draft
  "RateLimit header fields for HTTP", RFC 6585 §4, RFC 9110), a byte-reproducible
  buyer bundle, and a §7 owner-gate publish packet. The build ENDS at a queued
  owner ⚑ publish click (rail 13 / CONSTITUTION §13) — no publish, no spend, no
  accounts by the seat.
- **session:** Mirrors the proven idempotency-key-test-kit scaffold (the closest
  template — same correct-stub + naive-stub evidence pattern) but is a genuinely
  DIFFERENT product: rate-limiting / throttling correctness, not dedup or
  signature verification. The value proof is built in — the CORRECT stub passes
  every property while the NAIVE stub is FLAGGED on the limit-boundary /
  Retry-After / RateLimit-header properties, so the kit demonstrably
  distinguishes a correct limiter from a broken one. Honest caveat carried in
  PROVENANCE + the listing: the standard `RateLimit-*` header fields are an
  IETF DRAFT (not yet an RFC), so the kit tests the draft/legacy `X-RateLimit-*`
  model and says so; the 429 + Retry-After semantics are stable RFC 6585 / RFC
  9110. Born-red card holds the substrate-gate red until the deliberate
  completion flip.

## 💡 Session idea

💡 **Ship the "API Robustness Bundle" now that the third leg exists — and extract
`candidates/_api-hardening-core/` before the kits drift five ways.** With this kit
landed, the catalog has three sibling dev-tool kits that share ~70% of their
scaffold by copy: the byte-reproducible allow-list `package.sh`, the
reference-stub + naive-stub HTTP test scaffold, the `is_2xx`/verdict pair, the
`fire`/`post`/`get` HTTP shape, the `/_debug/reset` + counter/state demo pattern,
and the PROVENANCE discipline (a pinned per-fixture sha256 + a cited source per
fact). The webhook kits verify the INBOUND edge (a provider's signature on
requests coming in); the idempotency kit verifies the OUTBOUND SAFE-RETRY edge;
this kit verifies the OUTBOUND THROTTLING edge. Those last two are the two halves
of "make your own API robust," so the obvious higher-AOV move is an **API
Robustness Bundle** (Idempotency $29 + Rate-Limit $29 → a ~$49 anchor, the same
bundle-discount play the Webhook Verifier four-pack makes) — and a client that
retries on 429 with backoff is EXACTLY the client that needs idempotent writes, so
the cross-sell is native. The mechanical enabler (flagged now by three
independent cards — Shopify #227 💡, the bundle #231 💡, and the idempotency #233
💡): extract `candidates/_api-hardening-core/` the kits inherit, plus a
`provenance_lint.py` that FAILS any kit whose fixture lacks a pinned sha256 or a
cited source, so kit N+1 (pagination-cursor? optimistic-concurrency/ETag?
conditional-request `If-Match`/`304`?) is a scheme-and-fixtures diff, not a
re-implementation, and the honesty bar is machine-enforced. This build is the
strongest signal yet that the core is worth extracting: it stretched the template
from stateful dedup to timing-based throttling (real windowed waits, a
Retry-After parser spanning delay-seconds AND HTTP-dates, a two-interpretation
Reset heuristic) without breaking the shared shape — the divergence is starting,
and the core should be pulled before it hardens into three copies of the same
bugs.

## previous-session review

previous-session review: `.sessions/2026-07-18-paper-orange-backmatter.md` (PR
#235, the slice-5 back-matter & sellability package for the flagship novel *The
Paper Orange*) — a disciplined, honestly-scoped additive slice. It did the right
things: it held a hard `NO author's-prose changes` constraint (only new apparatus
files + card/claim/index row in the diff), grounded every derived fact in a full
read of the EN master manuscript rather than an assumed setting (the Hunger Winter
/ Liberation context is the manuscript's own), correctly declined to add a §7
packet or an OWNER-QUEUE row (apparatus is a launch ASSET, not a publish surface —
the ebook publish already rides the title's existing packet gate), and pinned a
manuscript `file@sha` provenance footer on each of the three assets. One
forward-looking note for that lane: the three apparatus files (historical note,
book-club guide, marketing copy) are now a repeatable per-title shape, so the same
"extract-the-common-scaffold" pressure this API-kit family is under (see this
card's 💡) will soon apply to the book lane too — an `apparatus/TEMPLATE.md` + a
provenance-footer lint would keep the next title's back-matter honest by
construction rather than by careful copy, the book-lane analog of the
`_api-hardening-core/` move.

## Work log

- 2026-07-18T17:48Z — Branch `claude/rate-limit-test-kit-2026-07-18` from
  origin/main (`c728933`); collision check clean (no `control/claims/`
  rate-limit claim, no `candidates/rate-limit-test-kit/`, no open PR covering
  it). Born-red card committed (first commit), pushed. Build begins.
- 2026-07-18T17:5xZ — Built the full kit as a NEW problem class (rate-limiting /
  throttling correctness, not signatures or dedup): `rltk.py` + `rltk.js`
  harness (six properties + demo + list), CORRECT `stub_handler.py` (thread-safe
  fixed-window limiter, short configurable window, 429 + Retry-After +
  RateLimit-* + legacy X-RateLimit-*, /_debug/state + /_debug/reset), NAIVE
  `stub_handler_naive.py` (off-by-one + no Retry-After + stuck/stale headers, the
  value proof), 27-test real-path suite, two docs-derived request templates +
  PROVENANCE (RFC 6585 §4 + RFC 9110 §10.2.3 stable; RateLimit-headers IETF
  DRAFT, honest). 27 tests green from source AND from the extracted zip;
  `rltk demo` both languages: correct all-6-pass + naive flagged on 4
  (over-limit, retry-after, headers, retry-after-honored), under-limit +
  window-reset honestly non-distinguishing; `package.sh` double-rebuild
  byte-identical (sha256
  `908dc84be5a3e6a5be6ee72123c80cac137f1b2338018e39c6af51ef767ecd45`, 35,991
  bytes, 13 content files); secret-shape scan 0 hits. Wired the
  `rate-limit-test-kit-tests` CI job. Landed the launch dir, the §7 vetting
  packet (backticked filenames in §7 checkboxes so the derive script emits no
  broken links), and the regenerated OWNER-QUEUE (Rate-Limit = new decision D14
  + a publish sequence; Shopify D14→D15, Slack D15→D16, Template Pack D16→D17;
  derive manual-review none). Reconciled the hand-maintained
  `docs/launch/CATALOG.md` (new row + positioning block + every shifted
  D-number). `bootstrap.py check --strict`: only the born-red HOLD red (by
  design). PR #236 opened READY. Card flipped `complete` (this commit).
