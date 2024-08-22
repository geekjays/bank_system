from models.account import Account

class AccountService:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name: str, initial_balance: float) -> Account:
        if name in self.accounts:
            raise ValueError("Account with this name already exists")
        account = Account(name, initial_balance)
        self.accounts[name] = account
        return account

    def get_account(self, name: str) -> Account:
        if name not in self.accounts:
            raise ValueError("Account not found")
        return self.accounts[name]

    def deposit(self, name: str, amount: float):
        account = self.get_account(name)
        account.deposit(amount)

    def withdraw(self, name: str, amount: float):
        account = self.get_account(name)
        account.withdraw(amount)

    def transfer(self, from_name: str, to_name: str, amount: float):
        from_account = self.get_account(from_name)
        to_account = self.get_account(to_name)
        from_account.transfer(amount, to_account)

    def get_transaction_history(self, name: str):
        account = self.get_account(name)
        return account.get_transaction_history()
