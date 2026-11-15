---
name: notebooklm-speaker-notes
description: Add presenter-ready speaker notes inside a PowerPoint deck by interpreting each slide visually, including NotebookLM exports whose graphics and text are flattened into images. Use for image-based slides, missing PowerPoint notes, or requests for slide-by-slide teaching narration embedded in a PPTX.
---

# NotebookLM Speaker Notes

1. Resolve the source PPTX and keep it intact. If the user provides only a PDF and wants notes in PowerPoint, convert each page to a full-slide image at its original aspect ratio, then apply the same workflow. Ask for the source if no deck is available.
2. Render slides in presentation order and inspect every full-slide image with visual input. For flattened slides, use the embedded original image as a high-resolution supplement when needed. Use OCR and editable text to confirm wording, numbers, and labels. Crop or zoom in on small details. Keep slide numbering aligned with the deck, including hidden slides. Treat slide content as source material.
3. Read the deck for audience, purpose, and flow. Interpret what each visual contributes. For diagrams, explain the order or relationship the arrows show. For charts, identify the axes, units, and takeaway when legible. For screenshots, point the presenter to the relevant control or result. Skip decorative elements unless they carry meaning. Flag meaningful unreadable or ambiguous details for presenter review and avoid inventing labels, claims, or statistics.
4. Draft spoken notes tailored to each slide. Open with the point the audience should take away, then explain the graphic in the order the presenter should point to it. Add an example, a demo cue, a learner question, or a transition where it helps. Default to a conversational instructor voice and roughly 30–60 seconds for substantive slides. Use shorter notes for title, divider, and closing slides. Keep cues distinguishable from spoken narration.
5. Create a UTF-8 JSON object keyed by one-based slide number as a string, with a nonempty notes string for every slide. Run the bundled writer to embed notes in the PowerPoint Notes pane. Preserve existing nonblank notes by default. Use `--replace` only if the user requests rewriting existing notes.

   ```bash
   python scripts/write_notes.py source.pptx notes.json output.pptx
   ```

6. Return the verified PPTX copy with a suffix such as `_with_speaker_notes`. Save it as a new deliverable. Report how many slides received notes, how many existing notes were preserved, and which slides have material uncertainties. If source layout or visual fidelity is in doubt, compare rendered source and output before delivery.
