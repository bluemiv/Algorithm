n = int(input())

ret = 0
for i in range(1, n):
    if n == i + sum(map(int, list(str(i)))):
        ret = i
        break
print(ret)
