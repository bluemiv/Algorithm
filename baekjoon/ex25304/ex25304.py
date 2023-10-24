import sys

total = int(sys.stdin.readline())
c = int(sys.stdin.readline())

while c > 0:
    c -= 1
    price, n = map(int, sys.stdin.readline().split(" "))
    total -= price * n

print("Yes" if total == 0 else "No")
