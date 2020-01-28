# -*- coding: utf-8 -*-


def solution(n, _open, close, bracket, result):
    if close == n:
        result.append(bracket)  # 닫는 괄호까지 모두 마쳤다면, 리스트에 추가
        return

    # 열었으면 닫아준다
    # 열고
    if _open < n:
        solution(n, _open + 1, close, bracket + "(", result)

    # 닫고
    if close < _open:
        solution(n, _open, close + 1, bracket + ")", result)


# main
if __name__ == "__main__":
    test_case = [1, 2, 3, 4, 5]

    for test in test_case:
        result = list()
        solution(test, 0, 0, "", result)
        print("Input:", test, "| Output:", result)
