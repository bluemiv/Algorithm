# -*- coding: utf-8 -*-

import unittest


def solution(numbers, target):
    answer = 0

    stack = [(numbers[0], 1), (-numbers[0], 1)]  # idx0: 누적합, idx1: 다음 원소

    while stack:
        _sum, idx = stack.pop()
        if idx >= len(numbers):
            if _sum == target:
                answer += 1
            continue

        next_idx = idx + 1
        stack.append((_sum + numbers[idx], next_idx))
        stack.append((_sum - numbers[idx], next_idx))

    return answer


class DfsBfsExam01(unittest.TestCase):

    def test(self):
        self.assertEqual(5, solution([1, 1, 1, 1, 1], 3))


if __name__ == "__main__":
    unittest.main()
