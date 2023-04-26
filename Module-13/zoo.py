from abc import ABC, abstractmethod

# Abstract base class
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    @property
    @abstractmethod
    def name(self):
        pass
    @abstractmethod
    def move(self):
        print("hanging on the branches of the trees")

class Monkey(Animal):
    def __init__(self):
        self.__name = "Monkey"
    def sing(self):
        print("Monkey is singing")
    
    def eat(self):
        print("eating banana")
    
    def move(self):
        print("moving aroung in the zoo")
        super().move()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

layka = Monkey()
print(layka)
layka.eat()
layka.move()
layka.name = "Moonkey"
print(layka.name)


