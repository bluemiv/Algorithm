def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


input()
nums = list(map(int, input().split()))
cnt = 0
for n in nums:
    if is_prime(n):
        cnt += 1
print(cnt)
