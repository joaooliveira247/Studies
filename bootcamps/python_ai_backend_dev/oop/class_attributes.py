class People:
    # This is a class attribute
    planet: str = "earth"

    def __init__(self, name: str, age: int) -> None:
        # These are instance attributes
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}, {self.age}, {self.planet}"


def main() -> None:
    p_1 = People("p1", 18)
    p_2 = People("p2", 21)
    print(p_1, p_2)


if __name__ == "__main__":
    main()
