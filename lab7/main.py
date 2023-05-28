from src import CartItem, Cart, DiscountVisitor, PaymentGateway


if __name__ == "__main__":
    # Create a cart and add some items
    cart = Cart()
    cart.add_item(CartItem(1, 'Product A', 10, 2))
    cart.add_item(CartItem(2, 'Product B', 20, 1))
    print(cart.get_total_price())

    # Apply a 10% discount to the cart
    cart.accept(DiscountVisitor(0.1))
    print(cart.get_total_price())

    # Save and restore cart
    memento = cart.create_memento()
    print(cart)
    cart.add_item(CartItem(3, 'Product C', 30, 5))
    print(cart)
    cart.restore_memento(memento)
    print(cart)

    # Process the payment
    payment_gateway = PaymentGateway('API_KEY')
    payment_gateway.process_payment(cart.get_total_price())
