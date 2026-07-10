# Review queue — post-merge review ledger

> **Status:** `living-ledger` — the merge-then-flag half of the self-merge
> grant ([`conventions.md`](conventions.md) rule 3; fleet-manager PR #10
> merge-authority policy). Nothing waits for review: PRs merge on green, and
> anything a reviewer should re-check gets a row here (and/or a Codex
> @-mention on the PR). Review is post-merge; veto = revert. An empty queue
> with all PRs merged is the healthy state.

| PR | What to re-check | Why |
|---|---|---|
| #9 | Buyer zips are clean (no seller `LISTING.md` / runtime `members.json` / build cruft) and match the committed `dist/*.zip`; launch-post copy carries no fabricated metrics; demo transcript reflects a real run. | Green (substrate-gate success) + `mergeable_state: clean`, but **not yet landed** — agent self-merge was walled this session (two verbatim classifier denials in `control/status.md` / `docs/PLATFORM-LIMITS.md`), so #9 is **awaiting the owner merge**; re-check post-merge per the merge-then-flag convention. |
