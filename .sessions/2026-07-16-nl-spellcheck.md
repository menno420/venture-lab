# Session — nl_NL hunspell spellcheck pass over the 4 NL manuscripts (capability probe + §6 per PRE-QA note)

> **Status:** in-progress

- **📊 Model:** Claude Opus · high · discovery/build
- **started (date -u):** Thu Jul 16 17:42:16 UTC 2026
- **branch:** `claude/nl-spellcheck` (PR TBD)
- **session:** ⚑ Follow-on to PR #214's pre-QA notes, closing the ONE
  mechanical lane that slice could not run. Every one of #214's four
  `PRE-QA.md` notes had to say "no spellcheck pass was run" purely because a
  hunspell nl_NL dictionary was assumed absent — that assumption is the
  target here. This slice runs a real Dutch spellcheck and folds a §6
  candidate-misspelling section into each of the four notes. It does **NOT**
  touch, tick, or clear the ⚑ Owner native-speaker proofread gate.

## WHAT

A DISCOVERY capability-probe followed by a spellcheck pass over the four
NL adult manuscripts that carry a PR#214 `PRE-QA.md` note:

- De geborgen boomgaard (`the-salvage-orchard`)
- Liefde in de kantlijn (`the-seed-catalogue-courtship`)
- De Marmeladepost (`the-marmalade-post`)
- De zoete zee (`the-sweetwater-sea`)

Each note gains a §6 mechanical spellcheck section; the stale "no spellcheck
pass was run" preamble line in each is corrected; and the nl_NL spellcheck
capability is recorded in `docs/CAPABILITIES.md` (append log, below the kit
fence) so no future session re-probes it.

## PROBE VERDICT — WORKS

- `pip install spylls` → **0.1.7**, exit 0 (pure-Python hunspell engine).
- OpenTaal / LibreOffice `nl_NL` hunspell **v2.20.21 (2021-07-03), 180,715
  stems**, fetched via the agent proxy from
  `raw.githubusercontent.com/LibreOffice/dictionaries/master/nl_NL/nl_NL.{dic,aff}`
  — both **HTTP 200** (dic 2,488,246 B, aff 46,557 B). `.aff` header self-identifies
  the OpenTaal source and the 2021-07-03 2.20.21 version.
- `pip install pyspellchecker` → 0.9.0, exit 0 (installed as a frequency-dict
  fallback; not needed — the real hunspell dictionary was the chosen path).
- **System hunspell is WALLED:** no `hunspell` CLI (`which hunspell` exit 1),
  no `/usr/share/hunspell` or `/usr/share/myspell` dictionary — only the
  `libhunspell-1.7-0` shared library is present. The spylls + OpenTaal path
  routes around it entirely.

## RESULT

**61,982 tokens** checked across the four manuscripts (512 raw unique flags).
After filtering **135 proper nouns / 87 documented craft coinages / 254 valid
dict-gap compounds** (hunspell nl_NL does no free compounding, so every valid
novel compound flags) plus accent- and casing-artifacts:

- **De Marmeladepost — 2 candidates:** `schifte` → **`schiftte`** (HIGH,
  L396, past tense of *schiften*, stem ends in -t → double t) and
  `geproefleesd` → **`proefgelezen`** (MED, L256, *lezen* is a strong verb).
- **The other three — 0 clear misspellings** (De geborgen boomgaard carries 2
  nonstandard *forms* — `anderser`, `gewrakte` — kept for a native register
  glance only, not proposed as corrections).

## NOT-THIS-PASS

- Mechanical candidates only. This is **NOT a proofread** and makes no claim
  about idiom, naturalness, or register quality.
- It does **NOT** clear the ⚑ Owner native-speaker proofread gate — that read
  stays the owner's. **No owner checkbox is ticked or altered.**
- The hard-gated owner-queue count is untouched by this slice.

## TRUTH (cites)

- Base: `main@973fb05` (branch cut from `origin/main`).
- Tool: `spylls` **0.1.7** (pip, exit 0).
- Dictionary: OpenTaal / LibreOffice `nl_NL` hunspell **v2.20.21 (2021-07-03)**,
  180,715 stems, both `.dic`/`.aff` HTTP 200 via the agent proxy.
- Timestamps: `date -u` (started 2026-07-16 17:42:16 UTC).

## ⟲ Previous-session review

previous-session review: `.sessions/2026-07-16-pre-qa-notes.md` (the ⚑
self-initiated pre-QA slice, PR #214). Its central fact holds under
re-verification this wake: each of the four `PRE-QA.md` notes it landed
carried a "no spellcheck pass was run" line because a hunspell nl_NL
dictionary was assumed absent — and that assumption is exactly the residue
this slice closes at the root (the probe proved spylls + OpenTaal nl_NL WORKS
from the agent seat). The four notes' §1–§5 consistency checks are untouched;
this slice only appends §6 and corrects the one false preamble sentence. The
⚑ Owner proofread gate #214 declined to touch stays untouched here too.

## 💡 Session idea

💡 **Fold the now-proven nl_NL spellcheck into a small reusable
`scripts/pre_qa.py`** so the mechanical lane (coined-term variant counts,
NL-caveated doubled-word scan, quote-char inventory, longest-paragraph seam
list, AND this hunspell candidate pass) is one re-runnable command per title
instead of hand-assembled per note. #214's 💡 proposed *provisioning* the
dictionary; this wake proved the dictionary is fetchable at runtime with zero
provisioning (spylls + a proxy `curl`), so the remaining cheap win is
codifying the pipeline — vendor the `nl_NL.{dic,aff}` fetch + the
proper-noun/glossary/compound filters the four §6 sections applied by hand, so
the next EN→NL fix propagation re-runs the spelling pass mechanically rather
than re-deriving the filter buckets.
