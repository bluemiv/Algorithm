# -*- coding: utf-8 -*-

import sys


def solution(n, m):

    def search(stack, visit, n, m):
        if len(stack) >= m:
            print(" ".join(map(str, stack)))
        else:
            for i in range(1, n + 1):
                if i in visit or (stack and stack[-1] > i):
                    continue

                visit.add(i)
                stack.append(i)  # 선택한다.

                search(stack, visit, n, m)

                visit.remove(i)
                stack.pop()  # 선택하지 않는다.

    search(list(), set(), n, m)


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split())
    solution(n, m)
