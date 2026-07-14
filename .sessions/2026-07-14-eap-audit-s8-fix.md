# Session — EAP audit §8 attribution fix (follow-up, 2026-07-14)

> **Status:** `complete`

- **📊 Model:** fable-5 · audit follow-up session
- **started (date -u):** Tue Jul 14 09:07:07 UTC 2026
- **branch:** `claude/eap-audit-s8-fix` — READY PR (born-red card holds the substrate gate red until this card flips `complete`)
- **session:** Follow-up correcting the audit's §8 attribution paragraph: the
  coordinator clarified the tasking's PR numbers were trading-strategy PRs,
  and this session verified that against the trading-strategy tree and
  GitHub before touching the doc (all four confirmed: TS #111 `d498018`
  selection-fair gate, #121 `c60183f` reason_class + review index, #109
  `3c628e4` KILL-SIG ratification, #100 `08ddbd4` KILL-SIG implementation).

## ⟲ Previous-session review

previous-session review: `.sessions/2026-07-14-eap-audit.md` (EAP audit,
complete) — the audit landed as promised (458 lines, PR #192) and its §8
correction paragraph did exactly the right thing with the evidence it had:
it refused to claim PR numbers it could not verify in venture-lab. Honest
nit: it stopped at "not independently verified" instead of checking the
sibling trading-strategy repo it already had read access to — which is why
this follow-up session exists.

## 💡 Session idea

💡 Cross-repo PR-number namespacing in fleet taskings: every PR cite in a
directive or tasking that crosses seat boundaries should be repo-qualified
(`trading-strategy#111`, not bare `#111`). The §8 misattribution class this
session corrects exists only because bare numbers collide across repos —
venture-lab's #100/#109/#111/#121 are book PRs while trading-strategy's are
the research-infra PRs the tasking meant. A one-token prefix at authoring
time eliminates the whole verification round-trip. (Deduped: not in
`docs/ideas/` and not in audit §10, which is platform-wishlist, not
fleet-convention.)

## Scope

- Open the claim `control/claims/eap-audit-s8-fix.md` and this born-red card
  as the session's FIRST commit; open the READY PR (repo convention: PR
  ready immediately, the born-red card is what holds it red).
- Deliverable: minimal edit to
  `docs/audits/eap-project-audit-2026-07-14.md` §8 — rewrite the correction
  paragraph to state the verified repo-qualified attributions; §11 checked
  for echoes of the same doubt (none found, left unchanged).
- Close-out: heartbeat line in `control/status.md`, then flip this card's
  Status badge to `complete` as the deliberate LAST step.

## Outcome

Delivered via PR #193: §8 correction paragraph rewritten with the four
verified repo-qualified attributions (TS #111 `d498018`, #121 `c60183f`,
#109 `3c628e4`, #100 `08ddbd4`; verbatim titles in the doc), the
repo-qualifier ambiguity finding retained, §11 checked and left unchanged
(no echo). Heartbeat appended to `control/status.md`; claim
`control/claims/eap-audit-s8-fix.md` released in this flip commit.
