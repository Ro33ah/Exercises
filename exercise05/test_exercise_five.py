from unittest import TestCase
from calculate_time, import compute_time


class TestExerciseFive(TestCase):
    def test_same_day(self):
        actual = compute_time("13:30", "2:12")
        expected = "15:42"
        self.assertEqual(actual, expected, 'Expected result is "15:42"')

    def test_next_day(self):
        actual = compute_time("14:02", "24:30")
        expected = "15:32 (1 day later)"
        self.assertEqual(actual, expected, 'Expected result to end with '
                                           '"(1 day later)" when it is next day')

    def test_days_later(self):
        actual = compute_time("23:17", "100:15")
        expected = "03:32 (5 days later)"
        self.assertEqual(actual, expected, 'expected additional string "(5 days later)"')

    def test_no_change(self):
        actual = compute_time("00:10", "0:00")
        expected = "00:10"

        self.assertEqual(actual, expected, 'expected the same time "00:10"')


