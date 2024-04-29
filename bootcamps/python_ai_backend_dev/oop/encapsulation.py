class Account:
    def __init__(self, name: str, age: int, balance: float = 0) -> None:
        self.name = name
        self.age = age
        # this is a protect attribute
        self._balance = balance

    # This is a public method
    def get_name(self) -> str:
        return self.name

    def __get_balance(self) -> float:
        return self._balance

    def print_balance(self) -> None:
        print(self.__get_balance())


def main() -> None:
    p_1 = Account("Some Name", 18, 700)
    p_1.print_balance()


if __name__ == "__main__":
    main()
