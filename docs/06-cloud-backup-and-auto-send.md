# Chapter 6 · Cloud Backup & "Auto-Send" Settings

*Time: about 15 minutes · Difficulty: medium*

"Auto-send to cloud" means any feature that quietly moves your stuff — files,
photos, passwords, bookmarks, your desktop — **from your computer to Microsoft's
cloud**, usually OneDrive, without asking every time. Sometimes that's wonderful
(photos survive a spilled coffee). Sometimes it's a surprise you'd rather not have
(a laptop syncing your whole Desktop to a shared work account). The settings that
control this live in a couple of places, they're friendly enough to click through,
and this chapter walks you to every one of them.

Same rule as always in this guide: **no registry edits**. Everything is clicks.

## 6.1 · The big picture: who syncs what, where

Windows 11 can sync four families of things, each with its own switch:

1. **Files and folders** — Documents, Desktop, Pictures, via OneDrive.
2. **Windows settings** — wallpaper, passwords(!), dark mode, and preferences, via
   "Windows Backup".
3. **App data & app lists** — via "Windows Backup" on newer builds too.
4. **Microsoft account web bits** — your *outlook.com* email, *Office* documents,
   and browser tabs, most of which have their own sync toggles.

None are mandatory. Turning them all off is a perfectly supported configuration
("I keep my files local, like a normal person in 2005"), and Chapter 7 gives you
that version of the world as an at-a-glance checklist.

## 6.2 · Windows Backup: the settings-sync switchboard

**Step 1.** Press **Windows key + I** to open **Settings**.

**Step 2.** Click **Accounts** in the left rail (older builds: top right corner).

**Step 3.** Click **Windows backup** (sometimes shown as a card near the top).

> **What you'll see:** the page shows your account at the top and a list of backup
> rows, each a toggle: **"Remember my apps"**, **"Remember my preferences"**,
> **"Windows Spotlight"**, and on some builds a **"Sync your settings"** section with
> sub-rows like *Passwords*, *Language preferences*, *Other Windows settings*
> — plus per-item toggles. Several may already be **on** — including, notably,
> **Passwords**.

**Step 4.** Decide each row:

- **Remember my apps** — restores the Microsoft Store list of apps to new machines.
  On = convenient if you re-setup PCs a lot; off = clutter-free.
- **Remember my preferences** — this is the "sync settings" master. Off means
  changes to wallpaper, theme, and (if separately toggled on) saved passwords stop
  traveling between computers.
- **"Remember my preferences" > Passwords** (individual row) — this is the one most
  people feel *some* kind of a way about: your Wi-Fi and web passwords synced to
  your Microsoft account. If you want passwords to live only on your hardware,
  toggle **off**. (Browsers like Chrome/Firefox have their own, separate sync
  settings — those are controlled in the browser's own menus, not here.)

**Good to know:** Turning these settings off does not delete cloud copies already
made. Chapter 7's checklist includes how to remove existing cloud-backed data.
It's fully reversible and doesn't affect your installed apps whatsoever.

## 6.3 · OneDrive folder backup ("auto-send" for your files)

This is the feature most people mean when they say *"my files keep showing up in
OneDrive."* Specifically: OneDrive's **known folder move**, which (on many new
computers, sometimes even before your first coffee) redirect your Desktop,
Documents, and Pictures folders into OneDrive-synced folders.

**Step 1.** Look at the taskbar right side. Find the **OneDrive cloud icon** (a
small cloud near the clock; click the tiny chevron (**^**) show-hidden-icons arrow if you
don't see it directly). Click it once.

> **What you'll see:** a small OneDrive status panel opens with rows about your
> sync status, a **gear icon** near the top right of that panel, and often a
> **"Get the OneDrive app"** or settings row.

**Step 2.** Click the **gear icon** in that panel, then choose **Settings** — this
opens the classic OneDrive Settings window with tabs across the top.

**Step 3.** Click the **Sync and backup** tab, then click **Manage backup**.

> **What you'll see:** a dialog with a visual: three folder tiles — **Desktop**,
> **Documents**, **Pictures** — each with a toggle under it describing whether
> backup is **on** or **off** (on = files in those folders are copied to OneDrive
> in the cloud).

**Step 4.** Turn off any tiles you don't want. If asked to confirm, click
**"Keep files on this device"** or **"Stop backup"** — the option you pick matters:
choose the keep-on-this-device wording so files stay in your real local folders
instead of staying only in cloud-only form.

> **What you'll see:** after stopping backup, Windows may show
> *C:\Users\YourName\Documents* returning to a plain local folder, and OneDrive
> shortcut-lookalike marks disappear. Your files did not vanish; they just stopped
> being cloud-copied. **If a file appears missing**, check
> `C:\Users\YourName\OneDrive\Documents` — files made during the backup era live
> there; drag them back into the local folder and they'll stay put.

**Step 5.** (Optional, if you're clearly out-of-bounds) un-tie OneDrive entirely:
in that same Settings window, **Account tab** > **Unlink this PC**. This stops
OneDrive syncing completely (the cloud app itself remains installed and harmless;
you can even uninstall it in **Settings** > **Apps** > **Installed apps** >
**OneDrive** > three-dots > **Uninstall** if you truly want no part of it).

## 6.4 · The Photos app sending photos to the cloud

People get surprised anew by the Photos app, which in newer versions can show your
OneDrive photos alongside local ones. That follows your OneDrive settings (as
Section 6.3), but there is also a Photos-level row:

**Step 1.** Open **Photos** (Start > `Photos` > **Enter**).

**Step 2.** Click the **gear icon** in the top-left corner of the Photos window.

> **What you'll see:** the settings page includes **"Show an account cloud gallery"**
> (or similar wording about OneDrive). Toggle it **off** if you don't want Photos to
> display or pull from your cloud gallery. Other rows (like *Import* settings)
> don't send anything anywhere.

## 6.5 · The Microsoft 365 / Office auto-save

(This is for people who use Word, Excel, or PowerPoint.) Documents saved to
OneDrive come with an **AutoSave** toggle turned on by default (top-left of Word's
window, labeled "AutoSave"). It's per-document, but Word also *remembers* the
choice for future OneDrive files. If you'd rather not have docs live in the cloud by
default:

**Step 1.** Open any Office app > **File** > **Options**.

**Step 2.** In **Options**, click **Save** in the left list and look for a checkbox
like **"Save to Computer by default"**. Check it and click **OK**.

> **What you'll see:** new documents now default to a Browse (Choose a location)
> dialog into your computer's folders instead of OneDrive. Existing OneDrive
> documents keep AutoSave unless you flip the toggle per-file in the title bar.

## 6.6 · A gentle word about "which settings did I sign up for?"

If you set up this PC with a Microsoft account (most people did, because the setup
screen *strongly suggests* it), a fair amount of this chapter's switches were on by default
at setup time. That is not a mistake you made — and Chapter 7 is the single list to
run through two or three times a year: after Windows feature updates, after a new
device, after "a friend borrowed the laptop."

Everything in this chapter can be re-checked in 5 minutes with your morning coffee.
Next: Chapter 7, the checklist you came here for.
