# -*- coding: utf-8 -*-

import unittest


class Exam07(unittest.TestCase):
    """하노이탑 알고리즘"""

    def hanoi(self, k, from_pos, to_pos, aux_pos):
        """하노이탑 알고리즘

        :param k: 원반 개수
        :param from_pos: 출발지 기둥
        :param to_pos: 도착지 기둥
        :param aux_pos: 보조 기둥
        :return: 이동 횟수
        """
        if k == 1:
            print("{}기둥 -> {}기둥".format(from_pos, to_pos))
            return 1

        cnt = self.hanoi(k - 1, from_pos, aux_pos, to_pos)

        cnt += 1
        print("{}기둥 -> {}기둥".format(from_pos, to_pos))

        cnt += self.hanoi(k - 1, aux_pos, to_pos, from_pos)
        return cnt

    def hanoi2(self, k):
        if k == 1:
            return 1
        return 2 * self.hanoi2(k-1) + 1

    def test_hanoi(self):
        print("== 원반 1개 ==")
        self.assertEqual(1, self.hanoi(k=1, from_pos=1, to_pos=3, aux_pos=2))

        print("== 원반 2개 ==")
        self.assertEqual(3, self.hanoi(k=2, from_pos=1, to_pos=3, aux_pos=2))

        print("== 원반 3개 ==")
        self.assertEqual(7, self.hanoi(k=3, from_pos=1, to_pos=3, aux_pos=2))

        print("== 원반 4개 ==")
        self.assertEqual(15, self.hanoi(k=4, from_pos=1, to_pos=3, aux_pos=2))

    def test_hanoi_during_time(self):
        print(self.hanoi2(100))


if __name__ == "__main__":
    unittest.main()
