import sys
input = sys.stdin.readline
from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)

# print(graph)

distance = [-1] * (n + 1)
distance[x] = 0

queue = deque([x])
while queue:
    v = queue.popleft()

    for i in graph[v]:
        # print(i)
        # print(visited)
        if distance[i] == -1:
            distance[i] = distance[v] + 1
            queue.append(i)

# print(distance)
# print(k)

# check = False

for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        # check = True
if k not in distance:
    print(-1)

# if not check:
#     print(-1)