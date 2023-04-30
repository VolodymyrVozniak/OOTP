from inventory_observer import InventoryObserver


class Inventory:
    __instance = None

    def __new__(cls):
        if Inventory.__instance is None:
            Inventory.__instance = object.__new__(cls)
            Inventory.__instance.products = {}
            Inventory.__instance.observers = []
        return Inventory.__instance

    def add_product(self, product):
        self.products[product.id] = product
        self.notify_observers()

    def update_product(self, id, stock_level):
        self.products[id].stock

    def remove_product(self, id):
        del self.products[id]
        self.notify_observers()

    def get_product(self, id):
        return self.products.get(id, None)

    def get_all_products(self):
        return self.products.values()

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)
