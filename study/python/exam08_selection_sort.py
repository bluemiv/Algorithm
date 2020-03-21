# -*- coding: utf-8 -*-

import unittest


class Exam08(unittest.TestCase):

    @classmethod
    def setUp(cls):
        pass

    @staticmethod
    def find_min_idx(data):
        """가장 작은 인덱스 값을 찾는다."""
        min_idx = 0  # 초기값은 인덱스의 가장 첫번째 값
        for idx in range(1, len(data)):
            if data[min_idx] > data[idx]:
                min_idx = idx
        return min_idx

    def test_selection_sort(self):
        """선택 정렬을 이용한 정렬 방법"""
        data = [2, 11, 3, 91, 7, 50, 33]
        sorted_data = list()

        for _ in range(len(data)):
            min_idx = self.find_min_idx(data)  # 가장 작은 인덱스 값
            min_num = data[min_idx]  # 가장 작은 값

            sorted_data.append(min_num)
            data.pop(min_idx)  # 결과 리스트에 담은 인덱스는 제거한다.
            print("{} 회차: {}, 가장 작은 값:{}, 결과 리스트: {}".format(_+1, data, min_num, sorted_data))

        self.assertEqual([2, 3, 7, 11, 33, 50, 91], sorted_data)

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
