import sys

students = [False] * 30
for _ in range(28):
    i = int(sys.stdin.readline())
    students[i - 1] = True

for i in range(30):
    student = students[i]
    if not student:
        print(i + 1)
