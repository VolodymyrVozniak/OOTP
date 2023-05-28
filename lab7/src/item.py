class CartItem:
    def __init__(self, item_id, name, price, quantity):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity
    
    def __str__(self):
        return f"CartItem(item_id={self.item_id}, name={self.name}, price={self.price}, quantity={self.quantity})"
