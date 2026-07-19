# Session — ENG-9: retire the legacy root `claims/` dir (= OPS-1)

> **Status:** `complete`

- **📊 Model:** opus-4.8 · medium · mechanical refactor
- **started (date -u):** Sun Jul 19 00:28 UTC 2026
- **branch:** `claude/eng-9-retire-legacy-claims`
- **base:** `main@7ba09d6`
- **purpose:** land ENG-9 (= OPS-1) from the veto-ready menu (#247) /
  overnight menu — **retire the legacy root `claims/` dir so there is ONE
  claim home** (`control/claims/`), not two. The kit unified the
  work-claim convention on `control/claims/` at EAP §6.4; the root `claims/`
  is a pre-unification alias (gba-homebrew's gen-2 §1 home) that still ships
  in venture-lab beside the canonical dir. It carries only a superseded
  `README.md` pointer — no live claim files — but its mere existence is a
  standing footgun: any new session dropping a claim there trips the
  `claims-legacy-location` advisory and, worse, splits "is someone on this?"
  across two dirs (the exact collision the one-file-per-claim ledger exists
  to kill). Retiring it collapses the ambiguity to one home. Fully
  git-reversible.
- **deliverable:** delete the legacy root `claims/` dir (only member:
  `claims/README.md`, a superseded convention pointer — its content is fully
  carried by the richer, canonical `control/claims/README.md`, so nothing is
  lost). Re-point the two LIVE usage references from root `claims/` to
  `control/claims/`: the repo directory-map row in `README.md` and the
  "Claim before build" rule (rule 6) in `docs/conventions.md`. The
  `claims-legacy-location` checker mechanism in `bootstrap.py`
  (`LEGACY_CLAIMS_DIRS`, the fleet-wide compat detector) is left intact — it
  is the fleet's shared legacy-home detector, not a venture-lab usage pointer;
  removing the venture-lab *instance* of the dir is what silences it here.
- **scope (files):** DELETE `claims/README.md` (retires the dir); EDIT
  `README.md` (one directory-map row) + `docs/conventions.md` (rule 6
  pointer). Plus this card + a `control/status.md` heartbeat. No
  `bootstrap.py` code change, no `control/inbox.md` edit, no SKU, no publish
  surface. The seat performs no publish/spend/account action.
- **guardrails:** born-red card holds substrate-gate red until the completion
  flip. SAFETY: this is a delete — verified redundancy BEFORE removing. Root
  `claims/` holds only `README.md` (no `<branch>.md` claim files, no active
  foreign claim for any live branch) — confirmed by `git ls-files claims/`
  and `ls -la claims/`; deleting is safe and touches no other session's
  claim. The canonical `control/claims/` keeps its README + seven existing
  claim files untouched.

## 💡 Session idea

💡 **Add a low-severity `claims-legacy-dir-present` advisory that fires when a
legacy claim dir EXISTS AT ALL — even empty — not only when it holds claim
files.** Today `claims-legacy-location` fires only on `*.md` claim FILES in a
legacy dir (`_work_claim_findings`: `if is_legacy and claim_files:`), so an
*empty* legacy dir is completely silent — which is exactly the state root
`claims/` was in for days (README-only, zero claim files) before this PR: the
footgun sat there un-nudged, and the advisory would only have fired the moment
some session dropped a claim in the wrong home — i.e. after the collision, not
before. That silence is why a retirement like this one had to be done by hand
rather than surfaced by the checker. Recipe: in `claim_scan_dirs`/
`_work_claim_findings`, when a dir is `is_legacy` and simply *present* (regardless
of file count), emit a one-line `claims-legacy-dir-present` advisory ("a
pre-unification claim dir exists at `<rel>/` — retire it or pin it via
`substrate.config.json` `claims_dir`"), strictly below `claims-legacy-location`
in severity and still exit-neutral. It makes the *retirement* the checked state,
not just the *misuse*, so a re-materialized empty `claims/` (an accidental
`mkdir`, a bad merge) can't silently regress this cleanup. Composes cleanly with
the existing `claims_dir` pin as the deliberate-home opt-out.

## previous-session review

previous-session review: this slice is the hygiene bookend to the #249–#256
baton. That run was distribution-and-tooling-first: #249's DISTRIBUTION-PLAYBOOK
templated the funnel-top recipe, #250/#251 (LM-1/LM-2) closed the last two
uncovered lead-magnet clusters, #252/#253 pre-chewed the live-SKU T+7/T+14 call,
#254 refreshed the current-state ledger, #255 drew the pre-EAP wind-down plan,
and #256 turned "which cluster still needs a magnet" into a standing checker.
Every one of those added or wired a NEW surface; ENG-9 instead *removes* one — it
collapses the two-claim-home ambiguity the fleet already decided against at EAP
§6.4 but never cleaned up in venture-lab. Worth flagging forward before the
2026-07-21 read-only cutover (#255): this was safe precisely because root
`claims/` was already empty of live claims — the same delete on a dir holding an
active foreign claim would NOT be a solo call, and the checker gives no
before-the-fact signal that a legacy dir even exists while empty (the 💡 above is
that gap). Confirmed the #256 checker still reads clean post-delete: nothing in
this diff touches the launch docs it scans.

## Work log

- 2026-07-19 — Branch `claude/eng-9-retire-legacy-claims` from `origin/main`
  (`7ba09d6`, #256 HEAD); clean base confirmed. Investigated both claim dirs:
  root `claims/` = README.md only (no live claim files), `control/claims/` =
  README + 7 claim files (canonical). `claims-legacy-location` advisory does
  NOT currently fire (fires only on claim FILES in a legacy dir) but the dir
  is a live footgun. Born-red card committed (first commit `414dcde`),
  pushed. PR #257 opened READY. Change begins.
- 2026-07-19 — Change: `git rm claims/README.md` (retires the dir — it was the
  dir's only member) + re-pointed the two live usage references at
  `control/claims/` (`README.md` directory-map row; `docs/conventions.md`
  rule 6). Left `bootstrap.py` `LEGACY_CLAIMS_DIRS` intact (fleet-wide legacy
  detector, not a venture-lab pointer). Committed (`191b3e8`), pushed.
- 2026-07-19 — Heartbeat: neutral in-flight pointer for PR #257 added to
  `control/status.md` (`updated:` bumped; other sections + `control/inbox.md`
  untouched). Committed (`d5c8842`), pushed.
- 2026-07-19 — `python3 bootstrap.py check --strict` pre-flip = the born-red
  HOLD only (in-progress Status + 5 unresolved `[[fill:]]` slots); the
  `claims-legacy-location` advisory is GONE (grep found no match — the retired
  dir is no longer scanned), and all non-hold checks pass (remaining advisories
  are pre-existing model-line/seat-digest, non-gating). Re-ran post-flip = EXIT
  0.
- 2026-07-19 — Flip to `complete` (this commit): Status badge, 📊 Model line
  (family-level `opus-4.8`), one 💡 idea (empty-legacy-dir advisory gap), a
  previous-session review acknowledging the #249–#256 baton, all 5 `[[fill:]]`
  slots resolved, guard-fire ledger delta committed. Born-red HOLD clears; this
  last commit releases auto-merge.
