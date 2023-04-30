class Proxy:
    def __init__(self, facade, user):
        self.facade = facade
        self.user = user

    def add_product(self, name, price, category):
        if self.is_authorized('add_product'):
            self.facade.add_product(name, price, category)

    def update_product(self, name, price, category):
        if self.is_authorized('update_product'):
            self.facade.update_product(name, price, category)

    def delete_product(self, name):
        if self.is_authorized('delete_product'):
            self.facade.delete_product(name)

    def search_by_name(self, name):
        return self.facade.search_by_name(name)

    def search_by_category(self, category):
        return self.facade.search_by_category(category)

    def place_order(self, product_names):
        if self.is_authorized('place_order'):
            self.facade.place_order(self.user, product_names)

    def is_authorized(self, action):
        # check if user is authorized to perform the given action
        # return True if authorized, False otherwise
        pass
