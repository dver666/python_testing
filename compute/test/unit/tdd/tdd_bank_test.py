import unittest
import sys
sys.path.append('/home/diver/www_python_testing/compute')
from compute.tdd_account import TDDAccount
from compute.tdd_bank import TDDBank

class BankTest(unittest.TestCase):
    """Accounts storage etc
    """
    def test_bank_is_initially_empty(self):
        """test bank
        """
        bank=TDDBank()
        self.assertEqual({},bank.accounts)
        self.assertEqual(len(bank.accounts),0)

    def test_add_account(self):
        """test add account
        """
        bank=TDDBank()

        acc1=TDDAccount(001,50)
        acc2=TDDAccount(002,100)

        bank.add_account(acc1)
        bank.add_account(acc2)

        self.assertEqual(len(bank.accounts), 2)

    def test_get_account_balance(self):
        """test get account balance
        """
        bank=TDDBank()
        acc1=TDDAccount(001,50)
        bank.add_account(acc1)
        self.assertEqual(bank.get_account_balance(001),50)

if __name__=='__main__':
    unittest.main()
