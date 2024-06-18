"""
Module for testing the arithmetic module.
"""
import unittest
import arithmetic

class TestArithmetic(unittest.TestCase):
    """
    Class for testing arithmetic functions.
    """

    def test_add(self):
        """
        Test the add function.
        """
        self.assertEqual(arithmetic.add(1, 2), 3)

    def test_subtract(self):
        """
        Test the subtract function.
        """
        self.assertEqual(arithmetic.subtract(3, 2), 1)

    def test_multiply(self):
        """
        Test the multiply function.
        """
        self.assertEqual(arithmetic.multiply(2, 3), 6)

    def test_divide(self):
        """
        Test the divide function.
        """
        self.assertEqual(arithmetic.divide(6, 2), 3)
        with self.assertRaises(ValueError):
            arithmetic.divide(1, 0)

if __name__ == "__main__":
    unittest.main()
