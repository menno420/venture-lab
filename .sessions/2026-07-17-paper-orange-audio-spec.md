# Session — The Paper Orange audiobook/narration EDITION-SPEC (gate-free format reach)

> **Status:** `in-progress`

- **📊 Model:** [[fill:model]]
- **started (date -u):** Fri Jul 17 23:28:45 UTC 2026
- **branch:** `claude/paper-orange-audio-spec-2026-07-17` (PR TBD)
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

[[fill:idea]]

## previous-session review

[[fill:prev-review]]
