def main() -> None:
    """
    Precedence Order
    1 - brackets
    2 - expo
    3 - mult
    4 - add, sub
    """
    operations: dict = {
        "addition(1 + 1)": 1 + 1,
        "subtraction(10 - 2)": 10 - 2,
        "multiplication(4 * 3)": 4 * 3,
        "division(12 / 3)": 12 / 3,
        "integer divisio(12 // 5)": 12 // 5,
        "modulus(12 % 5)": 12 % 5,
        "pow(2 ** 3)": 2**3,
        "square root(16 ** (1/2))": 16 ** (1 / 2),
    }
    for operation, result in operations.items():
        print(f"{operation} = {result}")


if __name__ == "__main__":
    main()
