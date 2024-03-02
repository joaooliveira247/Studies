from icecream.icecream import ic


def predict_paid_or_unpaid(year_experience: float) -> tuple[float, str]:
    if year_experience < 3:
        return year_experience, "paid"
    elif year_experience < 8.5:
        return year_experience, "unpaid"
    return year_experience, "paid"


def main() -> None:
    salaries_n_tenures: list[tuple[int, float]] = [
        (83000, 8.7),
        (88000, 8.1),
        (48000, 0.7),
        (76000, 6.0),
        (69000, 6.5),
        (76000, 7.5),
        (60000, 2.5),
        (83000, 10),
        (48000, 1.9),
        (63000, 4.2),
    ]

    paid_n_unpaid: list[tuple[float, str]] = [
        predict_paid_or_unpaid(x[1]) for x in salaries_n_tenures
    ]

    ic(paid_n_unpaid)


if __name__ == "__main__":
    main()
