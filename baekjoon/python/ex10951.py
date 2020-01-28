import sys


if __name__ == "__main__":
    _input = "init"
    while _input:
        _input = sys.stdin.readline().strip()
        if _input:
            print(sum(list(map(int, _input.split()))))
