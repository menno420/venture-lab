# 3 · Required-checks gating (the thing auto-merge waits for)

Native auto-merge is a *deferred* merge: "merge when the requirements are
met." If there are no requirements, there is nothing to defer to. This
chapter is about making the requirement real, because getting it wrong is
the single most common reason an enabler that looks correct does nothing —
or does something much worse.

## Auto-merge needs something pending to arm into

When you arm auto-merge on a PR, GitHub asks: is this PR already mergeable?
If the base branch has **zero required status checks**, the answer is yes —
the PR reaches `mergeable_state: clean` the moment it opens, because there
is nothing to wait for. There is no pending window to arm into, so one of
two bad things happens:

1. The arm is refused (nothing to defer to), or
2. worse, the arm merges the PR **instantly**, with no gate at all.

This is why the enabler's first guard counts required contexts and refuses
on zero (chapter 2, Guard 1). The guard is not paranoia; it is the
difference between a landing strip and a trapdoor.

## Contexts, not rules

The subtle version of the trap: a `required_status_checks` **rule** can
exist while requiring **zero contexts**. A rule with an empty context list
looks like protection in the settings UI and provides none — an armed PR
still merges with nothing to wait for. That is why the enabler queries the
rulesets API and counts `.parameters.required_status_checks[].context`
entries, not rules:

```
contexts="$(gh api "repos/$GITHUB_REPOSITORY/rules/branches/${{ github.base_ref }}" \
  --jq '[.[] | select(.type == "required_status_checks")
         | .parameters.required_status_checks // [] | .[].context]')"
```

"A required-checks rule exists" and "a check is actually required" are
different facts. Verify the second one.

## The required check must ALWAYS report

Once your gate is a required context you inherit a failure mode nastier
than a red X: **a required context that never reports stays pending
forever, and a pending required context blocks auto-merge indefinitely.**
No error, no red — just a PR that never lands.

The classic way to create this is the intuitive optimization "coordination
commits don't need the heavy suite, add `paths-ignore`." With
`paths-ignore`, the workflow doesn't run for those diffs, so the required
context never reports, so the armed PR waits for a check that will never
come. This repo's gate states the rule in its own header:

> If this check is REQUIRED, prefer an in-job short-circuit … over
> `paths-ignore`: a required context that never reports stays pending and
> blocks auto-merge forever.

The fix is an **in-job short-circuit**: the gate runs on every PR, and its
first step decides whether to run the heavy work — but the job **still
reports green** either way. Cheap when it can be, thorough when it must be,
always reporting. This repo's `substrate-gate` does exactly that with a
"control fast lane": a diff entirely under the coordination namespace
(`control/`) skips the heavy steps but still reports, so heartbeat PRs land
in seconds and code PRs get the full suite — and *both* satisfy the
required context. (Shipped verbatim as `recipes/substrate-gate.yml`;
chapter 4 covers what its heavy lane enforces.)

## Verify from the API, not the settings page

Two days after "the owner made the check required," it is entirely possible
the check still is not — the setting didn't take, the context name is
misspelled, the rule targets the wrong branch. Settings changes made in a
UI are unverified claims until observed. What verification looks like: open
a fresh PR and read its `mergeable_state` from the API. Until you see
`blocked` (or `pending`) with your gate's exact context name in the PR's
check runs, the required check does not exist, whatever the settings page
shows.

## The checklist

1. A branch ruleset on the default branch requires your gate's **exact
   context name** (the `name:` your workflow reports as).
2. "Allow auto-merge" is ON in repo settings (chapter 5 covers where).
3. Verified from the API: a fresh PR shows `blocked`/`pending` with your
   gate listed in its check runs — not just a green settings page.
4. Your gate **always reports** (in-job short-circuit, never
   `paths-ignore`).
5. Your enabler refuses to arm on zero required contexts (Recipe 1 does).

**Sources** (public repo `menno420/venture-lab`):
`.github/workflows/auto-merge-enabler.yml` @ `aa04700` (refuse-to-arm
guard; contexts-not-rules counting via the rulesets API);
`.github/workflows/substrate-gate.yml` @ `aa04700` (the `paths-ignore`
rule in the header; the control fast lane that skips heavy work but still
reports green, so a required context never jams auto-merge).
