from typing import Callable


def pow(x: int, y: int) -> int:
    return x**y


# this method to write lambda function like js is not recommended in python
SUM = lambda x, y: x + y


def posicional_args(*args: tuple) -> tuple:
    return args


def keywords_args(**kwargs: dict) -> dict:
    # ** it's used to unpack all key and values in a dict live arg=arg_value
    return kwargs


def default_value_arg(x: str = "Hello") -> str:
    return x


def function_without_arg() -> str:
    return "Hello"


def positional_only(
    model: str, year: int, car_plate: str, /, type_: str, motor: str, fuel: str
) -> None:
    print(model, year, car_plate, type_, motor, fuel)


def positional_keyword_args(
    model: str,
    year: int,
    car_plate: str,
    /,
    type_: str,
    *,
    motor: str,
    fuel: str,
) -> None:
    print(model, year, car_plate, type_, motor, fuel)


def print_result(a: int, b: int, func: Callable[[int, int], int]) -> None:
    result: int = func(a, b)
    print(result)


def main() -> None:
    print(
        pow(2, 3),
        SUM(2, 3),
        posicional_args(1, 2, 3, 4, 5, 6, 7),
        keywords_args(name="some name", value="some value"),
        default_value_arg(),
        function_without_arg(),
        sep=" | ",
    )

    positional_only(
        "palio", 1999, "ABC-1234", type_="fiat", motor="1.0", fuel="Gasoline"
    )

    positional_keyword_args(
        "palio", 1999, "ABC-1234", "fiat", motor="1.0", fuel="Gasoline"
    )

    print_result(10, 2, SUM)


if __name__ == "__main__":
    main()
