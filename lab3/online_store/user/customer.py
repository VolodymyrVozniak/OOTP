from order.order import Order
from order.order_command import PlaceOrderCommand


class Customer:
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

    def place_order(self, product, quantity):
        order = Order(id, product, quantity, self)
        command = PlaceOrderCommand(order)
        # TODO: execute the command
