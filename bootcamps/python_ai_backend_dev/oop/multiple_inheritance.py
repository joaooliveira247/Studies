class Animal:
    def __init__(self, paws: int, color: str) -> None:
        self.color = color
        self.paws = paws

    def __str__(self) -> str:
        return (
            f"({self.__class__.__name__}) "
            f"{', '.join([f'{key}={value}' for key,value in self.__dict__.items()])}"
        )

    def __repr__(self) -> str:
        return self.__str__()


class Mammal(Animal):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)


class Bird(Animal):
    def __init__(self, nozzle_color: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.nozzle_color = nozzle_color


class Dog(Mammal): ...


class Cat(Mammal): ...


class Lion(Mammal): ...


class TalkMixin:
    def talk(self) -> None:
        print("I'm talking")


class Platypus(Mammal, Bird, TalkMixin):
    def __init__(self, **kwargs) -> None:
        print(Platypus.__mro__)
        super().__init__(**kwargs)


class TalkMixin:
    def talk(self) -> None:
        print("I'm talking")


def main() -> None:
    cat = Cat(paws=4, color="Black")
    print(cat)
    platypus = Platypus(paws=2, color="Red", nozzle_color="Orange")
    print(platypus)
    platypus.talk()


if __name__ == "__main__":
    main()
