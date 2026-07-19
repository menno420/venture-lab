# Session — ENG-9: retire the legacy root `claims/` dir (= OPS-1)

> **Status:** `in-progress`

- **📊 Model:** [[fill:model-line]]
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

[[fill:idea]]

## previous-session review

[[fill:prev-review]]

## Work log

- 2026-07-19 — Branch `claude/eng-9-retire-legacy-claims` from `origin/main`
  (`7ba09d6`, #256 HEAD); clean base confirmed. Investigated both claim dirs:
  root `claims/` = README.md only (no live claim files), `control/claims/` =
  README + 7 claim files (canonical). `claims-legacy-location` advisory does
  NOT currently fire (fires only on claim FILES in a legacy dir) but the dir
  is a live footgun. Born-red card committed (first commit [[fill:card-sha]]),
  pushed. PR [[fill:pr]] opened READY. Change begins.
