"""make.fun entry: one-star review written by a house cat about its human.

Deterministic, no network. Writes the single review line to
$MAKEFUN_OUTPUT_DIR/entry.txt (falls back to ./entry.txt, then
./output/entry.txt).
"""

import os

MAX_CHARS = 200

ENTRY = (
    "One star. He shuts the bathroom door like privacy exists, "
    "then complains when I scream through it. He started it."
)


def main() -> None:
    assert len(ENTRY) <= MAX_CHARS, f"entry too long: {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
    else:
        out_path = "entry.txt"

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

    print(f"wrote {out_path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
