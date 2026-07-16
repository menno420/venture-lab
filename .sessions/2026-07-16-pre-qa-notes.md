# Session — mechanical pre-QA notes + length-band ruling prep (shrink the owner's cold NL proofread read to a guided checklist, without touching the owner gate)

> **Status:** `complete`

- **📊 Model:** Claude Opus · high · review/verify
- **started (date -u):** Thu Jul 16 16:58:12 UTC 2026
- **branch:** `claude/pre-qa-notes` (PR TBD)
- **session:** ⚑ Self-initiated slice, and the session's FINAL planned
  round. All inbox ORDERs 011–015 are terminal; nothing owner-queued asked
  for this. The binding constraint on ~13 ready NL editions is an
  OWNER-ONLY native-speaker proofread pass — an AI cannot clear it
  (confirmed by the #213 slice, which recognised it as HARD-GATED). This
  slice deliberately does **NOT** touch that gate. Instead it attacks the
  constraint sideways: it produces artifacts that SHRINK the owner's
  proofread work from a cold ~16k-word Dutch read per title down to a
  guided checklist — the native read stays the owner's, but it is no longer
  cold.
- **scope:** THREE parts, ONE PR.
  - **Part A** — a per-title MECHANICAL pre-QA note (`PRE-QA.md`, sibling to
    the version's `NOTES.md`) for the 3–5 NL titles closest to publishable.
    Each note carries ONLY what an agent can legitimately produce and an
    explicit disclaimer that it is machine pre-annotation, NOT a native
    proofread and NOT a gate clear: a coinage / craft-register inventory
    with a cross-manuscript CONSISTENCY check (variant spellings/inflections
    of a coined term, cited by location), the flagged word-count expansion
    seams isolated and quoted for the human to judge calque-padding, and
    mechanical nits (doubled words, quote/dialogue-punctuation
    inconsistencies) cited by location. hunspell nl_NL is NOT installed in
    this environment, so NO spellcheck pass is claimed — consistency-based
    checks only, stated as such in every note.
  - **Part B** — length-band ruling PREP for **De Morgendeur** (Book 2) and
    **De Oogstslag** (Book 3) of the Night-Kiln series: honest `wc -w`
    against the catalog band, the trade-off, and a clear RECOMMENDATION for
    a one-word owner ratify. The ruling itself stays the owner's — this
    slice does NOT rule.
  - **Part C** — tighten the D-item attribution in
    `scripts/derive_owner_queue.py` so a native-speaker proofread blocking
    row is never mis-classified as executing a D-item decision above (the
    Weduwenblauw "…for this title" ↔ "Title coupling" keyword-overlap bug
    the #213 slice flagged), + regression test, + OWNER-QUEUE regen. Same
    owner-misleading-wording class as #210/#213. Folded in only because it
    is small and self-contained.
- **walls:** no publish, spend, or external action; no edits to
  `control/inbox.md`; no merge or auto-merge from this seat; the generated
  OWNER-QUEUE.md is only ever written by the script; **no ⚑ Owner gate
  checkbox is ticked or altered** — the hard-gated count must stay 19;
  family-level model names only.
- **verify plan:** every pre-QA note cites real manuscript locations (no
  generic filler; a title that yields nothing meaningful says so rather
  than padding). Regenerate `docs/publishing/OWNER-QUEUE.md` via
  `python3 scripts/derive_owner_queue.py` and confirm hard-gated stays 19
  (Part C only changes Weduwenblauw's explanatory suffix, never gate state).
  `scripts/test_derive_owner_queue.py` + `scripts/lint_owner_gates.py` must
  pass; `python3 bootstrap.py check --strict` must exit 0 (its born-red HOLD
  on this card is the designed exception until the completion flip).
- **done-when:** the pre-QA notes + length-band prep + Part C fix land on a
  READY PR, CI green (kit-tests + substrate-gate), heartbeat re-stamped,
  and this card flipped `complete` as the last commit (clearing the
  born-red HOLD).

## Results (as landed)

- **Part A — four `PRE-QA.md` notes** (each a sibling of the version's
  `NOTES.md`), for the four NL titles judged closest to publishable
  (complete packet + manuscript present + band-correct novella):
  `candidates/adult-novels/the-salvage-orchard/versions/nl/PRE-QA.md`
  (De geborgen boomgaard — hen/hen/hun pronoun-strategy consistency, 43
  Ash+gendered-pronoun antecedent-check spots, `Enthoutbibliotheek`
  capitalization split at line 413, verbatim-motif punctuation drift, the
  283-line double-quote outlier),
  `.../the-marmalade-post/versions/nl/PRE-QA.md` (De Marmeladepost —
  single-mint coinage confirmed at line 521, the 26-site single-outer/
  double-inner quote-nesting inventory, je/u register axis),
  `.../the-sweetwater-sea/versions/nl/PRE-QA.md` (De zoete zee —
  craft-neologism inventory, `steunwet` capitalization checked-intentional
  via the in-text `Zuiderzeesteunwet` gloss, `Van Van` shown grammatical,
  tightest +1.5% seams),
  `.../the-seed-catalogue-courtship/versions/nl/PRE-QA.md` (Liefde in de
  kantlijn — full epistolary closing-register arc mapped, the line-359 and
  line-645 against-trend spots isolated, the 7 `belasting` load/tax
  dual-sense sites). Every citation is a real manuscript location; hunspell
  nl_NL absent so NO spellcheck claimed; each note carries the machine-
  pre-annotation disclaimer. Referenced from the 4 packets by an inert
  column-0 line — the OWNER-QUEUE regen was byte-identical for those
  packets (verified).
- **Honest per-title value:** genuine, not thin. Boomgaard and Liefde are
  the strongest (a load-bearing consistency axis each an AI can enumerate
  in full — the pronoun antecedents; the register arc). Marmeladepost and
  Zoete zee are medium (the quote-nesting inventory and the
  craft-term/steunwet checks are real but lighter). None is padding; the
  notes shrink a cold read to a finite check-list, they do not clear the
  gate.
- **Part B — length-band prep:**
  `candidates/adult-novels/the-night-kiln/LENGTH-BAND-PREP.md`. Honest
  `wc -w` 2026-07-16: De Morgendeur 16,730 NL / 15,995 EN (+4.6%, below the
  ~20k–30k band, at Book-1 parity 16,840); De Oogstslag 24,655 NL / 23,334
  EN (+5.7%, squarely in band). Recommendation for a one-word owner ratify:
  keep current lengths (Oogstslag already conforms; extend Books 1+2
  *together* only on owner say-so, never Book 2 alone). Prep only — did NOT
  rule.
- **Part C — proofread-gate D-item wording fix** (`scripts/derive_owner_queue.py`):
  a native-speaker proofread blocking row is never classified as executing
  a D-item decision above (`if PROOFREAD_GATE_RE.search(clean): linked =
  False`). OWNER-QUEUE diff is exactly Weduwenblauw's two rows — header now
  `**HARD-GATED** — blocking row: native-speaker proofread pass…` and the
  proofread click drops the wrong "executes its D-item above"; the
  title-ratify click KEEPS "(executes its D-item above)" and the three
  illustration books (Painted Stones, Puddle Museum, Windmill Mouse) are
  untouched. +1 regression test
  (`test_proofread_gate_with_title_overlap_names_proofread_row`).
- **Gates:** `scripts/test_derive_owner_queue.py` → OK (13 in the class,
  incl. the new regression + the retained genuine-D-item test);
  `scripts/lint_owner_gates.py` → `OK — 47 input(s) clean`;
  `python3 bootstrap.py check --strict` exit 0 (green except this card's own
  designed born-red HOLD, now cleared by this flip). guard-fire telemetry
  delta (7 records) committed with the build, not reverted.
- **Landed as PR #214**, READY, base main, head `claude/pre-qa-notes`.
  Hard-gated count stayed **19** throughout (no gate ticked or flipped).
  Heartbeat re-stamped (`control/status.md`, commit `9cb5837`);
  `control/inbox.md` untouched (still ends at ORDER 015).

## ⟲ Previous-session review

previous-session review: `.sessions/2026-07-16-proofread-gate-detection.md`
(the ⚑ self-initiated proofread-gate detection fix, PR #213, merged
`9473e5f`) — its central facts held under re-verification this wake: the
merge is on main and HARD-GATED now stands at 19, and its own honestly-
recorded nuance (Weduwenblauw's suffix reading the D-item variant because
"(…for this title)" keyword-overlaps a "Title coupling" ⚑ decision) is
exactly the residue this wake's Part C closed at the root — the proofread
row now names itself, and #213's `is_blocking_box` hard-gate logic and the
three normalised packets are untouched.

## 💡 Session idea

💡 **Provision `hunspell` + an `nl_NL` dictionary in the environment/CI so a
pre-QA pass can add a real spelling-candidate list — the one honest check
this slice could NOT run.** Every `PRE-QA.md` this wake had to say "no
spellcheck claimed" purely because the binary/dictionary is absent; a
one-line dependency add upgrades every future pre-QA note from
consistency-only to consistency+spelling, which is the single mechanical
lane that most shrinks a native proofread and that an AI can legitimately
own. Cheap follow-on: fold the mechanical sections (coined-term variant
counts, NL-caveated doubled-word scan, quote-char inventory, longest-
paragraph seam list, and the hunspell candidate pass) into a small reusable
`scripts/pre_qa.py` so the pattern is consistent and re-runnable after each
EN→NL fix propagation, instead of hand-written per title. Deduped against
prior `.sessions/*.md` 💡 lines: the proofread-gate-detection 💡 (tighten
the `linked`/D-item keyword heuristic) was *implemented* here as Part C, so
it is retired, not re-proposed; this idea is about the spelling-check
capability gap, a different lane.

## DRY-BACKLOG

Net-new inventory is paused, and this was the session's FINAL planned round.
The single binding lever on the ~13 ready NL editions is the owner-only
native-speaker proofread pass — an AI cannot clear it, so this wake spent
its value making that read guided (four pre-QA notes) rather than adding to
the pile. The remaining agent-executable work is now diminishing-value: the
pre-QA notes do not multiply cheaply past the closest titles, the
length-band and title ratifies are owner calls, and the hunspell gap (see
💡) is the only mechanical lane still worth opening. Honest next move: hold
for the owner's proofread / length-band / title-ratify decisions rather
than manufacture more churn.
