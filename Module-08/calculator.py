class Calculator:
    def add(self, num1, num2):
        return num1 + num2
    def subtract(self, num1, num2):
        return num1 - num2
    def multiply(self, num1, num2):
        return num1 * num2
    def divide(self, num1, num2):
        return num1 / num2

my_calculator = Calculator()
add = my_calculator.add(100, 200)
print(add)

subtract = my_calculator.subtract(200, 175)
print(subtract)

multiply = my_calculator.multiply(200, 3)
print(multiply)

divide  = my_calculator.divide(200, 5)
print(divide)