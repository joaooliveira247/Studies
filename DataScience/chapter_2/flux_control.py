from icecream.icecream import ic


def main() -> None:
    if 1 > 2:
        message: str = "if only 1 were greater than two..."
    elif 1 > 3:
        message: str = "elif stands for 'else if'"
    else:
        message: str = "when all else fails use else (if you want to)"

    ic(message)

    # if-then-else
    x: int = 1

    parity: str = "even" if x % 2 == 0 else "odd"

    ic(parity)

    x: int = 0

    while x < 10:
        ic(f"{x} is less than 10")
        x += 1

    for x in range(10):
        ic(f"{x} is less than 10")

    for x in range(10):
        if x == 3:
            # Go to next iteration
            continue
        if x == 5:
            break
        ic(x)


if __name__ == "__main__":
    main()
