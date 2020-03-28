# -*- coding: utf-8 -*-

import unittest


def binary_search(data, target):
    """data 에서 target 의 인덱스를 찾아 반환한다.

    :param data: 데이터 리스트
    :param target: 찾고 있는 수
    :return: target 의 인덱스
    """
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (end + start) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
        elif data[mid] > target:
            end = mid - 1

    return -1


class Exam13(unittest.TestCase):

    def test_binary_search(self):
        data = [1, 4, 9, 16, 25, 36, 49, 64, 81]
        self.assertEqual(0, binary_search(data, 1))
        self.assertEqual(1, binary_search(data, 4))
        self.assertEqual(2, binary_search(data, 9))
        self.assertEqual(3, binary_search(data, 16))
        self.assertEqual(4, binary_search(data, 25))
        self.assertEqual(5, binary_search(data, 36))
        self.assertEqual(6, binary_search(data, 49))
        self.assertEqual(7, binary_search(data, 64))
        self.assertEqual(8, binary_search(data, 81))
        self.assertEqual(-1, binary_search(data, 0))
        self.assertEqual(-1, binary_search(data, 999))


if __name__ == "__main__":
    unittest.main()
