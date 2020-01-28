# -*- coding: utf-8 -*-

import sys


def solve(arr, n):
    rtn = sorted(arr, reverse=True)
    return rtn[n-1]


if __name__ == "__main__":
    arr = list(map(int, sys.stdin.readline().split()))
    n = int(sys.stdin.readline())

    print(solve(arr, n))
