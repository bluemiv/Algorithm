# -*- coding: utf-8 -*-

import unittest


def bfs(graph, start):
    """너비 우선 탐색 알고리즘"""
    queue = [start]  # 초기값은 시작 노드
    visit = list()  # 방문했던 노드는 다시 재방문 하지 않기 위해 저장

    while queue:
        node = queue.pop(0)  # 큐에서 노드를 꺼내온다.

        if node not in visit:  # 방문하지 않은 노드인 경우, 방문한다.
            visit.append(node)  # 방문 리스트에 추가한다.

            # 큐에 인접한 노드들을 추가한다.
            # (extend()는 아래 코드와 동일하다)
            queue.extend(graph[node])
            # for new_node in graph[node]:
            #     queue.append(new_node)

    return visit


def dfs(graph, start):
    """깊이 우선 탐색 알고리즘"""
    stack = [start]
    visit = list()

    while stack:
        node = stack.pop()

        if node not in visit:
            visit.append(node)

            # 아래와 같이 해도 DFS 이지만, 오른쪽에서 왼쪽으로 탐색을 해서 결과값이 다르게 나온다.
            # ["A", "B", "D", "H", "K", "J", "M", "G", "C", "F", "I", "L", "E"]
            # stack.extend(graph[node])
            stack.extend(reversed(graph[node]))  # 왼쪽에서 오른쪽 탐색을 위해, reversed()를 이용해 연순으로 바꿔준다.

    return visit


class Exam15(unittest.TestCase):

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

    def test_bfs(self):
        self.assertEqual(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"], bfs(self.graph, "A"))

    def test_dfs(self):
        self.assertEqual(["A", "B", "C", "E", "F", "I", "L", "D", "G", "H", "J", "M", "K"], dfs(self.graph, "A"))


if __name__ == "__main__":
    unittest.main()
