# -*- coding: utf-8 -*-

import unittest


def solution(array, commands):
    answer = []

    for command in commands:
        i, j, k = command
        answer.append(sorted(array[i-1:j])[k-1])

    return answer


class SortExam01(unittest.TestCase):
    def test(self):
        self.assertEqual([5, 6, 3], solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))


if __name__ == "__main__":
    unittest.main()
