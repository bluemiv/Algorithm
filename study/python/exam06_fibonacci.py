# -*- coding: utf-8 -*-

import time
import unittest


class Exam06(unittest.TestCase):
    """피보나치 수열과 메모이제이션"""

    @classmethod
    def setUp(cls):
        pass

    def fibo(self, k):
        if k == 1:
            return 0
        elif k == 2:
            return 1
        return self.fibo(k-1) + self.fibo(k-2)

    def test_fibonacci(self):
        self.assertEqual(0, self.fibo(1))
        self.assertEqual(1, self.fibo(2))
        self.assertEqual(1, self.fibo(3))
        self.assertEqual(2, self.fibo(4))
        self.assertEqual(3, self.fibo(5))
        self.assertEqual(5, self.fibo(6))
        self.assertEqual(8, self.fibo(7))

    def test_too_much_during_time(self):
        start = time.time()
        self.fibo(35)
        end = time.time()
        print("수행 시간: {}".format(end - start))

    def fibo_memo(self, memo, k):
        # 이미 계산한 적이 있는 값
        if memo[k] != -1:
            return memo[k]

        # 처음 계산하는 값
        if k == 1:
            memo[k] = 0
        elif k == 2:
            memo[k] = 1
        else:
            memo[k] = self.fibo_memo(memo, k-1) + self.fibo_memo(memo, k-2)
        return memo[k]

    def test_with_memoization(self):
        memo = [-1, -1, ]
        self.assertEqual(0, self.fibo_memo(memo, 1))

        memo = [-1, -1, -1, ]
        self.assertEqual(1, self.fibo_memo(memo, 2))

        n = 35
        memo = [-1 for _ in range(n + 1)]
        self.assertEqual(5702887, self.fibo_memo(memo, n))

        n = 50
        memo = [-1 for _ in range(n + 1)]
        self.assertEqual(7778742049, self.fibo_memo(memo, n))

        n = 100
        memo = [-1 for _ in range(n + 1)]
        self.assertEqual(218922995834555169026, self.fibo_memo(memo, n))


if __name__ == "__main__":
    unittest.main()
