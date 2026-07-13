# 2 · Why auto-merge won't arm (the zero-required-checks trap)

The obvious fix for chapter 1 is GitHub-native auto-merge: arm it while
checks are pending, let GitHub perform the merge when they go green. The
merging identity is then GitHub itself, not your agent. This works — it is
the primary landing path in this cookbook — but most repos discover it
does not arm, and the reason is almost always the same.

## Auto-merge needs something to wait for

Native auto-merge is a *deferred* merge: "merge when the requirements are
met." If the branch has **zero required status checks**, a PR reaches
`mergeable_state: clean` the moment it opens. There is nothing pending, so
there is no waiting state to arm into — the arm either gets refused or,
worse, merges the PR instantly with no gate at all.

The source repo hit exactly this. Its ledger records the diagnosis on the
fleet's PR #9, after the wall from chapter 1:

> auto-merge **cannot arm** because PRs reach `clean` immediately with
> **0 branch-protection required checks** (`substrate-gate` is not a
> required context → no checks-pending window to arm into) … Result: a
> green, `clean` PR is **agent-unlandable** and sits one owner click from
> landing.

And the fix, recorded in the same entry:

> Fix = make `substrate-gate` a required check (auto-merge can then arm)
> **or** add a `GITHUB_TOKEN` merge-on-green workflow.

Those two branches are exactly this cookbook's Recipe 1 and Recipe 2.

## Verify the fix actually took (rulesets lie to the unobservant)

Two days after "the owner made the check required," the ledger records the
wall *still up* — the arm denial still cited "substrate-gate not required."
Settings changes made in a UI are unverified claims until observed from
the API. The repo's later entry shows what verification looks like: a PR
showing `mergeable_state: blocked` with named check runs actually gating.
Until you see `blocked`-while-pending with your own gate's context name,
the required check does not exist, whatever the settings page says.

The production enabler (Recipe 1) encodes this lesson as a guard rather
than a hope. Before arming, it counts required check **contexts** — not
rules — via the rulesets API:

```
contexts="$(gh api "repos/$GITHUB_REPOSITORY/rules/branches/${{ github.base_ref }}" \
  --jq '[.[] | select(.type == "required_status_checks")
         | .parameters.required_status_checks // [] | .[].context]')"
```

and refuses to arm on zero, because a `required_status_checks` rule with
an **empty context list** still lets an armed PR merge with nothing to
wait for. That distinction — rule present vs. contexts non-empty — is the
kind of edge you only learn by having merged something instantly.

## The checklist

1. Branch ruleset on the default branch requires your gate check's exact
   context name (the job name your workflow reports).
2. "Allow auto-merge" is ON in repo settings.
3. Verified from the API: a fresh PR shows `blocked` while the gate runs,
   with the gate listed in its check runs.
4. Your enabler refuses to arm on zero required contexts (Recipe 1 does).

**Sources** (public repo `menno420/venture-lab`):
`docs/PLATFORM-LIMITS.md` @ `2044dc6` (PR #9 no-pending-window diagnosis +
fix; 2026-07-11 "still not required" re-verification; PR #55
`mergeable_state: blocked` verification); `.github/workflows/auto-merge-enabler.yml`
@ `305646f` (refuse-to-arm guard, contexts-not-rules counting).
