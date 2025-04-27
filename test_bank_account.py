import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Alice", 1000)

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500)

    def test_withdraw(self):
        self.account.withdraw(300)
        self.assertEqual(self.account.get_balance(), 700)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(2000)

    def test_negative_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_negative_withdrawal(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-50)

    def test_zero_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    def test_withdraw_full_balance(self):
        self.account.withdraw(1000)
        self.assertEqual(self.account.get_balance(), 0)

    def test_multiple_transactions(self):
        self.account.deposit(200)
        self.account.withdraw(100)
        self.account.deposit(300)
        self.assertEqual(self.account.get_balance(), 1400)
