def main() -> None:
    poem_name: str = "I'm Nobody! Who are you?\n\n".title()
    buffer = open("example.txt", "r+")
    poem = "".join(buffer.readlines())
    buffer.seek(0)
    buffer.write(poem_name + poem)
    buffer.close()


if __name__ == "__main__":
    main()
