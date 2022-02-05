from collections import deque
import sys

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
# graph = [[]*(N+1)]
for _ in range(M):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    graph[line[0]].append(line[1])
    graph[line[1]].append(line[0])

for i in range(N+1):
    graph[i].sort()
# print(graph)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

dfs(graph, V, visited_dfs)
print()
bfs(graph, V, visited_bfs)

