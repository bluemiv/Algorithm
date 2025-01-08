import sys

input = sys.stdin.readline


def solution(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if not stack:
                print("NO")
                return
            else:
                stack.pop()
    if not stack:
        print("YES")
    else:
        print("NO")


case = int(input())

for i in range(case):
    solution(input().strip())
