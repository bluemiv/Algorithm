# -*- coding: utf-8 -*-

import sys
import unittest


def solve(year):
    """윤년이 되기 위한 조건
    1. 4로 나누어 떨어지지만 100으로 나누어 떨어지지 않는다.
    2. 4, 100, 400으로 모두 나누어 떨어진다.
    """

    if year % 4 == 0:
        if year % 100 != 0 or year % 100 == 0 and year % 400 == 0:
            return 1
    return 0


class UnitTest(unittest.TestCase):

    def test1(self):
        unittest.TestCase.assertEqual(self, 1, solve(2000))

    def test2(self):
        unittest.TestCase.assertEqual(self, 0, solve(1900))

    def test3(self):
        unittest.TestCase.assertEqual(self, 1, solve(2012))


if __name__ == "__main__":
    # unittest.main()
    year = int(sys.stdin.readline().strip())
    result = solve(year)
    print(result)

