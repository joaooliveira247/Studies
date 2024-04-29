class Bird:
    def fly(self) -> None:
        print(f"{self.__class__.__name__} is flying")


class Sparrow(Bird):
    def fly(self) -> None:
        return super().fly()


class Ostrich(Bird):
    def fly(self) -> None:
        print("Ostrich not fly")


def fly_plan(*inst: Bird) -> None:
    for animal in inst:
        animal.fly()


def main() -> None:
    p_1 = Sparrow()
    p_2 = Ostrich()
    fly_plan(p_1, p_2)
    print(isinstance(p_2, Bird))


if __name__ == "__main__":
    main()
