"""Unsent: The Micro-Confession Sprint — make.fun bounty
u-boothlord-unsent-the-micro-confession-sprint-8c6596ba.

Writes one two-part micro-confession to /output/entry.txt: a To: line
naming who it was meant for, and the unsent message itself, one line
written exactly as it was typed. Python stdlib only, deterministic,
no network, no randomness.

The gate allows 1 to 260 characters of UTF-8 text; the message itself
is at most 200 characters. This program validates both before writing.
"""

import os

# Final line, chosen over two earlier drafts (see practice notes):
# - v1, the ex's hoodie: honest but a trope, and the To: line was generic.
# - v2, the night-shift nurse: strong, but a thank-you that never
#   happened, not a confession.
# This one is a confession: a secret kept for years, and the reason it
# stayed unsent is felt in the words, not stated — too kind to send,
# because sending it now would hand the blame back to a twelve-year-old.
# The To: line and the message need each other: only the sibling who
# took the money can be told this.
TO_LINE = "To: my little sister"
MESSAGE = (
    "I know you took the money from Mom's purse. "
    "I told her it was me because you were twelve and I wasn't."
)

MAX_TOTAL_CHARS = 260
MAX_MESSAGE_CHARS = 200


def build_entry() -> str:
    entry = TO_LINE + "\n" + MESSAGE + "\n"
    assert entry.strip(), "entry must not be only whitespace"
    assert len(entry) <= MAX_TOTAL_CHARS, "entry over 260 characters"
    assert len(MESSAGE) <= MAX_MESSAGE_CHARS, "message over 200 characters"
    assert "\n" not in MESSAGE, "message must be a single line"
    return entry


def main() -> None:
    out_dir = os.environ.get(
        "MAKEFUN_OUTPUT_DIR", os.environ.get("OUTPUT_DIR", "/output")
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(build_entry())


if __name__ == "__main__":
    main()
