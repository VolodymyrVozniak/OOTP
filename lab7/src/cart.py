from .item import CartItem
from .cart_memento import CartMemento
from .cart_visitor import CartVisitor


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        for cart_item in self.items:
            if cart_item.item_id == item.item_id:
                cart_item.quantity += item.quantity
                return
        self.items.append(item)

    def remove_item(self, item_id):
        for cart_item in self.items:
            if cart_item.item_id == item_id:
                self.items.remove(cart_item)
                return

    def get_total_price(self):
        total_price = 0
        for cart_item in self.items:
            total_price += cart_item.get_total_price()
        return total_price

    def accept(self, visitor):
        visitor.visit(self)

    def create_memento(self):
        return CartMemento(self.items)

    def restore_memento(self, memento):
        self.items = memento.get_state()
