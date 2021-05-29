import unittest
import fizzbuzz



class TestCase(unittest.TestCase):
    def test_fizzbuzz1(self):
        result = fizzbuzz.fizzbuzz(5)
        self.assertEqual(result, "Buzz")


if __name__ == '__main__':
    unittest.main()
