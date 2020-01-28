def solution1(int_list):
    tmp = 0  # 누적 값
    rst_list = []  # 누적 값들의 리스트
    for _ in int_list:
        tmp = max([tmp + _, _])  # 누적 합과 현재 값 비교
        rst_list.append(tmp)  # 가장 큰 누적값들을 넣어줌.
    return max(rst_list)


def solution2(int_list):
    """
    정수 배열(int array)가 주어지면 가장 큰 이어지는 원소들의 합을 구하시오. 단, 시간복잡도는 O(n).
    Given an integer array, find the largest consecutive sum of elements.
    """
    tmp = 0  # 누적값
    rst_sum = float("-inf")  # 가장 큰 누적 값 (default: 가장 작은 수)
    for _ in int_list:
        tmp = max([tmp + _, _])  # 누적 합과 현재 값 비교
        rst_sum = max([tmp, rst_sum])  # 이전 최종값하고 현재 최종값 비교
    return rst_sum


# main
if __name__ == "__main__":
    test_case = [
        [-1, 3, -1, 5],
        [-5, -3, -1],
        [2, 4, -2, -3, 8],
        [2, 99, -233, -3, 92],  # 임의로 넣어본 예제 (2 + 99 = 103이 나와야 함)
    ]
    for test in test_case:
        print("Input:", test, "| Output:", solution1(test))
