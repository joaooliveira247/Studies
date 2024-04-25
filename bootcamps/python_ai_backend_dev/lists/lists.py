def main() -> None:
    """
    lists are implemented like linked lists data structure, in python lists are
    mutable
    lists supports slicing
    lists are iterables(implements __iter__ & __next__)
    """
    fruits = ["apple", "orange", "banana", "strawberry"]
    lang_letters = list("python")
    fruits.append("mango")
    fruits.remove("banana")
    fruits.pop(2)
    reverse_fruits = fruits.copy()  # or fruits[::]
    reverse_fruits.reverse()

    print(
        fruits,
        lang_letters,
        fruits[0],
        fruits[-1],
        reverse_fruits,
        sep=" | ",
    )

    nums = [1, 2, 3, 4, 5, 6]
    print([i + 1 for i in nums if i % 2 == 0])


if __name__ == "__main__":
    main()
