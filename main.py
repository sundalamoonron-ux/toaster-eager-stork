"""The Funniest Toaster Error Message.

Writes the winning toaster error line to /output/entry.txt.
The line was picked by a pairwise tournament over 10 candidates,
judged on the competition's own criteria: a real error message a
kitchen toaster would show its owner, fresh, tight, one voice,
landing on a single read.
"""

import os

# Winning line (55 characters, one line, UTF-8):
# "ERROR: Toasting cancelled. The bread filed a complaint."
LINE = "ERROR: Toasting cancelled. The bread filed a complaint."


def main() -> None:
    # Gate self-check (mirrors the competition gate): 1-120 chars,
    # exactly one line, not only whitespace, valid UTF-8.
    assert 1 <= len(LINE) <= 120, f"line is {len(LINE)} chars, gate is 1-120"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    LINE.encode("utf-8")

    path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
