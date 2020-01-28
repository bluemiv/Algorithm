# -*- coding: utf-8 -*-

import sys


def solve(plain, encrypt):
    # 유효성 검사
    assert len(plain) == len(
        encrypt), "Invalid value for argument. <{}, {}>".format(plain, encrypt)

    # 비교 시작
    alpa_dict = dict()  # 평문 문자에 대한 암호화 문자를 담고 있는 맵 자료형
    for i in range(len(plain)):
        p_c = plain[i]
        e_c = encrypt[i]
        print("[%r번째]" % i, end=" ")

        if p_c in alpa_dict.keys():
            # Case1. 이미 나온 문자
            print("%r, %r은 이미 등록된 문자" % (p_c, encrypt[i]))
            if alpa_dict[p_c] != e_c:
                return False  # 이미 등록된 문자와 다른 경우, 거짓
        else:
            # Case2. 처음 나온 문자
            print("%r, %r은 처음 등록된 문자" % (p_c, encrypt[i]))
            alpa_dict[p_c] = e_c

    return True


if __name__ == "__main__":
    _input = sys.stdin.readline().split(",")
    plain = _input[0].strip()
    encrypt = _input[1].strip()

    print(solve(plain, encrypt))
