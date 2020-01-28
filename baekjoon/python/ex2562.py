import sys


def solution(n):
    """첫번째 방법"""
    max_num = float("-inf")
    max_index = -1
    for _ in range(n):
        num = int(sys.stdin.readline().strip())

        if max_num < num:
            max_num = num
            max_index = _ + 1
        else:
            pass

    print(max_num)
    print(max_index)


def solution2(n):
    """두번째 방법"""
    num_list = list()
    for _ in range(n):
        num_list.append(int(sys.stdin.readline().strip()))

    max_num = max(num_list)

    print(max_num)
    print(num_list.index(max_num) + 1)


if __name__ == "__main__":
    solution2(9)
