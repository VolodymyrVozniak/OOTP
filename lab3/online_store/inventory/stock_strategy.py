from abc import ABC, abstractmethod


class StockStrategy(ABC):
    @abstractmethod
    def calculate_stock_level(self, product):
        pass
