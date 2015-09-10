import unittest
from compute.compute import Compute

class TestCompute(unittest.TestCase):
    def setUp(self):
        self.comp=Compute()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.comp.add(2,2))

    def test_add_method_raises_typeerror_if_not_ints(self):
        self.assertRaises(ValueError, self.comp.add, "Hello", "World")

if __name__=='__main__':
    unittest.main()
