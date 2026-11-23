"""Dad Joke Showdown entry: write one dad joke to /output/entry.txt."""

JOKE = "I renamed our Wi-Fi 'Dad'. Now when it goes down, the kids shout, 'Dad's not working again!'"


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
