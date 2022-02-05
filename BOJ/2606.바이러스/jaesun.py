from collections import deque
import sys


computer = int(input())
network = int(input())

graph = [[] for _ in range(computer+1)]

for _ in range(network):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(computer+1)
cnt = 0

def dfs(v):
    global cnt
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1 #1번컴퓨터를 통해 감염되는 컴퓨터 수 즉, 출발 노드 제외

dfs(1)
print(cnt)

visited = [0]*(computer+1)
cnt = 0

def bfs(v):
    global cnt
    queue = deque([v])
    visited[v] = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                cnt += 1

bfs(1)
print(cnt)
