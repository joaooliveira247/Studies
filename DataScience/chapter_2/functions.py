from typing import Callable
from icecream.icecream import ic


def double(x: int) -> int:
    # this is a docstring
    """
    x: int
    """
    return x * 2


def apply_to_one(f: Callable[[int], int]) -> int:
    return f(1)


def my_print(message: str = "my default message") -> None:
    # by default python return None
    # this function has a default value for arg message
    ic(message)


def full_name(first: str = "what's his name", last: str = "something") -> str:
    # the book recommend this return but this isn't a good code
    # return first + " " + last

    return f"{first} {last}"


def main() -> None:
    my_double = double  # this is reference to double function
    x = apply_to_one(my_double)

    ic(x)
    # we can pass a anonymous function (in rust it's call closure)
    y = apply_to_one(lambda x: x + 4)

    ic(y)

    # we can define lambdas as vars

    another_double: Callable[[int], int] = (
        lambda x: x * 2
    )  # most common in JS but in python is recommended use def

    ic(another_double(5))

    my_print()
    my_print("hello")

    ic(full_name())
    ic(full_name("joel", "Grus"))
    ic(full_name("Joel"))
    ic(full_name(last="Grus"))


if __name__ == "__main__":
    main()
