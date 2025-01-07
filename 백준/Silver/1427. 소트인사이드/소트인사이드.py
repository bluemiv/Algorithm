nums = sorted(map(int, list(input())), reverse=True)
ret = ""
for n in nums:
    ret += str(n)
print(ret)