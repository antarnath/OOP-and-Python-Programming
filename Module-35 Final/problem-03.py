# 4 type of scope in python
# 1. Local scope
# 2. Global scope
# 3. Enclosed scope
# 4. Build-in scope

# 1. Local scope:
num = 0  #defined outside the function, so it is not a local variable 
def demo():
    num = 1 #local variable that is declared and printed inside the function
    print(num) #output 1
demo()
print(num) #output 0

# 2.Global scope
def demo():
    print(Str) #print global variable
Str = "You are clever" #declared a global variable Str
demo()

# 3.Enclosed scope
x = "global" #declared a global variable x
def func_outer():
    x = "local" # local variable x declared function of func_outer
    def func_inner():
        x = "nonlocal" # nonlocal variable x declared function of func_inner
        print("inner:", x) # output inner: nonlocal
    func_inner() # called func_inner
    print("outer:", x) #output outer: local x value not change in func_inner function
func_outer() # called func_outer function
print(x) #output global


# 4. build-in scope
from math import pi # pi import math module
def func_outer():
    pi = 31.44 #local variable x declared function of func_outer
    def func_inner():
        pi = 33.55 # nonlocal variable x declared function of func_inner
        print(pi) #output 33.55 not change build-in pi value
    func_inner()  # called func_inner
    print(pi) #output 31.44 not change build-in value
func_outer() # called func_outer function
print(pi) #output 3.141592653589793 build-in value
