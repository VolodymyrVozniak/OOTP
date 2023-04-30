from inventory.inventory import InventoryObserver

class StoreManager(InventoryObserver):
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def add_product(self, product):
        pass

    def update_product(self, id, stock_level):
        pass

    def remove_product(self, id):
        pass

    def update(self, inventory):
        pass
