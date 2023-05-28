from online_store.store import Category, Product, Store, ShoppingCart, Order
from online_store.user import Authentication


if __name__ == "__main__":
    electronics = Category('Electronics')
    electronics.add_product(Product('Smartphone 1', 500, 15000))
    electronics.add_product(Product('Smartphone 2', 800, 10000))

    books = Category('Books')
    books.add_product(Product('Python Programming', 50, 200))
    books.add_product(Product('Clean Code', 40, 100))

    store = Store()
    store.add_category(electronics)
    store.add_category(books)
    smartphones = store.search_products('smartphone')
    sorted_electronics = store.sort_products(books, 'quantity')

    for smartphone in smartphones:
        print(smartphone)
    for electronic in sorted_electronics:
        print(electronic)

    cart = ShoppingCart()
    cart.add_item(electronics.products[0], 1)
    cart.add_item(books.products[1], 2)
    print(cart)

    order = Order(cart)
    auth = Authentication()
    auth.register('user1', 'password')
    if auth.login('user1', 'password'):
        order.verify_payment()
        order.ship()
        order.ship()
