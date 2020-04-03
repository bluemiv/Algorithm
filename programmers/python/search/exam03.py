# -*- coding: utf-8 -*-

import itertools
import unittest


def solution(baseball):
    def get_result(target, nums):
        strike, ball = 0, 0
        for t_num, num in zip(target, nums):
            if t_num == num:
                strike += 1
            else:
                if num in target:
                    ball += 1
        return strike, ball

    answer = 0
    for target in itertools.permutations(range(1, 10), 3):
        is_not_answer = False
        for _round in baseball:
            s, b = get_result("".join(map(str, target)), str(_round[0]))
            if s == _round[1] and b == _round[2]:
                pass
            else:
                is_not_answer = True
        if not is_not_answer:
            answer += 1

    return answer


class SearchExam03(unittest.TestCase):

    def test(self):
        self.assertEqual(2, solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))


if __name__ == "__main__":
    unittest.main()
