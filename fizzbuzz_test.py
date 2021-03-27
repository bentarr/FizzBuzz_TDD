import unittest
from fizzbuzz import FizzBuzz

class fizzbuzz_test(unittest.TestCase):
    def test_returns_error_with_number_0(self):
        with self.assertRaises(ValueError):
            FizzBuzz(0)

    def test_returns_error_with_negative_number(self):
        with self.assertRaises(ValueError):
            FizzBuzz(-2)

    def test_returns_Fizz_with_multiple_of_3(self):
        results = FizzBuzz(9)
        number = "Fizz"       
        self.assertEqual(results, number, "Nice Fizz")
    
    def test_returns_Buzz_with_multiple_of_5(self):
        results = FizzBuzz(20)
        number = "Buzz"
        self.assertEqual(results, number,  "Nice Buzz")
    
    def test_returns_FizzBuzz_with_multiple_of_3_and_5(self):
        results = FizzBuzz(30)
        number = "FizzBuzz"
        self.assertEqual(results, number,  "Nice FizzBuzz")