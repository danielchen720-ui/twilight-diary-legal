---
layout: default
title: Privacy Policy — Twilight Diary
---

# Privacy Policy — Twilight Diary

_Last updated: 2026-09-03_

Twilight Diary ("the app", "we", "us") is a private journaling app. This policy
explains what the app stores, where it goes, and your choices.

## Summary

- Your journal entries, emotion tags, and any voice/photo attachments are stored
  in your own isolated space in our backend. Other users cannot see them.
- The app does **not** show ads and does **not** sell your data or use it for
  advertising or tracking.
- Some features send the text of an entry to third-party AI providers to generate
  a response or a weekly summary. This is described below.
- You can export all of your data at any time, and you can delete it.

## What we store

When you use the app, the following is stored in our backend (hosted on
**Supabase**, US East (`us-east-1`)):

| Data | Why |
|---|---|
| Journal entry text | To show you your journal and provide the app's features |
| Emotion tags | Same |
| Voice recordings and transcripts (if you record) | To let you play back the original audio and read the transcript inside the entry |
| AI responses you asked for | They are written into the entry itself, so the entry reads as one piece |
| Photos you attach | To show them in your journal |
| "Chatted with AI" status, timestamps | Journal display and feature logic |
| Onboarding answers (your stated motivation, initial mood) | To adjust the tone of AI responses |
| Daily AI-usage counts | To enforce free/subscription limits |
| Feature-usage events (which screens and actions, never content) | To find where the app confuses people |
| Subscription status | To unlock paid features (via RevenueCat) |

**Account / identity.** On first launch the app creates an anonymous account so
your data is isolated to your device. There is no sign-up: we never ask for your
name, email address, or phone number, and this version offers no third-party
login. Because the account lives on this device, uninstalling the app without
exporting first means the data cannot be recovered — use Settings → Export &
Import before you switch devices.

**Your PIN.** The passcode that unlocks the app is stored **only on your device**
and is never sent to us.

## Third parties that process your content

To provide specific features, the app sends **only the content needed for that
feature** to these processors:

- **Anthropic (Claude API)** — when you use "AI's take" or the weekly recap, the
  text of the relevant entry (and, for context, recent entries) is sent to
  Anthropic to generate the response. See Anthropic's privacy terms.
- **Groq (Whisper API)** — when you record a voice entry and transcribe it, the
  audio is sent to Groq for speech-to-text.
- **Supabase** — our database, file storage, and serverless functions.
- **RevenueCat** — processes subscription purchases and entitlement status
  (receives an app-specific user ID and purchase events, not your journal).

**Usage analytics — ours, not a third party's.** The app records which features
you used, so we can tell where the app is confusing and whether it is worth what
it costs to run. These events are stored in our own Supabase, alongside your other
data — they are **not** sent to any analytics company, and there is no third-party
SDK in the app.

An event records the action, never the writing. For example: "an entry was saved,
its source was voice, it was 340 characters long, it had a photo" — not a single
word of what you wrote, spoke, or were told. The app enforces this with a
whitelist: anything that isn't a count, a duration, a flag, or a short predefined
label is dropped before it is sent. Deleting your account deletes these events too.

There is no crash-reporting SDK.

These providers process the data on our behalf to deliver the feature you
requested. We do not permit them to use your journal content to train models or
for their own purposes, to the extent their terms allow us to configure that.

Payments are handled by **Apple**; we never see your card details.

## What we do NOT do

- No advertising, no ad networks, no ad identifiers.
- No selling or renting of personal data.
- No cross-app or cross-site tracking.

## Data retention and deletion

- Your data stays until you delete it.
- **Delete one entry:** swipe it left in the journal list and confirm. Its text,
  its conversation, and any voice or photo files attached to it are removed.
- **Delete a recording but keep the words:** press and hold a 🎤 passage inside an
  entry and choose to keep only the text. The audio file is deleted permanently.
- **Delete everything:** Settings → Delete account. This removes your entries,
  conversations, emotion tags, onboarding answers, usage counts, subscription
  record, every voice and photo file, and the account itself. It cannot be undone.
  If a file cannot be removed at that moment, its path is queued and deleted by a
  cleanup job — it is never silently left behind.
- Deleting your account does **not** cancel an App Store subscription. The app
  tells you this before you confirm, and links you to iOS Settings to cancel.
- Backups you exported to your own device are yours to manage; we cannot reach
  them.
- Provider-side transient copies (e.g. an AI request in transit or short-term
  logs) are retained per each provider's policy.

## Your choices

- **Export:** Settings → Export & Import → export a full copy (optionally
  password-encrypted) at any time.
- **Don't use AI features:** the journal works without ever pressing "AI's take"
  or the weekly recap; in that case no entry text leaves our backend. Recording a
  voice entry does send that audio for transcription — type instead if you would
  rather nothing leave the device but the text you save.
- **Permissions:** microphone (voice entries) and photo library (attachments) are
  requested only when you use those features. Notifications are asked for only
  after you have written your first entry, and are used for one thing: a weekly
  recap on Sunday evening. All of these can be revoked in iOS Settings, and the
  weekly recap can be turned off in Settings → 每周回顾.

## Children

The app is not directed to children under 13 (or the equivalent minimum age in
your region) and is rated 17+.

## Changes

We'll update this page and the "last updated" date if this policy changes
materially.

## Contact

dchen720@gmail.com
