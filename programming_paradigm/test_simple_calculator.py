import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-2,-2), -4)
    def test_subtraction(self):
        self.assertEqual(self.calc.sub(5,2), 3)
        self.assertEqual(self.calc.sub(2,3), -1)
        self.assertEqual(self.calc.sub(-5,2),-7)
        self.assertEqual(self.calc.sub(5,-2), 7)
    def test_multiplication(self)
        self.assertEqual(self.calc.mup(3,5), 15)
        self.assertEqual(self.calc.mup(-6,2), -12)
        self.assertEqual(self.calc.mup(3,-5), -15)
        self.assertEqual(self.calc.mup(-7,-3), 21)
    def test_division(self)
        self.assertEqual(self.calc.div(6,3), 2)
        self.assertEqual(self.calc.div(-9,3), -3)
        self.assertEqual(self.calc.div(-15,-3), 5)
        self.assertEqual(self.calc.div(8,0), undifned):





