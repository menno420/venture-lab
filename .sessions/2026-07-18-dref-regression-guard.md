# Session — check_catalog_drefs.py guard + test: machine-catch OWNER-QUEUE renumber mispointing (the #245 class)

> **Status:** `complete`

- **📊 Model:** opus-4.8 · high · feature build
- **started (date -u):** Sat Jul 18 23:07 UTC 2026
- **branch:** `claude/dref-regression-guard`
- **base:** `main@cde8f6d`
- **purpose:** tonight PR #244 folded the CORS Preflight Test Kit into
  `docs/publishing/OWNER-QUEUE.md` as a new **D4**, renumbering every
  alphabetically-later decision +1 (D4→D5 … D27→D28). That silently MISPOINTED
  the D-ref cross-references in the sellable-bundle + catalog docs (owner would
  land on the wrong queue row); PR #245 hand-resynced them. The green checker
  (`bootstrap.py check --strict`) did NOT catch it — a D-ref is a SEMANTIC
  cross-reference, not a syntax error — so the regression shipped green. This
  slice adds a GUARD so the class is caught automatically the next time
  OWNER-QUEUE renumbers. (Directly builds the 💡 logged on the #245
  bundle-dref-resync card and the #244 owner-queue-cors-fold card.)
- **deliverable:** `scripts/check_catalog_drefs.py` — builds the live
  decision-ID → SKU map from OWNER-QUEUE.md §1 `### D<n> — <SKU>` headers (the
  source of truth), then scans an ALLOWLIST of live-cross-ref files and asserts
  each `D<n>` (a) resolves to an EXISTING decision and (b) points at the SKU the
  surrounding context names. Exit non-zero with a per-ref message on any
  dangling / mispointed ref, exit 0 clean. Stdlib-only.
  `scripts/test_check_catalog_drefs.py` — pass-case on the current clean tree +
  catch-case on a temp fixture with a deliberately-wrong D-ref (proves the guard
  fires, not just that it is green) + dangling-case + historical-exclusion case.
  Wired into `.github/workflows/kit-tests.yml`.
- **scope + exclusions (allowlist-based, not deny-all):** the allowlist = the
  files carrying LIVE cross-refs — `docs/launch/CATALOG.md`, the two bundle
  families (`docs/launch/{api-robustness,webhook-verifier}-bundle/*.md`,
  `docs/publishing/vetting/{api-robustness,webhook-verifier}-bundle.md`,
  `candidates/{api-robustness,webhook-verifier}-bundle/*.{md,json}`). Frozen
  point-in-time snapshots are HISTORY and deliberately NOT in the allowlist
  (`.sessions/*`, `control/inbox.md`/`outbox.md`, `docs/NEXT-TASKS.md`,
  `docs/NEXT-SESSION.md`, `docs/current-state.md`'s "N decisions D1-Dn" line);
  plus in-file renumber-arrow (`D4→D5`) and decision-range (`D1–D28`) lines are
  skipped as migration/summary prose, not per-SKU cross-refs.
- **guardrails:** no packet/queue edited (OWNER-QUEUE is the authority — read
  only). Diff is scripts/ + test + the one kit-tests CI job + claim + this card +
  a control/status.md heartbeat only. No publish/spend/account action. Born-red
  card holds substrate-gate red until the completion flip.

## 💡 Session idea

💡 **Give the D→SKU map a PACKET-SLUG identity (from OWNER-QUEUE §1's WHERE
line) so the bundle-family checks tighten from keyword-consistency to EXACT
slug match — and the gate-list refs become checkable too.** Every §1 decision
carries a `- **WHERE:** \`docs/publishing/vetting/<slug>.md\`` line whose slug
is a 1:1 decision identity (`github-webhook-test-kit` ⇒ D6). The current guard
resolves a ref's intended SKU by KEYWORDS derived from the title, which is
deliberately inclusive (never false-positives) but goes existence-only on two
carriers: (a) the bundle MANIFEST.json `"kit": "<slug>"` objects and packet
tokens `` `jwt-auth-test-kit.md` `` (checked only via keyword bleed today), and
(b) bare gate lists like `**HARD-GATED** on D11 + D21` where no kit is named on
the line. Parsing the WHERE slug into a `slug → id` map lets the checker (1)
verify MANIFEST/packet-token refs by exact slug identity — a sharper signal than
keyword overlap, catching an intra-family swap the keyword path misses — and (2)
resolve a bundle's gate-list refs against the component slugs the bundle's own
MANIFEST declares, turning those existence-only refs into full SKU checks.
Guard recipe: extend `build_decision_map()` in `scripts/check_catalog_drefs.py`
to also capture the WHERE slug (regex `WHERE:.*vetting/([a-z0-9-]+)\.md`), add a
`slug_to_id` dict, and in `context_for_ref`/`decisions_named_in` prefer an exact
slug hit over the keyword set; test target a fixture MANIFEST whose `kit` slug
and `D<n>` disagree, asserting the mispoint fires via slug identity (the keyword
path would pass it). Composes with this guard into one D-ref-integrity family
(the #245 card's `check_bundle_drefs` 💡, now folded into this one checker).

## previous-session review

previous-session review: `.sessions/2026-07-18-bundle-dref-resync.md` (PR #245
— the direct predecessor). #245 hand-resynced the mispointed bundle D-refs after
#244's CORS renumber and logged the exact 💡 this slice makes concrete
(`check_catalog_drefs.py` / `check_bundle_drefs.py`); its recorded map
(D6=GitHub … D18=Rate-Limit) was the spec I built the OWNER-QUEUE §1 parser
against, and re-deriving it from the live headers reproduced it byte-for-byte —
so the tree is genuinely resynced, not just claimed to be (163/163 refs
resolve). The one thing I'd flag forward: #245 scoped the proposed checker as an
ADVISORY (never exit-affecting, "same class as `lint_owner_gates.py`"); I made
it a REQUIRED `catalog-dref-guard` gate instead — a renumber-mispoint SHOULD red
CI rather than merely nag, and the catch-case + dangling-case tests prove the
guard fires before it can ever gate a real PR, so a hard gate is safe here (a
false-positive would have to survive the clean-tree pass-case that runs in the
same job).

## Work log

- 2026-07-18 — Branch `claude/dref-regression-guard` from `origin/main`
  (`cde8f6d`); collision check clean (no `control/claims/` entry for a D-ref
  guard; the #245 card only PROPOSED it as a 💡, never built it). Claim +
  born-red card committed (first commit), pushed. Build begins.
- 2026-07-18 — Built the guard: `scripts/check_catalog_drefs.py` (stdlib-only;
  OWNER-QUEUE §1 header parse → D→SKU map; allowlist-scoped scan; per-carrier
  context — JSON object / table row / prose logical block incl. blockquote-wrap
  continuation; renumber-arrow + range-line exclusion) +
  `scripts/test_check_catalog_drefs.py` (pass-case on the live tree, mispoint
  catch-case, dangling case, historical-exclusion case) + a required
  `catalog-dref-guard` job in `.github/workflows/kit-tests.yml`. Checker on the
  clean tree: EXIT 0, all 163 cross-ref D-refs resolve (0 dangling, 0
  mispointed) — no real mispoint found (the #245 fix holds). `git diff --stat
  origin/main` verified to carry ONLY scripts/ + test + the one CI job + claim +
  card. Committed, pushed.
- 2026-07-18 — Heartbeat: neutral in-flight pointer for PR #248 added to
  `control/status.md` (other sections + `control/inbox.md` untouched). Committed,
  pushed. CI `catalog-dref-guard` job green (checker step + unittest step both
  success, run 29664776267).
- 2026-07-18 — Flip to `complete` (this commit): Status badge, 📊 Model line
  (family-level), one 💡 idea, previous-session review, all `[[fill:]]` slots
  resolved. `python3 bootstrap.py check --strict` EXIT 0 (advisories only). Born-red
  HOLD clears.
