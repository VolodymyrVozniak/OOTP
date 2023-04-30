from stock_strategy import StockStrategy


class InventoryObserver:
    def update(self, inventory):
        pass


class BasedOnUnitsStockStrategy(StockStrategy):
    def calculate_stock_level(self, product):
        return product.stock_level


class BasedOnValueStockStrategy(StockStrategy):
    def calculate_stock_level(self, product):
        return product.stock_level * product.price
