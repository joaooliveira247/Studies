from typing import TypeVar

T = TypeVar("T")

A = TypeVar("A", int, float)

def echo(value: T) -> T:
    return value

def echo2(value: A) -> A:
    return value

def main() -> None:
    x = echo(2)
    y = echo("str")

    w = echo2(1.0)
    z = echo2("str")


if __name__ == "__main__":
    main()