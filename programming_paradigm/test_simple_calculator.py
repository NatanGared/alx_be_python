import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def __init__(self):
        pass

    def test_subtract(self):
       result = SimpleCalculator.subtract(6,7)
       self.assertEqual(result, -1)

    def test_add(self):
       result = SimpleCalculator.add(6,7)
       self.assertEqual(result,13)

    def test_multiply(self):
       result = SimpleCalculator.multiply(6,7)
       self.assertEqual(result,36)

    def test_divide(self):
       result = SimpleCalculator.divide(10,2)
       self.assertEqual(result,5)

if __name__ == "__main__":
  unittest.main()