# -*- coding: utf-8 -*-

import unittest


class Exam10(unittest.TestCase):

    @classmethod
    def setUp(cls):
        pass

    def test_merge_sort(self):
        """일반적인 병합 정렬"""
        def _merge_sort(group):
            # 재귀 종료 조건: 그룹이 없을때
            n = len(group)
            if n <= 1:
                return

            # 반으로 그룹을 나눈다.
            mid_idx = n // 2
            group1 = group[:mid_idx]
            group2 = group[mid_idx:]
            # print(group, group1, group2)

            # 재귀적으로 병합 정렬을 수행한다.
            _merge_sort(group1)
            _merge_sort(group2)

            # 정렬한다.
            idx, idx1, idx2 = 0, 0, 0  # 전체 그룹 인덱스, 그룹1 인덱, 그룹2 인덱스
            while idx1 < len(group1) and idx2 < len(group2):
                if group1[idx1] < group2[idx2]:
                    group[idx] = group1[idx1]
                    idx1 += 1
                else:
                    group[idx] = group2[idx2]
                    idx2 += 1
                idx += 1

            # 그룹에 남아있는 원소를 넣는다.
            while idx1 < len(group1):
                group[idx] = group1[idx1]
                idx1 += 1
                idx += 1
            while idx2 < len(group2):
                group[idx] = group2[idx2]
                idx2 += 1
                idx += 1

        data = [38, 27, 43, 3, 9, 82, 10]
        _merge_sort(data)

        self.assertEqual([3, 9, 10, 27, 38, 43, 82], data)

    def test_merge_sort_with_python(self):
        """파이썬을 이용한 병합 정렬"""
        def _merge_sort(group):
            # 종료 조건 설정
            n = len(group)
            if n <= 1:
                return group

            # 그룹 나누기
            mid_idx = n // 2
            group1 = _merge_sort(group[:mid_idx])
            group2 = _merge_sort(group[mid_idx:])

            # 정렬
            result = list()
            while group1 and group2:
                result.append(group1.pop(0) if group1[0] < group2[0] else group2.pop(0))
            result.extend(group1)
            result.extend(group2)
            # print(result)
            return result

        data = [38, 27, 43, 3, 9, 82, 10]
        sorted_data = _merge_sort(data)

        self.assertEqual([3, 9, 10, 27, 38, 43, 82], sorted_data)


if __name__ == "__main__":
    unittest.main()
