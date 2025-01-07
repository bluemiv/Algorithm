n = int(input())

cnt = 0
i = 666
while True:
    if "666" in str(i):
        cnt += 1
        if cnt == n:
            break

        if i <= 5000:
            i += 1000
        else:
            i += 1
    else:
        i += 1
print(i)
