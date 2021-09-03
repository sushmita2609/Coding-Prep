import unittest
import calc


class TextCalc(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calc.addition(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(calc.subtract(18, 4), 14)
        self.assertEqual(calc.subtract(-1, -8), 7)
        self.assertEqual(calc.subtract(7, -2), 9)

    def test_multiply(self):
        self.assertEqual(calc.multiply(1, 4), 4)
        self.assertEqual(calc.multiply(-24, 4), -96)
        self.assertEqual(calc.multiply(-56, -3), 168)

    def test_divide(self):
        self.assertEqual(calc.divide(8, 4), 2)
        self.assertEqual(calc.divide(48, 4), 12)
        self.assertEqual(calc.divide(5, 2), 2.5)
        self.assertRaises(ValueError, calc.divide, 10, 0)
        with self.assertRaises(ValueError):
            calc.divide(7, 0)


if __name__ == '__main__':
    unittest.main()
