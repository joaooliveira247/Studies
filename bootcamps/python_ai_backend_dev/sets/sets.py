def main() -> None:
    """
    sets in python are like math sets.
    sets only accept unique values
    sets are mutables
    unordered
    """
    list_1: list[int] = [1, 1, 1, 3, 4, 5]
    set_1: set[int] = {1, 2, 3, 4, 5}
    set_2: set[int] = set(list_1)

    print(
        set_1,
        set_2,
        set_1.union(set_2),
        set_1.difference(set_2),
        set_1.intersection(set_2),
        set_1.symmetric_difference(set_2),
    )

    set_1.add(6)
    print(set_1)
    set_1.pop()
    print(set_1)

    print({2, "oi", 1.7, True, 1})  # 1 don't will be printed 'cause 1 is true in python

    # to get an item u'll need cast a set to list to acess itens, or consume that
    # iterable


if __name__ == "__main__":
    main()
