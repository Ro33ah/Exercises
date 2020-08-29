from unittest import TestCase
from solution import sans_duplicates, max_sum_subarray

class TestExerciseSix(TestCase):
    def test_sans_duplicates(self):
        self.assertEqual(sans_duplicates([1, 1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5]), [1, 2, 3, 4, 5],
                         "Expected a sorted list without duplicates")
        self.assertEqual(sans_duplicates([-5, -3, -3, -1, 0, 0]), [-5, -3, -1, 0],
                         "Expected a sorted list without duplicates")

    def test_max_sum_subarray_empty_list(self):
        self.assertEqual(max_sum_subarray([], 3), 0, "Expected return value 0")
        self.assertEqual(max_sum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4], 4), 6, "Expected return value 6")
        self.assertEqual(max_sum_subarray([45, 12, 32, 90, 48], 2), 138, "Expected return value 138")
        self.assertEqual(max_sum_subarray([0, 0, 0, 0, 0, 0, 0], 4), 0, "Expected return value 0")

