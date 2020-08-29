from unittest import TestCase
from calculate_grade import compute_grade

class TestExerciseTwo(TestCase):
    def test_compute_grade(self):
        self.assertEqual(compute_grade(100), 1.0, "Expected a grade of 1.0")
        self.assertEqual(compute_grade(-40.5), "Not a valid score", "Expected an error")
        self.assertEqual(compute_grade(49.9), 5.0, "Expected a grade of 5.0")
        self.assertEqual(compute_grade(398), "Not a valid score", "Expected an error")
