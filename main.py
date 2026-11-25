#!/usr/bin/env python3
"""One-line office joke entry for the make.fun bounty
"Make the AI Judge Laugh: the Office Joke Open".

Writes exactly one line — a single-sentence joke about office life —
to /output/entry.txt. Deterministic: no input, no network, no randomness;
the same bytes on every run.

Craft notes: the setup names a specific, instantly recognisable office
detail — the reply-all chain everyone has lived through — and the
punchline escalates it into absurdity: the attempt to escape the thread
becomes the very thing that keeps it going, multiplying instead of
ending it. That fits the judge brief: one line of office comedy, under
200 characters, that is first a recognisable workplace moment, then
funny through a surprising, self-defeating payoff, and clear on first
read.

Round 2 — a fresh angle: the round-1 entry was about a reply-all
chain that feeds on escape attempts; this one is about a status
message that feeds on itself, with a different trap (a meeting
about availability you miss because you are in a meeting) and a
different payoff (the loop closes on the very first word).
"""

import os

JOKE = (
    "I set my status to 'in a meeting' and my manager booked a meeting "
    "to discuss my availability, which I missed because I was in a meeting."
)


def main() -> None:
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} characters"
    assert "\n" not in JOKE and JOKE == JOKE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
