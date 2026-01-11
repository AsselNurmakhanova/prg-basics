class Bank:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0
    def display_balance(self):
        print(f"Account Number: {self.account_number}, Balance: ${self.balance:.2f}")
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}")
        else:
            self.balance -= amount
            print("Insufficient funds on the account")