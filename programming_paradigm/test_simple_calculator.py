import unittest
import simple_calculator

class SimpleCalculator(unittest.TestCase):
    def __init__(self):
        pass

    def test_subtract(self):
       result = simple_calculator.subtract(6,7)
       self.assertEqual(result, -1)

    def test_add(self):
       result = simple_calculator.add(6,7)
       self.assertEqual(result,13)

    def test_multiply(self):
       result = simple_calculator.multiply(6,7)
       self.assertEqual(result,36)

    def test_divide(self):
       result = simple_calculator.divide(10,2)
       self.assertEqual(result,5)

if __name__ == "__main__":
  unittest.main()