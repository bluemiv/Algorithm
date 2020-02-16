# -*- coding: utf-8 -*-

import unittest


class Exam01(unittest.TestCase):

    def test_sum(self):
        """1 부터 n 까지 더하는 알고리즘"""
        answer = 0  # 정답
        for _ in range(1, 101):
            answer += _  # 1 부터 10 까지 더한다.
        self.assertEqual(answer, 5050)

    def test_sum2(self):
        """가우스 방법으로 문제 풀기"""
        n = 100000000
        answer = n * (n+1) // 2
        self.assertEqual(answer, 5000000050000000)


if __name__ == "__main__":
    unittest.main()
