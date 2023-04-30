class Search:
    @staticmethod
    def search_by_name(catalog, name):
        return [product for product in catalog.get_products() if name in product.name]

    @staticmethod
    def search_by_category(catalog, category):
        return [product for product in catalog.get_products() if product.category == category]
