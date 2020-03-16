# -*- coding: utf-8 -*-

import unittest


class Exam04(unittest.TestCase):
    """1부터 n 까지의 곱, 팩토리얼(factorial)을 구하기"""

    @classmethod
    def setUp(cls):
        pass

    def test1(self):
        """단순히 for 문을 이용하여 팩토리을 구한다."""
        n = 5
        result = 1
        for _ in range(1, n + 1):
            result *= _
        self.assertEqual(120, result)

    def test2_recursive(self):
        """재귀함수를 이용하여 팩토리얼을 구한다."""
        def factorial(k):
            if k <= 1:
                return 1
            return k * factorial(k-1)
        self.assertEqual(120, factorial(5))


if __name__ == "__main__":
    unittest.main()