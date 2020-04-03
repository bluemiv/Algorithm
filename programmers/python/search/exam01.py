# -*- coding: utf-8 -*-

import unittest


def solution(answers):
    answer = {
        1: [1, 2, 3, 4, 5],
        2: [2, 1, 2, 3, 2, 4, 2, 5],
        3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    }

    result = list()
    for _ in range(1, 4):
        answer[_] = (answer[_] * (len(answers) // len(answer[_]) + 1))[:len(answers)]

        cnt = 0
        for a, b in zip(answer[_], answers):
            if a == b:
                cnt += 1
        result.append(cnt)

    return [idx + 1 for idx, _ in enumerate(result) if _ == max(result)]


class SearchExam01(unittest.TestCase):

    def test(self):
        self.assertEqual([1], solution([1, 2, 3, 4, 5]))

    def test2(self):
        self.assertEqual([1, 2, 3], solution([1, 3, 2, 4, 2]))

    def test3(self):
        self.assertEqual([3], solution([1, 3, 2, 4, 2, 5, 2, 4, 1, 3, 3]))


if __name__ == "__main__":
    unittest.main()
