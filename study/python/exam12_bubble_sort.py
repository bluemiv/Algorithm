# -*- coding: utf-8 -*-

import unittest


class Exam12(unittest.TestCase):

    @classmethod
    def setUp(cls):
        pass

    def test_bubble_sort(self):
        data = [2, 6, 3, 4, 8, 9, 1, 10]

        n = len(data)
        for _ in range(n-1):
            for i in range(n-1):
                if data[i] > data[i+1]:
                    data[i], data[i+1] = data[i+1], data[i]

        self.assertEqual([1, 2, 3, 4, 6, 8, 9, 10], data)


if __name__ == "__main__":
    unittest.main()
