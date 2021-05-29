import unittest
import leapyear

class TestCase(unittest.TestCase):
    def test_leapyear1(self):
        result = leapyear.leapyear(4)
        self.assertEqual(result, True)
    def test_leapyear2(self):
        result = leapyear.leapyear(100)
        self.assertEqual(result, False)
    def test_leapyear3(self):
        result = leapyear.leapyear(400)
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
