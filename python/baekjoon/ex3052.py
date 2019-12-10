import sys


def solution(n, div_num):
    num_set = set()

    for _ in range(n):
        num = int(sys.stdin.readline().strip())
        num_set.add(num % div_num)

    print(len(num_set))


if __name__ == "__main__":
    solution(10, 42)
