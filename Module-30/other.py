# s = 'I am local'

# def antar():
#     print(s)


# from math import pi
# # print(pi)
# pi = 34.11
# def outer_scope():
#     # pi=33.11
#     def inner_scope():
#         # pi = 3.345
#         print(pi)
#     inner_scope()
#     # print(pi)
# outer_scope()
# # print(pi)

# lst = [(x,y) for x in [1, 2, 5, 6, 7] for y in [3, 4, 8, 9, 10] ]
# print(len(lst))


# class School:
#     school_name = "ABC School"
#     def __init__(self, name):
#         self.name = name
    
#     def printname(self):
#         print(self.name)

#     @classmethod
#     def get_name(cls):
#         cls.school_name = "ABCDE School"

# s = School('antar')
# # s.printname()
# # print(s.school_name)
# School.get_name()

# a = School('naim')
# print(a.school_name)


# abstract class / method
from abc import ABC, abstractmethod
class Vechicle(ABC):
    @abstractmethod
    def go(self):
        print('a car is going')
    @abstractmethod
    def run(self):
        print('a car is runing')

class Car(Vechicle):
    def go(self):
        print('i am a car')
    def run(self):
        pass

c = Car()
c.go()