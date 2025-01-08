import sys

input = sys.stdin.readline


def is_valid_bracket(s):
    stack = []
    for c in s:
        if c != "(" and c != ")" and c != "[" and c != "]":
            continue
        if c == "(" or c == "[":
            stack.append(c)
        else:
            if not stack:
                return False
            if (c == ")" and stack[-1] == "(") or (c == "]" and stack[-1] == "["):
                stack.pop()
            else:
                return False
    return not stack


while True:
    s = input().rstrip()
    if s == ".":
        break
    if is_valid_bracket(s):
        print("yes")
    else:
        print("no")
