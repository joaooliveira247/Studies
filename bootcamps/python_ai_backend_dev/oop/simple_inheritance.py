class Vehicle:
    def __init__(self, color: str, tires: int, license_plate: str) -> None:
        self.color = color
        self.license_plate = license_plate
        self.tires = tires

    def __str__(self) -> str:
        return (
            f"({self.__class__.__name__}) "
            f"{', '.join([f'{key}={value}' for key,value in self.__dict__.items()])}"
        )

    def __repr__(self) -> str:
        return self.__str__()

    def turn_on(self) -> None:
        print(f"turn on {self.__class__.__name__}")


class Car(Vehicle): ...


class Motorcycle(Vehicle): ...


class Truck(Vehicle):
    def __init__(
        self,
        color: str,
        tires: int,
        license_plate: str,
        load: bool,
    ) -> None:
        super().__init__(color, tires, license_plate)
        self.load = load

    def is_load(self) -> None:
        print(
            f"{self.__class__.__name__} is {'' if self.load else 'not'} load",
        )


def main() -> None:
    v_1 = Truck("Yellow", 6, "ABC-123", False)
    print(v_1)
    v_1.turn_on()
    v_1.is_load()
    v_2 = Car("Red", 4, "DEF-456")
    v_2.turn_on()


if __name__ == "__main__":
    main()
