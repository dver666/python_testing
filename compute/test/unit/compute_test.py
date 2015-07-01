import sys
sys.path.append('/home/diver/www_python_testing')
import unittest
from compute.compute import Compute

class TestCompute(unittest.TestCase):
    def setUp(self):
        self.compute=Compute()

    def test_add_method_returns_correct_result(self):
        # print "Hello"
        self.assertEqual(4, self.compute.add(2,2))
        # self.assertAlmostEquals(2,2)

    def test_add_method_raises_typeerror_if_not_ints(self):
        self.assertRaises(TypeError, self.compute.add, "Hello", "World")
        # self.assertRaises(TypeError, self.comp.add, type, type)

if __name__=='__main__':
    unittest.main()
