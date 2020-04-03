# -*- coding: utf-8 -*-

import itertools
import unittest


def solution(numbers):
    def is_prime(number):
        """소수이지 확인"""
        if number <= 1:
            return False

        i = 2
        while i * i <= number:
            if number % i == 0:
                return False
            i += 1
        return True

    # 순열 구하기
    primes = set()
    for i in range(1, len(numbers) + 1):
        for nums in itertools.permutations(numbers, i):
            num = int("".join(nums))
            if is_prime(num):
                primes.add(num)

    return len(primes)


class SearchExam02(unittest.TestCase):

    def test(self):
        self.assertEqual(3, solution("17"))

    def test2(self):
        self.assertEqual(2, solution("011"))

    def test3(self):
        self.assertEqual(0, solution("000"))

    def test4(self):
        self.assertEqual(1336, solution("1234567"))


if __name__ == "__main__":
    unittest.main()
