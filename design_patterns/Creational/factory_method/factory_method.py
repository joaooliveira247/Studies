from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print("Carro de luxo está buscando o cliente...")


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print("Carro popular está buscando o cliente...")


class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print("Moto de luxo está buscando o cliente...")


class MotoPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print("Moto popular está buscando o cliente...")


class VeiculoFactory(ABC):
    def __init__(self, type) -> None:
        self.carro = self.get_carro(type)

    @staticmethod
    @abstractmethod
    def get_carro(type: str) -> Veiculo:
        pass

    def buscar_cliente(self) -> None:
        self.carro.buscar_cliente()


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(type: str) -> Veiculo:
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


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(type: str) -> Veiculo:
        if type == "popular":
            return CarroPopular()
        raise "veiculo não encontrado."


if __name__ == "__main__":
    from random import choice

    veiculos_disponiveis_zona_norte = ["luxo", "popular", "moto", "moto_luxo"]
    veiculos_disponiveis_zona_sul = ["popular"]

    print("ZONA NORTE")
    for i in range(10):
        carro = ZonaNorteVeiculoFactory(
            choice(veiculos_disponiveis_zona_norte)
        )
        carro.buscar_cliente()

    print()

    print("ZONA SUL")
    for i in range(10):
        carro2 = ZonaSulVeiculoFactory(choice(veiculos_disponiveis_zona_sul))
        carro2.buscar_cliente()
