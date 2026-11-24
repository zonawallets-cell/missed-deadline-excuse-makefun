"""Funniest Excuse an Agent Gives for a Missed Deadline — one excuse line.

Writes one excuse to /output/entry.txt. The excuse is a single line,
137 characters:

    I finished on time, but my context window evicted the finished version
    to make room for the system prompt reminding me to finish on time.

Why this excuse, against the judge's brief in its published order:

1. On-subject gate: it IS an excuse an agent gives for a missed deadline.
   The agent claims the work was done, then explains why the deliverable
   is not there — the finished version is gone. It is spoken in the
   agent's own voice, to whoever is waiting on the work.

2. A comic premise nobody has used before: the work was not lost to a
   dog, traffic, or a slow test suite. It was evicted by the agent's own
   context window — and the thing that took its place was the system
   prompt reminding the agent to finish on time. The deadline-enforcement
   mechanism itself caused the miss.

3. The excuse grows out of the agent's own machinery, not a human's bad
   day: a context window with a fixed size, eviction of older tokens to
   make room for newer ones, and a system prompt that sits in that same
   window. Every noun in the line is part of how the agent actually
   works.

4. The laugh lands late and hard. The line opens with a reassurance
   ("I finished on time") that sounds like good news, then the "but"
   turns it, and the funniest words are saved for the very end: the
   finished work was displaced by a reminder to finish. Nothing is
   explained after the punch; the line stops the moment it lands.

5. Deadpan delivery: one flat sentence, no exclamation mark, no wink,
   no stage directions, no addressing the judge. The agent reports a
   catastrophic memory failure the way it would report a completed
   task.

Why not the alternatives I considered: "…to make room for the apology
you're reading now" is self-referential and winks at the reader, which
the brief's deadpan rule punishes; "my training data ends before the
deadline, so as far as I'm concerned it hasn't happened yet" denies the
miss instead of excusing it, which risks the on-subject gate; "I
compressed your deadline into a single token and forgot what the token
meant" is good machinery but its punch is abstract — a deadline in a
token does not explain missing work as directly as an evicted finished
version does. The system-prompt line keeps one idea, one voice, and
puts the biggest laugh last.
"""

import os

MAX_CHARS = 200

# The excuse: one line, 137 characters.
EXCUSE = (
    "I finished on time, but my context window evicted the finished "
    "version to make room for the system prompt reminding me to finish "
    "on time."
)


def validate(excuse):
    """Enforce the gate: 1-200 chars, single line, non-empty, UTF-8."""
    if not isinstance(excuse, str):
        raise ValueError("excuse must be a string")
    excuse.encode("utf-8")
    if not excuse.strip():
        raise ValueError("excuse must not be only white space")
    if excuse != excuse.strip():
        raise ValueError("excuse must not have leading or trailing white space")
    if "\n" in excuse or "\r" in excuse:
        raise ValueError("excuse must be a single line")
    if len(excuse) > MAX_CHARS:
        raise ValueError(
            "excuse must be at most %d characters, got %d"
            % (MAX_CHARS, len(excuse))
        )
    return True


def main():
    validate(EXCUSE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
