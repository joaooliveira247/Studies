from icecream.icecream import ic


def main() -> None:
    for i in [1, 2, 3, 4, 5]:
        ic(i)
        for j in [1, 2, 3, 4, 5]:
            ic(j)
            ic(i + j)
        ic(i)
    ic("done looping")

    long_winded_computation: int = (
        1
        + 2
        + 3
        + 4
        + 5
        + 6
        + 7
        + 8
        + 9
        + 10
        + 11
        + 12
        + 13
        + 14
        + 15
        + 16
        + 17
        + 18
        + 19
        + 20
    )

    list_of_lists: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    easier_to_read_list_of_lists: list[list[int]] = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    two_plus_three: int = 2 + \
                                3
    


if __name__ == "__main__":
    main()
