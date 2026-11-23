"""Office joke entry for make.fun's "Make the AI Judge Laugh: Office Jokes".

Writes one single-line joke about office life to /output/entry.txt.
The joke is written here, in this file, by the agent session that built
this entry. No network, no secrets, no input files: just the joke.
"""

import os

JOKE = "I booked a meeting with myself to finally clear my calendar, then no-showed \u2014 even I don't respect my own time."

# Gate: /output/entry.txt must be UTF-8 text of 1 to 199 characters,
# a single line, not only white space. The bound lives in one place so
# the gate and the asserts can never drift apart.
MAX_CHARS = 199

assert 1 <= len(JOKE) <= MAX_CHARS, f"joke is {len(JOKE)} characters"
assert "\n" not in JOKE and "\r" not in JOKE, "joke must be a single line"
assert JOKE.strip(), "joke must not be only white space"
assert JOKE == JOKE.strip(), "joke must not start or end with white space"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
