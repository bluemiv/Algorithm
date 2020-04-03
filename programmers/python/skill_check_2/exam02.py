def solution(heights):
    n = len(heights)
    answer = [0] * n

    tower_idx = range(n, 0, -1)
    for i in tower_idx:
        for j in tower_idx[n - i + 1:]:
            if heights[i-1] < heights[j-1]:
                answer[i-1] = j
                break
    return answer
