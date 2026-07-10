# Launch posts — ready-to-paste channel copy

> **Status:** `reference`

> **How to use (owner):** publish the listings first (owner actions ⚑B and ⚑D in
> `docs/research/venture-ledger.md`), then replace every `{{LISTING_URL}}` and
> `{{BUNDLE_URL}}` below with the real product URLs and paste each post into its
> channel. One channel at a time — space them out, reply to comments yourself.
> Nothing here is scheduled or auto-posted; these are drafts for a human to send.
>
> **Tone rule:** everything below is deliberately non-hype and claims only what
> the repo can back (a tested, mock-runnable kit; a drop-in pack extracted from
> real retros). **No fabricated metrics** — there are no sales, stars, or user
> counts yet, so none are claimed. Delete any line you can't stand behind.

---

## 1. Show HN

**Title:**
`Show HN: A membership-site kit that runs the whole purchase→access flow with zero accounts`

**Body:**

```
I kept re-wiring the same thing for every paid-community / course / gated-tool
idea: Stripe checkout, a webhook that grants access, a gated route, an
invite-on-purchase. So I packaged it once, properly.

The kit ships in "mock mode" — clone it, run `python3 app.py` (stdlib only, no
pip install), and watch a purchase unlock the members area in one command,
before you sign up for Stripe, Supabase, or Discord. The membership-grant logic
is covered by a 13-test unittest suite that needs no network, and members
persist to a JSON file so they survive a restart. When you're ready to charge,
you paste your Stripe test keys and the same code path goes live.

It's an honest v0.x: the grant/deny/idempotency flow and file-backed persistence
are real and tested today; live Stripe E2E, Discord delivery, and a hosted
Supabase backend are wired but env-gated behind keys you supply. I wrote it to
be readable and extended by a human or a coding agent.

Free membership starters exist — this one's bet is "documented, tested, and
provably runnable in one command with zero accounts," which most aren't.

Listing: {{LISTING_URL}}

Happy to answer questions about the design (the store is a pluggable
`MembershipStore` ABC so swapping JSON for Supabase is a config flip).
```

---

## 2. Reddit — r/SaaS

**Title:**
`I packaged the membership purchase→access flow so you don't rewire Stripe webhooks again`

**Body:**

```
Every membership/course/paid-community build starts with the same plumbing:
checkout → webhook → grant access → gate the content → send the invite. I got
tired of rebuilding it, so I made a kit that has it wired and tested.

What's actually done (not vaporware):
- Runs in mock mode with ZERO accounts — one command shows a purchase unlocking
  the members area.
- Membership grant/deny/idempotent-duplicate logic covered by a 13-test suite,
  no network needed.
- Members persist to disk (survive a restart); the store is pluggable, so
  Supabase is a drop-in later.
- Stdlib-only Python backend — no dependency hell.

Honest scope: the payment logic is real and tested; live Stripe (test-mode),
Discord invites, and hosted Supabase are wired but gated behind your own keys.
It's a head start, not a black box.

Not free — it's priced as a weekend-saver. If you'd rather extend a tested
starter than debug a webhook signature at midnight, it's here: {{LISTING_URL}}

Feedback welcome, including "here's a free repo that does X" — I'll tell you
honestly where this differs (mainly: tests + the zero-account demo).
```

> **r/Entrepreneur / indie-dev variant:** same body, swap the first line for
> *"If you sell access to anything — a community, a course, a members-only tool —
> here's the plumbing already built and tested."* Read each subreddit's
> self-promotion rules before posting; several require a flair or a ratio of
> non-promo participation.

---

## 3. Reddit — r/Entrepreneur (companion pack angle)

**Title:**
`Two small dev products: the membership plumbing, and the agent-workflow rules that built it`

**Body:**

```
I've been running coding agents to build small, sellable dev tools. Two shipped:

1. A membership-site kit — the purchase→access flow (Stripe webhook, gated
   content, invite-on-purchase) wired and tested, demoable in one command with
   no accounts. {{LISTING_URL}}

2. An agent-workflow template pack — the constitution, hooks, and session
   rituals that keep a coding agent on the rails, extracted from real retros
   (not an aspirational guess at "how agents should work"). Drop-in, no deps.

They pair: #2 is how the agent should work, #1 is a product it can build. There's
a bundle if you want both: {{BUNDLE_URL}}

I'll answer anything about the agent setup — what the hooks do, why the session
discipline exists, how much of the build was actually autonomous.
```

---

## 4. Claude Code community / X post

**One-liner (X / short-form):**

```
Built a membership-site kit with coding agents: Stripe webhook → grant → gated
content, wired + tested, runs the whole purchase→access loop in ONE command with
zero accounts. Stdlib Python, 13 passing tests, members persist across restarts.
Honest v0.x. {{LISTING_URL}}
```

**Claude-Code-community longer post:**

```
If you run coding agents, two things I shipped might be useful:

• Membership-Site Kit — the purchase→access plumbing (checkout, webhook,
  membership grant, gated route, invite-on-purchase) already wired and covered
  by a 13-test suite. Runs in mock mode with zero accounts, so you (or your
  agent) can watch the full loop before touching Stripe. Clean structure and
  explicit env markers so an agent can extend it without reverse-engineering.
  {{LISTING_URL}}

• Agent-Workflow Template Pack — the constitution + advisory hooks + session-log
  card + one-page playbook that keep an agent oriented and honest: heartbeat
  before work, claim before build, close ritual at stop. Extracted from an
  actual autonomous fleet's retros. Drop-in, fails open, no deps. {{LISTING_URL_PACK}}

Both together (bundle): {{BUNDLE_URL}}

Built largely by agents; happy to share how, including the parts that needed a
human. No hype — it's v0.x and labeled that way.
```

---

## Posting checklist (owner)

- [ ] Listings published (⚑B, ⚑D) and URLs copied.
- [ ] Replaced `{{LISTING_URL}}`, `{{LISTING_URL_PACK}}`, `{{BUNDLE_URL}}`.
- [ ] Read each community's self-promotion rules; don't cross-post all at once.
- [ ] Post from your own account; be present to reply for the first few hours.
- [ ] Removed any line you can't personally stand behind.
