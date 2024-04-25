def main() -> None:
    """
    tuples are imutables
    tuples accept slicing
    tuple are iterables
    """

    fruit = ("orange",)
    lang_letters = tuple("python")
    fruits = "banana", "strawberry", "lime"
    print(fruit, lang_letters, fruits, fruits[1], fruits[-1], sep=" | ")


if __name__ == "__main__":
    main()
