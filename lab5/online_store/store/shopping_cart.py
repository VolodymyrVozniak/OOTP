class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append((product, quantity))

    def remove_item(self, item):
        self.items.remove(item)

    def total_price(self):
        return sum([product.price * quantity for product, quantity in self.items])
