# Agent-Workflow Template Pack — Marketplace Listing

> Ready-to-publish copy for Gumroad / Lemon Squeezy. One publish click by the
> owner ships it. Nothing here has been published — the publish step is a
> queued ⚑ owner action.

---

**Title:** Agent-Workflow Template Pack — Session Discipline for Coding Agents

**Tagline:** Give your AI coding agent the constitution, hooks, and session
rituals that keep it on the rails — drop-in, no dependencies, extracted from a
real autonomous fleet.

## Description (≈120 words)

Coding agents don't fail because they can't write code — they fail because they
start every session cold, drift off without closing out, and leave no trail a
parallel session can trust. This pack fixes the *workflow*, not the model. You
get a starter **agent constitution** (autonomy rails, a done-when contract, a
quality floor), a set of **advisory Claude Code hooks** that remind the agent to
orient at start and close the ritual at stop, a **session-log card** carrying
the discipline markers, and a **one-page playbook** behind it all. No
framework, no dependencies, no build step — four short files and three tiny
scripts you fill in with your repo's specifics. Install in ten minutes; get a
recoverable, parallel-safe, honest agent workflow.

## Feature bullets

- **Starter agent constitution** — working agreement, act-vs-ask autonomy
  rails, PR conventions, and an explicit *done-when* completion contract, all
  as fill-in-the-blank `<FILL>` slots.
- **Quality-floor rule, built in** — one command that must pass before every
  push, so "done" means verified, not vibes.
- **Advisory Claude Code hooks** — `SessionStart` orientation, `Stop`
  close-ritual nudge, `PostToolUse` quality reminder — that **fail open** and
  never wedge a session.
- **Session-log card** — carries the Status badge, `💡` idea, `⟲` previous-
  session review, `📊` model line, and `date -u` timestamps that keep sessions
  recoverable.
- **One-page discipline playbook** — heartbeat-before-work, claim-before-build,
  the close ritual, timestamps from `date -u`, forward-only git — each rule
  paired with the failure it prevents.
- **Zero dependencies** — plain Markdown + shell; no install, no runtime, no
  lock-in. Works with any stack.
- **Parallel-safe by design** — the claim-before-build and heartbeat rules are
  written for multiple agents (or agents + humans) on one repo.
- **Customizable, not prescriptive** — every repo-specific value is a `<FILL>`;
  the pack ships the *shape*, you supply the specifics.

## Who it's for

Solo devs and small teams running AI coding agents (Claude Code and similar)
who want the agent to orient itself, hold a quality bar, and leave a trail —
instead of re-explaining the workflow every session and cleaning up half-done
work. If you've ever watched an agent go quiet for an hour or declare victory
on an unverified change, this is for you.

## Pricing

**Pay-what-you-want, $19 suggested** (one-time, free updates to the v0.x line).

Yes — you could assemble something like this from free gists and blog posts.
The honest pitch: $19 buys you the *assembled, battle-tested, coherent* version
so you skip the afternoon of stitching it together and the weeks of learning
which rules actually matter. A low anchor against the GitHub free-norm; the
value is the curation and the provenance, not artificial scarcity.

## FAQ

**Q: Isn't this just a bunch of Markdown I could write myself?**
Yes, and that's the point — you *could*, over several sessions of trial and
error. This is the assembled, proven version so you don't have to. The value is
the specific set of rules that survived real retros, not the file format.

**Q: Do the hooks block my agent if something misconfigures?**
No. Every hook is advisory and fails open — it prints a reminder and exits `0`.
A broken hook degrades to silence; it never wedges a tool, an edit, or a stop.

**Q: Does this lock me into a stack or a tool?**
No. It's plain Markdown and shell with `<FILL>` placeholders. The hooks target
Claude Code's hook events, but the constitution, card, and playbook are
tool-agnostic and work with any coding agent.

**Q: What do I actually do after buying?**
Copy four files in, resolve the `<FILL>` slots for your repo, merge the hooks
block into `.claude/settings.json`, and start using the session card. Full
quickstart in the README; ten minutes, no dependencies.

## Why this over free gists

**Extracted from a real autonomous agent fleet's retros, not aspirational.**
Most "AI workflow" templates are someone's untested guess at what an agent
*should* do. These rules are the ones that survived contact with agents
actually running unattended: the heartbeat rule exists because silent sessions
got mistaken for dead ones; claim-before-build exists because two agents built
the same file; the close ritual exists because sessions kept trailing off
`in-progress`. You're buying the distilled version of that learning — the
shape that works — for the price of a lunch.

## Pairs with

The **Membership-Site Boilerplate Kit** — this pack is the *workflow* layer
(how your agent should work); that kit is the *product* layer (a paid
membership site, wired and tested). Buy both to run an agent that builds a
shippable product with discipline. A bundle discount is a natural next step.
