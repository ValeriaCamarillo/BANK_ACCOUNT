class BankAccount:

    def __init__(self, int_rate=0.01, balance=0): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_account_info(self):
        print(f"Your Balance is: {self.balance}")
        return self.balance

    def yield_interest(self):
        self.balance += self.balance * self.int_rate

class User:

    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.balance = balance
        self.checking = BankAccount(.1, 1000)

checking = BankAccount()
savings = BankAccount(.1, 200000)
checking.deposit(1000)
print(checking.balance)

checking.withdraw(5)
print(f"Insufficient funds: charging a $5 fee: {checking.balance}")
print(f"Your Account Balance is: {checking.balance}")

checking.yield_interest()
print(checking.balance)

user1 = User('val', 'val@gmail.com', 1000 )
user2 = User('vale', 'vale@gmail.com', 1000)
print(user1.balance)
print(user1.email)
print(user1.name)
print(user2.balance)
print(user2.email)
print(user2.name)
print(user1.checking.deposit(50))

