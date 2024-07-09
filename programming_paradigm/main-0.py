# main-0.py
import sys
from bank_account import BankAccount

def main():
    # Check if arguments are provided correctly
    if len(sys.argv) < 3:
        print("Usage: python main-0.py <operation> <amount>")
        print("Operations: deposit, withdraw")
        return
    
    operation = sys.argv[1]
    amount = float(sys.argv[2])

    account = BankAccount()

    if operation == "deposit":
        success = account.deposit(amount)
        if success:
            print(f"Deposited ${amount:.2f}")
        else:
            print("Invalid deposit amount. Amount must be positive.")
    
    elif operation == "withdraw":
        success = account.withdraw(amount)
        if success:
            print(f"Withdrew ${amount:.2f}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")
    
    else:
        print("Invalid operation. Operations allowed: deposit, withdraw")

    account.display_balance()

if __name__ == "__main__":
    main()
