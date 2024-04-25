def main() -> None:
    book = "python fluence"
    print(dir(str))
    print(book.upper(), book.lower(), book.title(), sep=" | ")
    book_2 = "    Python Fluence    "

    print(book_2.strip(), book.lstrip(), book.rstrip(),)


if __name__ == "__main__":
    main()
