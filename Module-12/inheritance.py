# inheritance

# base class will have only the common attributes and methods

class Device:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def re_sale(self):
        print("ready to sell again")

class Laptop(Device):
    def __init__(self, brand, price, color, disc_size):
        super().__init__(brand, price, color)
        self.dise_size = disc_size

    def run(self):
        print("Running the laptop")

    def __repr__(self):
        return f"Laptop {self.brand} : {self.price} : {self.color}"
    
    def purchase(self, money, discount):
        if money < (self.price - self.price * discount/100):
            return "No laptop for you"
        else:
            print("This device is for you")
            return money-self.price


class Phone:
    def __init__(self, brand, price, color, camera,sim_num):
        self.brand = brand
        self.price = price
        self.color = color
        self.camera = camera
        self.sim_num = sim_num

    def is_dual_sim(self):
        return self.sim_num > 1
    
    def __repr__(self):
        return f"Phone {self.brand} : {self.price} : {self.color}"
    
    def purchase(self, money):
        if money < self.price:
            return "No laptop for you"
        else:
            print("This device is for you")
            return money-self.price

class Watch:
    def __init__(self, brand, price, color, watch_type):
        self.brand = brand
        self.price = price
        self.color = color
        self.watch_type = watch_type
    
    def is_digital(self):
        return self.watch_type == "digital"

    def purchase(self, money):
        if money < self.price:
            return "No laptop for you"
        else:
            print("This device is for you")
            return money-self.price

class Manager:
    def __init__(self, name, salary, experience, designation):
        pass

    def withdraw_salary(self):
        pass

    def day_total_sales(self):
        pass

    def handle_customer_complain(self):
        pass

class SalePerson:
    def __init__(self, name, salary, experience, designation, comission):
        pass

    def withdraw_salary(self):
        pass
    def handle_customer(self):
        pass


lenovo = Laptop("Lenovo", 42000, "Black", "512gb")
hp = Laptop("HP", 35000, "silver", "250gb")
print(lenovo)
print(hp)

oppo = Phone("OPPO", 15000, "Black", "16mp", 2)
samsung = Phone("Samsung", 21000, "Silver", "48mp", 1)
print(oppo)
print(samsung)

hp.re_sale()
