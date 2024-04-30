def first() -> None:
    print("run first")

    def func_inside() -> None:
        print("run func inside first")

    def func_2() -> None:
        print("run func 2")

    func_inside()
    func_2()


def main() -> None:
    first()


if __name__ == "__main__":
    main()
