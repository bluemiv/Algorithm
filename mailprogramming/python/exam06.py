# -*-coding: utf-8 -*-
import sys

def solution(string):
    return " ".join(map(lambda x: x[::-1], string.split()))


if __name__ == "__main__":
    _input = sys.stdin.readline()

    print(solution(_input))
