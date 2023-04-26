class Car:
    def __init__(self, driver, rate):
        self.driver = driver
        self.rate = rate

    def get_fare(self, distance):
        return distance * self.rate
    
class Pathao:
    def __init__(self):
        self.car = Car('Masud', 10)

    def get_a_ride(self, location, destination):
        self.car.get_fare(destination)