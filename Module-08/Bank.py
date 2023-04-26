class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 10000
    
    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            return f"no money for you. Minimum withdraw: {self.min_withdraw}"
        elif amount > self.max_withdraw:
            return f"you crossed max limit: {self.max_withdraw}"
        elif amount > self.balance:
            return "you are broke !!! NO money for you"
        else :
            self.balance = self.balance - amount
            return f"Here is your money : {amount}"
    def deposit(self, amount):
        self.balance = self.balance + amount

my_bank = Bank(5000)
replay = my_bank.withdraw(200)
print(replay)
print(my_bank.balance)
new_amount = my_bank.get_balance()
print(new_amount)
my_bank.deposit(3000)
print(my_bank.balance)