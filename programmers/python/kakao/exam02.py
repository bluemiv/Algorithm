# -*- coding: utf-8 -*-
# [2020카카오공채] 괄호 변환

import unittest


def is_collect(p):
    """올바른 괄호인지 확인"""
    if not p or p[0] == ")":
        return False  # 빈 문자열이거나 닫힌 괄호로 시작하는 경우 "올바른 괄호" 가 아니다.

    stack = list()
    for c in p:
        if "(" == c:
            stack.append(c)
        else:
            if not stack:
                return False
            stack.pop()

    return False if stack else True


def is_balance(p):
    """균형 잡힌 괄호인지 확인"""
    cnt = 0
    for c in p:
        cnt = cnt + 1 if "(" == c else cnt - 1
    return True if cnt == 0 else False


def get_new_u(u):
    _u = u[1:-1]
    new_u = ""
    for c in _u:
        if "(" == c:
            new_u += ")"
        else:
            new_u += "("
    return new_u


def solution(p):
    if is_collect(p) and is_balance(p):
        return p

    answer = ""
    n = len(p)
    for i in range(1, n):
        u, v = p[:i * 2], p[i * 2:]
        if not is_balance(u):
            continue
        else:
            if is_collect(u):
                # `올바른 괄호`인 경우
                answer = u + solution(v)
            else:
                # `올바르지 않은 괄호`인 경우
                answer = "(" + solution(v) + ")" + get_new_u(u)
            break
    return answer


class KakaoExam02(unittest.TestCase):

    def test1(self):
        self.assertEqual("(()())()", solution("(()())()"))

    def test2(self):
        self.assertEqual("()", solution(")("))

    def test3(self):
        self.assertEqual("()(())()", solution("()))((()"))


if __name__ == "__main__":
    unittest.main()
