import unittest
import sys
sys.path.append('/home/diver/www_python_testing/compute')
from compute.tdd_account import TDDAccount

class TDDTestAccount(unittest.TestCase):
    """TDD test account.
    fail to create test account object

    able to uniquely identify a bank account
    retrieve its balance
    """
    def test_account_object_can_be_created(self):
        """account object creation
        """
        tdda=TDDAccount("000",1)

    def test_account_object_returns_current_balance(self):
        """account object creation and class data
        """
        tddaccount=TDDAccount("001",100)
        self.assertEqual(tddaccount.account_number,"001")
        self.assertEqual(tddaccount.balance,100)

    def test_object_to_store_accounts_and_data(self):
        """Bank object is needed to store all Accounts
        
        It can be a dictionary where key is account_number
        and value is balance
        
        Create tdd_bank_test
        """
        pass

if __name__=='__main__':
    unittest.main()
