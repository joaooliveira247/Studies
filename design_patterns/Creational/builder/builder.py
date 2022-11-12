from abc import ABC, abstractmethod


class StringReprMixin:
    def __str__(self) -> str:
        params = ", ".join(
            [f"{k}={v}" for k, v in self.__dict__.items()]
        )

        return f"{self.__class__.__name__}({params})"

    def __repr__(self) -> str:
        return self.__str__()


class User(StringReprMixin):
    def __init__(self) -> None:
        self.fist_name: int = None
        self.last_name: int = None
        self.age: int = None
        self.phone_numbers: list[str] = []
        self.addresses: list[str] = []


class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self) -> User: pass

    @abstractmethod
    def add_firstname(self, firstname): pass

    @abstractmethod
    def add_lastname(self, lastname): pass

    @abstractmethod
    def add_age(self, age): pass

    @abstractmethod
    def add_phone(self, phone): pass

    @abstractmethod
    def add_address(self, address): pass


class UserBuilder(IUserBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._result = User()

    @property
    def result(self) -> User:
        return_data = self._result
        self.reset()
        return return_data

    def add_firstname(self, firstname):
        self._result.firstname = firstname
        return self

    def add_lastname(self, lastname):
        self._result.lastname = lastname
        return self

    def add_age(self, age):
        self._result.age = age
        return self

    def add_phone(self, phone):
        self._result.phone_numbers.append(phone)
        return self

    def add_address(self, address):
        self._result.addresses.append(address)
        return self


class UserDirector:
    def __init__(self, builder: UserBuilder) -> None:
        self._builder = builder

    def with_age(self, firstname, lastname, age) -> User:
        self._builder.add_firstname(firstname)\
            .add_lastname(lastname)\
            .add_age(age)
        return self._builder.result

    def with_address(self, firstname, lastname, address) -> User:
        self._builder.add_firstname(firstname)\
            .add_lastname(lastname)\
            .add_address(address)
        return self._builder.result


if __name__ == "__main__":
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)
    user1 = user_director.with_age('Luiz', 'Otávio', 30)
    user2 = user_director.with_address('Maria', 'Miranda', 'Av Brasil')
    print(user1)
    print(user2)
