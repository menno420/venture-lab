# Catalog keyword & category allocation map

> **Status:** `reference`
>
> One table answers "who owns this KDP phrase?" for the 14-title catalog.
> Implements the 💡 idea from `.sessions/2026-07-12-publishing-plan-retier.md`
> (PR #94): vetting packets draft "2 categories + 7 keywords" in isolation, so
> with 14 titles heading for the same storefront several will converge on the
> same high-value phrases and cannibalize each other's placement. This map
> makes each packet CLAIM its phrases at vetting time — the way
> `control/claims/` claims work — so the catalog deliberately tiles the KDP
> search space instead of piling onto the same shelf.

## How to use this map

- **Packets claim phrases here at vetting time** (CHECKLIST §6): before
  locking your 2 categories + 7 keywords, check this table; add one row per
  keyword/category you take. First claim on `main` wins a collision.
- **One row per keyword** — no shared free-text blob; conflicts are resolved
  in the CONFLICTS section below **before a packet ships** (§7 owner gate).
- **Files are truth:** each vetted title's rows below reproduce its packet §6
  verbatim; if a packet and this map disagree, fix the map in the same PR
  that changed the packet.
- Disputed reallocations that would change an already-shipped packet carry a
  **⚑ OWNER** marker — the seat proposes, the owner decides; packets are not
  edited retroactively without that decision.

## 1. Ownership table — vetted packets (source: each packet's §6, verbatim)

### Categories

| Category (KDP browse node) | Owning title | Source |
|---|---|---|
| Science Fiction → **First Contact** | The Slow Word | [`vetting/the-slow-word.md`](vetting/the-slow-word.md) §6 |
| **Literary Fiction** | The Slow Word | [`vetting/the-slow-word.md`](vetting/the-slow-word.md) §6 — **CONTESTED, see C1** |
| Mystery, Thriller & Suspense → Crime Fiction → **Police Procedurals** | The Weigh House | [`vetting/the-weigh-house.md`](vetting/the-weigh-house.md) §6 |
| Mystery → **International Mystery & Crime** | The Weigh House | [`vetting/the-weigh-house.md`](vetting/the-weigh-house.md) §6 |
| Literature & Fiction → Genre Fiction → **Historical Fiction** | Ultramarine (default title *The Widow's Blue*, ⚑ OWNER pick pending) | [`vetting/ultramarine.md`](vetting/ultramarine.md) §6 |
| Literature & Fiction → **Literary Fiction** | Ultramarine — **CONTESTED, see C1** | [`vetting/ultramarine.md`](vetting/ultramarine.md) §6 |
| Children's Books → **Mysteries & Detectives** | The Painted Stones | [`vetting/the-painted-stones.md`](vetting/the-painted-stones.md) §6 |
| Children's Books → Growing Up & Facts of Life → **Friendship** | The Painted Stones | [`vetting/the-painted-stones.md`](vetting/the-painted-stones.md) §6 |

### Keywords

| Keyword (verbatim) | Owning title |
|---|---|
| `first contact novella` | The Slow Word |
| `deep time science fiction` | The Slow Word |
| `literary sci-fi Pacific island` | The Slow Word |
| `radio telescope alien signal story` | The Slow Word |
| `indigenous knowledge science fiction` | The Slow Word |
| `slow message from the stars` | The Slow Word |
| `generational legacy novella` | The Slow Word |
| `Amsterdam crime novel` | The Weigh House |
| `Dutch police procedural` | The Weigh House |
| `police diver mystery` | The Weigh House |
| `canal murder Netherlands` | The Weigh House |
| `atmospheric European noir` | The Weigh House |
| `money laundering crime fiction` | The Weigh House |
| `widow investigates husband's death` | The Weigh House (see C2 — watched adjacency) |
| `Dutch Golden Age novel` | Ultramarine |
| `Delft 1654 historical fiction` | Ultramarine |
| `Vermeer era Netherlands story` | Ultramarine |
| `painter pigment art historical novel` | Ultramarine |
| `widow grief literary fiction` | Ultramarine (see C2 — watched adjacency) |
| `Delft Thunderclap gunpowder explosion` | Ultramarine |
| `17th century historical novella` | Ultramarine |
| `picture book mystery ages 4-8` | The Painted Stones |
| `girl detective picture book` | The Painted Stones |
| `new kid making friends story` | The Painted Stones |
| `read aloud mystery for kids` | The Painted Stones |
| `shy child friendship picture book` | The Painted Stones |
| `seaside village children's story` | The Painted Stones |
| `welcoming new neighbors book` | The Painted Stones |

## 2. CONFLICTS (resolved here before any packet ships)

### C1 — Category **Literary Fiction**: The Slow Word vs Ultramarine (dispute)

Both packets claim a Literary Fiction browse node as their second category
(Slow Word: "Literary Fiction"; Ultramarine: "Literature & Fiction →
Literary Fiction"). Two catalog titles occupying the same second node
compete with each other for the same also-boughts and category ranking
instead of covering two shelves.

**Proposed resolution:** **The Slow Word keeps Literary Fiction** — it is
that book's only non-SF node, so losing it would leave the title entirely
inside genre-SF browse, which its register doesn't fit. **Ultramarine swaps
its second category** to another Literature & Fiction node that matches a
widow-grief Delft novel: proposed **Literature & Fiction → Women's Fiction →
Domestic Life** (a widowed dyer's-daughter rebuilding a household and a
craft after the 1654 Thunderclap is squarely domestic-life fiction; the
Chevalier/Burton readership browses there too). Fallback alternative:
Literature & Fiction → Genre Fiction → **Family Saga** (weaker fit — the
book spans one household, not generations). Ultramarine keeps Historical
Fiction as its first node unchanged.

⚑ OWNER — this changes a shipped packet (`vetting/ultramarine.md` §6, landed
in PR #98). Packet NOT edited this slice; the swap is applied to the packet
(and this map's ownership row) only on owner approval, naturally bundled
with the pending ⚑ OWNER title pick from the same packet.

### C2 — "widow" keyword stem: Weigh House vs Ultramarine (watched adjacency, KEEP BOTH)

- The Weigh House: `widow investigates husband's death` — **crime buyer
  intent** (a reader searching this wants a mystery/procedural).
- Ultramarine: `widow grief literary fiction` — **literary buyer intent**
  (a reader searching this wants interior grief fiction).

The shared stem is superficial; the full phrases target disjoint intents and
would not surface in each other's result pages. **Resolution: KEEP BOTH.**
Recorded as a **watched adjacency**, not a dispute — revisit only if live
search results ever show the two listings landing on the same results page.
No packet change; no owner action.

### C3 — Netherlands/Dutch cluster: genre split as the ownership rule

Both Dutch-set titles draw on Netherlands phrases. The split that holds
today, recorded as the standing rule:

- **The Weigh House owns modern-Netherlands crime phrases** (`Amsterdam
  crime novel`, `Dutch police procedural`, `canal murder Netherlands`).
- **Ultramarine owns Golden-Age historical phrases** (`Dutch Golden Age
  novel`, `Delft 1654 historical fiction`, `Vermeer era Netherlands story`).

**Ownership rule:** Netherlands-flavored phrases are allocated by GENRE ERA
— contemporary-crime register → Weigh House; 17th-century-historical
register → Ultramarine. Any future Dutch-set title must pick phrases outside
both registers or negotiate a row here first. No conflict today; rule
recorded to prevent one.

## 3. Name-level reservations — unvetted titles (niche only, NO keyword drafting)

Reservations block other catalog titles from squatting a niche; actual
phrases are drafted only by that title's own vetting packet (CHECKLIST §6),
checked against this map at that time.

| Title (plan §7 name) | Reserved niche (name level only) | Notes |
|---|---|---|
| Lull | Quiet/literary novella — stillness, small-town hush | Bare word unsearchable; subtitle *"A Novella"* already planned (plan §7). |
| The Last Good Frequency | Post-collapse / analog-nostalgia radio DRAMA — **not** first-contact/alien-signal | **Must NOT reuse The Slow Word's radio/signal/first-contact phrases** — Slow Word owns `radio telescope alien signal story` and `first contact novella`. Reserve the human/apocalyptic radio angle instead (e.g. last-broadcast, ham-radio survival register). |
| The Undertow | Coastal/psychological suspense | Very strong title collision (plan §7) — rename/subtitle first; niche reserved regardless of final name. |
| Hollowtide | Seasonal/folk dark fantasy | Strong collision with an active fantasy series (plan §7); genre-signalling subtitle planned. |
| The Lantern Door | Kids bedtime / magical-door picture book | Kids cluster rule: Painted Stones owns picture-book-mystery + making-friends phrases; Lantern Door reserves the bedtime/door niche. |
| Tummel | Scottish river / journey fiction (tier pending owner illustration call) | One letter from *Tumble* (autocorrect drift, plan §7). |
| Dormouse / *"Pippa and the Tear in the Night"* | Kids night-comfort / fears-at-bedtime niche | Publish under the alt title (plan §7). Distinct from Lantern Door's bedtime/door: comfort-from-fear vs door-adventure. |
| Comet Biscuit (Book 1) | Kids space-adventure series niche | Kids cluster rule: space-adventure belongs to Comet Biscuit + Star Pirates, NOT to Painted Stones' mystery/friendship phrases. Series tag per cover (plan §7). |
| Comet Biscuit (Book 2) | Kids space-adventure series niche (shared with Book 1) | Series shares the niche; per-book keywords differentiate at vetting time. |
| Comet Biscuit (Book 3) | Kids space-adventure series niche (shared with Book 1) | Same as Book 2. |
| Bram the Yak Cannot Whisper | Kids animal-humor / loud-animal read-aloud niche | Best-differentiated title in the catalog (plan §7: collision None). |
| Star Pirates | Kids/YA space-pirate adventure niche | Shares the space shelf with Comet Biscuit — pirate-flavored phrases vs Comet Biscuit's cozy-space; split finalized when the second of the two is vetted. Avoid alt title *The Wrong Way Down* (plan §7). |

---

*Consult at CHECKLIST §6 time; add your rows in the same PR as your packet;
resolve any collision here before the §7 owner gate. First claim merged to
main wins.*
