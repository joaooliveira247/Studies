from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep


class IUser(ABC):
    """ Subject interface """

    fist_name: str
    last_name: str

    @abstractmethod
    def get_addresses(self) -> list[dict]: ...

    @abstractmethod
    def get_all_user_data(self) -> dict: ...


class RealUser(IUser):
    """ Real subject """

    def __init__(self, first_name: str, last_name: str) -> None:
        sleep(2)
        self.first_name = first_name
        self.last_name = last_name

    def get_addresses(self) -> list[dict]:
        sleep(2)
        return [
            {'rua': 'Av. Brasi - RJ', 'numero': 2450}
        ]

    def get_all_user_data(self) -> dict:
        sleep(2)
        return {
            "cpf": "999.666.888-22",
            "rg": "081747818928-8"
        }


class UserProxy(IUser):
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

        self._real_user: RealUser
        self._cached_addresses: list[dict]
        self._all_user_data: dict

    def get_real_user(self) -> None:
        if not hasattr(self, "_real_user"):
            self._real_user = RealUser(self.first_name, self.last_name)

    def get_addresses(self) -> list[dict]:
        self.get_real_user()

        if not hasattr(self, "_cached_addresses"):
            self._cached_addresses = self._real_user.get_addresses()

        return self._cached_addresses

    def get_all_user_data(self) -> dict:
        self.get_real_user()

        if not hasattr(self, "_all_user_data"):
            self._all_user_data = self._real_user.get_all_user_data()

        return self._all_user_data


if __name__ == "__main__":
    joao = UserProxy('joao', 'oliveira')

    # Responde instantaneamente
    print(joao.first_name)
    print(joao.last_name)

    # Responde em 6 segundos porque vem do real subject
    print(joao.get_all_user_data())
    print(joao.get_addresses())

    # Responde instantaneamente (porque está em cache)
    print('CACHED DATA:')
    for i in range(50):
        print(joao.get_addresses())
