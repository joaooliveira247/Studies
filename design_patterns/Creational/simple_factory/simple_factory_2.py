from abc import ABC, abstractclassmethod
from random import choice


class Veiculo(ABC):
    @abstractclassmethod
    def buscar_cliente(self) -> None:
        ...


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print("Carro de luxo está buscando cliente ...")


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print("Carro popular está buscando cliente ...")


class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print("Moto de luxo popular está buscando cliente ...")


class MotoPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print("Moto popular está buscando cliente ...")


class VeiculoFactory:
    def __init__(self, type: str) -> None:
        self.carro = self.get_veiculo(type)

    @staticmethod
    def get_veiculo(type: str) -> Veiculo:
        match type:
            case "luxo":
                return CarroLuxo()
            case "popular":
                return CarroPopular()
            case "moto":
                return MotoPopular()
            case "moto_luxo":
                return MotoLuxo()
        raise "veiculo não encontrado."

    def buscar_cliente(self) -> None:
        self.carro.buscar_cliente()


if __name__ == "__main__":
    available_cars = ["luxo", "popular", "moto", "moto_luxo"]

    for i in range(10):
        carro = VeiculoFactory(choice(available_cars))
        carro.buscar_cliente()
