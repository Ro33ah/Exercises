from unittest import TestCase
from solution import sans_duplicates

class TestExerciseSix(TestCase):
    def test_sans_duplicates(self):
        self.assertEqual(sans_duplicates([1, 1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5]), [1, 2, 3, 4, 5],
                         "Expected a sorted list without duplicates")
        self.assertEqual(sans_duplicates([-5, -3, -3, -1, 0, 0]), [-5, -3, -1, 0],
                         "Expected a sorted list without duplicates")

