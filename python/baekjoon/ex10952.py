import sys

a, b = 1, 1
while a and b:
    a, b = list(map(int, sys.stdin.readline().split()))
    _sum = a + b
    if _sum:
        print(_sum)
