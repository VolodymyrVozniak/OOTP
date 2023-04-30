from ..catalog import Catalog, Search, Product
from ..order import Order, OrderHistory


class Facade:
    def __init__(self):
        self.catalog = Catalog()
        self.order_history = OrderHistory()

    def add_product(self, name, price, category):
        product = Product(name, price, category)
        self.catalog.add_product(product)

    def update_product(self, name, price, category):
        self.catalog.update_product(name, price, category)

    def delete_product(self, name):
        self.catalog.delete_product(name)

    def search_by_name(self, name):
        return Search.search_by_name(self.catalog, name)

    def search_by_category(self, category):
        return Search.search_by_category(self.catalog, category)

    def place_order(self, user, product_names):
        products = []
        for product_name in product_names:
            for product in self.catalog.get_products():
                if product.name == product_name:
                    products.append(product)
                    break

        order = Order(user, products)
        self.order_history.add_order(order)
