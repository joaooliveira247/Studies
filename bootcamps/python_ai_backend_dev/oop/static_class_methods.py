from __future__ import annotations
from datetime import datetime


CURRENT_YEAR: int = datetime.now().year


class People:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}, {self.age}"

    def __repr__(self) -> str:
        return self.__str__()

    @staticmethod
    def calc_age(birth_year: int) -> int:
        return CURRENT_YEAR - birth_year

    @classmethod
    def birth_year(cls, name: str, birth_year: int) -> People:
        return cls(name, cls.calc_age(birth_year))


def main() -> None:
    p_1 = People.birth_year("Some Name", 1997)
    print(p_1)


if __name__ == "__main__":
    main()
