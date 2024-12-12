import unittest
from BankAccount import BankAccount


class TestBankAccount(unittest.TestCase):
    def test_create_account_with_positive_balance(self):
        account = BankAccount("12345", 100.0)
        self.assertEqual(account.get_balance(), 100.0)

    def test_create_account_with_negative_balance(self):
        with self.assertRaises(ValueError):
            BankAccount("12345", -100.0)

    def test_deposit_positive_amount(self):
        account = BankAccount("12345", 100.0)
        account.deposit(50.0)
        self.assertEqual(account.get_balance(), 150.0)

    def test_deposit_zero_or_negative_amount(self):
        account = BankAccount("12345", 100.0)
        with self.assertRaises(ValueError):
            account.deposit(0)
        with self.assertRaises(ValueError):
            account.deposit(-50)

    def test_withdraw_amount_within_balance(self):
        account = BankAccount("12345", 100.0)
        account.withdraw(50.0)
        self.assertEqual(account.get_balance(), 50.0)

    def test_withdraw_amount_exceeding_balance(self):
        account = BankAccount("12345", 100.0)
        with self.assertRaises(ValueError):
            account.withdraw(150.0)

    def test_withdraw_zero_or_negative_amount(self):
        account = BankAccount("12345", 100.0)
        with self.assertRaises(ValueError):
            account.withdraw(0)
        with self.assertRaises(ValueError):
            account.withdraw(-50)

    def test_get_balance(self):
        account = BankAccount("12345", 100.0)
        self.assertEqual(account.get_balance(), 100.0)


if __name__ == "__main__":
    unittest.main()
