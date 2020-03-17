# -*- coding: utf-8 -*-

import unittest


class Exam05(unittest.TestCase):
    """최대 공약수 구하기"""

    def setUp(self) -> None:
        pass

    @staticmethod
    def gcd(a, b):
        i = min(a, b)
        while True:
            if i <= 1:
                return -1

            if a % i == 0 and b % i == 0:
                return i

            i -= 1

    @classmethod
    def euclid_gcd(cls, a, b):
        if b == 0:
            return a  # gcd(n, 0) = n
        return cls.euclid_gcd(b, a % b)  # gcd(a, b) = gcd(b, a % b)

    def test_gcd(self):
        self.assertEqual(2, self.gcd(4, 6))
        self.assertEqual(14, self.gcd(14, 98))
        self.assertEqual(3, self.gcd(15, 99))

    def test_euclid_gcd(self):
        self.assertEqual(2, self.euclid_gcd(4, 6))
        self.assertEqual(14, self.euclid_gcd(14, 98))
        self.assertEqual(14, self.euclid_gcd(98, 14))
        self.assertEqual(3, self.euclid_gcd(15, 99))
        self.assertEqual(3, self.euclid_gcd(99, 15))


if __name__ == "__main__":
    unittest.main()
