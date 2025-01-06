n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

maxnum = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            s = nums[i] + nums[j] + nums[k]
            if s <= m:
                maxnum = max(maxnum, s)

print(maxnum)
