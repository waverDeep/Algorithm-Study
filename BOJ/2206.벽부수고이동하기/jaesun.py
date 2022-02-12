from collections import deque


N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    queue = deque()
    queue.append((0,0,0))
    visited[0][0][0] = 1
    while queue:
        x,y,z = queue.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                queue.append((nx,ny,z))
                visited[nx][ny][z] = visited[x][y][z] + 1
            if graph[nx][ny] == 1 and z == 0:
                queue.append((nx,ny,z+1))
                visited[nx][ny][z+1] = visited[x][y][z] + 1
    return -1

print(bfs())

for line in visited:
    print(line)
