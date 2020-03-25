# -*- coding: utf-8 -*-

import unittest


class Exam11(unittest.TestCase):

    @classmethod
    def setUp(cls):
        pass

    def test_quick_sort(self):
        """일반적인 퀵 정렬"""
        def _quick_sort(data, start, end):
            # 종료 조건: 정렬을 할 원소가 1개 이하인 경우
            if start >= end:
                return

            # 피봇 설정 (편의상 맨 마지막 원소를 피봇으로 지정)
            pivot = data[end]
            left = start

            # 왼쪽은 피봇보다 작은 수가 위치한다.
            # 오른쪽은 피봇보다 큰 수가 위치한다.
            for right in range(start, end):
                if data[right] <= pivot:
                    # data[right], data[left] = data[left], data[right] 와 동일
                    tmp = data[right]
                    data[right] = data[left]
                    data[left] = tmp

                    left += 1

            # 맨 마지막에 위치한 피봇과 위치를 바꿔준다.
            # [피봇보다 작은 수들] + [피봇] + [피봇보다 큰 수]
            data[end], data[left] = data[left], data[end]

            _quick_sort(data, start, left - 1)
            _quick_sort(data, left + 1, end)

        data = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
        _quick_sort(data, 0, len(data) - 1)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], data)

    def test_quick_sort_with_python(self):
        """파이썬 특징을 활용한 퀵 정렬"""
        def _quick_sort(data):
            # 종료 조건
            n = len(data)
            if n <= 1:
                return data

            # 피봇 값은 어떤값으로 하든 상관없음. 편의상 맨 마지막을 피봇으로 지정
            pivot = data[-1]
            group1 = list()  # 피봇보다 작은 값
            group2 = list()  # 피봇보다 큰 값

            for num in data[:-1]:
                if num < pivot:
                    group1.append(num)
                else:
                    group2.append(num)

            return _quick_sort(group1) + [pivot] + _quick_sort(group2)

        data = [4, 2, 6, 5, 3, 9]
        self.assertEqual([2, 3, 4, 5, 6, 9], _quick_sort(data))


if __name__ == "__main__":
    unittest.main()
