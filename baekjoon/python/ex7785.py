# -*-coding: utf-8 -*-

import sys
n = int(sys.stdin.readline())

result = dict()
for _ in range(n):
    name, action = sys.stdin.readline().split()
    if action == "enter":
        result[name] = True
    else:
        del result[name]

print("\n".join(sorted(result.keys(), reverse=True)))
