class Account:
    def __init__(self,name,balance, min_bal):
        self.name = name
        self.balance = balance
        self.min_bal = min_bal

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_bal:
            self.balance -= amount
        else:
            print("Sorry!! Not Enough Funds...")

    def statement(self):
        print("Account balance: ${}".format(self.balance))

class Current(Account):

    def __init__(self, name, balance):
        super().__init__(name, balance, min_bal=-1000)

    def __str__(self):
        print("{}'s Current account balance: ${}".format(self.name,self.balance))


class Savings(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_bal=0)

    def __str__(self):
        print("{}'s Saving account balance: ${}".format(self.name,self.balance))





