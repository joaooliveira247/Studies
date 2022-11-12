from __future__ import annotations
from copy import deepcopy


class StringReprMixin:
    def __str__(self) -> str:
        params = ", ".join(
            [f"{k}={v}" for k, v in self.__dict__.items()]
        )
        return f"{self.__class__.__name__}({params})"

    def __repr__(self) -> str:
        return self.__str__()


class Person(StringReprMixin):
    def __init__(self, first_name: str, last_name: str) -> None:
        self.firstname = first_name
        self.lastname = last_name
        self.addresses: list[Address] = []

    def add_address(self, address: Address) -> None:
        self.addresses.append(address)

    def clone(self) -> Person:
        return deepcopy(self)


class Address(StringReprMixin):
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number


if __name__ == "__main__":
    joao = Person("joao", "alberto")
    endereco_joao = Address("Av. Brasil", "250A")
    joao.add_address(endereco_joao)

    pai_joao = joao.clone()
    pai_joao.firstname = "carlos"

    print(joao)
    print(pai_joao)
