class Vehicle:
    def __init__(self, name, license, price):
        self.name = name
        self.license = license
        self.price = price
        print("Vehicle class init call")

    def start(self):
        print(f"{self.name} started")

class Bus(Vehicle):
    def __init__(self, name, license, price, seat, ticket_price):
        self.seat = seat
        self.availeable_seat = seat
        self.ticket_price = ticket_price
        print("Bus init called")
        super().__init__(name, license, price)
    
    def sell_ticket(self, customer_name, quantity, amount):
        self.availeable_seat -= quantity
        remainder = amount - self.ticket_price * quantity
        if remainder >=0 :
            return Ticket(customer_name)
        return "no ticket for you"


class AcBus(Bus):
    def __init__(self):
        print("Ac bus created")

class MiniBus(Bus):
    def __init__(self):
        print("Mini bus created")
        super().__init__("Mini Mini", "DKA125", 1200000, 50, 450)
        # Bus.__init__(self, "Mini Mini", "DKA125", 1200000, 50, 450)


class Ticket:
    def __init__(self, owner):
        self.owner = owner

mini = MiniBus()
# print(mini.seat)
# a = mini.sell_ticket("Antar", 20, 500)
# print(mini.availeable_seat)
# print(a)

print(mini.name)