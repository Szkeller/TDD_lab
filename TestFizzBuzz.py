import unittest

import FizzBuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
     '''
       test case for fizz scenario
     '''
     # capture the result from FizzBuzz.py
        result = FizzBuzz.fizz_buzz(3)
     # expectet result
        expected_result = 'Fizz'
     #check the expected result
        self.assertEqual(expected_result, result)


    def test_buzz(self):
           '''
           test case for buzz scenario
           '''
     
        result = FizzBuzz.fizz_buzz(5)
        expected_result = 'Buzz'
     #check
        self.assertEqual(expected_result,result)


    def test_Fizz_buzz(self):
        '''
        test case for FizzBuzz scenario
        '''
        result = FizzBuzz.fizz_buzz(15)
        expected_result = 'FizzBuzz'
        #check the excepted result
        self.assertEqual(expected_result,result)


    def test_normal_number(self):
        '''
         test case for the number cannot fall in those 3 cases
        '''
        result = FizzBuzz.fizz_buzz(1)
        expected_result = '1'
        # check the excepted result
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()