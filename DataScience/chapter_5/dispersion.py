from central_tendencies import mean
from common import num_friends
from central_tendencies import quantile

Vector = list[int]


def data_range(xs: list[int]) -> int:
    return max(xs) - min(xs)


def _dot_product(v: Vector, w: Vector) -> int:
    assert len(v) == len(w), "vectors must  be same length"

    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def _sum_of_squares(v: Vector) -> int:
    return _dot_product(v, v)


def de_mean(xs: list[int]) -> list[int]:
    x_bar = mean(xs)
    return [x - x_bar for x in xs]


def variance(xs: list[int]) -> float:
    assert len(xs) >= 2, "variance requires at least two elements"

    n = len(xs)
    deviatios: list[int] = de_mean(xs)
    return _sum_of_squares(deviatios) / (n - 1)


def standard_deviation(xs: list[int]) -> float:
    return variance(xs) ** (1 / 2)


def interquartile_range(xs: list[int]) -> float:
    return quantile(xs, 0.75) - quantile(xs, 0.25)


def test_data_range() -> None:
    assert data_range([25, 2, 8, 16, 5, 4]) == 23


def test_variance() -> None:
    assert 81.54 < variance(num_friends) < 81.55


def test_standard_deviation() -> None:
    assert 9.02 < standard_deviation(num_friends) < 9.04


def test_interquantile_range() -> None:
    assert interquartile_range(num_friends) == 6
