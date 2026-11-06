# Chapter 4 · AI in the Paint App

*Time: about 15 minutes · Difficulty: easy to medium*

Remember Paint? The little program you doodled in, with the bucket fill and the airbrush?
It quietly became one of the most surprising AI apps on Windows 11. The current Paint has:

- **Image Creator** — you type a caption ("a tabby cat wearing reading glasses in a
  garden"), and Paint generates a picture from the caption.
- **Cocreator** — you start drawing *something* rough, and while you draw, the AI
  fills in your style, in real time, as a duet with your sketch.
- **Remover** — erase an object from an image you opened (same idea as Photos' eraser).
- **Layers and transparency** — not AI but long overdue, and now real.

This chapter assumes you opened Paint (Start > type `Paint` > **Enter**). That's it.

> **Good to know before we start:** of all the Windows AI features, Paint's AI is the
> one with the most variety between computers. Which tools you see depends on your
> Windows 11 version, whether your PC is a Copilot+ PC, and which region you're in.
> Everything below is arranged roughly as "most common to least common," and every
> section tells you what to do if the tool isn't there. Treat this chapter like a
> menu, not a prescription.

## 4.1 · Image Creator: describe a picture, get a picture

**Step 1.** Open Paint (Start > `Paint` > **Enter**).

**Step 2.** Look at the top-right corner for a blue button labeled **Image Creator**
— sometimes it only shows a sparkle icon with the word beneath when the window is
narrow. Click it.

**Step 3.** A panel appears on the right with a text box that says something like
**"Describe what you'd like to create."** Also, the first time, a **Sign in**
prompt — sign in with your Microsoft account, same one you use for Copilot.

**Step 4.** Type a description. Be specific and loose:

```
A warm cartoon of an orange tabby nurse cat wearing tiny blue scrubs, giving a thumbs up in a sunny clinic, flat illustration style
```

**Step 5.** Press **Create** (or Enter). Wait a few seconds while a set of images
generates.

> **What you'll see:** a small grid of several thumbnail pictures appears in the
> right panel — usually three or four variations of your idea. Each has a little
> download/plus button; clicking it copies the variant onto your canvas as a new
> layer you can then crop, edit, or combine.

**Step 6.** The image lands on the canvas. From here it's just Paint: crop it with
the selection tool, add text with the **A** tool (a joke caption is basically law
for cat pictures), save with **File > Save**.

**Honest notes:**

- Image Creator looks the same across regions but this **is** a cloud AI feature —
  your caption and the results pass through Microsoft's servers. Captions should
  stay postcard-level private, same Copilot rule as Chapter 1.
- Expect the occasional misunderstanding: it may generate a calm nurse cat when you
  asked for a chaotic one. Just click **Create** again.
- There are content rules (no photorealistic public figures, no violence). When the
  tools refuse something, they say so — no mystery windows about it.

**If there is no Image Creator button:** your Windows/region version hasn't
activated it yet for your account. The Microsoft Paint app updates from the
**Microsoft Store** (Store app > search "Paint" > **Update** if offered). Even after
updating, some regions get it later than others — no registry hacking required or
possible, honestly; often you just wait a bit and check the Store again.

## 4.2 · Cocreator: draw badly, finish beautifully

This is the tool that surprises everyone most: it requires a **Copilot+ PC** (recent
laptops with a Neural Processing Unit). If you have one, this is worth trying even
if you think you can't draw — *especially* if you think you can't draw.

**Step 1.** In Paint, look for the **Cocreator** button in the toolbar
(a sparkle-and-brush icon, near **Image Creator**).

**Step 2.** The first time, accept the on-device model download prompt (a
notification-style dialog mentioning the software being downloaded to your PC — it's
a one-time ~hundred-megabytes process on Wi-Fi) and agree to the rules of use.

**Step 3.** In the panel on the right set **Creativity** using a slider from
**Low** to **High**. Two-way rule of thumb: the more you actually draw, the *lower*
you dial this; the more you want the AI to take over, the *higher*.

**Step 4.** Type a short description of what you're drawing
(`"a lighthouse on a foggy cliff at dusk"`), then pick a color and just… draw shapes
with the pencil. As you sketch, the canvas mostly fills in in real time, keeping
your strokes and adding theirs.

> **What you'll see:** the canvas evolves continuously while you draw: lines you
> make stay, and the AI repaints the rest in a style you can nudge. It feels less
> like a tool and more like drawing next to a friend who is eerily good.

**Step 5.** When you like a version, click **Apply** or **Stop** to freeze it, and
save. **Undo** works on AI fills exactly like everything else.

**Honest notes:** on **low** creativity, results stick close to your sketch (good
for coloring book pages); on **high**, it may go somewhere unexpected — squash and
draw again. And the whole file stays on your machine: Cocreator runs on the device
once downloaded, which is a genuinely nice contrast with image-creator-style
services.

## 4.3 · Remover (erase an object in Paint)

**Step 1.** Open any photo in Paint (**File > Open**, or right-click a photo in
File Explorer > **Open with** > **Paint**).

**Step 2.** Find the **Removal** or **Remover** tool in the Paint toolbar (eraser
with a sparkle).

**Step 3.** Brush over the thing to remove (a sign, a trash bag, a person on a
hiking track), release, wait a beat.

> **What you'll see:** a light mask over the brushed area, the area then re-fills
> and cleans up. The **undo** arrow in the quick access bar (top area) reverses it —
> explore a few tries; each try is a fresh result.

**Step 4.** Click **Save** when you're happy. As always in this book — **save as a
new copy**; your original is precious.

## 4.4 · A full picture of Paint's AI and privacy

Quick recap to decide what's comfortable to you:

- **Image Creator** → runs in cloud. Your description and generated image travel
  through Microsoft's servers. (Low-risk if your descriptions are ordinary.)
- **Cocreator** → downloaded model, runs **on your PC**. Your sketch stays with you.
- **Remover** → runs on-device in current versions on Copilot+ machines; on other
  PCs, may fall back to the cloud and follow the same rules as Image Creator.
- **Save behavior** → everything saves to your own Pictures folder. Paint isn't
  auto-signing your files to OneDrive or anything sneaky.

When you're done making cat scrubs illustrations, close Paint like always. Next
chapter is a big one: Recall, the privacy decisions that come with it, and exactly
which switches you should think hard about before flipping.
