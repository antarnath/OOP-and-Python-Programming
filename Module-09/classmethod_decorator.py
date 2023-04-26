class Shopping:
    mall = "Jamuna Future Park"
    def __init__(self, customer):
        self.customer = customer
        self.items = []
        self.total = 0
    @staticmethod
    def multiply(x, y):
        return x * y

    def add_to_total(self, amount):
        self.total += amount

    def opening_hour(cls, day):
        return cls.mall
        
    def add_to_card(self, item, price, quantity):
        item_total = price * quantity
        self.add_to_total(item_total)
        self.items.append(item)

    def checkout(self):
        pass
