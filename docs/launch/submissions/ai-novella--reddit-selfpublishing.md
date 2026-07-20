# ai-novella cluster → Reddit submission, r/selfpublishing (paste-ready)

> **Status:** `reference`

- **Suggested subreddit:** **r/selfpublishing** — indie authors shipping their own books; tolerant of process/method posts, including honest AI-assisted-workflow discussion. This is the article's strongest single fit.
- **Where to click:** https://www.reddit.com/r/selfpublishing/submit
- **CTA reminder:** value-first. The teaching IS the post; the single soft product line sits at the very end. No links in the body. Replace `⟨owner: …⟩` before posting, or drop that last line entirely if the sub's rules are strict on self-promo.

**How to post:** open the submit link, choose a **Text** post, paste the **Title**, then paste the **Body** into the text field (Reddit renders Markdown).

**Title:**

```
How to run an AI-assisted novella production line without shipping slop — 7 failure modes and the fix for each
```

**Body:**

````markdown
AI assistants are spectacular at *starting* a novel and terrible at *finishing* one. Ask for chapter one and you get two thousand fluent, atmospheric words in seconds. Ask for the book and you get the graveyard: the middle drifts, the tone wanders, a character's eyes change color, and around chapter four the project quietly becomes a new project. The reflex is to blame prose quality and chase a better model or a cleverer prompt. That's the wrong layer. What separates a finished, publishable manuscript from a pile of promising fragments isn't sentence-level talent — the model already has that. It's **production structure**: something that declares what "finished" means, holds continuity across sessions, survives a crashed run, and refuses to call a draft publishable until it actually is.

"Slop" is what you ship when that structure is missing — not bad sentences, *unowned* ones: filler nobody decided to write, continuity nobody checked, a length nobody targeted, a blurb promise the book never keeps. Seven failure modes that produce slop while every individual paragraph still *reads* fine.

**1. Nothing declares when the book is finished.** You start with a vibe ("a cozy mystery novella") and no declared length, so the AI optimizes for the only thing it can see: the next good paragraph. Chapters come out 400 words then 3,000, and "done" becomes a feeling you stop having. *Fix:* declare a **length band up front** as a spec, not a wish — a target word range and chapter count chosen before you draft (a workable default is ~15,000–16,000 words across 12 chapters, but the number matters less than *having* one). Check it mechanically with `wc -w` per chapter so drift shows up as a number the same session it happens.

**2. There's no structure pass, so the middle wanders.** Hand the AI "write chapter five" with only the story-so-far and no brief for what chapter five must *accomplish*, and you get a locally excellent scene that does no structural work. Enough of those and you have a middle that's pleasant to read and going nowhere. *Fix:* do a **structure pass before the prose pass** — one line per chapter (the job it does, the promise it advances, what changes by its end), and draft each chapter *to its brief*, not to "continue."

**3. Editing means infinite rewrites instead of one aimed repair pass.** The draft is uneven so you "polish": re-prompt a scene, get a *different* scene, re-prompt forever. Each full regenerate is a new roll of the dice that fixes one thing and breaks another, re-introducing the drift your earlier passes removed. *Fix:* replace open-ended rewriting with **one aimed repair pass** against a written list of *named* defects (this promise is unpaid, this scene misses its brief, this name is inconsistent). Edit *at* a list, never *toward* a feeling — a bounded pass terminates; "make it better" doesn't.

**4. Nothing mechanically checks the book keeps its promises.** Your blurb promises a slow-burn romance, a locked-room reveal, and a wintry coastal town; the draft delivers the romance, forgets the locked-room mechanic, and sets half the book in a city you never mentioned. A human reread is the wrong tool — you pattern-match to your *intention*, not the page. *Fix:* build a **promise manifest** before you draft — two grep-able lists extracted from your own blurb: phrases/beats that MUST appear, and register fences that must appear zero times. Check them with a literal search, not a reread. A `grep` has no memory of what you meant.

**5. Continuity drifts because the canon lives only in the last session.** The sister's name, the rule that magic costs memory, the hook planted in chapter two to pay off in chapter ten — all live in scrollback. Each new session remembers some and invents the rest, and continuity quietly rots. A model's context window is a lossy, sliding window that drops or confabulates the older facts first, and fluent-wrong is far harder to catch than obviously broken. *Fix:* keep a **series bible — a CANON file — outside the chat** (laws quoted byte-exact, cast + fixed constraints, every open hook with the coordinates where you planted it), feed the relevant slice into each session, and update it the same sitting a fact is established.

**6. A crashed drafting session takes the work down with it.** A long run dies mid-flight — tab closes, tool crashes, session times out — and if your state lived in that session you've lost not just words but *position*. The usual response is to redo the chapter from memory, which re-introduces drift; enough of these and the project dies of attrition. *Fix:* make state **recoverable by design and recovery forward-only** — keep the length band, briefs, CANON file, a short decisions record, and each finished chapter committed to files (version control is ideal) outside any single session, and resume *forward* from the last committed state against the brief.

**7. You ship "a draft exists" as if it meant "this is publishable."** The manuscript is finished, so you publish — but *written* and *publishable* are different states, and the gap is where the avoidable one-star reviews live (an untitled or title-colliding book, a price from thin air, a blurb that doesn't match the text, packaging that fights the genre). *Fix:* put an explicit **publish gate** between *written* and *listed* — a fixed vetting checklist you run every time (title + collision scan, intended market, a defensible price band, packaging, listing copy that matches the manuscript, a final click checklist) and you don't list until every box is checked.

**The pattern under all seven:** treating a model's fluency as if it were production discipline. The model will produce the next good paragraph forever — with no target length, no chapter brief, no memory of your canon, no record of your promises, no gate before the listing — because producing the next good paragraph is the one thing it does unconditionally. Slop is what that fluency turns into when nothing outside the model owns the *whole*. You don't fix it with a better prompt; the structure around the prompt is the missing piece.

Cheapest place to start today: before your next drafting session, write down one length band and one line per chapter, and draft the next chapter *to its brief*. That ten-minute structure pass catches the wandering middle before you've written a word of it.

---

*(One line of disclosure: I wrote this method up as a small, tool-agnostic kit — no software, just the method + blank-slate templates. Entirely optional; you can build every discipline above by hand from what's written here. ⟨owner: your Gumroad link⟩)*
````
