# -*- coding: utf-8 -*-

import unittest


class Exam09(unittest.TestCase):

    @classmethod
    def setUp(cls):
        pass

    def test_insertion_sort(self):
        data = [2, 4, 5, 1, 3]
        n = len(data)

        for i in range(1, n):
            key = data[i]

            j = i - 1
            while j >= 0 and data[j] > key:
                data[j + 1] = data[j]  # 오른쪽으로 밀어준다. (공간 확보)
                j -= 1
            data[j + 1] = key
            # print(key, data)
        self.assertEqual([1, 2, 3, 4, 5], data)

    def test_insertion_sort_with_python(self):
        data = [2, 4, 5, 1, 3]
        sorted_data = list()
        while data:
            value = data.pop(0)

            n = len(sorted_data)  # value 보다 큰 원소가 없는 경우 맨 뒤로 배치 (default)
            insert_idx = n

            # value 보다 큰 원소를 찾는다.
            for i in range(n):
                if value < sorted_data[i]:
                    insert_idx = i
                    break

            sorted_data.insert(insert_idx, value)
            # print(value, sorted_data)

        self.assertEqual([1, 2, 3, 4, 5], sorted_data)


if __name__ == "__main__":
    unittest.main()
