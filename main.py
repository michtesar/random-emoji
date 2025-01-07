#!/usr/bin/env python3

import random

import pyperclip
import requests


def main() -> None:
    url = "https://unicode.org/Public/emoji/latest/emoji-test.txt"
    response = requests.get(url)
    emoji_list = []

    for line in response.text.splitlines():
        if line.strip() == "" or line.startswith("#"):
            continue

        # Extract the Unicode code points and convert them into an emoji
        unicode_sequence = line.split(";")[0].strip()
        emoji = "".join(chr(int(cp, 16)) for cp in unicode_sequence.split())
        emoji_list.append(emoji)

    random_emoji = random.choice(emoji_list)
    pyperclip.copy(random_emoji)

    print(f"Your random emoji: {random_emoji} (Copied to clipboard!)")


if __name__ == "__main__":
    main()
