import sys

total, m = map(int, sys.stdin.readline().split())

bucket = [0 for _ in range(total)]
for _ in range(m):
    to, _from, n = map(int, sys.stdin.readline().split())
    for i in range(to, _from + 1):
        bucket[i - 1] = n

print(*bucket)
