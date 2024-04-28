class Dog:
    def __init__(self, name: str, color: str, sleep: bool = True) -> None:
        self.name = name
        self.color = color
        self.sleep = sleep

    # garbage collector cares it
    def __del__(self):
        print("del dog")


def main() -> None:
    d_1 = Dog("Some name", "Some color")
    del d_1


if __name__ == "__main__":
    main()
