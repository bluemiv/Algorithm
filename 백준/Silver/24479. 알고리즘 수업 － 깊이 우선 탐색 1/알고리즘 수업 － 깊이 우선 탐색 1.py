import sys

input = sys.stdin.readline

n, m, start = map(int, input().strip().split())

graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    snode, enode = map(int, input().strip().split())
    graph[snode].append(enode)
    graph[enode].append(snode)

for key in graph.keys():
    graph[key].sort(reverse=True)

stack = [start]
count = [0] * (n + 1)
cnt = 1
while stack:
    node = stack.pop()
    if count[node] != 0:
        continue

    count[node] = cnt
    cnt += 1
    for neighbor in graph[node]:
        stack.append(neighbor)

for i in range(1, len(count)):
    print(count[i])
