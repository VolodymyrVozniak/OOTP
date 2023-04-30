from online_store.ui import UI, Proxy, Facade
from online_store.order import User


if __name__ == "__main__":
    ui = UI()
    user = User('John', 'john@example.com', 'password')
    proxy = Proxy(ui.facade, user)

    proxy.add_product('Product 1', 10.0, 'Category 1')
    proxy.update_product('Product 1', 15.0, 'Category 2')

    result = ui.search_by_name('Product 1')
    for product in result:
        print(product.name, product.price, product.category)

    result = ui.search_by_category('Category 1')
    for product in result:
        print(product.name, product.price, product.category)

    ui.place_order(user, ['Product 1', 'Product 2'])
