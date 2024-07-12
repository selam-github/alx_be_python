#main-0.py
import sys
from bank_account import BankAccount
def main():
    if len(sys.argv) < 3:
        print("Usage: python main-0.py <operation> <amount>")
        sys.exit(1)

    operation = sys.argv[1]
    try:
        amount = float(sys.argv[2])
    except ValueError:
        print("Amount must be a number.")
        sys.exit(1)

    account = BankAccount()

    if operation == 'deposit':
        account.deposit(amount)
           print(f"Deposited: ${amount}")
    elif operation == 'withdraw':
        success = account.withdraw(amount)
        if success:
            print(f"Withdrew: ${amount:.1f}")
        else:
            print("Insufficient funds.")
    else:
        print("Unknown operation. Use 'deposit' or 'withdraw'.")

    account.display_balance()
    if __name__ == "__main__":
    main()
