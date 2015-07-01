import unittest
import sys
sys.path.append('/home/diver/www_python_testing')
from mock import Mock, patch
from compute.account import Account
from compute.account import ConnectionError

class TestAccount(unittest.TestCase):
    @patch('compute.account.requests')
    def test_get_current_balance_returns_data_correctly(self, mock_requests):
        #mock_requests.get.return_value='500'
        #account=Account(Mock())
        #self.assertEqual('500',account.get_current_balance('1'))
        mock_response=Mock()
        mock_response.status_code=200
        mock_response.text='some text'
        mock_requests.get.return_value=mock_response
        account=Account(Mock())
        self.assertEqual({'status': 200, 'data': 'some text'},account.get_current_balance('1'))

    def test_account_when_connect_exception_raised(self):
        mock_data_interface=Mock()
        mock_data_interface.get.side_effect=ConnectionError()
        account=Account(mock_data_interface)
        self.assertEqual("Connection Error occured. Try again.",account.get_account(1))

if __name__=='__main__':
    unittest.main()
