from unittest import TestCase
from simple_gui import compute_exponent, compute_modulus


class TestExerciseFive(TestCase):
    def test_compute_square_root(self):
        self.assertEqual(9, 3, "Expected function to return 3")
        self.assertEqual(25, 5, "Expected function to return 5")
        self.assertEqual(31, 5.568, "Expected function to return 5.568")
        self.assertEqual(0, 0, "Expected function to return 0")
        self.assertEqual(-81, "Invalid input", 'Expected function to return "Invalid input"')
# more edge cases
    def test_compute_exponent(self):
        self.assertEqual(compute_exponent(-3, 2), 9, "Expected function to return 9")
        self.assertEqual(compute_exponent(2, -3), 0.125, "Expected function to return 0.125")
        self.assertEqual(compute_exponent(5, 5), 3125, "Expected function to return 3125")

    def test_compute_modulus(self):
        self.assertEqual(compute_modulus(2, 2), 0, "Expected function to return 0")
        self.assertEqual(compute_modulus(100, 30), 10, "Expected function to return 10")
        self.assertEqual(compute_modulus(-100, 30), -10, "Expected function to return -10")
        self.assertEqual(compute_modulus(-100, -30), -10, "Expected function to return -10")
        self.assertEqual(compute_modulus(100, -30), 10, "Expected function to return 10")

