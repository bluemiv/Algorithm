# -*- coding: utf-8 -*-


def solution(arr):
    result = 0

    for i in range(len(arr[0])):
        for j in range(1, len(arr)):
            if len(arr[j]) < i + 1 or arr[j-1][i] != arr[j][i]:
                return result  # 인덱스를 벗어나는 경우 또는 전의 값과 지금 값이 다른경우(결과 반환)
        result += 1

    return result


if __name__ == "__main__":
    test_case = [
        ["apple", "apps", "ape"],
        ["hawaii", "happy"],
        ["dog", "dogs", "doge"],
        ["banana", "b", "banana"],
        ["happy", "happy", "happy"]
    ]

    for test in test_case:
        print("Input:", test, "| Output:", solution(test))
