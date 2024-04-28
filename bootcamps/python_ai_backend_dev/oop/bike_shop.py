class Bike:
    def __init__(
        self,
        color: str,
        model: str,
        year: int,
        value: float,
    ) -> None:
        self.color = color
        self.model = model
        self.year = year
        self.value = value

    def __str__(self) -> str:
        return (
            f"({self.__class__.__name__}) "
            f"{", ".join([f'{key}={value}' for key,value in self.__dict__.items()])}"
        )

    def honk(self) -> None:
        print("Plim plim....")

    def stop(self) -> None:
        print("Stoping Bike")
        print("Bike stoped!")

    def run(self) -> None:
        print("Vrummmmm...")

    def get_color(self) -> str:
        return self.color


def main() -> None:
    b1 = Bike("Red", "Caloi", 2016, 600)
    b1.honk()
    b1.run()
    b1.stop()
    print(b1.color, b1.model, b1.year, b1.value)
    print(b1.get_color())


if __name__ == "__main__":
    main()
