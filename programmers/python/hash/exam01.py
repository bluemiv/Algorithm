# -*- coding: utf -*-

import unittest
import collections


def solution(participant, completion):
    _p = collections.defaultdict(lambda: 0)
    _c = collections.defaultdict(lambda: 0)

    for name in participant:
        _p[name] += 1

    for name in completion:
        _c[name] += 1

    for key in _p.keys():
        if 0 == _c[key] or _p[key] != _c[key]:
            return key
    return -1


class HashExam01(unittest.TestCase):

    def test1(self):
        self.assertEqual("leo", solution(["leo", "kiki", "eden"], ["eden", "kiki"]))

    def test2(self):
        self.assertEqual(
            "vinko",
            solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))

    def test3(self):
        self.assertEqual(
            "mislav",
            solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))


if __name__ == "__main__":
    unittest.main()
