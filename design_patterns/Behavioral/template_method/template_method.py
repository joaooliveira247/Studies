from abc import ABC, abstractmethod


class Abstract(ABC):
    def template_method(self) -> None:
        self.hook()
        self.operation_1()
        self.base_class_method()
        self.operation_2()

    def hook(self) -> None: ...

    def base_class_method(self) -> None:
        print("From abstract class.")

    @abstractmethod
    def operation_1(self) -> None: ...

    @abstractmethod
    def operation_2(self) -> None: ...


class ConcreteClass1(Abstract):
    def hook(self) -> None:
        print(
            f"i'm the hook of concrete class: {self.__class__.__name__}"
            )

    def operation_1(self) -> None:
        print("Operation 1 executed")

    def operation_2(self) -> None:
        print("Operation 2 executed")


class ConcreteClass2(Abstract):
    def operation_1(self) -> None:
        print("Operation 2 executed from another class")

    def operation_2(self) -> None:
        print("Operation 2 executed from another class ")


if __name__ == "__main__":
    c1 = ConcreteClass1()
    c1.template_method()

    print()

    c2 = ConcreteClass2()
    c2.template_method()
