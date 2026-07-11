# Session — Agent Fleet Field Manual v0.1

> **Status:** `complete`

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

- **Born-red card** committed alone as the first commit on `claude/agent-fleet-field-manual-v0.1` (`b692dc5`).
- **Chapters (11):** `candidates/agent-fleet-field-manual/chapters/00-preface.md` … `10-appendix-templates.md`. Two FREE: `01-the-d1-lesson.md`, `02-the-13-green-tests-trap.md`. Every lesson cited to a real repo artifact — citation map: ch01→`docs/NEXT-SESSION.md` (THE D1 LESSON) + ORDER 003 card `.sessions/2026-07-11-order-003-stripe-real-path.md` + test-kit vendored fixtures; ch02→`control/status.md` self-review + PR #22 `6fea90b` + PR #28 `fc7f39c`; ch03→`bootstrap.py` born-red HOLD logic + superbot-games #40; ch04→`docs/launch/membership-kit/owner-actions.md` + `docs/launch/stripe-webhook-test-kit/publish-owner-action.md`; ch05→`docs/PLATFORM-LIMITS.md` (PR #9 twice, PR #15 three terminal denials, substrate-gate-not-required; owner branch-protection statement `a7bc924a` flagged as NOT agent-verified); ch06→`docs/NEXT-SESSION.md` single-writer rules; ch07→`docs/NEXT-SESSION.md` Routines (cadence flagged operational, not universal); ch08→this candidate's `INTAKE.md`; ch09→heartbeat PR #29 `74894e5` (~284k vs 120k, ~2.3×).
- **Templates (3):** `templates/session-card.md`, `owner-action-block.md`, `intake-skeleton.md` — card-like skeletons kept inside code fences so the born-red checker (which strips fenced blocks) is not tripped.
- **Build:** `build.py` — stdlib-only Markdown-subset → single self-contained `dist/agent-fleet-field-manual-v0.1.html`; auto TOC + FREE badges + light/dark CSS, zero external assets. Verified: 11/11 TOC anchors resolve to section ids, 11 back-to-top links resolve to `#top`, 2 free badges, 0 external `http` asset refs.
- **Packaging:** `package.sh` (`set -eu`, runs `build.py` first, `touch -t 200001010000.00`, sorted `-X`) → `dist/agent-fleet-field-manual-v0.1.zip` (21 entries: README, LISTING, chapters/, templates/, dist HTML). Byte-reproducible: two consecutive builds → identical sha256 `7eff9235024619a632020c06f7c47da24667f8134c828715694eaa8755a29176`. Excludes INTAKE.md, build.py, package.sh, nested zip. HTML re-verified from INSIDE the extracted zip (TOC + backlinks resolve).
- **Buyer-facing:** candidate `README.md` + `LISTING.md` (mirror membership-kit). `docs/launch/agent-fleet-field-manual/`: 2 free chapters exported as standalone articles (intro + soft CTA, no external links), `one-pager.md`, `LISTING.md`, `publish-owner-action.md` (`STATUS: NOT-QUEUED`). Appended `## Agent Fleet Field Manual ($39)` section to `docs/launch/README.md` (append-only; existing sections untouched). All `docs/launch/**` files carry a `> **Status:**` badge (required by the launch-doc scan).
- **Honesty:** no fabricated case studies, no invented reads/sales numbers; family-level model names only; env-var NAMES only, no secret values. Where evidence is thin the text says so (ch05 unverified branch-protection; ch07 cadence as operational detail; ch09 this build's own 90k budget strain).

## Status / outcome

**Complete.** v0.1 of the $39 Agent Fleet Field Manual is authored and built.
- **Zip:** `dist/agent-fleet-field-manual-v0.1.zip`, 21 files, byte-reproducible (sha256 `7eff9235…a29176`, identical across two builds); `unzip -l` manifest captured in the PR body.
- **HTML build:** `dist/agent-fleet-field-manual-v0.1.html` (stdlib build), all 11 TOC links + 11 backlinks resolve, verified standalone from the extracted zip; no external assets.
- **Gate:** `python3 bootstrap.py check --strict --session-log .sessions/2026-07-11-agent-fleet-field-manual-v0.1.md` → **exit 0 / green** once this card flips complete (verbatim output pasted in the PR/report). While in-progress it correctly returned the born-red HOLD.
- **PR:** opened READY (not draft) on `claude/agent-fleet-field-manual-v0.1`; CI (substrate-gate) runs on push. Child seat does NOT self-merge and does NOT arm auto-merge — the coordinator lands on green under the owner's genuine-user turn (per `docs/PLATFORM-LIMITS.md`).
- **Publish:** NOT-QUEUED — `docs/launch/agent-fleet-field-manual/publish-owner-action.md` opens `STATUS: NOT-QUEUED`; no external publish, spend, or account action taken.
- **Token-budget honesty (vs 90k cap):** estimate only, not a metered measurement — build-effort (excluding the separate orientation/read pass) is estimated to press against or modestly strain the 90k cap for a v0.1 of this size (11 cited chapters + from-scratch stdlib HTML build + deterministic packaging + 3 templates + full launch doc set). Consistent with Chapter 9's own admission that this build's budget could be strained; if a metered figure lands over 90k it is to be ledgered negative in the open like the test-kit's ~2.3× overrun (PR #29 `74894e5`). Conservative revenue: $39, 0–4 sales/90d ($0–$156), $0 without distribution; same saturated funnel as membership-kit/template-packs — does not diversify channel risk.
