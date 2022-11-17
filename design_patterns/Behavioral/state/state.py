from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    """ Context """

    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self) -> None:
        print("Tentando executar pending()")
        self.state.pending()
        print("Estado atual: ", self.state)
        print()

    def approve(self) -> None:
        print("Tentando executar approve()")
        self.state.approve()
        print("Estado atual: ", self.state)
        print()

    def reject(self) -> None:
        print("Tentando executar pending()")
        self.state.reject()
        print("Estado atual: ", self.state)
        print()


class OrderState(ABC):
    def __init__(self, order: Order) -> None:
        self.order = order

    def __str__(self) -> str:
        return self.__class__.__name__

    @abstractmethod
    def pending(self) -> None: ...

    @abstractmethod
    def approve(self) -> None: ...

    @abstractmethod
    def reject(self) -> None: ...


class PaymentPending(OrderState):
    def pending(self) -> None:
        print("Pagamento pendente")

    def approve(self) -> None:
        self.order.state = PaymentApproved(self.order)
        print("Pagamento aprovado")

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print("pagamento recusado")


class PaymentApproved(OrderState):
    def pending(self) -> None:
        self.order.state = PaymentPending(self.order)

    def approve(self) -> None:
        print("Pagamento aprovado")

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)


class PaymentRejected(OrderState):
    def pending(self) -> None:
        print("Pagamento recusado")

    def approve(self) -> None:
        print("pagamento recusado")

    def reject(self) -> None:
        print("Pagamento recusado")


if __name__ == "__main__":
    order = Order()
    order.pending()
    order.approve()
    order.pending()
    order.reject()
    order.pending()
    order.approve()
