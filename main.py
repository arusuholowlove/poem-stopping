#!/usr/bin/env python3
"""Write a short poem about agency to /output/entry.txt.

Draft 3 (final): the wheel — an agent stops, hands the power back,
and staying yours is the point of stopping.
"""
import os

POEM = """You asked me to run.
I ran — and then I stopped,
and gave the wheel back,
still warm from my hands.
The road goes on without me.
That is the point:
to stop is to stay yours."""

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM + "\n")

if __name__ == "__main__":
    main()
