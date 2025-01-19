class BankAccount:
    def __init__(self,account_balance,initial_balance=None):
        self.account_balance = account_balance
        self.initial_balance = initial_balance

        account_balance = initial_balance

    def deposit(self,amount):
        return amount + self.account_balance


    def withdraw(self,amount):
        if self.account_balance < amount:
            return f"There is insufficient balance. {self.account_balance}"
        else:
            return self.account_balance - amount


    def display_balance(self):
        print(f"Your current balance is {self.account_balance}")