from online_store import ProductFactory, Inventory, Customer, StoreManager

if __name__ == "__main__":
    factory = ProductFactory()
    product = factory.create_product('book', 1, 'Python for Data Science', 29.99, 100)

    inventory = Inventory()
    inventory.add_product(product)

    customer = Customer(1, 'John Doe', '123 Main St, Anytown USA')
    customer.place_order(product, 2)

    manager = StoreManager(1, 'Jane Smith', 'jane@example.com')
    inventory = Inventory()
    inventory.add_observer(manager)

    inventory = Inventory()
    product = inventory.get_product(1)
    product.stock_level = 50
    inventory.update_product(product)

    inventory = Inventory()
    inventory.remove_product(1)

