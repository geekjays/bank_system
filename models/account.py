
from decorators.logging_decorator import log_operation

class Account:
    def __init__(self, name: str, balance: float):
        self.name = name
        self.balance = balance
        self.transactions = []

    @log_operation
    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self.transactions.append(f"Deposited {amount}")

    @log_operation
    def withdraw(self, amount: float):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.transactions.append(f"Withdrew {amount}")

    @log_operation
    def transfer(self, amount: float, to_account: 'Account'):
        self.withdraw(amount)
        to_account.deposit(amount)
        self.transactions.append(f"Transferred {amount} to {to_account.name}")

    @log_operation
    def get_transaction_history(self):
        return self.transactions.copy()

    def __str__(self):
            return f"Account({self.name}, Balance: {self.balance})"
