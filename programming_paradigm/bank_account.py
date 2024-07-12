#bank_account.py
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance  += amount
            print(f"Deposited:  ${amount:.1f}")
        else:
            print("Invalid deposit amount. Amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew:  ${amount}")
            return True
        else:
            print("Insufficient funds or invalid withdrawal amount.")
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.1f}")

