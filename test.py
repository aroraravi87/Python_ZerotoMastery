#Python Testing

import unittest
import main 

class Test_Utility(unittest.TestCase):
    def test_addition(self):
        test_param = 10
        test_param2=15
        result = main.addition(test_param, test_param2)
        self.assertEqual(result, 25)
    
    def test_multiply(self):
        test_param = 10
        test_param2=15
        result = main.multiply(test_param, test_param2)
        self.assertEqual(result, 150)
    
    def test_division(self):
        test_param = 10
        test_param2=15
        result = main.divide(test_param, test_param2)
        self.assertNotEqual(result,25)

unittest.main()


