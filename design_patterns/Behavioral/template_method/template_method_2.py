from abc import ABC, abstractmethod


class Pizza(ABC):
    """Classe abstrata"""

    def prepare(self) -> None:
        """ Template method """
        self.hook_before_add_ingredients()
        self.add_ingredients()
        self.hook_after_add_ingredients()
        self.cook()
        self.cut()
        self.serve()

    def hook_before_add_ingredients(self) -> None:
        ...

    def hook_after_add_ingredients(self) -> None:
        ...

    def cut(self) -> None:
        print(
            f"{self.__class__.__name__}: Cortando pizza."
        )

    def serve(self) -> None:
        print(
            f"{self.__class__.__name__}: Servindo pizza"
        )

    @abstractmethod
    def add_ingredients(self) -> None: ...

    @abstractmethod
    def cook(self) -> None: ...


class Amoda(Pizza):
    def add_ingredients(self) -> None:
        print(
            "Amoda - adicionando ingredientes: presunto, queijo"
        )

    def cook(self) -> None:
        print(
            "Amoda - cozinhando por 45 min no forno a lenha"
        )


class Veg(Pizza):
    def hook_before_add_ingredients(self) -> None:
        print(
            "Veg - Lavando ingredientes"
        )

    def add_ingredients(self) -> None:
        print(
            "Veg - adicionando ingredientes: ingrediente veganos"
        )

    def cook(self) -> None:
        print(
            "Veg - cozinhando por 5 min em forno comum"
        )


if __name__ == "__main__":
    a_moda = Amoda()
    a_moda.prepare()

    print()

    veg = Veg()
    veg.prepare()
