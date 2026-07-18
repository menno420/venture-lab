# Session — DIST-1 distribution playbook (reusable lead-magnet recipe, no spend)

> **Status:** `complete`

- **📊 Model:** opus-4.8 · high · docs-only
- **started (date -u):** Sat Jul 18 23:20 UTC 2026
- **branch:** `claude/dist-1-distribution-playbook`
- **base:** `main@2705da8`
- **purpose:** the binding constraint in this repo is REVENUE/DISTRIBUTION, not
  inventory — 1 LIVE SKU with 0 organic sales + ~18 publish-READY SKUs that are
  built-but-undiscovered (see `docs/launch/CATALOG.md`). Two cluster lead magnets
  now exist — PR #243 (dev/webhook + API-robustness) and PR #246 (agent-ops /
  fleet) — and both were derived the same way by hand: a teaching article → channel
  drafts in `distribution-drafts.md` → a CATALOG funnel-top registration → an owner
  paste-and-post. That recipe is now proven twice but lives only as two worked
  examples; the next cluster's author still has to reverse-engineer it from the
  outputs. This slice distils the repeatable recipe into ONE reusable playbook
  (`docs/launch/DISTRIBUTION-PLAYBOOK.md`) so the next cluster magnet is
  fill-in-the-blank instead of re-derived: a step-by-step template, a copy-paste
  skeleton for a new `docs/launch/<cluster>-lead-magnet.md`, a pre-publish
  checklist, and an OWNER-ACTION handoff that stops at paste-ready (owner-gated
  publishing — the doc never auto-publishes). Docs/markdown-only, reversible; NO
  owner spend/publish/account action.
- **honesty bar (repo rule):** NO fabricated metrics, NO invented testimonials,
  NO "used by X companies," NO fake benchmark numbers — real technical substance,
  soft honest funnel. Matches the tone of the shipped
  `docs/launch/api-robustness-lead-magnet.md` and `agent-ops-lead-magnet.md`.
- **scope (files):** NEW `docs/launch/DISTRIBUTION-PLAYBOOK.md`; EDIT
  `docs/launch/README.md` (add one reachable link so the docs-gate passes). Born-red
  card holds the substrate-gate red until the completion flip.

## 💡 Session idea

💡 **A `docs/launch/DISTRIBUTION-PLAYBOOK.md`-conformance advisory that flags
cluster lead magnets which drift from the playbook's own checklist.** The
playbook now names the recipe (article → drafts → CATALOG funnel-top → owner
paste-and-post) and a pre-publish checklist, but nothing mechanically checks a
*future* `docs/launch/*-lead-magnet.md` against it — the next author can skip the
soft-footer-last rule, forget the CATALOG funnel-top bullet, or leave the article
unreachable and still land green, exactly the drift the playbook was written to
prevent. The fix pairs naturally with the `funnel-cluster-uncovered` deriver
idea logged on the agent-ops card (`.sessions/2026-07-18-agent-ops-lead-magnet.md`):
where that one asks "does every cluster HAVE a magnet?", this asks "does every
magnet FOLLOW the playbook?" — a tiny stdlib `scripts/check_leadmagnet_shape.py`
that, for each `docs/launch/*-lead-magnet.md`, advisory-warns (never
exit-affecting, same class as the claims/kill-clock linters) when it lacks a
`reference` badge in the first 12 lines, has no matching CATALOG funnel-top
bullet, is unreachable from an index, or carries a resolved `<PRODUCT_URL>`
(which would mean a live link committed in-repo — a publish-surface smell). Turns
the playbook's prose checklist into a standing, greppable signal so magnet #4
onward is not just fill-in-the-blank but fill-in-the-blank-and-mechanically-checked.

## previous-session review

previous-session review: `.sessions/2026-07-18-agent-ops-lead-magnet.md` (PR #246
— the agent-ops cluster lead magnet, the second worked example this playbook
distils). This slice picks up the #242–#248 distribution-first baton and does the
one thing that series kept re-doing by hand: #243 and #246 each re-derived the
same article → drafts → CATALOG → owner-post recipe from scratch, so instead of
building a third magnet I lifted the recipe itself into one reusable playbook —
the meta-move that makes the next cluster magnet fill-in-the-blank. Kept scope to
a single docs slice (playbook + one reachable README link) with no new SKU and no
publish surface, matching the tight-diff discipline the #243/#246 cards flagged
forward.

## Work log

- 2026-07-18 — Branch `claude/dist-1-distribution-playbook` from `origin/main`
  (`2705da8`); clean base verified. Born-red card committed (first commit), pushed;
  PR #249 opened READY. Build begins.
- 2026-07-18 — Built the payload: `docs/launch/DISTRIBUTION-PLAYBOOK.md` (recipe
  template + copy-paste `<cluster>-lead-magnet.md` skeleton + pre-publish checklist
  + OWNER-ACTION handoff), linked from `docs/launch/README.md` (Cross-product) for
  reachability. Committed, pushed.
- 2026-07-18 — Heartbeat: neutral in-flight pointer for PR #249 added to
  `control/status.md` (other sections + `control/inbox.md` untouched). Committed,
  pushed.
- 2026-07-18 — Flip to `complete` (this commit): Status badge, 📊 Model line
  (family-level), one 💡 idea, previous-session review, all `[[fill:]]` slots
  resolved. `python3 bootstrap.py check --strict` EXIT 0 (advisories only). Born-red
  HOLD clears — this is the last commit, releasing the landing workflow.
