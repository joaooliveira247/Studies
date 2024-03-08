from icecream.icecream import ic


class CountingClicker:
    """A class can have a docstring, like functions"""

    # every class in python use PascalCase to nome it

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(count={self.count})"

    def __init__(self, count: int = 0) -> None:
        self.count = count

    def click(self, num_times: int = 1) -> None:
        self.count += num_times
        return

    def read(self) -> int:
        return self.count

    def reset(self) -> None:
        self.count = 0


class NoResetCountingClicker(CountingClicker):
    # python permit double inhehitance
    def reset(self) -> None: ...


def main() -> None:
    clicker1 = CountingClicker()
    clicker2 = CountingClicker(100)
    clicker3 = CountingClicker(count=1000)

    ic((clicker1, clicker2, clicker3))

    clicker = CountingClicker()
    clicker.click()
    clicker.click()
    assert clicker.read() == 2
    clicker.reset()
    assert clicker.read() == 0

    clicker2 = NoResetCountingClicker()
    assert clicker2.read() == 0
    clicker2.click()
    assert clicker2.read() == 1
    clicker2.reset()
    assert clicker2.read() == 1


if __name__ == "__main__":
    main()
