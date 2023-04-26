class Shop:
    def __init__(self, name):
        self.name = name
        self.card = []

    
    def add_to_cart(self, item, price, quantity):
        self.card.append({"name": item, "price": price, "quantity": quantity})

    def checkout(self, amount):
        price = 0
        for item in self.card:
            price = price + item["price"] * item["quantity"]
        print(price)
        if amount < price:
            return f"Please give me more money : {price - amount}"
        elif amount > price:
            return f"Here is the items and extra money :{amount - price}"
        else:
            return "here are the items "

shopping  = Shop("Antar")
shopping.add_to_cart("shirt", 400, 3)
shopping.add_to_cart("shoes", 899, 4)
shopping.add_to_cart("pant", 1400, 2)

shopping.checkout(5000)