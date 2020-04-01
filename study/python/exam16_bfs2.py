# -*- coding: utf-8 -*-

import unittest


def bfs(graph, start):
    """BFS 를 이용하여 각 노드들의 비용을 구한다."""
    result = {start: 0}

    queue = [(start, 0)]  # idx 0: 노드(Node), idx 1: 비용(Cost)
    visit = [start]

    while queue:
        node, cost = queue.pop(0)

        cost += 1

        near_nodes = graph[node]
        for near_node in near_nodes:
            if near_node not in visit:
                visit.append(near_node)  # 방문 표시
                queue.append((near_node, cost))  # 근접한 노드 정보(노드, 비용) 추가
                result[near_node] = cost  # 결과 값 저장
    return result


class Exam16(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.graph = {
            "A": ["B"],
            "B": ["A", "C", "D"],
            "C": ["B", "E", "F"],
            "D": ["B", "G", "H"],
            "E": ["C"],
            "F": ["C", "I"],
            "G": ["D"],
            "H": ["D", "J", "K"],
            "I": ["F", "L"],
            "J": ["H", "M"],
            "K": ["H"],
            "L": ["I"],
            "M": ["J"],
        }

    def test_bfs_a(self):
        self.assertEqual(
            {"A": 0, "B": 1, "C": 2, "D": 2, "E": 3, "F": 3, "G": 3, "H": 3, "I": 4, "J": 4, "K": 4, "L": 5, "M": 5},
            bfs(self.graph, "A")
        )

    def test_bfs_b(self):
        self.assertEqual(
            {"A": 1, "B": 0, "C": 1, "D": 1, "E": 2, "F": 2, "G": 2, "H": 2, "I": 3, "J": 3, "K": 3, "L": 4, "M": 4},
            bfs(self.graph, "B")
        )

    def test_bfs_c(self):
        self.assertEqual(
            {"A": 2, "B": 1, "C": 0, "D": 2, "E": 1, "F": 1, "G": 3, "H": 3, "I": 2, "J": 4, "K": 4, "L": 3, "M": 5},
            bfs(self.graph, "C")
        )


if __name__ == "__main__":
    unittest.main()
