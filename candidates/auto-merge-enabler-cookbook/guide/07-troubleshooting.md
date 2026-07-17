# 7 · Troubleshooting: why a green PR didn't auto-merge

Everything is installed, the settings are on, the gate is required — and a
green PR is still sitting there. This chapter is the diagnostic flow, worst
offender first. Every item here is a wall this repo actually hit and wrote
down.

## 1. The PR was created by an API/MCP client and fired no workflow at open

**Symptom:** an agent opened the PR through the GitHub API (or an MCP
`create_pull_request` tool), the PR is green, but the enabler never ran, so
auto-merge was never armed.

**Cause:** GitHub does not run `pull_request`-triggered workflows for PRs
created by some tokens/integrations the same way it does for a normal push
— an API-created PR can open with **zero triggered workflow runs**. The
enabler's `on: pull_request` never fired, so nothing armed.

**Fix:** push one more commit to the PR head (even an empty
`git commit --allow-empty` or a whitespace touch). That push fires the
`synchronize` event, which the enabler listens for (chapter 2) — and
because arming is idempotent, that single push arms the already-green PR.
This is why the enabler includes `synchronize` in its trigger list at all:
it is the recovery path for "opened but never armed." The cultural version
of the fix: have your agent push its branch **first**, then open the PR, so
the head already exists and a subsequent event has something to arm.

## 2. The required check never reported (pending forever)

**Symptom:** no red X, no error — the PR just never becomes mergeable.

**Cause:** a required context that never reports stays pending, and
auto-merge waits on it forever (chapter 3). Almost always a `paths-ignore`
on the required workflow, or a job whose `if:` skipped it without reporting.

**Fix:** make the gate an in-job short-circuit that **always reports green**
(chapter 3), never `paths-ignore`. Check the PR's check-runs from the API:
a required context you *don't* see listed is the culprit.

## 3. Zero required contexts — it armed and merged instantly (or refused)

**Symptom:** the PR merged the second it opened with no gate, or the arm
step logged "Refusing to arm."

**Cause:** the base branch requires zero status contexts (chapter 3's
trap). The refuse-to-arm guard caught it (good) — or, if you removed the
guard, an unfinished PR merged instantly (bad).

**Fix:** make your gate a *required* context and confirm from the API
(`mergeable_state: blocked`/`pending` on a fresh PR). Keep the
refuse-to-arm guard.

## 4. GraphQL quota exhausted at fleet scale

**Symptom:** intermittent arm failures under heavy concurrency, clustering
roughly hourly.

**Cause:** `gh pr merge --auto` and draft/ready flips go through GraphQL,
whose secondary-rate/quota limits exhaust at fleet scale (this repo's
platform ledger records the ~hourly pattern). One asymmetric gotcha:
**draft→ready flips are GraphQL-only**, so a fleet that opens drafts and
flips them burns quota on the flip.

**Fix (cultural, not technical):** **open PRs READY, never draft.** The
cheapest fix is to never spend quota on a ready-flip you didn't need. When
the native arm is genuinely quota-walled, a REST `GITHUB_TOKEN`
merge-on-green workflow (fired on `workflow_run: completed` of your gate) is
the fallback landing path — the merge is REST, not GraphQL. This cookbook
does not ship that fallback as a production-run recipe (this repo lands via
the native arm); treat it as documented doctrine and trial it on a scratch
repo. The companion **Agent Merge-Wall Cookbook** ships a parse-verified
REST merge-on-green recipe if you need one.

## 5. It merged — but no CI ran on `main` afterward

**Symptom:** the squash landed on `main`, but your `on: push` workflows
never ran for it.

**Cause:** the enabler merges with `GITHUB_TOKEN` (as
`github-actions[bot]`), and **GitHub suppresses `on: push` workflows for
events created by that token** — a recursion guard. So a squash the enabler
performed produces *zero* push-triggered CI on `main`. This is not a bug in
your gate; it is by design.

**Fix:** verify `main` on a **schedule**, not on push. This repo runs a
`main-verify.yml` on a cron (`17 */6 * * *`) that re-runs the same test
suite against `main` HEAD regardless of how the merge was performed —
because scheduled workflows always run on the default branch. If you rely
on post-merge automation, either add a scheduled verifier or use a
PAT/App token for the merge so downstream `on: push` workflows fire.

## 6. The PR was opted out (working as intended)

**Symptom:** a specific PR never arms, everything else does.

**Cause:** it carries `do-not-automerge` (chapter 5), or it's on a branch
outside your agent namespace. This is the feature, not a fault. Check the
PR's labels and head-ref prefix before debugging further.

**Sources** (public repo `menno420/venture-lab`):
`.github/workflows/auto-merge-enabler.yml` @ `aa04700` (`synchronize`
re-arm trigger; refuse-to-arm guard; `GITHUB_TOKEN`/PAT token choice);
`.github/workflows/main-verify.yml` @ `f8ccc60` (the scheduled post-merge
verifier + its header note that `github-actions[bot]` squashes suppress
`on: push` CI on `main`); `.github/workflows/substrate-gate.yml` @
`aa04700` (always-report / never-`paths-ignore` rule); the READY-never-draft
and GraphQL-quota gotchas are this repo's documented fleet conventions.
