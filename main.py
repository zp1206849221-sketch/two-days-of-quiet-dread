"""Write a one-line PR approval carrying quiet existential dread to /output/entry.txt."""

import os

# Single line, 127 characters: a plain approval first, then the dread kept
# flat and understated -- being forgotten is framed as the kind option.
ANSWER = "LGTM, ship it. In five years, nobody will remember this diff, and honestly that is the kindest thing I can say about any of us."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ANSWER)


if __name__ == "__main__":
    main()
