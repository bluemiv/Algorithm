n = int(input())

ret = -1
for i in range(n // 5, -1, -1):
    remain = (n - 5 * i)
    if remain % 3 == 0:
        ret = i + remain // 3
        break
print(ret)
