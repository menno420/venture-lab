# The Paper Orange — audiobook / narration edition spec

Production spec for a single-narrator **audiobook** of the **full** EN novella
*The Paper Orange — A Novel of the Hunger Winter* (canonical manuscript
`../../en/the-paper-orange.md`, **15,811 words** per
`wc -w candidates/adult-novels/the-paper-orange/en/the-paper-orange.md` →
`15811`, 2026-07-17). **Spec only — no recording, no narrator hire, no audio
file, no distribution**; a narrator/producer reads the base manuscript
unchanged. This spec covers the **EN edition only** — the Dutch edition
(`../nl/de-papieren-sinaasappel.md`, 16,203 words measured) would need its own
narration spec (Dutch narrator, native pronunciation, separate ACX/Findaway
listing) if a Dutch audiobook is ever wanted; it is **not** in scope here.
Structure mirrors the sibling `../large-print/EDITION-SPEC.md` (the print
format extension of this same title). Publishing/production is owner-gated
([`docs/publishing/vetting/the-paper-orange.md`](../../../../../docs/publishing/vetting/the-paper-orange.md) §7).

Provenance: created 2026-07-17 (night run, ORDER 016 — improve an existing
sellable by adding a new gate-free format edition, extending the "versions are
cheap once the research exists" line the `versions/` index carries from
ORDER 008 item 1). Source manuscript pinned above with its measured `wc -w`.

## Narration source & scope

- **Source of truth:** the EN master `../../en/the-paper-orange.md`, read
  verbatim. A version NEVER edits the master (`../README.md` convention);
  nothing in this spec changes a word of the prose.
- **Voicing:** single narrator, all parts (no full-cast dramatization). Close
  third person on Mies throughout — the narrator IS the narrative voice, and
  differentiates the small cast by light shading, not impersonation (see
  *Tone / pacing / character-voice notes*).
- **Language:** English. Dutch place-names, forms of address, and ration-era
  terms are embedded in the English text and must be pronounced correctly (see
  *Pronunciation guide*) — the narrator does not translate them.

## Narration script order

What the narrator reads, in order. The manuscript's markdown is a print
convention; the narrator reads the *text*, not the markup.

1. **Opening credits** (producer-supplied boilerplate, spoken): *"The Paper
   Orange, A Novel of the Hunger Winter, written by [author], narrated by
   [narrator]."* — exact wording set at production; not in the manuscript.
2. **Title + subtitle** — "The Paper Orange" / "A Novel of the Hunger Winter"
   (manuscript lines 1–3).
3. **Content note** (manuscript line 9) — read in full, unhurried, before the
   story. This is a sensitive-history title (famine deaths, deportation
   references, one distant shooting); the note is the reader's informed-consent
   moment and must not be skipped or rushed. ACX/retailer listings should also
   carry it in text.
4. **Chapters One–Twelve, in sequence** — announce each chapter by its spoken
   title (e.g. *"Chapter One. Half a Sack."*), then read the chapter body. A
   short, held silence (~1.5–2 s) at each chapter opener and at the
   scene-break rule (`---`) inside chapters; a longer beat between chapters.
5. **Closing credits** (producer-supplied): *"You have been listening to The
   Paper Orange… This recording is copyright…"* — set at production.

**SKIP (do not voice):**
- The **back-cover blurb** — the `>` block-quote at manuscript line 5
  ("Amsterdam, the winter of 1944…"). It is marketing copy for the listing
  page and the retail sample, not body text; reading it doubles the opening.
  (If the producer wants a spoken teaser for the retail sample clip, this is
  the text to use — but it is NOT part of the book body.)
- All **markdown markup**: the `#` heading hashes, the `---` horizontal rules
  (voiced as a silence, not a word), the `>` quote marker, and the `*…*`
  italic asterisks. Italics are read as **emphasis / interior thought**, never
  announced.
- Any **page numbers, running heads, or file metadata** — none exist in the
  manuscript, but if a typeset PDF is used as the read-from copy, ignore them.

## Pronunciation guide

Dutch place/character names and period terms that **appear in the manuscript**
(verified by grep against the EN master — terms the story does NOT use, e.g.
*onderduiker*, *hongertocht*, are deliberately omitted; the text says "people
in hiding" and "hunger trek" in English). IPA is broad Standard-Dutch; the
plain respelling is a good-enough English-speaker target. The Dutch **g/ch**
is a guttural fricative (written *kh* below — like the *ch* in Scottish
*loch*); a rolled/tapped **r**; **oe** = *oo* as in "boot"; **ui** = a rounded
diphthong with no clean English equivalent (approximated *ow/oy*); **ij/ei**
= *ay* as in "eye"-ish.

### People

| Name | IPA (broad) | Plain respelling | Note |
|------|-------------|------------------|------|
| Mies (Verhoeven) | [mis] | **MEESS** (rhymes with "niece") | the protagonist; not "my-ess" |
| Verhoeven | [vərˈɦuvə(n)] | **fuhr-HOO-vun** | family / the printworks name; final -n lightly dropped |
| Hendrik | [ˈɦɛndrɪk] | **HEN-drik** | Mies's late husband |
| Fien | [fin] | **FEEN** (rhymes with "seen") | daughter, 10 |
| Dirk | [dɪrk] | **DEERK** | son, 6; short Dutch *i*, tapped *r* |
| Vos | [vɔs] | **VOSS** | the network man ("V." in the note) |
| Mevrouw Aalders | [məˈvrʌu ˈaːldərs] | **muh-VROW AHL-ders** | elderly neighbour; *Mevrouw* = "Mrs" |
| Meneer (Vos) | [məˈneːr] | **muh-NAIR** | "Mr" / "sir" |
| De Wit(s) | [də ˈʋɪt] | **duh VIT** | the family sheltered |
| Blom | [blɔm] | **BLOM** | minor character |
| Trijn | [trɛin] | **TRAYN** | minor character |
| Sal Winkler | [ˈsɑl ˈʋɪŋklər] | **SAL VINK-ler** | minor character |

### Places

| Name | IPA (broad) | Plain respelling | Note |
|------|-------------|------------------|------|
| Egelantiersgracht | [ˌeːɣəlɑnˈtirsˌɣrɑxt] | **AY-khuh-lahn-TEERS-khrakht** | Mies's canal street (*gracht* = canal) |
| Rozengracht | [ˈroːzə(n)ˌɣrɑxt] | **ROH-zuh-khrakht** | Jordaan street |
| Prinsengracht | [ˈprɪnsə(n)ˌɣrɑxt] | **PRIN-suh-khrakht** | canal |
| Jordaan | [jɔrˈdaːn] | **yor-DAHN** | the neighbourhood; *J* = English *y* |
| Zuiderkerk | [ˈzœydərˌkɛrk] | **ZOY-der-kairk** | church used as temporary morgue |
| Weteringschans | [ˈʋeːtərɪŋsˌxɑns] | **VAY-ter-ings-khahns** | street (transports east) |
| IJ | [ɛi] | **EYE** | the waterway north of the city |
| Amstel | [ˈɑmstəl] | **AHM-stul** | river |
| Dam | [dɑm] | **DAHM** (not "damn") | Dam square (the 7 May shooting, kept at distance) |
| Eindhoven | [ˈɛinthoːvə(n)] | **AYNT-hoh-vun** | liberated south; Mies's sister's city |
| Brabant | [ˈbraːbɑnt] | **BRAH-bahnt** | the liberated southern province |

### Period terms & phrases

| Term | IPA (broad) | Plain respelling | Meaning / note |
|------|-------------|------------------|----------------|
| noodkacheltje | [ˈnoːtˌkɑxəltjə] | **NOHT-kakh-ul-tyuh** | the tin emergency stove |
| bonkaart | [ˈbɔnˌkaːrt] | **BON-kahrt** | ration card / coupon sheet |
| persoonsbewijs | [pərˈsoːnzbəˌʋɛis] | **per-SOHNS-buh-vayss** | wartime ID card (the one she refuses to forge) |
| razzia | [ˈrɑzija] | **RAH-zee-ah** | an occupation round-up / raid |
| Landwacht / Landwachter | [ˈlɑntˌʋɑxt] / [-ər] | **LAHNT-vakht / -er** | the collaborationist home guard at the checkpoint |
| Sint Nicolaas | [ˌsɪnt ˈnikoːlaːs] | **sint NEE-koh-lahss** | the network's cover name ("friends of Sint Nicolaas") |
| Drukkerij (Verhoeven) | [ˌdrʏkəˈrɛi] | **druk-uh-RAY** | "printers" — the shop fascia |
| Oranje / Oranje Boven | [oːˈrɑɲə ˈboːvə(n)] | **oh-RAHN-yuh BOH-vun** | "Orange" / "Orange Aloft" — the forbidden royal colour; Ch. 12 title |
| Hollandsche Mediaeval | [ˈɦɔlɑntsə mediˈɐval] | **HOL-lahnt-suh may-dee-AH-val** | the real typeface named in-text (S.H. de Roos) |

## Runtime estimate

**WPM assumption:** **~150 words per minute**, the standard single-narrator
audiobook delivery rate (industry norm ~150 wpm; literary fiction with this
book's restrained, close-interiority register typically sits **140–155 wpm**,
so treat every figure below as the midpoint of a ±~5% band). Estimates are
derived from an **honest per-chapter `wc -w`** of the EN master
(`csplit` on the chapter rules, then `wc -w` each piece; the twelve chapter
counts + the front block sum **exactly** to the whole-file `15811`).

| Section | Words (`wc -w`) | Est. runtime @150 wpm |
|---------|----------------:|----------------------:|
| Front matter (title, subtitle, content note) | 147 | ~0:59 |
| Chapter One — Half a Sack | 1,913 | 12:45 |
| Chapter Two — Meneer Vos | 1,596 | 10:38 |
| Chapter Three — The Drawer | 1,192 | 7:57 |
| Chapter Four — Grey-Green | 1,263 | 8:25 |
| Chapter Five — What Burned | 1,167 | 7:47 |
| Chapter Six — The Barrow | 1,552 | 10:21 |
| Chapter Seven — The Shortest Month | 1,211 | 8:04 |
| Chapter Eight — Locked Formes | 1,241 | 8:16 |
| Chapter Nine — White Bread | 1,281 | 8:32 |
| Chapter Ten — Manna | 877 | 5:51 |
| Chapter Eleven — The Seam | 1,183 | 7:53 |
| Chapter Twelve — Oranje Boven | 1,188 | 7:55 |
| **Total (whole read-aloud text)** | **15,811** | **≈ 1:45:24 (~1 h 45 m)** |

- **Chapters-only body** (excludes the ~1-min front matter): 15,664 words ≈
  **1:44:26**.
- **Add pacing overhead** (chapter-opener and scene-break silences, breaths,
  the deliberately slower delivery this material wants): a realistic **finished
  runtime ~1 h 48 m – 1 h 55 m**. At ~9,000 words/finished-hour (150 wpm × 60)
  the book is **≈ 1.75 "finished hours"** — the unit ACX/producers quote for
  narrator cost and royalty math (that math is owner-gated; not computed here).
- **Recording-time rule of thumb** (not runtime): finished audiobooks take
  ~2–3× the runtime to record + edit + master, so ~1.75 finished hours ≈
  **~4–5 studio hours** of narrator/engineer effort — an input to the owner's
  hire decision, listed for planning only.

## Tone / pacing / character-voice notes

- **Register:** literary-historical, close and restrained. The prose does the
  emotional work; the narrator **under-plays**. Grief, hunger, and the two
  deaths (Hendrik's offpage pneumonia; Mevrouw Aalders in February) are
  delivered plainly — no sentimental swell. The book's own discipline ("you do
  not gild an orange", Ch. 12) is the narration's discipline.
- **Pace:** unhurried, winter-slow. This is a cold, quiet, interior novella;
  resist the impulse to speed the exposition. Let the ration-arithmetic
  passages (peeling bulbs, counting chimneys, the coupon work) breathe.
- **The children:** Dirk (6) is bright, literal, hungry-for-chocolate;
  differentiate with a lighter, quicker touch — **do not** do a cartoon
  child-voice. Fien (10) has taught herself the "flat voice she used now for
  facts" — read her lines level and careful, older than her years. The
  contrast between the two is a load-bearing emotional device; keep it subtle.
- **Vos:** seen only from outside (period-true compartmentalisation). His few
  lines are quiet, careful, never warm — the narrator gives him restraint, not
  menace or heroism; his offpage fate stays unresolved and unmourned aloud.
- **Dutch words:** pronounce them cleanly and move on — they are lived-in, not
  exhibited. The guttural *g/ch* and the *gracht* names should sound native,
  not laboured. Inline italic Dutch (*Oranje boven*) is emphasis, not a
  language-switch performance.
- **The paper orange motif:** the folded-orange passages (Ch. 1 origin, Ch. 11
  the seam, Ch. 12 the window) are the emotional spine — read them with a
  fraction more space and stillness, but still **without** underlining. The
  final image (orange in the window; the street's children folding their own)
  lands quietest of all.
- **Sensitive history:** the content note, the refused staircase (Ch. 5, the
  deported bookbinder), and the distant Dam shooting (Ch. 12) are handled with
  dignity in the text; the narration matches that — no dramatization of
  atrocity, no lingering.

## Production reference (when owner green-lights)

*Listed for planning only — none of this is executed or authorized here.*

1. Narrator audition against a sample scene (suggested: Ch. 1 bulb-peeling
   open, or the Ch. 6 checkpoint) — tests the restrained register AND the
   Dutch pronunciation in one pass.
2. Record from the EN master unchanged; hold to the *Narration script order*
   above (skip the blurb; content note read in full).
3. Master to the distributor's technical spec (ACX and Findaway both publish
   RMS/peak/noise-floor targets and a per-file chapter layout; verify the live
   spec at production — not reproduced here).
4. Cover: reuse the standard-edition cover art (when it exists) at the
   audiobook's square ratio; any art spend is an owner decision.
5. Run the relevant `docs/publishing/CHECKLIST.md` steps for the format.

## NOT included / owner-gated

This file is a **production-ready spec only**. Every one of the following is an
**owner decision** and is explicitly **out of scope** for this slice — nothing
here authorizes any of them:

- **Recording** — no audio has been produced; no narration performed.
- **Narrator hire / casting** — any audition, contract, per-finished-hour fee,
  or royalty-share is a spend and stays owner-gated.
- **Distribution** — ACX, Findaway Voices, Spotify/Audible, or any retailer
  account, upload, listing, price, or category selection.
- **Any spend / accounts** — no accounts touched, no purchase, no publish.

⚑ **Recording, hire, distribution, and price clicks stay owner-gated**
(vetting packet §7; `docs/publishing/CHECKLIST.md` §7 / CONSTITUTION rail 13) —
nothing in this spec creates a listing, sets a price, hires a narrator, or
spends. Audiobook **production remains a future owner-gated step**; this slice
ships only the preparatory spec.

---

**Provenance footer.** Derived from the EN master
`candidates/adult-novels/the-paper-orange/en/the-paper-orange.md@aa04700`
(last commit touching the file; blob `703377e`), `wc -w` = **15,811**,
per-chapter counts measured 2026-07-17 via `csplit` on the chapter rules +
`wc -w` (twelve chapters + front block sum exactly to 15,811). Canonical
title/subtitle facts from
`candidates/adult-novels/the-paper-orange/DECISIONS.md`. No manuscript text
was altered.
