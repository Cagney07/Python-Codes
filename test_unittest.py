import unittest

from myunittest import square ,double

class TestMyModule(unittest.TestCase):
    def test_square(self):#in order to run the test cases ,start with test keyword is used
        self.assertEqual(square(2),4)
    def test_double(self):
        self.assertEqual(double(0),0)
#assertEqual is used to create test cases
if __name__=='__main__':
    unittest.main()