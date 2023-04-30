from online_store.store import Category, Product, Store, ShoppingCart, Order
from online_store.user import Authentication


if __name__ == "__main__":
    electronics = Category('Electronics')
    electronics.add_product(Product('Smartphone', 500))
    electronics.add_product(Product('Tablet', 800))

    books = Category('Books')
    books.add_product(Product('Python Programming', 50))
    books.add_product(Product('Clean Code', 40))

    store = Store()
    store.add_category(electronics)
    store.add_category(books)
    sorted_products = store.sort_products('price')

    cart = ShoppingCart()
    cart.add_item(electronics.products[0], 1)
    cart.add_item(books.products[1], 2)

    order = Order(cart)
    auth = Authentication()
    auth.register('user1', 'password')
    if auth.login('user1', 'password'):
        order.verify_payment()

    order.ship()
