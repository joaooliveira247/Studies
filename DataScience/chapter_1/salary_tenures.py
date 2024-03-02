from collections import defaultdict
from icecream.icecream import ic


def tenure_bucket(tenure: float) -> str:
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    return "more than five"


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

    salary_by_tenure: defaultdict[float, list] = defaultdict(list)

    for salary, tenure in salaries_n_tenures:
        salary_by_tenure[tenure].append(salary)

    avg_sal_by_ten = {
        tenure: sum(salaries) / len(salaries)
        for tenure, salaries in salary_by_tenure.items()
    }

    ic(avg_sal_by_ten)

    salary_by_tenure_bucket: defaultdict[str, list] = defaultdict(list)

    for salary, tenure in salaries_n_tenures:
        bucket: str = tenure_bucket(tenure)
        salary_by_tenure_bucket[bucket].append(salary)

    avg_salary_by_bucket: dict[str, float] = {
        tenure_bucket: sum(salaries) / len(salaries)
        for tenure_bucket, salaries in salary_by_tenure_bucket.items()
    }

    ic(avg_salary_by_bucket)


if __name__ == "__main__":
    main()
