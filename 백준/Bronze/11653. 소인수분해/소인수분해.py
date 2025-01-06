n = int(input())

arr = []
while True:
    if n == 1:
        break
    i = 2
    while i < n + 1:
        if n % i == 0:
            n //= i
            arr.append(i)
            i = 2
        else:
            i += 1
print("\n".join(map(str, arr)))
