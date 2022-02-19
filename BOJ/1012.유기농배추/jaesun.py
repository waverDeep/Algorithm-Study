from collections import deque

T = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x,y,graph):
    queue = deque([(x,y)])
    graph[x][y] = 0
    global cnt
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    cnt += 1

for _ in range(T):
    cnt = 0    
    M, N, K = map(int, input().split())
    graph = [[0]*N for _ in range(M)]
    for _ in range(K):
        a, b = map(int, input().split())
        graph[a][b] = 1
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                bfs(i, j, graph)
    print(cnt)




