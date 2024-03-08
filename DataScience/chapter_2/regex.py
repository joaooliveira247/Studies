from icecream.icecream import ic
import re


def main() -> None:
    re_examples: list[bool] = [
        not re.match("a", "cat"),
        re.search("a", "cat"),
        not re.search("c", "dog"),
        3 == len(re.split("[ab]", "carbs")),
        "R-D-" == re.sub("[0-9]", "-", "R2D2"),
    ]

    ic(re_examples)

    assert all(re_examples)


if __name__ == "__main__":
    main()
