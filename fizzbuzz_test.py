import unittest
from fizzbuzz import FizzBuzz

class fizzbuzz_test(unittest.TestCase):
    def test_returns_error_with_number_0(self):
        with self.assertRaises(ValueError):
            FizzBuzz(0)

    def test_returns_error_with_negative_number(self):
        with self.assertRaises(ValueError):
            FizzBuzz(-15)
    
    def test_returns_fizz_with_multiple_of_3(self):
        number = FizzBuzz(15)
        returns = "Fizz"
        self.assertEqual(number, returns, "d")