def main() -> None:
    buffer = open("example.txt", "r")
    poem = "".join(buffer.readlines())
    print(poem)
    buffer.close()


if __name__ == "__main__":
    main()
