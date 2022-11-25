from __future__ import annotations
from abc import ABC, abstractmethod


class BoxStructure(ABC):
    """ Component """
    @abstractmethod
    def print_contentent(self) -> None: ...

    @abstractmethod
    def get_price(self) -> float: ...

    def add(self, child: list[BoxStructure]) -> None: ...

    def remove(self, child: list[BoxStructure]) -> None: ...


class Box(BoxStructure):
    """ Composite """

    def __init__(self, name: str) -> None:
        self.name = name
        self._children: list[BoxStructure] = []

    def print_contentent(self) -> None:
        print(f"\n{self.name}:")
        for child in self._children:
            child.print_contentent()

    def get_price(self) -> float:
        return sum(
            [child.get_price() for child in self._children]
        )

    def add(self, child: list[BoxStructure]) -> None:
        for struct in child:
            self._children.append(struct)

    def remove(self, child: list[BoxStructure]) -> None:
        for struct in child:
            if struct in self._children:
                self._children.remove(child)


class Product(BoxStructure):
    """ Leaf """

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def print_contentent(self) -> None:
        print(self.name, self.price)

    def get_price(self) -> float:
        return self.price


if __name__ == "__main__":
    # Leaf
    camiseta1 = Product('camiseta1', 10)
    camiseta2 = Product('camiseta2', 10)
    camiseta3 = Product('camiseta3', 10)

    # Composite
    caixa_camisetas = Box('Caixa de camiseta')
    caixa_camisetas.add([camiseta1, camiseta2, camiseta3])

    # Leaf
    smartphone1 = Product('smartphone1', 10000)
    smartphone2 = Product('smartphone2', 10000)

    # Composite
    caixa_smartphones = Box('Caixa de Smartphones')
    caixa_smartphones.add([smartphone1, smartphone2])

    # Composite
    caixa_grande = Box('Caixa grande')
    caixa_grande.add([caixa_camisetas, caixa_smartphones])
    caixa_grande.print_contentent()
    print(caixa_grande.get_price())
