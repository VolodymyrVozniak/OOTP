from .facade import Facade


class UI:
    def __init__(self):
        self.facade = Facade()

    def add_product(self, name, price, category):
        self.facade.add_product(name, price, category)

    def update_product(self, name, price, category):
        self.facade.update_product(name, price, category)

    def delete_product(self, name):
        self.facade.delete_product(name)

    def search_by_name(self, name):
        return self.facade.search_by_name(name)

    def search_by_category(self, category):
        return self.facade.search_by_category(category)

    def place_order(self, user, product_names):
        self.facade.place_order(user, product_names)
