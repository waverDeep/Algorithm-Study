from collections import deque

M, N, H = map(int, input().split())

graph = [[] for _ in range(H)]
for i in range(H):
    for _ in range(N):
        graph[i].append(list(map(int, input().split())))

queue = deque()
result = 0

for z in range(H):
    for y in range(N):
        for x in range(M):
            if graph[z][y][x] == 1:
                queue.append((x,y,z))

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def bfs():
    while queue:
        x,y,z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0  or nx >= M or ny < 0 or ny >= N or nz < 0 or nz >= H:
                continue
            if graph[nz][ny][nx] == -1:
                continue
            if graph[nz][ny][nx] == 1:
                continue
            if graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                queue.append((nx,ny,nz))

bfs()

for z in range(H):
    for y in range(N):
        for x in range(M):
            if graph[z][y][x] == 0:
                print(-1)
                exit(0)
        result = max(result, max(graph[z][y]))
print(result - 1)



# 파이썬 3차원 리스트 높이*가로*세로 리스트[높이][세로][가로]
# [[0 for col in range(3)] for row in range(4)] 3*4 2차원리스트 
# [[[0 for col in range(3)] for row in range(4)] for depth in range(2)]
