class A:
    def print_something(self):
        print("I'm on A")

class B(A):
    def print_something(self):
        print("I'm on B")

class C(A):
    def print_something(self):
        print("I'm on C")

class D(B, C):
    def print_something(self):
        print("I'm on D")

obj1 = A()
obj2 = B()
obj3 = C()
obj4 = D()

obj1.print_something()
obj2.print_something()
obj3.print_something()
obj4.print_something()