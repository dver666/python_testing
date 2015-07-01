import sys
# sys.path.append('/all/your/base/tuda+reload')
sys.path.append('/home/diver/www_python_testing/compute/test/unit/tdd')
sys.path.append('/home/diver/www_python_testing/compute')

class TDDAccount(object):
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
