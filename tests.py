import unittest
from utils import merge_ranges
from input import input_values


class TestCalendar(unittest.TestCase):

    def setUp(self):
        self.normal_meetings = [(0, 1), (3, 5), (4, 8), (5, 8), (9, 12), (10, 12)]
        self.meetings_without_break = [(0, 1), (3, 5), (4, 8), (5, 8), (9, 12), (10, 12), (2, 5), (0, 13)]
        self.meetings_with_repeat = [(0, 1), (2, 5), (2, 6), (2, 5), (8, 9)]

        self.result_normal_list = [(0, 1), (3, 8), (9, 12)]
        self.result_list_without_break = [(0, 13)]
        self.result_with_repeat = [(0, 1), (2, 6), (8, 9)]

    def test_input(self):
        """
        Please input (0, 1) ,(0, 3), (4, 5), (5, 8) to run the test

        """
        tester_arr = input_values()
        self.assertEqual(tester_arr, [(0, 1), (0, 3), (4, 5), (5, 8)])

    def test_normal_meetings(self):
        self.assertEqual(merge_ranges(self.normal_meetings), self.result_normal_list)

    def test_meetings_without_break(self):
        self.assertEqual(merge_ranges(self.meetings_without_break), self.result_list_without_break)

    def test_meetings_with_repeat(self):
        self.assertEqual(merge_ranges(self.meetings_with_repeat), self.result_with_repeat)


if __name__ == '__main__':
    unittest.main()