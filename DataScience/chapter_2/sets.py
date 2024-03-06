from icecream.icecream import ic


def main() -> None:
    primes_below_10: set[int] = {2, 3, 5, 7}
    ic(primes_below_10)

    # new empty set, cannot create with {} 'cause it is an empty dict
    # A set object is an unordered collection of distinct hashable objects.
    # Common uses include membership testing, removing duplicates from a
    # sequence, and computing mathematical operations such as intersection,
    # union, difference, and symmetric difference.
    # sets are mutable sequence, to a immutable version use fronzeset
    # 'in' in sets word better than others sequences
    s: set[int] = set()
    s.add(1)
    s.add(2)
    s.add(2)
    ic((len(s), 2 in s, 3 in s))

    item_list: list[int] = [1, 2, 3, 1, 2, 3]
    num_items: int = len(item_list)
    item_set: set[int] = set(item_list)
    num_distinct_items = len(item_set)
    distinct_item_list = list(item_set)
    ic(
        (
            item_list,
            num_items,
            item_set,
            num_distinct_items,
            distinct_item_list,
        )
    )


if __name__ == "__main__":
    main()
