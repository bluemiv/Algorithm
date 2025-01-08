import sys

input = sys.stdin.readline

case = int(input())

stack = []
for i in range(case):
    nums = input().split()
    command = nums[0]
    if command == "1":
        num = int(nums[1])
        stack.append(num)
    elif command == "2":
        print(stack.pop() if len(stack) > 0 else -1)
    elif command == "3":
        print(len(stack))
    elif command == "4":
        print(1 if len(stack) == 0 else 0)
    else:
        print(stack[-1] if len(stack) > 0 else -1)
