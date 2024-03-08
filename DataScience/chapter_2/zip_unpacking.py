from icecream.icecream import ic


def add(a: int, b: int) -> int:
    return a + b


def main() -> None:
    list1: list[str] = ["a", "b", "c"]
    list2: list[int] = [1, 2, 3]

    ic([pair for pair in zip(list1, list2)])

    pairs: list[tuple[str, int]] = [("a", 1), ("b", 2), ("c", 3)]

    letters, numbers = zip(*pairs)
    ic((letters, numbers))

    ic(add(1, 2))

    try:
        ic(add([1, 2]))
    except TypeError:
        print("add expects two inputs")

    ic(add(*[1, 2]))


if __name__ == "__main__":
    main()
