import csv
from models.account import Account

class CSVService:
    @staticmethod
    def save_accounts(accounts, filename="accounts.csv"):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Balance", "Transactions"])
            for account in accounts.values():
                writer.writerow([account.name, account.balance, ";".join(account.transactions)])

    @staticmethod
    def load_accounts(filename="accounts.csv"):
        accounts = {}
        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    name, balance, transactions = row
                    account = Account(name, float(balance))
                    account.transactions = transactions.split(";")
                    accounts[name] = account
        except FileNotFoundError:
            print(f"{filename} not found, starting with an empty account list.")
        return accounts
