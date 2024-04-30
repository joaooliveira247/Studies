from __future__ import annotations


class MyIterator:
    def __init__(self, nums: list[int]) -> None:
        self.nums = nums
        self._pointer = 0

    def __iter__(self) -> MyIterator:
        return self

    def __next__(self) -> int:
        try:
            num = self.nums[self._pointer]
            self._pointer += 1
            return num * 2
        except IndexError:
            raise StopIteration


def main() -> None:
    for i in MyIterator(nums=[1, 2, 3, 4]):
        print(i)


if __name__ == "__main__":
    main()
