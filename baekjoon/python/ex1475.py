# -*- coding: utf-8 -*-
import sys

_input = sys.stdin.readline()[:-1]
cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for n in _input:
    index = int(n)
    if index == 9:
        index = 6
    cnt[index] += 1

cnt[6] = (cnt[6] + 1) // 2
print(max(cnt))
