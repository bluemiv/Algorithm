# -*- coding: utf-8 -*-

import unittest


class Exam03(unittest.TestCase):
    """n 명의 주어진 이름들이 있을때, 동명이인인 이름을 찾는다."""

    @classmethod
    def setUp(cls):
        cls.names = ["Tom", "Jerry", "Mike", "Tom"]

    def test1(self):
        """방법 1. 집합을 이용한 방법"""
        name_set = set()
        duplicated_names = set()
        for name in self.names:
            if name in name_set:
                duplicated_names.add(name)
            name_set.add(name)
        self.assertEqual({"Tom"}, duplicated_names)

    def test2(self):
        """방법 2. 단순 비교해봄"""
        name_len = len(self.names)
        duplicated_names = list()
        for idx, name in enumerate(self.names):
            for i in range(idx + 1, name_len):
                if name == self.names[i]:
                    duplicated_names.append(name)
        self.assertEqual(["Tom"], duplicated_names)


if __name__ == "__main__":
    unittest.main()
