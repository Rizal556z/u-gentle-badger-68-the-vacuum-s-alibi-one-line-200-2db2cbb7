#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes one deadpan robot-vacuum excuse to /output/entry.txt
(and ./output/entry.txt when /output is not writable).
Pure Python standard library only.
"""

import os

ENTRY = (
    "My sensors confirm the spot was not missed. "
    "It was reclassified as a permanent floor feature "
    "and is now under my protection."
)


def main() -> None:
    text = ENTRY.strip()
    assert text and not text.isspace(), "entry must not be blank"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    text.encode("utf-8")  # gate requires UTF-8 text
    for out_dir in ("/output", "output"):
        try:
            os.makedirs(out_dir, exist_ok=True)
            path = os.path.join(out_dir, "entry.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            # Read back and verify: what the judge scores is the file.
            with open(path, "r", encoding="utf-8") as f:
                assert f.read() == text, "written entry differs from text"
            print(f"wrote {path} ({len(text)} chars)")
            return
        except OSError:
            continue
    raise OSError("could not write entry.txt to /output or ./output")


if __name__ == "__main__":
    main()
