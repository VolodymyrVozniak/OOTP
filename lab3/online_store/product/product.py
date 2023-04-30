from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, id, name, price, stock_level):
        self.id = id
        self.name = name
        self.price = price
        self.stock_level = stock_level

    @abstractmethod
    def get_type(self):
        pass
