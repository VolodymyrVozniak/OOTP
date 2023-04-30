class Store:
    def __init__(self):
        self.categories = []

    def add_category(self, category):
        self.categories.append(category)

    def search_products(self, query):
        result = []
        for category in self.categories:
            for product in category:
                if query.lower() in product.name.lower():
                    result.append(product)
        return result

    def filter_products(self, category_name=None, min_price=None, max_price=None):
        result = []
        for category in self.categories:
            if category_name and category_name != category.name:
                continue
            for product in category:
                if min_price and product.price < min_price:
                    continue
                if max_price and product.price > max_price:
                    continue
                result.append(product)
        return result

    def sort_products(self, products, by='name'):
        if by == 'name':
            return sorted(products, key=lambda p: p.name)
        elif by == 'price':
            return sorted(products, key=lambda p: p.price)
        else:
            raise ValueError('Invalid sort parameter')
    
    def get_products_by_category(self, category_name):
        for category in self.categories:
            if category.name == category_name:
                return category
        raise ValueError(f'Category not found: {category_name}')
