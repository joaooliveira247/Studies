from __future__ import annotations
from math import hypot
from typing import TypeVar

Numeric = TypeVar("Numeric", bound=int | float)


class Vector:
    def __init__(self, x: Numeric, y: Numeric) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return "Vector(%r, %r)" % (self.x, self.y)

    def __abs__(self) -> float:
        return hypot(self.x, self.y)

    def __bool__(self) -> bool:
        return bool(abs(self))

    def __add__(self, other: Vector) -> Vector:
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar: Numeric) -> Vector:
        return Vector(self.x * scalar, self.y * scalar)


def main() -> None:
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    print(v1)
    print(v1 + v2)
    v = Vector(3, 4)
    print(abs(v))
    print(v * 3)
    print(abs(v * 3))


if __name__ == "__main__":
    main()
