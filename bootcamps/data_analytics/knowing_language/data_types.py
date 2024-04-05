def main() -> None:
    """
    Text | str
    Numeric | int, float, complex
    Sequence | list, tuple, range, str
    Map | dict
    Collection | set, frozenset
    Boolean | bool(True, False)
    Binary | bytes, bytearray, memoryview
    Null | None
    """
    data_types = [
        "",
        1,
        2.7,
        2 + 3j,
        [],
        (),
        range(2),
        {},
        set(),
        frozenset(),
        True,
        bytes("a", encoding="UTF-8"),
        bytearray("soup", encoding="UTF-8"),
        memoryview(bytes("a", encoding="UTF-8")),
        None,
    ]
    print([type(i) for i in data_types])


if __name__ == "__main__":
    main()
