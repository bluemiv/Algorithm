def solution(s):
    nums = list(map(str, sorted(map(int, s.split()))))
    return " ".join([nums[0], nums[-1]])
