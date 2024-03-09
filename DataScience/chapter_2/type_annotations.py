from icecream.icecream import ic
from typing import Union, Optional, Iterable, Callable


Number = int

Numbers = list[Number]


class Vector: ...


def add(a, b):
    return a + b


def another_add(a: int, b: int) -> int:
    return a + b


def dot_product(x: Vector, y: Vector) -> float: ...


def secretly_ugly_function(value, operation): ...


def ugly_function(
    value: int, operation: Union[str, int, float, bool]
) -> int: ...


def total(xs: list) -> float:
    return sum(total)


def another_total(xs: list[float]) -> float:
    return sum(xs)


def twice(repeater: Callable[[str, int], str], s: str) -> str:
    return repeater(s, 2)


def comma_repeater(s: str, n: int) -> str:
    n_copies: list[str] = [s for _ in range(n)]
    return ", ".join(n_copies)


def other_total(xs: Numbers) -> Number:
    return sum(xs)


def main() -> None:
    assert add(10, 5) == 15
    assert add([1, 2], [3]) == [1, 2, 3]
    assert add("hi ", "there") == "hi there"

    try:
        add(10, "five")
    except TypeError:
        print("cannot add an int to a string")

    # dinamic typing, when u type like a function in static type python will run it anyway
    ic((another_add(10, 5), another_add("hi ", "there")))

    # var typing

    x: int = 5

    values: list[int] = []

    best_so_far: Optional[float] = None

    counts: dict[str, int] = {"data": 1, "science": 2}

    lazy: Optional[bool] = False

    if lazy:
        evens: Iterable[int] = (x for x in range(10) if x % 2 == 0)
    else:
        evens: list[int] = [0, 2, 4, 6, 8]

    assert twice(comma_repeater, "type hints") == "type hints, type hints"


if __name__ == "__main__":
    main()
