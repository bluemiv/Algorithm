# -*- coding: utf-8 -*-

import unittest


class Exam08(unittest.TestCase):

    @classmethod
    def setUp(cls):
        pass

    def test_selection_sort(self):
        """선택 정렬을 이용한 정렬 방법"""
        data = [2, 11, 3, 91, 7, 50, 33]
        length = len(data)

        for i in range(length):
            min_idx = i

            for j in range(i+1, length):

                if data[min_idx] > data[j]:
                    # 더 작은 최솟값이 있다면, 교환(swap)한다.
                    tmp = data[min_idx]
                    data[min_idx] = data[j]
                    data[j] = tmp

            print("{} 회차: {}".format(i+1, data))

        self.assertEqual([2, 3, 7, 11, 33, 50, 91], data)

    def test_python_selection_sort(self):
        """파이썬 답게 풀어보기"""
        data = [2, 11, 3, 91, 7, 50, 33]
        sorted_data = list()

        while data:  # data 에 값이 없을때까지 반복한다.
            min_num = min(data)  # 리스트 중 `가장 작은 값`을 찾는다.
            data.remove(min_num)  # 데이터에서 `가장 작은 값`을 제거한다.
            sorted_data.append(min_num)  # `가장 작은 값`을 `결과 리스트`에 넣는다.

        self.assertEqual([2, 3, 7, 11, 33, 50, 91], sorted_data)


if __name__ == "__main__":
    unittest.main()
