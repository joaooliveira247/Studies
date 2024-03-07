from icecream.icecream import ic


def main() -> None:
    even_numbers: list[int] = [x for x in range(5) if x % 2 == 0]
    squares: list[int] = [x * x for x in range(5)]
    even_squares: list[int] = [x * x for x in even_numbers]

    ic((even_numbers, squares, even_squares))

    square_dict: dict[int, int] = {x: x * x for x in range(5)}
    square_set: set[int] = {x * x for x in range(5)}
    # we cannot do it with tuples, 'cause () gen a generator
    ic((square_dict, square_set))

    zeros: list[int] = [0 for _ in even_numbers]

    ic((len(even_numbers), len(zeros)))

    pairs: list[int] = [(x, y) for x in range(10) for y in range(x + 1, 10)]

    ic(pairs)

    


if __name__ == "__main__":
    main()
