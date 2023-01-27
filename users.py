from re import A
from bank_account import BankAccount, checking

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdraw(self, amount):
        self.account.withdraw(amount)

    def transfer_money(self, amount, other_user):
        self.make_withdraw(amount)
        other_user.make_deposit(amount)
    
    def display_user_balance(self):
        print(f"Your Balance is: {self.balance}")
        return self.balance

valeria = User('valeria', 'valeria@gmail.com')
valeria.make_deposit(2000)
beverly = User('beverly', 'beverly@hotmail.com')
valeria.transfer_money(1000, beverly)
print(valeria.account.balance)
print(beverly.account.balance)