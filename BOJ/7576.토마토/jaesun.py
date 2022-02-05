from collections import deque

M, N = map(int,input().split())
graph = []
queue = deque([])
for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i,j))
 
dx=[0,0,1,-1]
dy=[1,-1,0,0]
res = 0

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

bfs()
    
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(-1)
            exit(0)
    res = max(res, max(graph[i]))
print(res - 1)