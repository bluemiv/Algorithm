n, m = map(int, input().split(" "))

col_sums = [0] * m
for j in range(n):
    for i, num in enumerate(input().split(" ")):
        col_sums[i] += int(num)

k = int(input())

window_sum = sum(col_sums[:k])
answer = window_sum

for r in range(k, m):
    window_sum -= col_sums[r - k]
    window_sum += col_sums[r]
    answer = max(answer, window_sum)

print(answer)