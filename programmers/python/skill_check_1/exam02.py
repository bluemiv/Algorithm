def solution(a, b):
    if a == b:
        return a
    return sum(range(a, b + 1) if a < b else range(b, a + 1))
