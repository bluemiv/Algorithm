# -*- coding: utf-8 -*-

import unittest


def solution(numbers):
    str_numbers = map(str, numbers)  # 각 원소를 문자열로 변환
    sorted_numbers = sorted(
        str_numbers,
        key=lambda x: x * 3,  # 각 원소에 3을 곱한다. (문자열 곱셈)
        reverse=True)  # 내림차순 정렬
    return str(int("".join(sorted_numbers)))


class SortExam02(unittest.TestCase):

    def test(self):
        self.assertEqual("6210", solution([6, 10, 2]))

    def test2(self):
        self.assertEqual("9534330", solution([3, 30, 34, 5, 9]))


if __name__ == "__main__":
    unittest.main()
