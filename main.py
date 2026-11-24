"""One-Line Roast: The Gadget You Use Every Day (make.fun bounty
u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610).

Writes a single one-line roast of a daily gadget to /output/entry.txt.
Deterministic: the same bytes on every run, no network, no input,
no randomness.

The roast: a laptop fan that screams like a jet engine the moment a
spreadsheet opens, as if the numbers personally offended it. It names
a gadget everyone uses daily, lands on first read, carries a concrete
detail (the fan spinning up on a spreadsheet, not on heavy work), and
is tight at 114 characters.
"""

import os

LINE = (
    "My laptop fan screams like a jet engine every time I open a "
    "spreadsheet, as if the numbers personally offended it."
)

MAX_CHARS = 200


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= MAX_CHARS, "line must be 1-200 characters"
    assert text == text.strip(), "no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "must be a single line"
    assert text.strip(), "must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
