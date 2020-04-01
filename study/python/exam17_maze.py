# -*- coding: utf-8 -*-

import unittest


def bfs(graph, start, end):
    """BFS 를 이용하여 미로 찾기 알고리즘을 구현한다.

    :param graph: 미로 그래프
    :param start: 출발 지점(노드)
    :param end: 도작 지점(노드)
    :return: 최소 이동 거리
    """
    queue = [(start, 0)]  # idx 0: 노드, idx 1: 이동 거리
    visit = {start, }  # 방문한 노드 저장 공간

    while queue:
        node, distance = queue.pop(0)

        new_distance = distance + 1
        for near_node in graph[node]:
            # 방문한 적 없는 노드인 경우
            if near_node not in visit:
                print("{} Node 방문".format(near_node))

                # 도착 지점에 도착한 경우 총 이동거리를 반환
                if near_node == end:
                    return new_distance

                visit.add(near_node)  # 방문
                queue.append((near_node, new_distance))  # 이동 거리를 1 증가 시킨다.

    return -1  # 도착 지점이 막힌 경우(없는 경우)


def dfs(graph, start, end):
    """DFS 를 이용하여 미로 찾기 알고리즘을 구현한다.

    :param graph: 미로 그래프
    :param start: 출발 지점(노드)
    :param end: 도작 지점(노드)
    :return: 최소 이동 거리
    """
    stack = [(start, 0)]  # idx 0: 노드, idx 1: 이동 거리
    visit = {start, }  # 방문한 노드 저장 공간

    while stack:
        node, distance = stack.pop()

        new_distance = distance + 1
        for near_node in graph[node]:
            # 방문한 적 없는 노드인 경우
            if near_node not in visit:
                print("{} Node 방문".format(near_node))

                # 도착 지점에 도착한 경우 총 이동거리를 반환
                if near_node == end:
                    return new_distance

                visit.add(near_node)  # 방문
                stack.append((near_node, new_distance))  # 이동 거리를 1 증가 시킨다.

    return -1  # 도착 지점이 막힌 경우(없는 경우)


class Exam17(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.graph = {
            "A": ["B"],
            "B": ["A", "C"],
            "C": ["B", "D"],
            "D": ["C", "E"],
            "E": ["D", "F"],
            "F": ["E", "G"],
            "G": ["F", "J"],
            "H": ["I"],
            "I": ["H", "P"],
            "J": ["G", "K", "O"],
            "K": ["J", "L"],
            "L": ["K", "M"],
            "M": ["L"],
            "N": ["O"],
            "O": ["J", "N", "P"],
            "P": ["I", "O"]
        }

    def test_bfs(self):
        self.assertEqual(10, bfs(self.graph, "A", "M"))

    def test_dfs(self):
        self.assertEqual(10, dfs(self.graph, "A", "M"))


if __name__ == "__main__":
    unittest.main()
