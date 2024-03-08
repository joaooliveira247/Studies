from typing import Callable


def doubler(f: Callable) -> Callable:
    def g(x: int) -> int:
        return 2 * f(x)

    return g


def f1(x: int) -> int:
    return x + 1


def f2(x: int, y: int) -> int:
    return x + y


def magic(*args: int, **kwargs: str) -> None:
    print(f"unnamed args: {args}\nkeyword args: {kwargs}")


def other_way_magic(x: int, y: int, z: int) -> int:
    return x + y + z


def doubler_correct(f: Callable) -> Callable:
    def g(*args: tuple, **kwargs: dict) -> int:
        return 2 * f(*args, **kwargs)

    return g


def main() -> None:
    g = doubler(f1)
    assert g(3) == 8
    assert g(-1) == 0

    g = doubler(f2)
    try:
        g(1, 2)
    except TypeError:
        print("as defined, g only takes one arg")

    magic(1, 2, key="word", key2="word2")

    x_y_list: list[int] = [1, 2]

    z_dict: dict[str, int] = {"z": 3}

    assert other_way_magic(*x_y_list, **z_dict) == 6

    g = doubler_correct(f2)
    assert g(1, 2) == 6


if __name__ == "__main__":
    main()
