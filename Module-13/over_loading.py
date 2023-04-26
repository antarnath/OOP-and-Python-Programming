# print(max(12, 45, 87, 12, 98, 45, 62, 458, -8))
# methode overloading
def add(num1, num2, num3=0):
    return num1 + num2 + num3

result = add(12, 13)
# print(result)
result = add(12, 13, 50)
# print(result)

def add2(*args, **kwargs):
    pass

# operator overloading
# print(12 + 13)

class Account:
    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance
    
    def __add__(self, other):
        return self.__balance + other.__balance
    
    def __eq__(self, o):
        return self.__balance == o.__balance

my_acccount = Account("Antar Nath", 90000)
her_account = Account("her", 90000)
print(my_acccount==her_account)
