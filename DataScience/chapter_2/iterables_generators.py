from typing import Generator


def generate_range(n: int) -> Generator:
    # generators can be used by every struct that implements __next__ method
    i = 0
    while i < n:
        yield i
        i += 1


def main() -> None:
    for i in generate_range(10):
        print(i)
    print("===================================")
    a = generate_range(5)
    print(next(a))
    print(next(a))
    print(next(a))
    # one way to consume all generator is using an iterator that will consume
    # all in one time, like a type cast
    print(list(a))

    evens_bellow_20: Generator = (i for i in generate_range(20) if i % 2 == 0)
    print(evens_bellow_20)

    # iterables

    names: list[str] = ["Alice", "Bob", "Charlie", "Debbie"]

    # not pythonic
    for i in range(len(names)):
        print(f"name {i} is {names[i]}")
    print("===========================")
    # not pythonic
    i = 0
    for name in names:
        print(f"name {i} is {names[i]}")
        i += 1
    print("==========================")
    # pythonic
    for i, name in enumerate(names):
        print(f"name {i} is name")


if __name__ == "__main__":
    main()
