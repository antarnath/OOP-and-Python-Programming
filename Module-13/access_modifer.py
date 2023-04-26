class Account:
    def __init__(self, holder):
        self._account_holder = holder
    


class StudentAccount(Account):
    def __init__(self, holder, balance, school):
        self.__balance = balance
    
    def withdraw(self, amount):
        if amount > self.__balance:
            return "no money for you"
        self.__balance -= amount
        return amount

    def deposit(self, amount):
        if amount < 0:
            return "Negative amount can not be added"
        self.__balance += amount

    def get_balance(self):
        return self.__balance

antar = StudentAccount("Antar", 12000, "FEC")

antar.deposit(50000)
antar.deposit(15000)
print(antar.get_balance())

# print(dir(antar))
antar._StudentAccount__balance = 0
print(antar._StudentAccount__balance)
