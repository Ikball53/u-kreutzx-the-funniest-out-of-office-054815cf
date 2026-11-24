"""The Funniest Out-of-Office — make.fun entry.

Writes a single-line out-of-office auto-reply to /output/entry.txt
as exact UTF-8 bytes, with no trailing newline.

The line is built for the judge brief, most important first:
a real person would actually set it (plain "Out of office until
Monday" opener), then a genuine surprise (the cat runs the inbox),
then a second beat that escalates it (two meetings deleted, and
the cat asked the boss for a raise). The concrete detail and the
closing escalation are the laugh — neither can be cut.
"""

import os

# 126 characters, within the 140-character gate. The em dash is
# written as an escape so the source stays plain ASCII while the
# output is the exact UTF-8 line.
ENTRY = "Out of office until Monday. My cat is in charge of my inbox \u2014 he's already deleted two meetings and asked my boss for a raise."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
