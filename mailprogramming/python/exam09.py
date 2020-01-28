# -*- coding: utf-8 -*-


def solution(arr):
    def _generator(arr):
        """메모리 절약을 위해 제너레이터 이용"""
        for e in arr:
            if e != 0:
                yield e

    rst = list()
    for e in _generator(arr):
        rst.append(e)  # 이터레이터에서 0이 아닌 값을 가져옴

    rst.extend([0 for _ in range(len(rst), len(arr))])  # 나머지는 0으로 채움
    return rst


# Main
if __name__ == "__main__":
    test_case = [
        [0, 5, 0, 3, -1],
        [3, 0, 3]
    ]

    for test in test_case:
        print("Input:", test)
        print("Output:", solution(test))
