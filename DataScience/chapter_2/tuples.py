from icecream.icecream import ic


def sum_and_product(x: int, y: int) -> tuple[int, int]:
    return x + y, x * y


def main() -> None:
    # tuples is immutables, it's accept slicing 'cause it's a sequence
    my_list: list[int] = [1, 2]
    my_tuple: tuple[int] = (1, 2)
    other_tuple: tuple[int] = 1, 2

    ic((my_tuple, other_tuple))

    try:
        my_tuple[1] = 3
    except TypeError:
        print("cannot modify a tuple")

    ic(sum_and_product(2, 3))

    s, p = sum_and_product(5, 6)

    ic(s, p)

    x, y = 1, 2
    ic((x, y))
    y, x = x, y
    ic((x, y))


if __name__ == "__main__":
    main()
