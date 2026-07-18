# Session — The Night Kiln (trilogy) audiobook/narration EDITION-SPEC (gate-free format reach)

> **Status:** `complete`

- **📊 Model:** claude-opus-4-8 family · high effort · edition-spec (content)
- **started (date -u):** Sat Jul 18 00:16:29 UTC 2026
- **branch:** `claude/night-kiln-audio-spec-2026-07-18` (PR #228)
- **base:** `main@12e221d`
- **purpose:** add a new **gate-free format edition** to the completed EN
  *Night Kiln* trilogy — an **audiobook / narration-ready EDITION-SPEC** a
  narrator/producer could follow, landed as ONE PR. New file
  `candidates/adult-novels/the-night-kiln/versions/audio/EDITION-SPEC.md`,
  covering the three EN books as **one trilogy audio program** (per-book
  audiobooks + an optional single omnibus audio program), mirroring the
  just-merged Paper Orange audio spec (PR #225) and the sibling
  `versions/large-print/` + `versions/omnibus-en/` + `versions/README.md`
  convention. The spec ships **per-book narration script order** (front-matter
  read order, 12-chapter sequence, back matter, what to SKIP), a
  **pronunciation / voice-consistency guide** for the invented proper names
  that recur across three books (grep-verified — the text is entirely English
  invented cozy-fantasy, so there are **no** real Dutch/foreign-language terms
  to translate, stated honestly), **honest per-book AND per-chapter `wc -w`**
  (numbers shown, reconciling exactly to 15,999 / 15,995 / 23,334) with
  runtime @ ~150 wpm + ACX finished-hours per book and a **trilogy total**,
  tone/pacing/character-voice notes, and an explicit owner-gated NOT-included
  section. **Spec only — no recording, no narrator hire, no distribution, no
  spend.** Actual narration/production stays owner-gated.
- **distinct-from:** the `versions/large-print/` + `large-print-book-2/` specs
  are *per-book print* format extensions (6×9, 16pt, KDP royalty math); the
  `nl/` `nl-book-2/` `nl-book-3/` dirs are *translations*; the
  `versions/omnibus-en/` spec is a *single-volume recombination* (higher-AOV
  print/ebook box-set). THIS is the *audio* format extension (script order,
  pronunciation/voice consistency, runtime) off the SAME three EN masters — no
  overlap; near-zero-marginal-cost catalog reach off research that already
  exists ("versions are cheap once the research exists").
- **NL note:** this spec is **EN-only**. An NL narration edition (*De Nachtoven*
  / *De Morgendeur* / *De Oogstslag*, all three NL editions complete under
  `../nl/`, `../nl-book-2/`, `../nl-book-3/`) is a natural mirror but is
  **deferred**: it rides the owner's still-open one-word length-band ratify in
  `LENGTH-BAND-PREP.md` (needs a Dutch narrator + native pronunciation +
  separate ACX/Findaway listing). The EN audio program does **not** depend on
  that ratify and does not touch it.
- **queue note:** editions do **not** get their own §7 vetting packet or
  OWNER-QUEUE row — the large-print sibling created neither, and
  `scripts/derive_owner_queue.py` derives the queue only from vetting packets'
  §7 blocks (confirmed on the slice-3 audio spec #225 and the slice-4 omnibus
  spec #226). This slice adds **no queue row** and regenerates nothing.
  Audiobook **production** (recording, narrator hire, ACX/Findaway
  distribution, any spend) stays owner-gated under the title's existing packet
  gate; this slice invents no publish surface.
- **session:** Born-red card holds substrate-gate red (in-progress badge +
  unresolved fill slots) until the deliberate completion flip; mirrors the
  Paper Orange audio-spec scaffold exactly (identity → per-book script order →
  pronunciation/voice guide → per-book+per-chapter `wc -w` runtime → tone →
  owner-gate → per-`file@sha` provenance footer).

## 💡 Session idea

💡 **A trilogy audio box-set + Whispersync ebook/audiobook pairing** is the
distinct next move once these recordings exist (dedup: slice-3's #225 💡 already
covers templatizing the audio *spec* into `versions/audio/EDITION-SPEC.template.md`
— this is about the *product*, not the scaffold). The catalog already has, off
these SAME masters, three EN ebooks, a print/ebook omnibus, and now an audio
program — Amazon/Audible's **Whispersync for Voice** lets a buyer own the ebook
and audiobook of a title and switch between reading and listening mid-book, and
it is the single strongest cross-sell audiobooks have. So the owner-ready
listing shape is: **(a)** each book's audiobook Whispersync-paired to its
existing ebook (read-and-listen for one shopper), and **(b)** a **single
omnibus audio SKU** paired to the omnibus ebook — the exact "one click, whole
arc" AOV lift the print omnibus already argues, now with a switch-media hook.
The mechanical enabler: a tiny **`scripts/derive_audio_runtime.py`** that
`csplit`s any EN master on its `# Chapter` rules, `wc -w`s each piece, and emits
the per-chapter + per-book runtime table (words ÷ 150 wpm) and ACX finished-hours
straight into a per-title **`AUDIO-RUNTIME.md`** — so the one genuinely
per-title number in every audio spec (the runtime table) is machine-derived and
drift-proof, and the pairing/Whispersync eligibility check becomes a listing-time
checklist rather than hand math. Recording/hire/distribution/Whispersync
enrollment all stay parked at the single owner ⚑ gate; the pairing is a listing
decision, zero new prose.

## previous-session review

previous-session review: `.sessions/2026-07-17-shopify-webhook-test-kit.md`
(PR #227, slice-5 of ORDER 016 — the Shopify Webhook Test Kit $29) — a clean
N+1 build of the proven Stripe/GitHub/Slack webhook-kit scaffold that did the
honest things right: it called out the Shopify-specific scheme differences
out loud (base64 HMAC not hex, signed over the raw body with **no** timestamp
so there's no replay mode, no vendor known-answer constant so the `vector`
command is an honest kit-internal parity proof, not a faked reproduction),
carried pinned per-fixture sha256 provenance, proved a byte-reproducible bundle,
and correctly **ended at the queued owner ⚑ publish click** — no publish, no
spend, no accounts. Its 💡 — extract a shared `_webhook-kit-core/` + a
`provenance_lint.py` that FAILS a kit whose fixture lacks a pinned sha256 — is
the same "templatize the proven tier and machine-enforce the honesty bar before
it drifts" instinct this card's audio 💡 applies to the runtime table; both
lanes independently converging on "extract the shared derivation now, don't
hand-repeat it" is the strongest signal that the mechanical-derivation slice is
the next high-leverage consolidation in each.
