from unittest import TestCase
from student_class import overall_score, compute_grade
from stack import Stack


class TestExerciseThree(TestCase):
    def test_overall_score(self):
        self.assertEqual(overall_score("Max_Mustermann", [0, 15, 0, 15, 25]), 50, "Expected 50")
        self.assertEqual(overall_score("Max_Mustermann", [-10, 15, 15, 15, 50]), 77.3, "Expected 77.3")
        self.assertEqual(overall_score("Max_Mustermann", [15, 15, 15, 15, 50]), 100, "Expected 100")
        self.assertEqual(overall_score("Max_Mustermann", [0, 0, 0, 0, 0]), 0, "Expected 0")
        self.assertEqual(overall_score("Max_Mustermann", [-1, -1, -1, -1, -1]), 0, "Expected 0")


    def test_compute_grade(self):
        self.assertEqual(compute_grade(100), 1.0, "Expected a grade of 1.0")
        self.assertEqual(compute_grade(-40.5), "Not a valid score", "Expected an error")
        self.assertEqual(compute_grade(49.9), 5.0, "Expected a grade of 5.0")
        self.assertEqual(compute_grade(398), "Not a valid score", "Expected an error")

    def test_push(self):
        s = Stack()
        s.push(9)
        s.push(17)
        self.assertEqual([9, 17], s.items, "Expected a stack with items 9 and 17")

    def test_pop(self):
        s = Stack()
        s.push(8)
        s.push(9)
        s.pop()
        self.assertEqual(1, s.size(), "Expected current stack size = 1")

    def test_peek(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.peek(), 3, "Expected topmost element to be returned")
