import sys

input = sys.stdin.readline

n = int(input())
line = list(map(int, input().strip().split()))

cnt = 1
stack = []
for student in line:
    stack.append(student)
    while stack and stack[-1] == cnt:
        stack.pop()
        cnt += 1

print("Sad" if stack else "Nice")
