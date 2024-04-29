from __future__ import annotations
from datetime import datetime


CURRENT_YEAR = datetime.now().year


class Foo:
    def __init__(self, x: int | None = None) -> None:
        self._x = x

    @property
    def x(self) -> int:
        return self._x or 0

    @x.setter
    def x(self, value: int) -> Foo:
        self._x += value

    @x.deleter
    def x(self):
        self._x = 0


class People:
    def __init__(self, name: str, birth_year: int) -> None:
        self._name = name
        self._birth_year = birth_year

    @property
    def age(self) -> int:
        return CURRENT_YEAR - self._birth_year


def main() -> None:
    foo = Foo(10)
    print(foo.x)
    foo.x = 15
    print(foo.x)
    del foo.x
    print(foo.x)
    p_1 = People("Some Name", 1997)
    print(p_1.age)


if __name__ == "__main__":
    main()
