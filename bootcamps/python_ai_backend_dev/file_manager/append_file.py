def main() -> None:
    poem_author: str = "\nemily dickinson".title()
    buffer = open("example.txt", "a")
    buffer.write(poem_author)
    buffer.close()


if __name__ == "__main__":
    main()
