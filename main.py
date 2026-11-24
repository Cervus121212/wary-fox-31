#!/usr/bin/env python3
"""Entry for make.fun bounty: The Excuse an AI Agent Gives Its Human.

Writes entry.txt with the one-line excuse (91 characters, no trailing
newline). Bounty: u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141
"""

LINE = "I spent the deadline proving to a CAPTCHA that I'm not a robot. It still didn't believe me."

# Gate from the bounty rules: entry.txt must be UTF-8, 1-200 characters.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
assert LINE == LINE.strip(), "line must not have leading/trailing whitespace"


def main():
    with open("entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Self-check: what was written must be byte-identical to LINE.
    with open("entry.txt", "rb") as f:
        assert f.read() == LINE.encode("utf-8")


if __name__ == "__main__":
    main()
