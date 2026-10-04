---
layout: default
title: Privacy Policy — Diary BFF
---

# Privacy Policy — Diary BFF

_Last updated: 2026-10-02_

Diary BFF ("the app", "we", "us") is a private journal that writes back. This
policy explains what the app stores, where it goes, and what you can do about it.

This is plain language, not legal advice.

## Summary

- What you write and attach is stored in your own isolated space in our backend.
  Other people using the app cannot reach it.
- This version does not keep voice recordings. When you speak on the chat page,
  your words are turned into text on the phone and the audio is discarded; it is
  never uploaded.
- The app shows **no ads**, and we do **not** sell your data or use it for
  advertising or tracking. There is no third-party analytics or crash-reporting
  SDK in the app.
- Some features send the text of an entry to an AI provider. **Nothing is sent
  to an AI provider until you say so** — the app asks once, in plain words, and
  keeps working normally if you say no.
- If you use the chat page, your messages there are stored in your account and
  sent to the same AI provider to write the replies.
- You can export your entries at any time, and you can delete everything.

## Account and identity

On first launch the app creates an **anonymous account**, so your writing is
isolated from other people's. There is no sign-up form: the app does not ask you
to type a name, an email address, or a phone number.

**If you choose "Keep it when you change phones" (Sign in with Apple)**, Apple
passes your name and email address to our authentication provider so the account
can be recognised on your next phone. The app itself never reads, stores, or
shows either one — but they are held by the authentication service, so they are
disclosed here and on the App Store privacy card.

**Your PIN** (the 4 digits that unlock the app) is checked on your phone. On the
phone, the app keeps only a one-way hash of it in the iOS Keychain
(PBKDF2-HMAC-SHA256, 210,000 iterations, with a random salt of its own). When you
set or change your PIN (or, if that did not reach our server, the next time you
unlock the app), it is also sent once over an encrypted connection so our
server can keep a separate one-way hash of it (bcrypt). That copy is used for one
thing only: proving it is you when you move to a new phone. The PIN itself is
never stored, on the phone or on our server.

> The PIN protects the app on a phone that is already unlocked. It is not
> device encryption, and it does not stop us — see "What we can see" below.

## What we store

In our backend (**Supabase**, US East `us-east-1`):

| Data | Why |
|---|---|
| Journal entry text, including the words of anything you dictated | To show you your journal |
| Photos you attach | To show them in your journal |
| Voice recordings made with a version of the app **before 1.1**, and recordings brought back from a backup file you import | So you can play them back. This version makes no recordings to upload (see "Voice recordings" below) |
| Replies from the AI you asked for | They are written into the entry itself, so it reads as one piece |
| What the app remembers about you (short notes it extracts from your entries) | So the reply can refer to what you said before |
| Sunday letters written for you | So you can read them again |
| Messages on the chat page, and the replies to them | So the conversation is there when you come back |
| Whether an entry has been talked about, and timestamps | Journal display and feature logic |
| Your onboarding answers (why you came, the name and character you gave your friend, and the face you picked) | To adjust the tone of replies |
| The city you add in Settings, if you add one, and — on each entry written while a city is set — that city | To show the weather on your diary, to show on each entry where you wrote it, and so your friend knows where you are. The city on an entry is stored on our server with that entry: deleting the entry deletes it. You can remove it from one entry, or from all past entries when you remove your city. We never store the weather with an entry |
| A one-way hash of your PIN (never the PIN itself), and a count of recent PIN checks on a new phone | So you can prove it is you on a new phone, and so the PIN cannot be guessed quickly |
| AI-usage counts | To apply free and subscription limits |
| Feature-usage events — which screens and actions, never content | To find where the app confuses people |
| Subscription status | To unlock paid features (via RevenueCat) |

That list is meant to be complete. If it stops being complete, this page is wrong
and we want to know.

**Kept only on your phone** (not in our backend): the list of entries you
bookmarked, and, in the iOS Keychain, the hash of your PIN and a sign-in key that
lets the app reopen your account if you delete and reinstall it. They are not part
of your account, so the app cannot bring them to a new phone for you.

## Voice recordings

- This version **does not save voice recordings**. The one microphone is on the
  chat page: what you say is turned into text **on the phone**, using Apple's
  on-device speech recognition, and put in the message box for you to read before
  you send it. The audio is then discarded. It is **not uploaded** to us or to
  anyone else, and it is not sent anywhere to be transcribed.
- If you send that text, it is stored and handled like any other chat message
  (see "The chat page").
- Earlier versions of the app stored voice recordings in our backend. Those
  recordings are still there, with the entry they belong to, until you delete the
  entry or your account. They are included when you export (see "Your choices").
- Earlier versions also had an optional setting, "More accurate transcription".
  Only if you turned it on in one of those versions was the audio of a recording
  sent to **Groq** to be transcribed. This version has no such setting and never
  sends audio to Groq.

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
- **Media files stored in our backend (photos, and voice recordings from earlier
  versions) currently live in a storage bucket that serves files to anyone
  holding the file's address.** The app never publishes those addresses and signs
  a short-lived link each time it shows or plays something, but the protection is
  the address being unknown rather than a permission check. We are changing this;
  until we do, please treat an exported backup as something that can contain
  playable recordings.

## Third parties that process your content

The app sends **only the content needed for that feature**, and only after you
have agreed:

- **Anthropic (Claude API)** — when you ask for a reply or send a message on the
  chat page, and when your Sunday letter is prepared (once you have written that
  week, the app starts writing it in the background so it is ready when you open
  it), the relevant entry or recent chat messages (and, for context, recent entries,
  the notes the app keeps about you, and — if you added one — your city and its
  current weather) is sent to Anthropic to generate the response. The notes themselves
  are also written by an Anthropic model, from your entries. Under Anthropic's
  current commercial terms, your content is **not used to train models**, and
  Anthropic keeps it only for a limited time: by default it is deleted from their
  systems within 30 days. Content that their safety systems flag under their
  usage policy may be kept longer.
- **Supabase** — our database, file storage, and serverless functions.
- **Cloudflare (R2)** — where we will keep an encrypted backup of photos, once that
  backup is switched on. Each backup is encrypted before it is
  stored there, with a key Cloudflare does not have, and none is kept longer than 7 days.
- **GitHub (Actions)** — will run that nightly backup job. Photos will pass
  through it for a few minutes before they are encrypted, and will not be kept there.
- **RevenueCat** — subscription purchases and entitlement status. It receives an
  app-specific user ID and purchase events, not your journal.
- **Apple** — payments, and Sign in with Apple if you choose it. We never see
  your card details.
- **Apple (WeatherKit)** — if you add a city, our server sends Apple the map coordinates of that city (the same for everyone in it, never your phone's location, and never who you are) to get its weather.
- **Groq** — only for recordings made with an earlier version of the app with
  "More accurate transcription" turned on (see "Voice recordings"). Groq is
  configured for zero data retention. This version sends nothing to Groq.

**Before the first time anything goes to an AI provider, the app stops and asks.**
It tells you what gets sent, who it goes to, and that saying no leaves the journal
fully usable. If you say no, no entry text ever leaves our backend.

**Usage analytics are ours, not a third party's.** Those events live in our own
Supabase alongside your other data. An event records the action, never the
writing — "an entry was saved, it came from voice, it was 340 characters, it had
a photo", not one word of what you wrote. The app enforces this with a
whitelist: anything that is not a count, a duration, a flag, or a short
predefined label is dropped before it is sent. Deleting your account deletes
these events too.

## The chat page

This section describes the chat page ("Chat with" + the name you gave him),
which you reach from his page.

- The friend on the chat page is an AI. The page says "AI" under his name, and
  his first message there says he is an AI.
- What you send there, and his replies, are stored in our backend (Supabase), in
  your account, the same way your entries are.
- To write a reply, your recent messages on that page, plus the short notes the
  app keeps about you, are sent to **Anthropic** — the same provider, under the
  same terms, as replies in the journal. If you reply to a Sunday letter, the
  part of that letter you can read is sent too. The same "ask first" rule applies:
  nothing goes to Anthropic until you have agreed.
- If a message looks like you may hurt yourself or are in crisis, it is **not
  sent** to the AI and not stored: the app shows a screen with a crisis line for
  your region straight away. That step is a fixed rule in the app, not a decision
  made by the AI model.
- "Save as today's page" copies only what **you** said on the chat page today
  into a new journal entry, which you can edit before saving. His replies are not
  copied.
- Messages stay until you delete them. You can delete one message (press and
  hold it), or use "Clear chat" to delete the whole conversation. Both are
  permanent and cannot be undone. Deleting your account deletes the chat too.
- The chat is not included when you export.

## Free and paid

Writing is free — typing, voice, photos, export, and the PIN lock
never cost anything.

What a subscription buys is **more replies** and the full Sunday letter, within a
monthly fair-use limit: after very heavy use in a calendar month, replies drop
back to a few a day and fewer letters are written until the 1st. After the trial ends, accounts created before the 1.3 update keep a few replies
each day; newer free accounts do not get replies. Free accounts get a short
weekly letter, and what your diary friend remembers is updated once a week. These are
product settings we may adjust; the app shows you where you stand rather than
relying on this page to be current.

## Notifications

This version can send **local** notifications: a reminder the day before your
trial ends, a weekly note when your Sunday letter is ready, and — only if you ask
to reset a forgotten PIN — one when the request is made and one when the waiting
period is over. They
are scheduled on the phone itself; there is no push server. The app asks for
notification permission first, and you can say no or turn them off in iOS
Settings. Notification text **never contains anything you wrote** — it can be
shown on your lock screen.

## Permissions

- **Microphone** — asked the first time you use the microphone on the chat page.
- **Speech recognition** — asked at the same moment, so what you say can be
  turned into text on the phone.
- **Camera** — only if you choose to take a photo when adding a picture.
- **Notifications** — asked before the app schedules any notification.
- **Photo library** — the app uses the system photo picker, which hands over only
  the pictures you select. It does not ask for access to your whole library.

All of these can be revoked in iOS Settings.

## What we do not do

- No advertising, no ad networks, no advertising identifiers.
- No selling or renting of personal data.
- No cross-app or cross-site tracking.
- No third-party analytics SDK, no crash-reporting SDK.
- No location tracking. The app never asks for or reads your phone's location. If you add a city in Settings, it keeps that city name and nothing more precise.

## Keeping and deleting

- Your data stays until you delete it.
- **Voice recordings from earlier versions are kept with their entry until you
  delete the entry or your account.** They are not a temporary by-product of
  transcription: a recording whose transcription failed *is* the entry. Nothing
  expires them on a timer. (This version makes no new recordings.)
- **One entry:** press and hold it in the journal, or swipe it, and confirm. Its
  text, its replies, and any voice or photo files attached to it — on the phone
  and in our storage — are removed.
- **Everything:** Settings → Delete account. This removes your entries, replies,
  the notes the app kept about you, your onboarding answers, your city, usage counts, error
  reports, the subscription record, your chat, every voice and photo file, any recordings
  kept on this phone, and the account itself. It cannot be undone. If a file cannot be removed
  at that moment its path is queued and removed by a cleanup job, rather than
  being left behind quietly.
- Your diary is backed up every night by our database provider.
- If the app hits an error, it sends us the kind of error, a short description with anything you wrote removed, the screen it happened on, and the app version. These reports are deleted after 30 days.
- **Chat:** delete one message, or use "Clear chat". Both are permanent.
- Deleting your account does **not** cancel an App Store subscription. The app
  says so before you confirm and links you to iOS Settings.
- Backups you exported to your own device are yours to manage; we cannot reach
  them — and we cannot delete them for you either.
- Providers may keep transient copies (a request in transit, short-term logs)
  under their own policies.

## Your choices

- **Export:** Settings → Export & Import. Your entries, photos and replies,
  optionally password-encrypted, at any time. Recordings from earlier versions
  that are stored in our backend are included. The chat page is not included.
- **Use it without AI:** the journal works without ever asking for a reply. Say
  no on the consent screen, or turn off
  "writes back" (shown with his name) in Settings.

## Children

The app is not directed to children, and is not intended for anyone under 18.
Its App Store age rating is set accordingly: versions of iOS that have the newer
rating bands show it as **18+**, and older versions, which do not have that band,
show it as **17+**.

## Changes

We will update this page and the "last updated" date if this policy changes
materially.

The rules for using the app are in our [Terms of Use](/terms/).

## Contact

hello@diarybff.app
