#!/usr/bin/env python3
"""Five Seconds to Explain the Glass.

Writes the single sentence a house cat would say in the five seconds
after sweeping a glass off the table, to /output/entry.txt.

The sentence is one sentence, at most 200 characters, in the cat's own
voice: no apology, no confession, just the most convincing case the cat
can make for itself. The cat pleads its case as a matter of household
law: anything left on the table's edge falls under its inspection, and
this glass failed its audit. Spoken in five seconds, it lands its punch
in the final words ("failed its audit") rather than up front.
"""

import os

# The cat's statement (109 characters, one sentence, no apology).
ENTRY = (
    "Under the Household Treaty, anything on the table's edge is mine "
    "to inspect, and that glass failed its audit."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    # One sentence: exactly one terminal full stop, no apology or confession.
    assert text.count(".") == 1 and text.endswith("."), "entry must be a single sentence"
    assert "sorry" not in text.lower(), "no apology allowed"
    out_path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
