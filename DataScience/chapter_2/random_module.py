from icecream.icecream import ic
import random


def main() -> None:
    random.seed(10)

    four_uniform_randoms: list[float] = [random.random() for _ in range(4)]

    ic(four_uniform_randoms)

    random.seed(10)

    ic(random.random())

    random.seed(10)

    ic(random.random())

    ic(random.randrange(10))

    ic(random.randrange(3, 6))

    up_to_ten: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    random.shuffle(up_to_ten)
    ic(up_to_ten)

    my_best_friend: str = random.choice(["Alice", "Bob", "Charlie"])

    ic(my_best_friend)

    lottery_numbers = range(60)
    winnig_numbers: list[int] = random.sample(lottery_numbers, 6)
    ic(winnig_numbers)

    four_with_replacement: list[int] = [
        random.choice(range(10)) for _ in range(4)
    ]

    ic(four_with_replacement)


if __name__ == "__main__":
    main()
