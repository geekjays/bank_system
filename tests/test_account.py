import unittest
from models.account import Account

class TestAccount(unittest.TestCase):
    def test_deposit(self):
        account = Account("Test", 100)
        account.deposit(50)
        self.assertEqual(account.balance, 150)

    def test_withdraw(self):
        account = Account("Test", 100)
        account.withdraw(50)
        self.assertEqual(account.balance, 50)

    def test_transfer(self):
        account1 = Account("Test1", 100)
        account2 = Account("Test2", 50)
        account1.transfer(50, account2)
        self.assertEqual(account1.balance, 50)
        self.assertEqual(account2.balance, 100)

    def test_withdraw_insufficient_funds(self):
        account = Account("Test", 50)
        with self.assertRaises(ValueError):
            account.withdraw(100)

    def test_transfer_insufficient_funds(self):
        account1 = Account("Test1", 50)
        account2 = Account("Test2", 100)
        with self.assertRaises(ValueError):
            account1.transfer(100, account2)

    def test_deposit_negative_amount(self):
        account = Account("Test", 100)
        with self.assertRaises(ValueError):
            account.deposit(-50)


if __name__ == "__main__":
    unittest.main()
