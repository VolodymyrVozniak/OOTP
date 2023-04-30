from abc import ABC, abstractmethod


class OrderCommand(ABC):
    @abstractmethod
    def execute(self):
        pass


class PlaceOrderCommand(OrderCommand):
    def __init__(self, order):
        self.order = order

    def execute(self):
        pass
