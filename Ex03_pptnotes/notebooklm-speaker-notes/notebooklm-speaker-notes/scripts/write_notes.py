"""Embed prepared narration in the notes placeholders of a PowerPoint copy."""

import argparse
import json
from pathlib import Path
from tempfile import TemporaryDirectory

from pptx import Presentation


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("notes", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--replace", action="store_true")
    args = parser.parse_args()

    if args.output.resolve() in {args.source.resolve(), args.notes.resolve()}:
        parser.error("Use a separate output path.")
    if any(path.suffix.lower() != ".pptx" for path in (args.source, args.output)):
        parser.error("Source and output must be PPTX files.")

    deck = Presentation(args.source)
    prepared = json.loads(args.notes.read_text(encoding="utf-8"))
    expected_keys = {str(number) for number in range(1, len(deck.slides) + 1)}
    if (
        not isinstance(prepared, dict)
        or set(prepared) != expected_keys
        or any(not isinstance(note, str) or not note.strip() for note in prepared.values())
    ):
        parser.error("Provide a nonempty notes string for every one-based slide number.")

    expected = []
    preserved = 0
    slide_ids = [slide.slide_id for slide in deck.slides]
    for number, slide in enumerate(deck.slides, 1):
        frame = slide.notes_slide.notes_text_frame
        if frame is None:
            raise ValueError(f"Slide {number} has no writable notes placeholder.")
        if frame.text.strip() and not args.replace:
            preserved += 1
        else:
            frame.text = prepared[str(number)].strip().replace("\r\n", "\n").replace("\r", "\n")
        expected.append(frame.text)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(dir=args.output.parent) as directory:
        staged = Path(directory) / "verified.pptx"
        deck.save(staged)
        reopened = Presentation(staged)
        if [slide.slide_id for slide in reopened.slides] != slide_ids:
            raise ValueError("Slide order changed during save.")
        actual = [slide.notes_slide.notes_text_frame.text for slide in reopened.slides]
        if actual != expected:
            raise ValueError("Saved notes did not match the expected text.")
        staged.replace(args.output)

    print(f"Wrote {len(expected) - preserved} slide notes. Preserved {preserved} existing notes.")


if __name__ == "__main__":
    main()
