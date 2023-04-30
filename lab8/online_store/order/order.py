class Order:
    def __init__(self, user, products):
        self.user = user
        self.products = products

    def get_total(self):
        return sum(product.price for product in self.products)


class OrderHistory:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def get_orders(self):
        return self.orders
