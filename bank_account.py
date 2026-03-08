class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            raise ValueError("Deposit amount must be greater than zero")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            raise ValueError("Insufficient funds or invalid withdrawal amount")

    def get_balance(self):
        return self.balance