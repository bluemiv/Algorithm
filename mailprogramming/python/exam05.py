# -*- coding: utf-8 -*-
import time
from functools import wraps


def getRunningTime(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            return func(*args, **kwargs)
        finally:
            end = time.time()
            print(end - start)
    return wrapper


@getRunningTime
def solution(n, _open, close, bracket, result):
    if close == n:
        result.append(bracket)
        return

    # 열고
    if _open < n:
        solution(n, _open + 1, close, bracket + "(", result)

    # 닫고
    if close < _open:
        solution(n, _open, close + 1, bracket + ")", result)


# main
if __name__ == "__main__":
    # 시간 체크
    n = 4

    result = list()
    solution(n, 0, 0, "", result)
    print(len(result))
