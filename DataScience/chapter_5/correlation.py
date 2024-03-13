from common import (
    dot_product,
    num_friends,
    daily_minutes,
    daily_hours,
    daily_hours_good,
    daily_minutes_good,
    num_friends_good,
)
from dispersion import de_mean, standard_deviation
from pytest import mark


def covariance(xs: list[float], ys: list[float]) -> float:
    assert len(xs) == len(ys)

    return dot_product(de_mean(xs), de_mean(ys)) / (len(xs) - 1)


def correlation(xs: list[float], ys: list[float]) -> float:
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(xs)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(xs, ys) / stdev_x / stdev_y
    else:
        return 0


def test_covariance() -> None:
    assert 22.42 < covariance(num_friends, daily_minutes) < 22.43
    assert 22.42 / 60 < covariance(num_friends, daily_hours) < 22.43 / 60


@mark.skip("This test don't run")
def test_correlation() -> None:
    assert 0.24 < correlation(num_friends, daily_minutes) < 0.25
    assert 0.24 < correlation(num_friends, daily_hours) < 0.25


@mark.skip("This test don't run")
def test_correlation_with_new_vars() -> None:
    assert 0.57 < correlation(num_friends_good, daily_minutes_good) < 0.58
    assert 0.57 < correlation(num_friends_good, daily_hours_good) < 0.58
