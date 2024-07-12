#bank_account.py
class BankAccount:
    def __init__(self, account_balance , initial_balance=0):
        self.current_balance = account_balance 


    def deposit(self, amount):
        self.current_balance += amount
        return  self.current_balance

    def withdraw(self, amount):
        if amount <=  self.current_balance :
             self.current_balance  -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current balance: ${self.account_balance:.0f}")

