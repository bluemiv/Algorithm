def is_primary(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
m = int(input())
arr = []
for i in range(n, m + 1):
    if is_primary(i):
        arr.append(i)

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])
