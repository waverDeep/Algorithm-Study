import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
temp = [[0] * m for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, input().split())))

result = 0

def virus(x, y):

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx > -1 and nx < n and ny > -1 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

def score():
    point = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                point += 1
    return point

def dfs(count):
    global result
    # 울타리 3개
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]
        # 바이러스 전파
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        result = max(result, score())
        return

    # 울타리 설치
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1

dfs(0)

print(result)
