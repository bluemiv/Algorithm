import sys


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        print(
            "Case #{}: {}"
            .format(
                _ + 1,
                sum(list(map(int, sys.stdin.readline().split())))
            )
        )
