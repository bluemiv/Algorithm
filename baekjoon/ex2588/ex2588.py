import sys

[na, nb] = map(int, [sys.stdin.readline(), sys.stdin.readline()])

c1 = na * (nb % 10)
c2 = na * (nb % 100 // 10)
c3 = na * (nb // 100)

print(c1)
print(c2)
print(c3)
print(sum([c1, c2 * 10, c3 * 100]))
