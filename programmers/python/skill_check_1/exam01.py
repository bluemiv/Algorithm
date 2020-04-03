def is_prime(number):
    a = [False, False] + [True] * (number - 1)
    primes = list()

    for i in range(2, number + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, number + 1, i):
                a[j] = False
    return a


def solution(n):
    answer = 0
    table = is_prime(n)
    for num in range(1, n + 1):
        if table[num]:
            answer += 1
    return answer
