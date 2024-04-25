def loop_for() -> None:
    """
    for's accept else statment
    """
    n = int(input("type a number: "))
    for i in range(1, n + 1):
        print(i)


def loop_while() -> None:
    n = 0
    while True:
        n += 1
        if n == 10:
            break
        if n % 2 == 0:
            continue
        print(n)


def main() -> None:
    # loop_for()
    loop_while()


if __name__ == "__main__":
    main()
