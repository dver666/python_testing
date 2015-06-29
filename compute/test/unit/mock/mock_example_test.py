import unittest
from mock import Mock

class TestMocking(unittest.TestCase):
    def test_mock_method_returns(self):
        my_mock=Mock()
        my_mock.my_method.return_value="Hello"
        self.aseertEquals("Hello", my_mock.my_method())

if __name__ == '__main__':
    unittest.main()
