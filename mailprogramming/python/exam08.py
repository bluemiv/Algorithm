# -*- coding: utf-8 -*-


def solution(arr):
    # 최댓값을 구함
    max_num = float("-inf")
    for e in arr:
        max_num = max(max_num, max(e[0], e[1]))

    # 최대값만큼 리스트를 생성
    flag = [0 for _ in range(max_num+1)]
    for e in arr:
        # 비트를 1로 바꿔줌. (그래프를 그림)
        for idx in range(e[0], e[1]+1):
            flag[idx] = 1

    # 결과값 반환
    rst, tmp_range = list(), list()
    for idx in range(max_num):
        if flag[idx] == 0 and flag[idx+1] == 1:
            # 처음 시작점
            tmp_range.append(idx+1)
        elif (flag[idx] == 1 and flag[idx+1] == 0):
            # 끝나는점
            tmp_range.append(idx)
        elif (idx == max_num-1 and flag[idx] == 1 and flag[idx+1] == 1):
            # 맨 마지막점인데, 값이 1인경우
            tmp_range.append(idx+1)

        # 구간이 만들어지면 결과값에 넣음
        if len(tmp_range) == 2:
            rst.append(tmp_range)
            tmp_range = list()
    return rst


if __name__ == "__main__":
    test_case = [[[2, 4], [1, 5], [7, 9]], [[3, 6], [1, 3], [2, 4]]]
    for test in test_case:
        print("Input:", test)
        print("Output:", solution(test))
