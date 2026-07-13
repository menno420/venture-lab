# Session — counts sync: NEXT-SESSION + current-state vs OWNER-QUEUE at HEAD (2026-07-13)

> **Status:** `complete`

- 📊 Model: Claude Fable 5
- **session:** coordinator-specified follow-up to PR #165 — that brief merged
  carrying pre-#164 numbers (PR #164 landed while the slice was in flight and
  the enabler merged #165 before the re-derive could push). This slice syncs
  the prose counts in `docs/NEXT-SESSION.md` AND `docs/current-state.md` to
  the generated OWNER-QUEUE at HEAD `5944109`, every number grep-counted, not
  remembered.
- **applied:** docs/NEXT-SESSION.md (count/derivation fixes) ·
  docs/current-state.md (stale count lines only) ·
  control/claims/2026-07-13-counts-sync.md (deleted at this flip) · this
  card. Nothing else touched.
- **verify:** `python3 bootstrap.py check --strict`
- **started (date -u):** Mon Jul 13 14:38 UTC 2026 (born-red first commit)
- **closed (date -u):** Mon Jul 13 14:42 UTC 2026

## ⟲ Previous-session review

Direct review of PR #165 (NEXT-SESSION rewrite, merged by the enabler as
squash `5944109` — the slice this card fixes). The rewrite itself held up:
every number was genuinely re-derived at its branch base `e252b46`, the
strict check caught two retro docs the rewrite would have orphaned, and the
merge diff was exactly its declared scope. What failed was structural, not
sloppy: PR #164 merged at 14:29Z, the worker pushed at ~14:34Z off
`e252b46`, and the enabler landed #165 green a minute later — an
**enabler-vs-in-flight-rebase race** in which a "derived at HEAD X" doc can
merge when main is already at X+1, with no signal anywhere. The saving
grace worth copying: #165's own drift note ("the generated queue at HEAD
wins over prose counts") pre-limited the damage of exactly the staleness it
went on to suffer.

## 💡 Session idea

**Freshness-check self-declared `derived at HEAD <sha>` stamps at CI time.**
Docs like NEXT-SESSION.md and current-state.md carry a machine-findable
"derived/re-derived at HEAD `<sha>`" literal. A small advisory step (the
`check_ledger_drift.py` nag pattern — warn, never gate) could, on PRs
touching such docs, compare each stamped sha against the PR's live merge
target: "derivation base `e252b46` is 1 commit behind main (`d71649b`) —
re-derive before the enabler lands this." That converts today's silent
#164/#165 race into a visible pre-merge nag. Deduped: my previous card
(2026-07-13-next-session-refresh) proposes a generated COUNTS footer +
prose-count drift grep — that catches *number* drift after regen; this
catches *derivation-stamp* staleness against a moving merge target, the
failure mode the counts-footer idea would NOT have flagged (the counts were
correct for the stamped sha). No other `.sessions/` card proposes stamp
freshness checking.

## Outcome

- `docs/NEXT-SESSION.md`: derivation stamps moved `e252b46`→`5944109`;
  catalog 8→9 publish-READY (+ Multi-Agent Control-Plane Pack $29, PR #164,
  INTAKE-gated, = queue item D7 storefront pick, default Gumroad); queue
  counts 17/30/172 → **18 decisions (D1–D18) / 31 sequences / 177 unchecked
  clicks** (6 sequences hard-gated); the now-satisfied current-state drift
  note replaced with a standing "generated file at HEAD wins" pointer.
- `docs/current-state.md`: the same queue counts fixed (was 19/171 from the
  pre-ORDER-010 era), re-derive citation updated to PR #163 + PR #164, the
  products line 8→9 with MACP appended to the publish-READY list. No other
  section touched.
- All counts grep-derived from `docs/publishing/OWNER-QUEUE.md` at
  `5944109`: decisions `awk '/^## 1\./,/^## 2\./' | grep -c '^### D'` → 18;
  sequences `awk '/^## 2\./,/^## 3\./' | grep -c '^### '` → 31; clicks
  `awk '/^## 2\./,/^## 3\./' | grep -c '^- \[ \]'` → 177;
  `grep -c HARD-GATED` → 6.
- `python3 bootstrap.py check --strict` green at this flip (prior red was
  the designed born-red HOLD only).

## Work log

- 2026-07-13T14:38Z — Branch `claude/counts-sync-2026-07-13` off origin/main
  (`5944109`, PR #165); no sibling claim on these files at HEAD; claim +
  born-red card committed first (e690dcb), pushed; READY PR #166 opened via
  MCP.
- 2026-07-13T14:40Z — Two-file count sync committed (b7ccdb6), numbers
  grep-counted at HEAD.
- 2026-07-13T14:42Z — Card flipped complete, claim deleted same commit;
  strict check green; left to the enabler on green — no auto-merge armed by
  this session.
