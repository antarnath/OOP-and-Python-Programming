class Shop:
    
    card = []

    def __init__(self, buyer):
        self.buyer = buyer
    
    def add_to_card(self, item):
        self.card.append(item)

shopper_1 = Shop("Antar")
shopper_1.add_to_card("Tshirt")
shopper_1.add_to_card("Pant")
shopper_1.add_to_card("luggi")

print(shopper_1.card)

shopper_2 = Shop("Arnob")
shopper_2.add_to_card("shoes")
print(shopper_2.card)