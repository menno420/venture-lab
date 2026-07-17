# Session — The Paper Orange audiobook/narration EDITION-SPEC (gate-free format reach)

> **Status:** `complete`

- **📊 Model:** claude-opus-4-8 family · high effort · edition-spec (content)
- **started (date -u):** Fri Jul 17 23:28:45 UTC 2026
- **branch:** `claude/paper-orange-audio-spec-2026-07-17` (PR #225)
- **base:** `main@5f85816`
- **purpose:** add a new **gate-free format edition** to the flagship title
  *The Paper Orange* — an **audiobook / narration-ready EDITION-SPEC** a
  narrator/producer could follow, landed as ONE PR. New file
  `candidates/adult-novels/the-paper-orange/versions/audio/EDITION-SPEC.md`,
  mirroring the existing `versions/large-print/EDITION-SPEC.md` convention.
  Spec ships **narration script order** (front-matter read order, 12-chapter
  sequence, back-matter, what to SKIP), a **Dutch pronunciation guide** for the
  place/character names and ration-era terms that appear in the text, **honest
  per-chapter `wc -w` runtime estimates** at a stated ~150 wpm, tone/voice
  notes, and an explicit owner-gated NOT-included section. **Spec only — no
  recording, no narrator hire, no distribution, no spend.** Actual
  narration/production stays owner-gated.
- **distinct-from:** the `versions/large-print/` spec is a *print* format
  extension (trim/typography/KDP royalty math); THIS is the *audio* format
  extension (script order, pronunciation, runtime) off the SAME EN master. No
  overlap; both are near-zero-marginal-cost catalog reach off research that
  already exists.
- **queue note:** editions do **not** get their own §7 vetting packet or
  OWNER-QUEUE row — the large-print spec created neither, and
  `scripts/derive_owner_queue.py` derives the queue only from vetting packets'
  §7 blocks. Audiobook **production** (recording, narrator hire,
  ACX/Findaway distribution, any spend) remains an owner-gated future step
  under the title's existing packet gate; this slice adds no queue row and
  invents no publish surface.
- **session:** Born-red card holds substrate-gate red until the deliberate
  completion flip; mirrors the `versions/large-print/EDITION-SPEC.md`
  edition-spec scaffold exactly (identity → read order → pronunciation →
  runtime → tone → owner-gate → provenance footer).

## 💡 Session idea

💡 This spec's shape — identity → narration script order → pronunciation guide
→ per-chapter `wc -w` runtime @ a stated wpm → tone/voice notes → owner-gate →
provenance footer — is **title-agnostic**. Lift the non-story scaffolding into
a reusable **`versions/audio/EDITION-SPEC.template.md`** (or a
`scripts/new_audio_spec.py` that stubs the per-chapter runtime table straight
from `csplit` + `wc -w`), and every EN catalog title inherits a
narrator-ready audiobook spec for the cost of one grep-and-fill: the runtime
table and the pronunciation guide are the only genuinely per-title parts, and
both are mechanical to derive. Same "versions are cheap once the research
exists" economics the large-print bundle proved — a whole gate-free format
tier across the catalog, each spec landing red→green as its own tiny PR, with
recording/hire/distribution still parked at the single owner ⚑ gate. The
audio tier pairs naturally with the existing large-print tier: one print
accessibility format, one audio accessibility format, both spec-only, both
inheriting the same owner-gate.

## previous-session review

previous-session review: `.sessions/2026-07-17-auto-merge-enabler-cookbook.md`
(PR #224, slice-2 of ORDER 016) — a clean N+1 build of the proven
guide-shaped cookbook scaffold that did the honest thing twice over: it was
**verified-by-production** (its subject IS this repo's live enabler workflow,
so it cited `file@sha` + real squash-merge event IDs rather than a synthetic
test), and it named its own commercial risk out loud (narrow shared
agent-builder audience) and turned it into the "CI/CD for Agent Fleets" bundle
💡 instead of hiding it. Its regenerate-don't-hand-edit instinct for
OWNER-QUEUE.md is the same anti-drift principle that told THIS slice to add no
queue row at all — editions aren't a publish surface, so inventing one would
have been the drift the enabler card warns against.
