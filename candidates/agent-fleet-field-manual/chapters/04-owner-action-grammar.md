# Chapter 4 — The Owner-Action Grammar: How Agents Handle Money Without Spending It

The single hardest interface in a revenue-producing agent fleet is the one where money changes hands. You want the agents to do the work that leads to revenue — build the product, write the listing, prepare the launch — and you absolutely do not want them to create accounts, spend funds, or publish charges on their own authority. The resolution this lane uses is a small piece of grammar: agents never act on money; they **queue a click-level instruction** for the owner, in a fixed six-field format, with a conservative earnings expectation attached.

## The six fields

Every owner-action is a block with exactly these fields:

- **WHAT** — the action, stated at the level of a single decision. "Publish the field manual at $39 on a digital marketplace."
- **WHERE** — the exact surface. "Gumroad → New product → Digital product, or Lemon Squeezy → Products → New."
- **HOW** — the click-level steps, specific enough that the owner performs them without re-deriving anything: sign in, upload *this* file, paste *this* copy, set *this* price, publish, copy the URL.
- **WHY** — the justification, tied to the candidate and its provenance, with a conservative expectation. "Revenue-lane candidate; conservative expectation 0–2 sales/month absent distribution."
- **UNBLOCKS** — what becomes possible once the owner acts. Usually the next step in a funnel, or a document that needs the live URL.
- **VERIFIED-WHEN** — the observable condition that proves the action succeeded. "The public URL returns HTTP 200 on a purchasable page."

You can see real instances in `docs/launch/membership-kit/owner-actions.md` (the `⚑B` block, publish the $49 kit) and `docs/launch/stripe-webhook-test-kit/publish-owner-action.md` (publish the $29 kit). Both were written by agents; neither was executed by an agent.

## Why the grammar matters

The grammar is not bureaucracy — each field defends against a specific failure.

**WHAT at decision-level** keeps the agent from smuggling several actions into one. An owner-action that says "set up the storefront and publish and post to Reddit" is three decisions wearing one coat; the owner cannot give informed consent to a bundle.

**HOW at click-level** is what makes the action *owner-performable*. The whole point is that the agent has done all the derivation — which file, which price, which copy — so the human's role is reduced to clicks it can verify, not judgment calls it must reconstruct. If the HOW field requires the owner to figure something out, the agent has offloaded work rather than queuing an action.

**WHY with a conservative number** is the honesty valve. The lane's standing rule (traceable to its "expect bad results, never overstate" principle) is that the expectation attached to a money action is deliberately low: for the products here, "0–2 sales/month absent distribution," and "zero distribution = $0." An owner-action that promises a windfall is manipulating consent, not requesting it.

**VERIFIED-WHEN as an observable** closes the loop the way Chapter 2 demanded: the action is not "done" because the agent queued it or the owner clicked, but because a specific observable condition holds — a URL returns 200, a preview shows the file delivered. It is the same "prove it, don't assert it" discipline applied to the money boundary.

## The block is inert until reviewed

An owner-action block sits in the repository in one of a few explicit states. The field manual's own publish block opens `STATUS: NOT-QUEUED` — written, but not yet presented to the owner, because the gate conditions (built, verified) are not all met. The test kit's block was flipped to `QUEUED` only after its real-path suite was green in CI on the built SHA *and* an independent worker re-verified it. The membership kit's block spent time `FROZEN ❄️` — explicitly do-not-present — until its real-Stripe-path fix merged. The state is machine-visible and the transitions are gated. An agent writing the block never advances it to actionable on its own say-so; the coordinator queues it to the owner only after reviewing the evidence.

## No secret values, ever

One hard sub-rule: an owner-action names environment-variable *names*, never values. The test kit's publish block spells this out — "the webhook signing secret is read from an environment variable at test time and never stored in the repo or the bundle." Secrets are the owner's to hold; the agent's job is to say which named slot a secret goes in, never to know or record the secret itself.

## The rule you take away

Give your agents a money interface that is a *request grammar*, not an *action*. Six fields — WHAT, WHERE, HOW, WHY, UNBLOCKS, VERIFIED-WHEN — force the agent to reduce a money decision to a reviewable, click-level, honestly-priced request with an observable success condition, and to leave the irreversible act to a human who can see all six. The agent produces the leverage; the owner keeps the trigger.
