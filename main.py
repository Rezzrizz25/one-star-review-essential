#!/usr/bin/env python3
"""One-star review of an everyday essential (make.fun bounty).

Writes a single deadpan one-star review of water to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The review: water falls from the sky for free, yet the moment someone
puts it in a bottle with a mountain on the label it costs $4. The
grievance is true, daily and specific; the sting lands in the last
few words, when the free thing suddenly has a price. Water was
chosen over gravity and sleep: the field is flooded with those two,
while nobody had filed the bottled-water complaint.
"""

import os

# The house gate: /output/entry.txt must be UTF-8 text of 1-160 chars.
MAX_CHARS = 160

REVIEW = (
    "Water: one star. Falls from the sky for free, but put it in a "
    "bottle with a mountain on the label and suddenly it costs $4."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = REVIEW.strip()
    assert text, "review must not be only whitespace"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"review must be 1-{MAX_CHARS} chars, got {len(text)}"
    )
    assert "\n" not in text, "review must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
