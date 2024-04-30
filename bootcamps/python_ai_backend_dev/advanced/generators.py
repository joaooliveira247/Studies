def my_generator(nums: list[int]):
    for num in nums:
        yield num * 2


def main() -> None:
    for i in my_generator([1, 2, 3, 4, 5]):
        print(i)


if __name__ == "__main__":
    main()
