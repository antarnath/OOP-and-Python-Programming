# Single inheritance: Single inheritance enables a derived class to inherit properties from a single parent class
#example:

class Parent:
    def func1(self):
        print('This is parent class')

class Child(Parent): #inherit Parent class 
    def func2(self):
        print('This is child class')

object = Child()
object.func1() # func1() it is parent class function Child class inherit parent class so accese parent class
object.func2()


# multiple inheritance: When a class can be derived from more than one base class this type of inheritance is called multiple inheritances

class Father:
    father_name = ""
    def father(self):
        print(self.father_name)
class Mother:
    mother_name = ""
    def mother(self):
        print(self.mother_name)

class Son(Father, Mother): # two class inherit and two class accese and two class
    def parents(self):
        print(self.father_name)
        print(self.mother_name)

son = Son()
son.father_name = "ABC"
son.mother_name = "XYZ"
son.parents()


# Multilevel Inheritance :In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class

class Employees(): 
 
   def Name(self): 
       print ("Employee Name: Khush")
 
class salary(Employees): # salary class inherit Employee class
   def Salary(self):
       print ("Salary: 10000")
 
class Designation(salary): # Designation class inherit salary class
   def desig(self):
       print ("Designation: Test Engineer")
 
call = Designation()
call.Name()
call.Salary()
call.desig()