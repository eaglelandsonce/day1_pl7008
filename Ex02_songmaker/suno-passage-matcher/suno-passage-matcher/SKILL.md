---
name: suno-passage-matcher
description: Analyzes a passage of text (prose, poetry, book excerpt, scripture, scene description, or raw notes) to determine the best matching musical styles using a 21-axis Suno schema, provides 3 distinct Style of Music prompt options (under 200 characters each), and automatically adapts and rhymes the passage into a complete, metatag-structured Suno Lyrics block. Use when the user asks to match a passage for Suno, analyze text for Suno style, turn a text passage into a song, or uses suno-passage-matcher.
---
# Suno Passage Matcher

Analyzes any input text passage for mood, imagery, era, and rhythmic cadence, maps it to 3 distinct style directions from the 21-axis Suno schema, and adapts the text into rhymed, meter-aligned song lyrics with full dynamic metatags.

## When to Use

- The user shares a passage of text (story excerpt, poem, monologue, article, scripture, or scene) and wants to know what musical style fits it or wants it turned into a Suno song.
- The user triggers `suno-passage-matcher` or asks to "match this passage for Suno" or "analyze this text for Suno style".

## Workflow Steps

1. **Analyze the Input Passage:**
   - **Imagery & Setting:** Identify time period cues, geographical/cultural atmosphere, and physical sensory details.
   - **Emotional Valence & Tension:** Determine the dominant emotional arc, harmonic mood (e.g., melancholic Dorian, exotic Phrygian Dominant, bright Ionian), and dynamic peaks.
   - **Cadence & Pacing:** Evaluate sentence length, syllable density, and natural rhythm to select a fitting BPM, time signature, and groove pocket.

2. **Generate 3 Distinct Style Options (From `references/suno-schema.json`):**
   Map the passage onto 3 complementary sonic directions so the user has creative choices:
   - **Option 1: Atmospheric / Setting Match** (Directly reflects the literal era, region, and acoustic environment of the text).
   - **Option 2: Emotional / Modern Reinterpretation** (Captures the psychological core using a contemporary, indie, electronic, or R&B/soul palette).
   - **Option 3: Cinematic / Genre-Fusion Contrast** (A bold hybrid or unexpected cross-genre fusion that heightens the drama of the passage).

   For each of the 3 options, provide:
   - **Coordinate Breakdown:** Era/Region/Genre Fusion, Key & Mode, BPM/Meter/Groove, Lead & Backing Instruments, Vocal Persona, and Production/Ambience/Mood.
   - **Style of Music Prompt:** A comma-separated string inside a plain code block, strictly **<= 200 characters**, following the priority order (`genre_primary`, `mood`, `bpm`, `key`, `instrument_lead`, `vocal_timbre`, `production`). Include the exact character count.
   - **Exclude Styles (Negative Prompt):** A plain code block listing opposing styles/instruments to prevent genre bleed.

3. **Adapt and Rhyme the Passage into a Tagged Suno Lyrics Block:**
   - Transform the core imagery, phrases, and narrative arc of the original passage into a complete, rhymed song structure (`[Intro]`, `[Verse 1]`, `[Pre-Chorus]`, `[Chorus]`, `[Verse 2]`, `[Bridge]`, `[Instrumental Solo]`, `[Outro]`).
   - Preserve the most evocative words and metaphors from the source passage while reshaping line lengths and rhyme schemes (e.g., AABB, ABAB, or internal rhymes) so Suno's vocal engine sings with natural prosody.
   - Embed dynamic and structural metatags (`[Whispered]`, `[Belted]`, `[Stripped Back]`, `[Crescendo]`, `[Half-Time Feel]`, `[Key Change]`, plus instrument solo tags matching Option 1 by default, with brief inline notes on how to swap the solo tag if using Option 2 or 3).
   - Include parenthetical backing vocal callouts `(ooh...)` and ambient foley cues in the intro/outro.

## Gotchas

- **Strict 200-Character Ceiling:** Every Style of Music prompt across all 3 options must be verified at or under 200 characters.
- **Spelled-Out Key Signatures:** Always use full key names (`D minor`, `F# minor`, `Bb Major`) rather than shorthand (`Dmin`).
- **Prosody Over Prose:** Never leave clunky, un-rhymed prose blocks inside `[Verse]` or `[Chorus]` sections; actively distill and rhyme the text so the syllable counts lock into the chosen meter (keep `[Spoken Word Narration]` only for an intentional `[Bridge]` or `[Intro]` if appropriate).
