# -*-coding: utf-8 -*-
from collections import defaultdict


def solution(n):
    """memoization을 이용하여 시간 단축

    variable:
        result: 반환값(피보나치 수열에서 n보다 작은 짝수들의 합)
        memo: 연산된 값을 저장하기 위한 Dictionary 자료형
    """
    result = 0
    memo = defaultdict(lambda: -1)  # 0과 1로 시작
    memo[0] = 0
    memo[1] = 1
    for k in range(n):
        if memo[k] != -1:
            continue  # 이미 계산한적이 있음
        else:
            memo[k] = memo[k-1] + memo[k-2]
            if memo[k] < n:
                # n 보다 작은 경우만
                if memo[k] % 2 == 0:
                    result += memo[k]
            else:
                break  # n보다 크거나 같은 경우 종료
    return result


def fibo(n):
    if n < 2:
        return n
    return fibo(n-1) + fibo(n-2)


def useNotMemo(n):
    """memoization을 사용하지 않는 경우
    """
    result = 0
    for n in range(2, n):
        if fibo(n) % 2 == 0:
            result += fibo(n)
    return result


if __name__ == "__main__":
    test_case = [12, 144, 300, 800, 1000]

    for test in test_case:
        print("Input:", test, "| Output:", solution(test))
        # print("Input:", test, "| Output:", useNotMemo(test))
