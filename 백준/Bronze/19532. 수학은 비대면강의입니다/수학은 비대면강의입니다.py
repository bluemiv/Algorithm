a, b, c, d, e, f = map(int, input().split())

x = (c * e - f * b) // (e * a - b * d)
y = (c * d - f * a) // (b * d - e * a)
print(x, y)
