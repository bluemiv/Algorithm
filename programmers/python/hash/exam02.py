# -*- coding: utf-8 -*-

import unittest


def solution(phone_book):
    _book = sorted(phone_book)

    for a, b in zip(_book, _book[1:]):
        if b.startswith(a):
            return False
    return True


class HashExam02(unittest.TestCase):

    def test(self):
        self.assertFalse(solution(["119", "97674223", "1195524421"]))

    def test2(self):
        self.assertTrue(solution(["123", "456", "789"]))

    def test3(self):
        self.assertFalse(solution(["12", "123", "1235", "567", "88"]))


if __name__ == "__main__":
    unittest.main()
