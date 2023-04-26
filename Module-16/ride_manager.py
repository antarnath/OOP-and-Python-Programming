class RideManager:
    def __init__(self):
        print("Ride manager activated")
        self.__availavle_cars = []
        self.__availavle_bikes = []
        self.__availavle_cng = []

    def add_a_vehicle(self,vehicle_type, vehicle):
        if vehicle_type == 'car':
            self.__availavle_cars.append(vehicle)
        elif vehicle_type == 'bike':
            self.__availavle_bikes.append(vehicle)
        else:
            self.__availavle_cng.append(vehicle)

    def get_available_cars(self):
        return self.__availavle_cars

    def find_a_vehicle(self, rider, vehicle_type, destination):
        if vehicle_type == 'car':
            if len(self.__availavle_cars) == 0:
                print("sorry no cars is available")
                return False
            for car in self.__availavle_cars:
                print("potential", rider.location, car.driver.location)
                if abs(rider.location - car.driver.location) < 10:
                    print('find a match for you')
                    return True

uber = RideManager()