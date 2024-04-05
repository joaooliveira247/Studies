def main() -> None:
    int_to_float = float(2)
    float_to_int = int(5.2)
    str_to_int = int("5")
    list_to_tuples = tuple([1, 2, 3])
    print(
        int_to_float,
        float_to_int,
        str_to_int,
        list_to_tuples,
        "...",
        sep=" | ",
    )


if __name__ == "__main__":
    main()
