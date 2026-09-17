---
layout: default
title: Privacy Policy — Diary BFF
---

# Privacy Policy — Diary BFF

_Last updated: 2026-09-17_

Diary BFF ("the app", "we", "us") is a private journal that writes back. This
policy explains what the app stores, where it goes, and what you can do about it.

This is plain language, not legal advice.

## Summary

- What you write, say, and attach is stored in your own isolated space in our
  backend. Other people using the app cannot reach it.
- The app shows **no ads**, and we do **not** sell your data or use it for
  advertising or tracking. There is no third-party analytics or crash-reporting
  SDK in the app.
- Some features send the text of an entry to an AI provider. **Nothing is sent
  to an AI provider until you say so** — the app asks once, in plain words, and
  keeps working normally if you say no.
- You can export everything at any time, and you can delete it.

## Account and identity

On first launch the app creates an **anonymous account**, so your writing is
isolated from other people's. There is no sign-up form: the app does not ask you
to type a name, an email address, or a phone number.

**If you choose "Keep it when you change phones" (Sign in with Apple)**, Apple
passes your name and email address to our authentication provider so the account
can be recognised on your next phone. The app itself never reads, stores, or
shows either one — but they are held by the authentication service, so they are
disclosed here and on the App Store privacy card.

**Your passcode** (the 4 digits that unlock the app) is stored **only on your
device**, as a salted hash. It is never sent to us.

> The passcode protects the app on a phone that is already unlocked. It is not
> device encryption, and it does not stop us — see "What we can see" below.

## What we store

In our backend (**Supabase**, US East `us-east-1`):

| Data | Why |
|---|---|
| Journal entry text | To show you your journal |
| Voice recordings and their transcripts | So you can play back the original and read the words in the entry |
| Photos you attach | To show them in your journal |
| Replies from the AI you asked for | They are written into the entry itself, so it reads as one piece |
| What the app remembers about you (short notes it extracts from your entries) | So the reply can refer to what you said before |
| Whether an entry has been talked about, and timestamps | Journal display and feature logic |
| Your onboarding answers (why you came, the name and character you gave the companion) | To adjust the tone of replies |
| AI-usage counts | To apply free and subscription limits |
| Feature-usage events — which screens and actions, never content | To find where the app confuses people |
| Subscription status | To unlock paid features (via RevenueCat) |

That list is meant to be complete. If it stops being complete, this page is wrong
and we want to know.

## What we can see

We are a small operation running a database. **Staff with backend access could
read what is stored**, the same as with any hosted service. We do not do this as
a matter of course, and we do not use your writing for anything except giving you
the features you asked for.

We are telling you this because the app's whole promise is privacy, and a promise
that overstates itself is worth less than one that doesn't.

Two specific things worth knowing:

- **Entries are not end-to-end encrypted.** They are encrypted in transit and at
  rest by the hosting provider, which protects against interception and against
  someone walking off with a disk — not against us.
- **Media files (voice and photos) currently live in a storage bucket that serves
  files to anyone holding the file's address.** The app never publishes those
  addresses and signs a short-lived link each time it plays something back, but
  the protection is the address being unknown rather than a permission check.
  We are changing this; until we do, please treat an exported backup as
  something that contains playable recordings.

## Third parties that process your content

The app sends **only the content needed for that feature**, and only after you
have agreed:

- **Anthropic (Claude API)** — when you ask for a reply or a Sunday letter, the
  relevant entry (and, for context, recent entries and the notes the app keeps
  about you) is sent to Anthropic to generate the response. Per Anthropic's
  commercial terms, your content is **not used to train models**. Anthropic
  deletes it from their systems within 30 days.
- **Groq (Whisper API)** — speech-to-text runs **on your phone** by default. Only
  if you turn on "More accurate transcription" in Settings does the audio leave
  the phone and go to Groq. Groq is configured for zero data retention.
- **Supabase** — our database, file storage, and serverless functions.
- **RevenueCat** — subscription purchases and entitlement status. It receives an
  app-specific user ID and purchase events, not your journal.
- **Apple** — payments. We never see your card details.

**Before the first time anything goes to an AI provider, the app stops and asks.**
It tells you what gets sent, who it goes to, and that saying no leaves the journal
fully usable. If you say no, no entry text ever leaves our backend — except that
recording a voice note with "More accurate transcription" on still sends that
audio to Groq, because that is how it becomes words.

**Usage analytics are ours, not a third party's.** Those events live in our own
Supabase alongside your other data. An event records the action, never the
writing — "an entry was saved, it came from voice, it was 340 characters, it had
a photo", not one word of what you wrote. The app enforces this with a
whitelist: anything that is not a count, a duration, a flag, or a short
predefined label is dropped before it is sent. Deleting your account deletes
these events too.

## Free and paid

Writing is free, always — typing, voice, photos, export, and the passcode lock
never cost anything.

What a subscription buys is **more replies** and the full Sunday letter. After
the trial ends, the free tier still gets a few replies each day, and the Sunday
letter arrives with its first part readable and the rest held back. These are
product settings we may adjust; the app shows you where you stand rather than
relying on this page to be current.

## Notifications

**This version of the app does not send notifications and does not ask for
notification permission.** If that changes in a later version, this section will
say what they are and when they are asked for. Notification text, if it ever
ships, will never contain anything you wrote — it would be shown on your lock
screen.

## Permissions

- **Microphone** — asked for the first time you record.
- **Photo library** — the app uses the system photo picker, which hands over only
  the pictures you select. It does not ask for access to your whole library.

Both can be revoked in iOS Settings.

## What we do not do

- No advertising, no ad networks, no advertising identifiers.
- No selling or renting of personal data.
- No cross-app or cross-site tracking.
- No third-party analytics SDK, no crash-reporting SDK.

## Keeping and deleting

- Your data stays until you delete it.
- **One night:** press and hold it in the journal and confirm. Its text, its
  replies, and any voice or photo files attached to it are removed.
- **A recording, keeping the words:** press and hold a 🎤 passage inside an entry
  and choose to keep only the text. The audio file is deleted.
- **Everything:** Settings → Delete account. This removes your entries, replies,
  the notes the app kept about you, your onboarding answers, usage counts, the
  subscription record, every voice and photo file, and the account itself. It
  cannot be undone. If a file cannot be removed at that moment its path is
  queued and removed by a cleanup job, rather than being left behind quietly.
- Deleting your account does **not** cancel an App Store subscription. The app
  says so before you confirm and links you to iOS Settings.
- Backups you exported to your own device are yours to manage; we cannot reach
  them — and we cannot delete them for you either.
- Providers may keep transient copies (a request in transit, short-term logs)
  under their own policies.

## Your choices

- **Export:** Settings → Export & Import. A full copy, optionally
  password-encrypted, at any time.
- **Use it without AI:** the journal works without ever asking for a reply. Say
  no on the consent screen, or turn the companion off in Settings.
- **Keep voice on the phone:** leave "More accurate transcription" off. Then
  speech-to-text runs on the device and the audio does not leave it.

## Children

The app is not directed to children, and is not intended for anyone under 18.
Its App Store age rating is set accordingly: versions of iOS that have the newer
rating bands show it as **18+**, and older versions, which do not have that band,
show it as **17+**.

## Changes

We will update this page and the "last updated" date if this policy changes
materially.

## Contact

hello@diarybff.app
