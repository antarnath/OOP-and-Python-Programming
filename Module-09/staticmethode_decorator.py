class Shopping:
    def __init__(self, customer):
        self.customer = customer
        self.items = []
        self.total = 0
    @staticmethod
    def multiply(x, y):
        return x * y

    def add_to_total(self, amount):
        self.total += amount

    def add_to_card(self, item, price, quantity):
        item_total = price * quantity
        self.add_to_total(item_total)
        self.items.append(item)

    def checkout(self):
        pass

result = Shopping.add_to_total(40)