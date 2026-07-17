# Session — fresh-start cleanup (docs, go-live owner-steps, next-tasks)

> **Status:** `complete`

- **📊 Model:** Claude Opus · high · docs-only
- **started (date -u):** Fri Jul 17 13:39:44 UTC 2026
- **branch:** `claude/fresh-start-cleanup` (PR TBD)
- **session:** Owner-authorized fresh-start cleanup ahead of the EAP read-only
  cutover (2026-07-21) and the owner recreating projects. The repo is full of
  EAP-era / autonomous-fleet ceremony (archive-and-reboot narratives, dead
  trigger ids, an agent-side auto-merge doctrine that the ~2026-07-15 classifier
  now denies) that would misorient a fresh seat. Goal: leave the repo clean
  enough that a recreated seat boots from the repo alone, and hand the owner an
  accurate, actionable next-task set with the exact go-live click-steps for the
  finished products.
- **scope:** Surgical docs/instruction cleanup + one new curation doc. No
  runtime/product source touched; no workflow files deleted; no publish/spend/
  merge performed. (1) Verified `claims/` + `control/claims/` hold only READMEs
  — no stale claims to prune. (2) Rewrote `docs/current-state.md` to a slim
  current-truth ledger (EAP cutoff 2026-07-21, autonomy wind-down, recreation,
  HEAD/PR #217, dead-routines note, failsafe 403). (3) Removed the
  agent-side auto-merge / "it lands itself" doctrine from `CONSTITUTION.md` and
  `docs/conventions.md` (owner-merges model) and badged the two enabler guides
  historical. (4) Created `docs/NEXT-TASKS.md` curating the 38-proposal overnight
  menu + the exact owner go-live steps (Stripe/Supabase/Discord env NAMES,
  publish clicks) + the open owner items. (5) Deprecation banners on the
  EAP/control scaffolding docs.
- **walls:** no publish, no spend, no account/portal step, no external action; no
  edits to `control/inbox.md` (append-only gate); no merge or auto-merge from
  this seat — the owner merges; no secret VALUES written (env var names only);
  workflow files and `candidates/` product source untouched; family-level model
  names only.
- **verify plan:** `python3 bootstrap.py check --strict` must exit 0 (run locally
  before every push; ran green incl. the docs-reachability gate after badging the
  two orphaned enabler docs historical); confirm no `.sessions/` card deleted and
  `control/inbox.md` untouched (keeps the substrate-gate + inbox append-only gate
  green); open the PR READY (non-draft) and leave it for the owner to merge.
- **done-when:** the cleanup lands on a READY PR, CI green (kit-tests +
  substrate-gate), this card flipped `complete` as the last commit, and the PR
  handed to the owner to merge (this seat does not self-merge).

## Results (as landed)

- **Claims:** `staleClaims` (from the recon digest) was empty; `claims/README.md`
  + `control/claims/README.md` kept. During the session PR #217 merged and left a
  stale claim `control/claims/claude-coordinator-closeout-heartbeat.md` (its PR is
  terminal) — pruned on sight (fix-drift), so a fresh seat sees no phantom claim.
- **Mid-session merge:** PR #217 (coordinator close-out) landed on main after this
  branch was cut; merged `origin/main` in (resolved the `control/status.md`
  conflict by taking #217's close-out heartbeat + re-applying the deprecation
  banner) and refreshed the ledger #216 → #217. Forward-only (merge, no rebase/
  force-push, per conventions rule 5).
- **`docs/current-state.md`** rewritten to a slim "what is true now" ledger:
  platform wind-down block (EAP read-only 2026-07-21, ~2026-07-15 classifier,
  owner-merges, merge≠deploy), main HEAD `16cec26` / PR #217 (merged mid-session),
  the 38-proposal menu pointer, dead-triggers note, the failsafe git-push 403
  owner item, accurate product/revenue state (1 live + 10 publish-READY + 2
  hard-gated), and a "Recently shipped" ledger through #217. Replaces the EAP
  archive/reboot snapshots.
- **Instruction doctrine fixed:** `CONSTITUTION.md` autonomy rail "arm auto-merge
  → it lands itself" → "open READY + green; the owner merges"; `docs/conventions.md`
  §"PR state and merge authority" rewritten to the owner-merges model (rules 2/3/4)
  and rule 8 walking-skeleton "auto-merge lands it" → "owner merges". The two
  enabler guides (`operations/auto-merge-guards.md`, `operations/owner-action-auto-merge.md`)
  badged `historical` (also resolves the reachability orphan created by removing
  the enabler link from conventions).
- **`docs/NEXT-TASKS.md`** created — curated 38-proposal menu (P/PUB/REV/OPS
  tables with effort + owner-gated flags) + §1 exact owner go-live steps (SWTK
  kill-clock; membership-kit `STRIPE_SECRET_KEY`/`STRIPE_WEBHOOK_SECRET`/
  `DISCORD_INVITE_URL`/`STORE_BACKEND`+`SUPABASE_URL`/`SUPABASE_KEY`, with the
  correction that no `DATABASE_URL` exists in-repo; the OWNER-QUEUE publish wave)
  + §2 open owner items (failsafe 403, proofread pass, length-band ratify) +
  §4 relaunch hygiene.
- **Scaffolding banners** (no deletions): `control/README.md` (retires the
  message-bus + neutralizes the "never edit inbox" restriction), `control/outbox.md`,
  `control/status.md` (grammar-safe — status-only + full check both green),
  `docs/ROUTINES.md`, `docs/NEXT-SESSION.md`, `docs/seat-digest.md` left as-is
  (generated render), `docs/eap-closeout-walkthrough-2026-07-14.md`,
  `docs/_merge_verification_2026-07-15.md`.

## ⟲ Previous-session review

previous-session review: `.sessions/2026-07-17-overnight-menu.md` (the PR #216
overnight planning session). It did well: it honestly declared the backlog DRY,
generated a genuinely useful 38-proposal veto menu, and kept the heartbeat
honest. What it left for this session: the menu is excellent raw material but was
not distilled into an owner-actionable form, and the repo's own EAP/merge-doctrine
drift (the classifier-tripping "arm auto-merge" instruction, dead trigger ids in
`NEXT-SESSION.md`, EAP-framed `current-state.md`) was left in place — exactly the
misorientation a recreated seat would hit. System improvement it surfaces: a
`docs/NEXT-TASKS.md` (owner-facing curated digest) should be a standing companion
to the raw ideas menu, and a docs-freshness checker (menu OPS-5) would have caught
the stale `current-state.md`/`NEXT-SESSION.md` stamps automatically.

## 💡 Session idea

💡 **A `historical`/`deprecated` badge should carry a machine-checkable
"superseded-by" pointer.** This cleanup badged ~9 docs historical and hand-wrote
"read current-state.md / NEXT-TASKS.md instead" into each banner. If the badge
grammar accepted an optional `superseded-by:` field (e.g.
`> **Status:** \`historical\` — superseded-by: docs/current-state.md`), the
existing reachability checker could (a) treat a historical doc's target as its
required inbound link and (b) red if the pointer target doesn't exist — turning
"is this deprecation banner pointing somewhere real?" into a checked fact. Cheap:
one regex + one reachability rule; reuses the badge parser already in
`bootstrap.py check`. Deduped against the overnight menu — OPS-5 (docs-freshness)
and OPS-6 (link/orphan checker) are adjacent but check staleness/link-validity,
not deprecation-pointer integrity.
