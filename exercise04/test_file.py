from unittest import TestCase
from the_solutions import square_it, change_list, lambda_version, random_matrix


class ExerciseTest(TestCase):
    def test_change_list(self):
        actual = change_list([2, 4, 16], square_it)
        expected = [4, 16, 256]
        self.assertEqual(actual, expected, "Expected something different bro")

    def test_lambda_version(self):
        actual = lambda_version([2, 4, 16])
        expected = [4, 16, 256]
        self.assertEqual(actual, expected, "Expected something different bro")

    def test_random_matrix(self):
        actual = random_matrix().shape
        expected = (10, 10)
        self.assertEqual(actual, expected, "Expected a 10 x 10 matrix")
