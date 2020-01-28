# -*- coding: utf-8 -*-

import sys


def solve(a, b):
    if a > b:
        return ">"
    elif a == b:
        return "=="
    elif a < b:
        return "<"
    else:
        raise RuntimeError("Unexpected error. {} {}".format(a, b))


if __name__ == "__main__":
    a, b = list(map(int, sys.stdin.readline().split()))

    result = solve(a, b)

    print(result)
