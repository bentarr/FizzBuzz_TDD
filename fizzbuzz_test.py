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
        number = FizzBuzz(3)
        results = "Fizz"       
        self.assertEqual(number, results, "Nice Fizz")
    
    def test_returns_Buzz_with_multiple_of_5(self):
        number = FizzBuzz(50)
        results = "Buzz"
        self.assertEqual(number, results,  "Nice Buzz")
    
    def test_returns_FizzBuzz_with_multiple_of_3_and_5(self):
        number = FizzBuzz(30)
        results = "FizzBuzz"
        self.assertEqual(number, results,  "Nice FizzBuzz")

    def test_returns_alice_number_if_neither_Fizz_Buzz_FizzBuzz(self):
        number = FizzBuzz(7)
        results = "7"
        self.assertEqual(number, results, "Sad FizzBuzz")

    def test_returns_error_if_is_not_int(self):
        with self.assertRaises(ValueError):
            FizzBuzz("Not int")
