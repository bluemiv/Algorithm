import sys

input = sys.stdin.readline

n = int(input())
line = list(map(int, input().strip().split()))

cur = 1
stack = []
while line or stack:
    if not line and stack and stack[-1] != cur:
        break
    while stack and stack[-1] == cur:
        stack.pop()
        cur += 1

    if line:
        student = line.pop(0)
        stack.append(student)
print("Sad" if stack else "Nice")
