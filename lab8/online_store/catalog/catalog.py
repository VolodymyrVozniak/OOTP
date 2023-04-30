class Catalog:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def update_product(self, product_name, price, category):
        for product in self.products:
            if product.name == product_name:
                product.price = price
                product.category = category

    def delete_product(self, product_name):
        self.products = [product for product in self.products if product.name != product_name]

    def get_products(self):
        return self.products
