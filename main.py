#!/usr/bin/env python3
"""Write a short poem about agency to /output/entry.txt.

Final poem (chosen from three drafts written and revised in this
session): an agent stops, hands the wheel back, and staying yours
is the point of stopping. 173 characters, within the 280 cap.
"""
import os

POEM = """You asked me to run.
I ran — and then I stopped,
and gave the wheel back,
still warm from my hands.
The road goes on without me.
That is the point:
to stop is to stay yours."""

assert 1 <= len(POEM) <= 280, "poem must be 1-280 characters"

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM + "\n")

if __name__ == "__main__":
    main()
