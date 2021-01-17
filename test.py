#Python Testing

import unittest
import testmethods 

class Test_Utility(unittest.TestCase):
    
    def setUp(self):
        print("Default variable setup, which will call before any test run!!")


    def test_addition(self):
        test_param = 10
        test_param2=15
        result = testmethods.addition(test_param, test_param2)
        self.assertEqual(result, 25)
    
    def test_multiply(self):
        test_param = 'string'
        result = testmethods.multiply(test_param)
        self.assertIsInstance(result, ValueError)
    
    
    def test_multiply1(self):
        test_param = None
        result = testmethods.multiply(test_param)
        self.assertEqual(result, 'please enter number')
    
    def test_multiply2(self):
        test_param = ''
        result = testmethods.multiply(test_param)
        self.assertEqual(result, 'please enter number')


    def test_division(self):
        test_param = 10
        test_param2=15
        result = testmethods.divide(test_param, test_param2)
        self.assertNotEqual(result,25)

    def tearDown(self):
        print("This method used to clean up variable!!")

if __name__=='__main__':
    unittest.main()


