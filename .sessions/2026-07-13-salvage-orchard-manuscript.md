# Session — The Salvage Orchard (adult solarpunk novella, EN)

> **Status:** `complete`

- **📊 Model:** fable-5 · BOOKS-lane landing worker · day run 2026-07-13
- **session:** day-run BOOKS clause — first complete manuscript for a round-2 vetted concept
- **applied:** candidates/adult-novels/the-salvage-orchard/{en/the-salvage-orchard.md,DECISIONS.md}
- **verify:** `python3 bootstrap.py check --strict`
- **started:** 2026-07-13T10:20Z
- **closed:** 2026-07-13T10:40Z

## ⟲ Previous-session review
Concept lane state inherited clean: the salvage-orchard vetting packet
(`docs/publishing/vetting/the-salvage-orchard.md`, PR #143) parks at "no
manuscript" (§3/§5) — this session is that write-slice. Sibling today works
`claude/seed-catalogue-manuscript` (disjoint paths); no covering claim in
`control/claims/` at HEAD f15e9f1 (re-verified after #153 merged mid-run:
no overlap with this slice's paths) and no
`candidates/adult-novels/the-salvage-orchard/` directory existed. Direct
review of `.sessions/2026-07-13-marmalade-post-manuscript.md` before
drafting: its executable craft rule (repair an under-floor count where the
audit is thinnest — there, the clue audit) transferred to this lane as a
PROMISE audit and was executed verbatim — first count 13,529, and the
~1,500-word repair went precisely where the packet-§6-blurb/plant→payoff
audit was thinnest (the literal "through windshields" image existed only as
glass mulch; the ch. 3 convent plant had no payoff; the teaching season and
harvest ran on summary where the register wanted scene) — raising premise
fidelity instead of diluting it. Honest nit on the same card: its 💡
(adult-novels README § Works index rot) is real and now one title deeper —
per that card's own convention the backfill belongs to a docs/graduation
lane, not a manuscript claim, so this slice knowingly worsens the count it
cannot fix. The weigh-house → night-kiln → marmalade formatting conventions
(front-matter shape, `# Chapter N — Name` headings, ⁂ scene breaks,
DECISIONS.md) were matched throughout.

## 💡 Session idea
Run under the day-run BOOKS lane (owner day run 2026-07-13). Write the FIRST
COMPLETE MANUSCRIPT for **The Salvage Orchard** — the adult solarpunk
novella concept vetted in `docs/publishing/vetting/the-salvage-orchard.md`
(landed via PR #143, collision Low), which parks at "no manuscript"; this
session is the write-slice that unparks it. Target 15,000–16,000 words
(book-parity default; the packet §3 plans ~25k–35k — the departure is
flagged honestly here and in DECISIONS.md). Solarpunk contract: near-future
repair-and-community register, hopeful without being saccharine, concrete
ecological/technical texture, human-scale stakes, complete emotional arc;
NOT dystopia, NOT a lecture; register-distinct from The Slow Word (no
first-contact/radio/signal/deep-time stems). One READY PR, left OPEN on
green.

## 💡 Idea (deduped vs all 2026-07-13 cards)
**Packets make register-disjointness CLAIMS; manuscripts drift into them —
make the stem lists grep-able and check them at landing time.** The
salvage-orchard packet §6 promises zero stem overlap with The Slow Word's
owned rows ("no `radio`/`signal`/`telescope` stems — disjoint by
construction"), and that construction held at the KEYWORD level — but the
15k MANUSCRIPT drafted today independently produced "hand signals" and "the
co-op radio" in ordinary prose, and only a manual pre-flip grep caught them.
Every future manuscript slice re-runs that risk from memory. Cheap fix in
two parts: (1) packets that assert register disjointness encode it as a
machine-readable stem line (e.g. `register-stems-forbidden: radio, signal,
first contact, telescope, deep time`) instead of prose only; (2) a ~15-line
advisory checker (same tolerant contract as `check_claims`) greps each
`candidates/*/*/en/*.md` against its packet's forbidden-stem line and warns
on hits. Deduped: distinct from marmalade's works-index checker (catalog
listing drift), the graduation checker (packet↔manuscript existence),
paper-orange-graduation's length-budget single-source rule (plan forking),
pepper-ledger's premise-departure register (blurb↔manuscript drift), and
glass-rectory's chronology ledger (intra-book date consistency) — this is
CROSS-BOOK register separation, the one §6 claim currently enforced by
nothing but a worker remembering to grep.

## Outcome
- Complete manuscript delivered:
  `candidates/adult-novels/the-salvage-orchard/en/the-salvage-orchard.md` —
  12 chapters, full arc, THE END. Honest count: `wc -w` = **15,045**
  (includes front matter and chapter headings), inside the 15,000–16,000
  brief band. Packet §3 plans ~25k–35k; the run's book-parity default won —
  flagged here, in DECISIONS.md, and in the PR body, not papered over.
- Solarpunk contract kept: repair-register, hopeful-not-saccharine (real
  losses: frost takes a fifth of the cherries, the storm takes the plums and
  the convent pear, the designation is a revocable audited pilot, the
  grandmother stays dead); concrete texture (grafting craft, brownfield lead
  protocol, bounded mycoremediation, swales/check dams/gauge boards,
  consensus process with minuted fears); conflict fully civic — nobody
  shoots anybody; the antagonist is a reasonable assessor with a half-blind
  rubric. All packet §6 blurb promises verified on the page (audit table in
  DECISIONS.md). Register-disjointness from The Slow Word verified
  mechanically: zero hits for radio/signal/first-contact/telescope/deep-time
  stems in the final text (two incidental draft uses caught and rephrased).
- Emotional arc complete: Ash Okafor's hoarder's grief regrafted into the
  inherited rule ("a graft is a gift, or it dies") — closed by splitting the
  scion roll to the departing apprentice and planting the walnut they won't
  live to pick.
- ⚑ Publishing untouched: all clicks stay queued in the packet §7 OWNER-GATE
  block; keyword-map rows remain name-level reservations.
- Claim `control/claims/salvage-orchard-manuscript.md` deleted in this flip
  commit per the claims README.

## Work log
- 2026-07-13T10:20Z — Branch `claude/salvage-orchard-manuscript` from
  origin/main (f15e9f1); premise check clean (no
  `candidates/adult-novels/the-salvage-orchard/` at HEAD, no covering claim
  in `control/claims/`). Born-red card + claim file committed (first commit,
  8b7c2c6) and pushed; READY PR #151 opened.
- 2026-07-13T10:35Z — All 12 chapters drafted in 3-chapter chunks (commits
  70a0515, 12dff80, 74ce15d, 1379f16): notice → consensus-to-measure →
  scionwood inheritance → assessor visit → teaching Saturdays/frost →
  open-gates argument → storm proof → reversal → scion-library pivot →
  evidentiary harvest → dual-use designation → the walnut. First count
  13,529 → promise-audit expansion (windshield apricot, Mrs. Szabó scene,
  first-pressing naming, convent-lodgment payoff, minuted-fears beat) +
  register-stem scrub → honest 15,045.
- 2026-07-13T10:38Z — DECISIONS.md written (0e7cc11). origin/main re-fetched
  (e3dfab8, #153 merged mid-run); no overlap with this slice's paths;
  merged in. `python3 bootstrap.py check --strict`: only the by-design
  born-red hold remained pre-flip. Card flipped complete, claim file deleted
  same commit, branch pushed; PR #151 left OPEN on green — no auto-merge
  armed.
