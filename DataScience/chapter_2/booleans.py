from icecream.icecream import ic


def some_function_returns_string() -> str:
    return ""


def main() -> None:
    one_is_less_than_two: bool = 1 < 2
    true_equals_false: bool = True == False

    ic((one_is_less_than_two, true_equals_false))

    x = None
    assert x == None  # Not recomended method to verify
    assert x is None  # Pythonic mode to verify

    # all false (False, None, [], {}, "", set(), (), 0, 0.0)

    s: str = some_function_returns_string()

    if s:
        first_char: str | None = s[0]
    else:
        first_char: str | None = None

    ic(first_char)

    first_char = s and s[0]

    ic(first_char)

    safe_x = x or 0

    ic(safe_x)

    safe_x = x if x is not None else 0

    ic(safe_x)

    ic(
        (
            all([True, 1, {3}]),
            all([True, 1, {}]),
            any([True, 1, {}]),
            all([]),
            any([]),
        )
    )


if __name__ == "__main__":
    main()
