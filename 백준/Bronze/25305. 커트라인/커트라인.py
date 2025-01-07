n, k = map(int, input().split())
students = sorted([int(n) for n in input().split()], reverse=True)
print(students[k - 1])
