from services.account_service import AccountService
from services.csv_service import CSVService

def main():
    account_service = AccountService()
    accounts = CSVService.load_accounts()
    account_service.accounts = accounts

    while True:
        print("\n--- Banking System ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. View Transaction History")
        print("6. Save & Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter account name: ")
            balance = float(input("Enter initial balance: "))
            account_service.create_account(name, balance)
        elif choice == "2":
            name = input("Enter account name: ")
            amount = float(input("Enter deposit amount: "))
            account_service.deposit(name, amount)
        elif choice == "3":
            name = input("Enter account name: ")
            amount = float(input("Enter withdrawal amount: "))
            account_service.withdraw(name, amount)
        elif choice == "4":
            from_name = input("Enter your account name: ")
            to_name = input("Enter recipient account name: ")
            amount = float(input("Enter transfer amount: "))
            account_service.transfer(from_name, to_name, amount)
        elif choice == "5":
            name = input("Enter account name: ")
            history = account_service.get_transaction_history(name)
            print(f"Transaction History for {name}:")
            for transaction in history:
                print(transaction)
        elif choice == "6":
            CSVService.save_accounts(account_service.accounts)
            print("Accounts saved. Exiting.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
