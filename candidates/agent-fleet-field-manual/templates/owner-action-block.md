# Template — Six-Field Owner-Action Block

An owner-action is how an agent requests a money/publish/account action
without performing it. The agent fills all six fields; a human performs the
click. The block stays inert (`STATUS: NOT-QUEUED`) until the gate conditions
are met and a coordinator reviews the evidence and queues it.

Rules the block must honor:

- **No secret values, ever** — name environment-variable *names*, never their
  values. Secrets are the owner's to hold.
- **WHY carries a conservative number** — the earnings expectation is
  deliberately low; never overstate to manufacture consent.
- **VERIFIED-WHEN is an observable** — a URL returning 200, a preview showing
  delivery — not "the agent queued it."

```markdown
**STATUS: NOT-QUEUED**

> **Status:** `owner-guidance`

## Evidence
- [[fill: what is built]]
- [[fill: what CI/verification proved — real path, non-author]]

### ⚑ [[fill: short action label]]
- **WHAT:** [[fill: the single decision, e.g. publish <product> at $<price>]]
- **WHERE:** [[fill: exact surface, e.g. Gumroad → New product → Digital product]]
- **HOW:** [[fill: click-level steps — sign in; upload <file>; paste <copy>; set price; publish; copy URL]]
- **WHY:** [[fill: candidate + provenance + conservative expectation, e.g. 0–2 sales/month absent distribution]]
- **UNBLOCKS:** [[fill: what becomes possible once the owner acts]]
- **VERIFIED-WHEN:** [[fill: observable success condition, e.g. public URL returns HTTP 200]]

No secret values are involved — [[fill: which secret is read from which env-var NAME]].
The owner performs the click; no agent publishes, spends, or creates accounts.
```
