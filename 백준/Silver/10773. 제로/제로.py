import sys

input = sys.stdin.readline

case = int(input())

stack = []
for i in range(case):
    n = int(input())
    if n == 0:
        if stack:
            stack.pop()
    else:
        stack.append(n)
print(sum(stack))
