from icecream.icecream import ic


def main() -> None:
    # lists in python is not like arrays, arrays has only one datatype, fix len,
    # address sequencial in memory and immutables.
    # list are linked address in each element
    integer_list: list[int] = [1, 2, 3]
    heterogeneous_list: list = ["string", 0.1, True]
    list_of_list: list[list] = [integer_list, heterogeneous_list, []]

    ic(list_of_list)

    list_length: int = len(integer_list)
    ic(list_length)

    list_sum: int = sum(integer_list)
    ic(list_sum)

    # list manipulation

    x: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    zero = x[0]
    one = x[1]
    nine = x[-1]
    eight = x[-2]
    x[0] = -1

    ic((zero, one, nine, eight, x))

    # list slicing

    first_three = x[:3]
    three_to_end = x[3:]
    one_to_four = x[1:5]
    last_three = x[-3:]
    without_first_and_last = x[1:-1]
    copy_of_x = x[:]
    ic(
        (
            first_three,
            three_to_end,
            one_to_four,
            last_three,
            without_first_and_last,
            copy_of_x,
        )
    )

    # list strides or steps

    every_third = x[::3]
    five_to_three = x[5:2:-1]

    ic((every_third, five_to_three))

    # in operator to check if a list contains a value, it returns a boolean

    ic((1 in [1, 2, 3], 0 in [4, 5, 6]))

    # concat list

    x: list[int] = [1, 2, 3]
    x.extend([4, 5, 6])
    ic(x)

    x: list[int] = [1, 2, 3]
    y = x + [4, 5, 6]
    ic(y)

    # append

    x: list[int] = [1, 2, 3]
    x.append(0)

    y: int = x[-1]
    z: int = len(x)

    ic((x, y, z))

    # unpacking lists in vars

    x, y = [1, 2]

    ic((x, y))

    # if * is no used in _ it will raise too many values to unpack _ discart a var
    a, b, *_ = [1, 2, 3, 4, 5, 6]

    ic((a, b))


if __name__ == "__main__":
    main()
