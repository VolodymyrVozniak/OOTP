class CartVisitor:
    def visit(self, cart):
        pass


class DiscountVisitor(CartVisitor):
    def __init__(self, discount):
        self.discount = discount

    def visit(self, cart):
        for cart_item in cart.items:
            cart_item.price -= cart_item.price * self.discount
