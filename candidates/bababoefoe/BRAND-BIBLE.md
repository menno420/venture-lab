# Bababoefoe — Brand Bible

> **Status:** `reference`
>
> The universe, naming grammar, and design rules for the Bababoefoe plush family.
> Cozy · collectible · kid-safe. This is the usable source of truth for tone and
> naming; the machine-readable edition list lives in `site/editions.json`.

## What a Bababoefoe is

A **Bababoefoe** (say it *bah-bah-BOO-foo*) is a small, round, ultra-fluffy plush
critter — a chubby teardrop body a bit like a friendly hamster, with tiny ears,
big shiny black eyes, and stubby little hands. They are palm-sized, huggable, and
built to be collected. Every Bababoefoe is the *same soul* wearing a *different
story*: change the colorway and the costume and you get a new **edition**, but the
warmth underneath is always the same.

They are made to sit in a row. They are made to hold hands.

## Where they come from (the fiction)

Bababoefoes come from the **Boefoe Burrow**, a warm hollow under an old hill where
the fluff grows in every color. When a Bababoefoe is ready to go out into the
world, it packs one tiny keepsake into its **hidden pocket**, learns one small
story to carry, and joins hands with the next one leaving the burrow. That is why
you rarely find just one — they travel in a **boefoe-chain**, hand in hand,
looking after each other.

Every edition remembers a different adventure. That is why each has **its own
origin story** — and its own QR tag, so the story travels with the plush.

## The three physical features → the fiction

The product's real, manufacturable features each carry a piece of the story. This
mapping is the heart of the brand — keep it consistent everywhere.

| Feature | In the product | In the story |
|---|---|---|
| **Magnetic hands** | Small magnets let two Bababoefoes clasp hands and hold in a chain | They form a **boefoe-chain** — nobody adventures alone; holding hands is how they stay brave |
| **Hidden pocket** | A small sewn pocket, tucked where you least expect it | Each carries **one tiny keepsake** that matches its story — a memory it refuses to leave behind |
| **QR tag** | A printed tag with a QR code | Scanning it **opens that edition's origin story** — the plush tells you where it's been |

> Compliance note (not fiction): magnets in children's products are heavily
> regulated. The "magnetic hands" feature is a real safety decision, not just a
> story beat — see `MAKE-IT-REAL-PLAN.md` → SAFETY/COMPLIANCE.

## Naming grammar for editions

The rule is simple and always the same:

> **`<Costume/Theme> Bababoefoe`** — costume first, then the family name.

- Pirate → **Pirate Bababoefoe**
- Chef → **Chef Bababoefoe**
- Police officer → **Police Bababoefoe** (kid-friendly short form of "Police-Officer Bababoefoe")
- Santa → **Santa Bababoefoe**
- Witch → **Witch Bababoefoe**

Rules of the grammar:
- **One theme per edition.** No stacking ("Pirate Chef Bababoefoe" is not a thing).
- **Colorway is a variant, not a new name.** A teal Pirate and an orange Pirate are
  both "Pirate Bababoefoe"; the colorway is recorded in the registry, not the name.
- **Slugs** are lowercase, hyphenated, stable, and never reused:
  `pirate-bababoefoe`, `chef-bababoefoe`, `police-bababoefoe`, `santa-bababoefoe`,
  `witch-bababoefoe`. The slug is what the QR tag and the story file share — once
  printed on a tag it must never change.
- **Seasonal editions** (Santa, Witch) are named the same way; "seasonal" is a tag
  in the registry, not part of the name.

## Colorways

The fluff comes in these core colorways. Any edition can, in principle, appear in
any colorway; specific pairings are decided per drop and recorded in the registry.

teal · orange · pink · green · blue · yellow · purple · brown

## Tone of voice

- **Cozy first.** Soft, warm, unhurried. Read-aloud quality — a parent should be
  able to read any story at bedtime.
- **Kid-safe always.** No real peril, no scary endings, no violence. A pirate
  Bababoefoe hunts *buried snacks*, not treasure to fight over. A police
  Bababoefoe helps lost ducklings, never chases villains.
- **Gently collectible.** It's okay to love that there are more to find, but the
  brand never pressures. The joy is the chain growing longer, not "gotta catch 'em all."
- **Small and specific.** One keepsake, one small kindness, one little adventure
  per story. Charm lives in the tiny concrete detail, not in scale.

## Product line (concept)

Trendy collectible plushies across price points, all sharing the family + registry:
- **Keychains** — the smallest, most giftable, magnet-free by default (see compliance).
- **Small stuffed animals for kids** — the core huggable size.
- **Pillows** — oversized comfort editions.
- **Collector editions** — costumed, numbered, with the full pocket + tag + (where
  legal and age-gated) magnetic hands.

Every edition, at every size, points its QR at the same per-edition story page. The
registry (`site/editions.json`) is the single source of truth so a physical tag can
be printed later without guessing a URL.
