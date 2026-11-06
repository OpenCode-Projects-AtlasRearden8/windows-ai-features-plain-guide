# Chapter 3 · AI in the Photos App

*Time: about 15 minutes · Difficulty: easy*

Your photos already live in the **Photos** app — the one that opens when you tap a
picture file. What a lot of people don't know is that the *Edit* button hides one
of the friendliest set of AI tools Microsoft ships: remove a whole background,
erase a photobomber, restyle a picture, or clean up an old scanned snapshot — all
in a couple of clicks, all right-click-and-undo-able.

This chapter is the desktop / laptop side of things. (Our *AI on Your Phone* guide
covers doing the same magic from your phone's gallery.)

## 3.1 · Open the app the boring-but-reliable way

**Step 1.** Click **Start** and type `Photos`, then press **Enter**. (Or double-click
any photo in File Explorer — Explorer opens it in Photos by default.)

**Step 2.** Click any photo in your library (thumbnails scroll down the middle of
the window), then click the **pencil-ish icon that says "Edit"** — top center of the
photo view, or right-click the image and pick **Edit**.

> **What you'll see:** the photo moves center-screen and a toolbar appears along the
> top or the left edge with labels like **Crop, Adjustments, Filters, Background,
> Restyle** (older versions: a row of buttons along the bottom, same names). Every
> tool described below exists somewhere in that Edit view — just look for the
> matching name.

**Good to know:** If Windows offers to open your photos with something else, that
was a one-time dialog from somebody double-clicking — go **Start** > `Photos` >
right-click the app tile > **Pin to taskbar** once, and this stops being an issue
forever.

## 3.2 · Remove the background (the wow-effect tool)

This is the one that makes people gasp: your photo, with the background
gone in one click, saved as a new image with transparency ready for a card, slide,
or Christmas letter.

**Step 1.** With your photo open in Edit view, click **Background** in the toolbar.

**Step 2.** A button appears that says **Remove background**. Click it. A few
seconds… done: your subject stays, most of the rest of the picture becomes a grey
checkered pattern (that's the universal symbol for "now transparent").

**Step 3.** Refine if the cutout is imperfect: two small tools appear —
**"Add"** (brush over areas that should have stayed) and **"Remove"** (brush over
areas that should have gone). Drag the mouse over the picture to paint; release,
and it re-cuts. Also useful: a small **brush size** slider for delicate work.

**Step 4.** Click **Apply** or **Next** (bottom-right), then **Save** or
**"Save a copy"** in the corner menu. **Always save a copy**, not overwrite,
as with everything in this book — original photos are sacred.

> **What you'll see:** Windows prompts nothing else; the new file lands in your
> Pictures folder (or the same folder the original came from), usually named
> something like *"IMG_1001 - Copy"*. If you don't see the checkerboard pattern,
> look for a **"Download quality"** or format row when saving: choose **PNG**,
> which is the format that keeps transparency.

**Good to know:** On most PCs, background removal is fully free and runs on the
device. On some feature sets Microsoft marks it as a *Premium* item (a small
badge appears) that wants a **Microsoft 365** subscription for higher-resolution
saving — but the low-resolution version stays free on almost every machine. If you
get a "sign in" prompt, sign in with your Microsoft account and the free version
continues without a purchase.

## 3.3 · Erase a photobomber ("Remove objects")

**Step 1.** In Edit view, find the row of tools and click **Adjustments** or scroll
the toolbar until you see a tool named **"Remove objects"**, **Erase**, or
**"Magic Eraser"** (names vary by year; it's always an eraser-ish icon).

**Step 2.** A brush appears with a **size** slider. Drag across the unwanted object
— the stranger in the background, a power line, your ex (we don't judge).

**Step 3.** Let go, wait a breath, and the app politely fills the hole using the
scene around it. Wrong result? **Undo** (top-left, the curved arrow, or Ctrl + Z)
and brush differently — smaller, tighter strokes give better results than one big
swoop.

> **What you'll see:** a light blue wash over the area you brushed, then the area
> smoothly redraws — like watching a sky repair its own clouds. There are no
> progress bars: small images finish in a few seconds.

**Honest note:** this is AI inpainting, and it does not always win. Complex
backgrounds (sidewalks with texture, water, crowd scenes) can leave smudges. When
it fails, crop wider instead. Chapter 8's troubleshooting includes the "smudge" fix.

## 3.4 · Restyle Image (Copilot+ PCs and newer Photos versions)

Some versions of Photos include a **Restyle** tool with dozens of art styles —
watercolor, comic, oil pastel, that kind of thing — that repaint your photo in the
style you pick. Where it's available:

**Step 1.** In Edit view, click **Restyle** (a sparkle or palette icon).

**Step 2.** A short horizontal row of style thumbnails scrolls under your photo.
Click one to see it preview on the photo.

**Step 3.** Adjust the **intensity** slider if offered (how heavily the style
applies), then **Apply**, then **Save a copy** as before.

> **What you'll see:** the photo re-renders in 2–10 seconds; several styles queue
> instantly, a couple take noticeably longer the first time (they download a small
> model, which is a one-time few-megabytes affair over your internet).

**Good to know:** Restyle needs a modern machine (a Neural Processing Unit, NPU —
the "Copilot+ PC" class, or a decent graphics card) and the current Photos version
from the Microsoft Store. If you see it, use it; if you don't, background and erase
still work on most PCs from the last several years.

## 3.5 · One-tap cleanups that deserve a shout

Two tools that don't say "AI" but are the same tech underneath, and take ten seconds:

- **Enhance** (wand icon in Adjustments): one click auto-fixes light, contrast, and
  color. Two clicks if you use it twice on the same photo — the second click
  usually overshoots, as with everything with the word "auto."
- **Increase resolution** / **"Upscale"** (in Adjustments, modern versions):
  doubles a small photo's size with AI smoothing. Genuine life-saver for old
  screenshots and tiny saved-from-web pictures you want in a family newsletter.

## 3.6 · Copy text out of a picture (that's Snipping)

This is the feature people mean when they say *"photos had an AI thing that read
the text in the image."* Text *copying* lives in the **Snipping Tool**, not Photos:

**Step 1.** Press **Windows key + Shift + S** (or **Windows key + PrtSc** on some
setups), and drag a rectangle over whatever is on your screen that contains text.

**Step 2.** A small notification pops up in the lower right saying snip saved.
Click it (or open **Start** > type `Snipping Tool` > **Enter**, and open the latest
snip).

**Step 3.** With the snip open, click the **Text actions** button in the toolbar —
the tool highlights every bit of text it finds, and offers **Copy all text** (and a
redact button that black-boxes anything you picked). Click **Copy all text**, then
paste anywhere with **Ctrl + V**.

> **What you'll see:** a subtle yellow-ish highlight appears over detected text
> lines while the Text actions panel is open. One click and it's in your clipboard
> — great for receipts, code from tutorial videos, and phone numbers on screenshots.

That's the whole Photos / snips feature tour. It is genuinely more approachable than
online tools because they run on your PC, save to your PC, and don't dump your
vacation photos to a third-party "free upload" website. It's the kind of tool
that's safe to hand your aunt at Thanksgiving — and in this guide's humble opinion,
that's the highest bar Microsoft's photo tools ever get to clear.
