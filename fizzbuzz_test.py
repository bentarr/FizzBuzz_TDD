import unittest
from fizzbuzz import FizzBuzz

class fizzbuzz_test(unittest.TestCase):
    def test_returns_error_with_number_0(self):
        with self.assertRaises(ValueError):
            FizzBuzz(0)