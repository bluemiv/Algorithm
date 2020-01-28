import sys


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())

    for _ in range(n):
        print(sum(list(map(int, sys.stdin.readline().split(" ")))))
