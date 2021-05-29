import unittest
import fizzbuzz



class TestCase(unittest.TestCase):
    def test_fizzbuzz1(self):
        result = fizzbuzz.fizzbuzz(5)
        self.assertEqual(result, "Buzz")
    def test_fizzbuzz2(self):
        result = fizzbuzz.fizzbuzz(2)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
