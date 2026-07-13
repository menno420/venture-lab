# Edition-variant matrix — <Book Title>

Planning surface for deriving editions from ONE base manuscript
(guide chapter 3). Rules: every edition derives from the base, never
from another edition; the base is the source of truth for story
canon — an edition adapts presentation, never silently changes canon;
every edition enters the publish gate (guide chapter 4) as its own
product.

**Base manuscript:** `<path>` · **measured:** <`wc -w` count> words ·
**canon:** `CANON.md`

| Edition | Audience / angle | Band / length target | Format | What changes vs base | Gate status |
|---|---|---|---|---|---|
| Novella cut | <e.g. faster paid edition> | <target words> | ebook | <what is cut; what must survive (promise manifest still holds)> | not started / packet parked / queued |
| Serial (N parts) | <episode buyers> | <words/part> | ebook ×N | cold open per part, in-voice "story so far" recap, episode-ending hooks — WRITTEN for serial, not sliced | <...> |
| Translation (<lang>) | <market> | ≈ base | ebook | native re-telling, not literal translation; register re-verified in target language | <...> |
| Large print | <accessibility market> | = base | print spec | an EDITION-SPEC (trim, font, size, leading) — a spec any formatter can execute; text unchanged | <...> |
| <other> | <...> | <...> | <...> | <...> | <...> |

Per-edition folder convention:

```
versions/
  <edition>/
    <text file(s)>
    NOTES.md   <- honest count (command shown), what changed vs base,
                  market position, every money/publish step marked
                  as the human's
```

<!-- Kill-rule note (guide chapter 7): an edition inherits the base
     manuscript's validation-signal state. Deriving editions is cheap
     supply; supply was never the constraint. -->
