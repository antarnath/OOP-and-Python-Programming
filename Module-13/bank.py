class Account:

    def __init__(self, holder, initial_balanec):
        self._account_number = 165
        self.holder = holder
        self.__balance = initial_balanec


    def deposit(self, amount):

        print(f"Adding {amount} to your account")
        self.__balance += amount
    

    def withdraw(self, amount):

        print(f"Withdrawing {amount} from your account")
        self.__balance -= amount


class StudentAccount(Account):

    def __init__(self, holder, initial_balanec, school):

        self.school = school
        super().__init__(holder, initial_balanec)

    def get_balance(self):
        return self._account_number

rafsan = StudentAccount("Rafsan", 50000, "FEC")
# print(rafsan.__balance)
print(rafsan.holder)

rafsan.deposit(20000)

rafsan.deposit(35000)

rafsan.deposit(15000)
# rafsan.__balance = 0
# print(rafsan.__balance )
print(rafsan._account_number)
print(rafsan.get_balance())