memo = {0: 0, 1: 1}


def f(n):
    if memo.get(n) is not None:
        return memo[n]
    memo[n] = f(n - 1) + f(n - 2)
    return memo[n]


print(f(int(input())))
