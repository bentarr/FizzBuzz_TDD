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

    def test_returns_buzz_with_multiple_of_5(self):
        number = FizzBuzz(20)
        returns = "Buzz"
        self.assertEqual(number, returns, "ED")

    def test_returns_fizzbuzz_with_multiple_of_3_and_5(self):
        number = FizzBuzz(30)
        returns = "FizzBuzz"
        self.assertEqual(number, returns, "AD")