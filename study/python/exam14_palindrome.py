# -*- coding: utf-8 -*-

import unittest


def is_palindrome(text):
    """회문(거꾸로 읽어도 같은 문자)인지 확인한다."""
    queue = list()  # FIFO
    stack = list()  # LIFO

    # 큐와 스택에 각각 문자열을 담는다.
    for c in text:
        queue.append(c)
        stack.append(c)

    # 큐와 스택이 모두 비어있을때 까지 반복한다. (`while queue:` 또는 `while stack:` 을 사용해도 됨)
    while queue and stack:
        # 큐에서 꺼낸 값과 스택에서 꺼낸값이 다르면 회문(palindrome)이 아니다.
        if queue.pop(0) != stack.pop():
            return False
    return True


class Exam14(unittest.TestCase):

    def test_palindrome(self):
        self.assertTrue(is_palindrome("mom"))
        self.assertTrue(is_palindrome("기러기"))
        self.assertTrue(is_palindrome("나야나"))
        self.assertTrue(is_palindrome("기러기"))
        self.assertTrue(is_palindrome("bob"))
        self.assertFalse(is_palindrome("1234"))
        self.assertFalse(is_palindrome("blah blah"))


if __name__ == "__main__":
    unittest.main()
