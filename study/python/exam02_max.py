# -*- coding: utf-8 -*-

import unittest


class Exam02(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.items = [10, 92, 4, 7, 44, 80, 98, 50, 74, 32]

    def test_find_max(self):
        """최댓값 찾기"""
        max_num = self.items[0]  # 첫번째 원소를 default 값으로 가짐
        for item in self.items[1:]:  # n-1 번 수행하기 때문에 시간복잡도는 O(n-1) = O(n) 이다.
            if max_num < item:
                max_num = item
        self.assertEqual(98, max_num)

    def test_find_max_idx(self):
        """최댓값의 인덱스 찾기"""
        max_idx = 0
        for idx in range(1, len(self.items)):
            if self.items[max_idx] < self.items[idx]:
                max_idx = idx
        self.assertEqual(6, max_idx)

    def test_find_max_idx2(self):
        """최댓값의 인덱스 찾기 - enumerate() 이용하기"""
        max_idx = 0
        for idx, item in enumerate(self.items):
            if self.items[max_idx] < item:
                max_idx = idx
        self.assertEqual(6, max_idx)

    def test_find_max2(self):
        """max() 메소드 이용하기"""
        self.assertEqual(98, max(self.items))


if __name__ == "__main__":
    unittest.main()
