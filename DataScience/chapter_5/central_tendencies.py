from collections import Counter


def mean(xs: list[int]) -> int | float:
    return sum(xs) / len(xs)


def _median_odd(xs: list[int]) -> int | float:
    return sorted(xs)[len(xs) // 2]


def _median_even(xs: list[int]) -> int | float:
    sorted_xs: list[int] = sorted(xs)
    hi_midpoint: int = len(xs) // 2
    return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2


def median(v: list[int]) -> int | float:
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)


def quantile(xs: list[int], p: float) -> int | float:
    return sorted(xs)[int(p * len(xs))]


def mode(x: list[int]) -> list[int]:
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]


def test_mean() -> None:
    assert mean([10, 12, 8]) == 10


def test_median() -> None:
    assert median([1, 10, 2, 9, 5]) == 5
    assert median([1, 9, 2, 10]) == (2 + 9) / 2


def test_quantile() -> None:
    quantile_test_list: list[int] = [5, 7, 9, 17, 42, 99, 86]
    assert quantile(quantile_test_list, 0.3) == 9
    assert quantile(quantile_test_list, 0.9) == 99
    assert quantile(quantile_test_list, 0.17) == 7


def test_mode() -> None:
    assert set(
        mode(
            [
                1,
                1,
                5,
                5,
                5,
                6,
                8,
                8,
                8,
                9,
                9,
                9,
                9,
                9,
                9,
                9,
            ]
        )
    ) == {9}
