# Chapter 8 · If Something Goes Wrong

*Time: as needed · Difficulty: none (this is the "breathe" chapter)*

Nothing in this guide can break your computer. Everything here is toggles,
buttons, and menus — reversible by definition. When something *looks* wrong, it is
almost always one of these eight situations. Find yours, do the calm fix, carry on.

## 8.1 · "I can't find Copilot at all"

**Likely cause:** Windows has been updating Copilot out of the built-in panel and
into a standalone app; your version is somewhere in that transition.

**Fix:** Press **Windows key + C**. If nothing opens, click **Start** and type
`Copilot`. If Start finds nothing, open the **Microsoft Store** (Start > type
`Store` > Enter), search `Microsoft Copilot`, and **Install/Update**. After it
installs, pin it: Start > right-click the Copilot tile > **Pin to taskbar** — and
you'll never hunt for it again.

## 8.2 · "A feature is greyed out / says 'coming later'"

**Likely cause:** Microsoft features roll out gradually — by region, by Windows
version, and by hardware class (Copilot+ PC or not). Nothing you did.

**Fix:** Two honest levers:

1. **Settings > Windows Update > Check for updates**, install what's offered, and
   restart. A surprising share of "missing" features are updates waiting for their
   restart.
2. **Microsoft Store > Library** (bottom left) > **Get updates** — this refreshes
   *app* updates (Photos, Paint, Copilot are apps).

Neither lever fixes everything. Some things simply arrive weeks later than for
other people. This is normal and the guide's step descriptions will still work when
your version arrives.

## 8.3 · "I turned off OneDrive backup and a folder looks empty"

**Almost never an actual loss.** During the OneDrive era your files physically
lived in `C:\Users\YourName\OneDrive\Documents` (or Desktop, Pictures) — and
stopping backup sometimes leaves them there.

**Fix:** Open **File Explorer**, click your name at the top-left (under "Home"), and
open **OneDrive** in that file tree. Find **Documents / Desktop / Pictures** inside
it. Select the files (**Ctrl + A**), then **Cut** (Ctrl + X), navigate to your
*real* Documents folder under "This PC > Documents", and **Paste** (Ctrl + V).
They're home, and they'll stay.

## 8.4 · "Photos erased a thing and left a smudge"

**Likely cause:** inpainting struggles with textured backgrounds (water, sidewalks,
large crowds). The smudge is the ceiling of the tool, not your fault.

**Fixes, in order of ease:**

1. **Undo** (Ctrl + Z) and brush *tighter* — small strokes, several passes.
2. Try the **brush size** slider smaller.
3. If it's hopeless: **Crop** the object out instead — sometimes the real answer.
4. Open the same photo in **Paint** and try its **Remover** tool; different model,
   sometimes different luck.

## 8.5 · "Recall is on and I want it off, now"

Two clicks to stop recording: **Settings** > **Privacy & security** >
**Recall & snapshots** > toggle **Save snapshots** off. Then — because turned off is
not the same as gone — click **Delete all snapshots** on the same page and confirm.
Timeline: gone going forward, gone going backward. Nothing else needed.

## 8.6 · "Copilot gave me a wrong answer with total confidence"

**Fix:** Same move as with any confident human: ask again differently.

- Say **"Double-check that"** or **"What are common mistakes people make on this?"**
- Ask for sources: **"Where does this come from?"** — links will appear below
  (with web search enabled). Click them before trusting anything that matters.
- For anything with stakes — health, taxes, legal, an eBay listing policy — treat
  chat answers as *a starting point to verify*, never as the final word. (Our whole
  series: AI is a helpful assistant, not an authority. Drafts, ideas, and curiosity,
  then check the official page.)

## 8.7 · "A setting I turned off came back after an update"

**Likely cause:** some toggles have been resurrected by Windows feature updates.
Annoying-but-normal.

**Fix:** just re-run **Chapter 7** — that's exactly what the checklist is *for*.
Keep the page bookmarked. Five minutes, everything back to your settings, no
support hotline needed.

## 8.8 · "I'm overwhelmed and this is a lot"

**This is completely fair**, and it's why each chapter ends with an explicit "you
could stop right here" moment. The genuinely useful, minimum-viable privacy setup
(beyond which there are diminishing returns for most people) is just these three:

1. Windows Backup > **Passwords sync off** (Settings > Accounts > Windows backup)
2. OneDrive folder tiles off for anything you want local (Chapter 6.3)
3. Recall off **if you didn't choose it** (Chapter 5.5, first checkbox)

Do those three, close the laptop, eat a real lunch. Everything else in this guide
is optional polish, fun, or curiosity.
