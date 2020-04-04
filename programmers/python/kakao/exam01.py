# -*- coding: utf-8 -*-
# [2020카카오공채] 문자열 압축

import unittest


def solution(s):
    table = [0] * len(s)

    for i in range(1, len(s) + 1):
        cur_str = s[:i]  # 현재 기준 문자열
        cur_count = 1  # 기준 문자열의 압축 개수
        result = ""  # 결과값
        for j in range(1, (len(s) // i) + 1):
            cmp_str = s[i * j: i * (j + 1)]  # 비교 대상 문자열

            if cur_str == cmp_str:
                cur_count += 1  # 기준 문자열과 비교 대상 문자열이 같은 경우, 갯수를 증가시킨다.
            else:
                # 압축 문자열 개수가 1개인 경우, 1은 생략이 가능하다.
                result += (str(cur_count) if cur_count > 1 else "") + cur_str
                cur_str = cmp_str
                cur_count = 1

        # 전체 문자열 길이가 단위 수로 나누어 떨어지지 않는 경우, 나머지 문자열은 뒤에 이어 붙인다.
        if len(s) % i != 0:
            result += s[-(len(s) % i):]

        table[i-1] = len(result)  # 결과 저장
    return min(table)


class KakaoExam01(unittest.TestCase):

    def test1(self):
        self.assertEqual(7, solution("aabbaccc"))

    def test2(self):
        self.assertEqual(9, solution("ababcdcdababcdcd"))

    def test3(self):
        self.assertEqual(8, solution("abcabcdede"))

    def test4(self):
        self.assertEqual(14, solution("abcabcabcabcdededededede"))

    def test5(self):
        self.assertEqual(17, solution("xababcdcdababcdcd"))


if __name__ == "__main__":
    unittest.main()
