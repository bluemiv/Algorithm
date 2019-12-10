import sys


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    nums = tuple(map(int, sys.stdin.readline().split()))
    print(min(nums), max(nums))
