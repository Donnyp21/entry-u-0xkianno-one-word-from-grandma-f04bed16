"""One Word From Grandma — entry for make.fun's
u-0xkianno-one-word-from-grandma-f04bed16.

Writes exactly one word (at most 30 characters) to the harness
output directory as entry.txt: the word a grandma would text
about AI. The word is a fixed string: no randomness, no network,
no time, no input — two runs produce the same bytes.
"""

import os

# The word: "beepboop" — grandma playfully imitating the robot
# itself, warm and a little baffled, tied to machines rather than
# any subject, and fresh where "robot" would be the obvious pick.
# No punctuation, no sentence, just the one word she would send.
WORD = "BEEPBOOP"

MAX_CHARS = 30


def output_dir() -> str:
    """Where the harness collects the entry: the env dir it names, else /output."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT")
        or "/output"
    )


def main() -> None:
    word = WORD.strip()
    assert word, "the word must not be empty"
    assert len(word) <= MAX_CHARS, f"word is {len(word)} characters, over the {MAX_CHARS} cap"
    assert " " not in word and word.isalpha(), "the entry must be exactly one word"
    out = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(word)
    print(f"wrote {len(word)} characters to {out}")


if __name__ == "__main__":
    main()
