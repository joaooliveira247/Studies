from typing import Callable


def calc(opr: str) -> Callable[[int, int], int | float]:
    def plus(a: int, b: int) -> int:
        return a + b

    def sub(a: int, b: int) -> int:
        return a - b

    def mult(a: int, b: int) -> int:
        return a * b

    def div(a: int, b: int) -> int | float:
        return a / b

    match opr:
        case "+":
            return plus
        case "-":
            return sub
        case "*":
            return mult
        case "/":
            return div
        case _:
            raise "Operation not found."


def main() -> None:
    print(calc("+")(5, 6))


if __name__ == "__main__":
    main()
