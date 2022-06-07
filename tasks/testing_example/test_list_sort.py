import list_sort
import random
import unittest

randomised_list = [random.random() for i in range(1, 11)]

class List_sort_tests(unittest.TestCase):

    def test_0_list_sort(self):
        self.assertEqual(list_sort.list_sort([2, 3, 1], "asc"), [1, 2, 3])

    def test_1_list_sort(self):
        self.assertEqual(list_sort.list_sort([3, 5, 4], "desc"), [5, 4, 3])

    def test_2_list_sort(self):
        self.assertEqual(list_sort.list_sort(randomised_list, "none"), randomised_list)

    def test_3_list_sort(self):
        self.assertEqual(list_sort.list_sort([5, 7, 1, 2, 3, 1, 1, 9, 6], "none"), [5, 7, 1, 2, 3, 1, 1, 9, 6])

    def test_4_list_sort(self):
        self.assertEqual(list_sort.list_sort([3, 4, 5], "hello"), "Unknown keyword")