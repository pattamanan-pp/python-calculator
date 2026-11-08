import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    # Additional test for add()
    def test_add_2(self):
        self.assertEqual(self.calc.add(5, 3), 8)

    def test_add_3(self):
        self.assertEqual(self.calc.add(10, 4), 14)
        
    # Test subtract()
    def test_subtract_1(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_subtract_2(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    # Test multiply()
    def test_multiply_1(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)

    def test_multiply_2(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)

    # Test divide()
    def test_divide_1(self):
        self.assertEqual(self.calc.divide(5, 2), 2)

    def test_divide_2(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    # Test modulo()
    def test_modulo_1(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)

    def test_modulo_2(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    
if __name__ == '__main__':
    unittest.main()