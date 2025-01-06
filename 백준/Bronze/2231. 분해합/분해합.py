strnum = input()
n = int(strnum)

minnum = len(strnum) * 10
ret = 0
for i in range(n - minnum if n > minnum else 1, n):
    if n == i + sum(map(int, list(str(i)))):
        ret = i
        break
print(ret)
