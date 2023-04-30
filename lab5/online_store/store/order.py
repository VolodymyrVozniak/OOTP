class Order:
    def __init__(self, cart):
        self.cart = cart
        self.status = NewOrderState()

    def cancel(self):
        self.status.cancel()

    def verify_payment(self):
        self.status.verify_payment()

    def ship(self):
        self.status.ship()


class OrderState:
    def cancel(self):
        raise NotImplementedError()

    def verify_payment(self):
        raise NotImplementedError()

    def ship(self):
        raise NotImplementedError()


class NewOrderState(OrderState):
    def cancel(self):
        self._update_status('cancelled')

    def verify_payment(self):
        self._update_status('paid')

    def _update_status(self, status):
        print(f'Order status updated: {status}')
        self.status = status


class PaidOrderState(OrderState):
    def cancel(self):
        self._update_status('cancelled')

    def verify_payment(self):
        print('Payment already verified')

    def ship(self):
        self._update_status('shipped')

    def _update_status(self, status):
        print(f'Order status updated: {status}')
        self.status = status


class ShippedOrderState(OrderState):
    def cancel(self):
        print('Order already shipped')

    def verify_payment(self):
        print('Payment already verified')

    def ship(self):
        print('Order already shipped')
