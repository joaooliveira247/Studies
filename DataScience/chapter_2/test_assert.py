from doctest import testmod


def double(n: int) -> int:
    # this is call doctest, but in python is common use pytest
    """
    >>> double(5)
    10
    """
    return n * 2


def smallest_item(x: list[int]) -> int:
    return min(x)


def main() -> None:
    assert 1 + 1 == 2

    assert smallest_item([10, 20, 5, 40]) == 5
    assert smallest_item([1, 0, -1, 2]) == -1


if __name__ == "__main__":
    testmod()
