# Session — Agent Fleet Field Manual v0.1

> **Status:** `in-progress`

- **📊 Model:** opus-4.8 · high · revenue-lane candidate build
- **session:** author + build v0.1 of the $39 Agent Fleet Field Manual (candidate #4), un-deferred by owner steer 2026-07-11 (event 4df864d6).
- **started (date -u):** Sat Jul 11 17:17:13 UTC 2026 (born-red first commit)

## ⟲ Previous-session review

Previous-session review: ORDER 006 landed the coordinator's dated self-review in `control/status.md` (PR #35 `a658863`); the lane has test-kit v0.1 built + adversarially verified (14/14 real-path HTTP tests green in CI, PR #28 `fc7f39c`), three products launch-ready (membership-kit $49, template-packs $19, test-kit $29), and PR #29 (`74894e5`) ledgered the test-kit's ~2.3× budget overrun (~284k vs 120k cap) in the open. No regressions observed; this build reuses that scar tissue as its source material.

## 💡 Session idea

This candidate (#4) packages the lane's OWN scar tissue as a sellable $39 book: the D1 payment-verification lesson, the 13-green-tests trap, born-red session cards, the six-field owner-action grammar, the merge wall, single-writer control files, kill-rule intake discipline, and honest negative ledgering. Honesty IS the differentiator — every lesson is cited to a real repo artifact (SHA/PR/file), and where evidence is thin the text says so. Un-deferred from its INTAKE's build-deferral by a direct owner steer (2026-07-11, event 4df864d6: "maybe think about creating guides or books to sell").

## Scope

- 11 chapters (00 preface + 01–10) authored from lived repo history; every lesson cited to a repo SHA/PR/file; 2 free chapters (01 the D1 lesson, 02 the 13-green-tests trap).
- `build.py` — stdlib-only markdown→HTML build to a single self-contained `dist/*.html` with auto TOC + FREE badges.
- `package.sh` — deterministic (`touch -t`, sorted `-X`) buyer zip `dist/agent-fleet-field-manual-v0.1.zip`.
- `templates/` — three runnable artifacts (born-red session-card, six-field owner-action block, kill-rule intake skeleton).
- `README.md` + `LISTING.md` (candidate root, mirror membership-kit).
- `docs/launch/agent-fleet-field-manual/` — 2 free chapters exported as articles, one-pager, LISTING, publish OWNER-ACTION (NOT-QUEUED); append product section to `docs/launch/README.md`.

## Work log

- Born-red card committed alone as the first commit on `claude/agent-fleet-field-manual-v0.1`.
- (filled as build proceeds)

## Status / outcome

(close-out written at flip: zip verification, HTML build + TOC resolution, `check --strict --session-log` result, PR#, CI runs, token-budget honesty vs the 90k cap)
