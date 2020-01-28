# -*- coding: utf-8 -*-

import sys


def get_new_minute(minute):
    if minute < 45:
        change_hour = True
        new_minute = 60 + (minute - 45)
    else:
        change_hour = False
        new_minute = minute - 45

    return new_minute, change_hour


def solve(hour, minute):
    # 예외. 시간이 0이고 분이 45분보다 작은 경우 23시로 바뀐다.
    new_minute, change_hour = get_new_minute(minute)

    if change_hour:
        if hour == 0:
            return 23, new_minute
        else:
            return hour - 1, new_minute
    else:
        return hour, new_minute


if __name__ == "__main__":
    hour, minute = list(map(int, sys.stdin.readline().split()))

    result = solve(hour, minute)

    print(result[0], result[1])
