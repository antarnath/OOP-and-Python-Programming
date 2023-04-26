""" Manages Bank Account """
class Account:
    accID = 1
    def __init__(self, name, age, nid_number, balance):
        self.name = name
        self.age = age
        self.nid_number = nid_number
        self.balance = balance

        # update acc id
        self.account_id = Account.accID
        Account.accID += 1

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

acc1 = Account("Antar", 21, 12345, 500)
# acc2 = Account("kona", 21, 23456, 1000)
# acc3 = Account("Arnob", 10, 399876, 77777)

# print(acc1.account_id)
# print(acc2.account_id)
# print(acc3.account_id)
acc1.deposit(1500)
print(acc1.balance)

acc1.withdraw(1000)
print(acc1.balance)
