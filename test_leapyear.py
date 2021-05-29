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
    def test_leapyear4(self):
        result = leapyear.leapyear(3)
        self.assertEqual(result, False)
    def test_leapyear5(self):
        result = leapyear.leapyear("NotInt")

if __name__ == '__main__':
    unittest.main()
