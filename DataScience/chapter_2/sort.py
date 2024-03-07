from icecream.icecream import ic


def main() -> None:
    x: list[int] = [4, 1, 2, 3]
    # gen a new list with sorted values
    y = sorted(x)
    # alter the old list
    x.sort()
    ic((x, y))

    x = sorted([-4, 1, -2, 3], key=abs, reverse=True)
    ic(x)

if __name__ == "__main__":
    main()
