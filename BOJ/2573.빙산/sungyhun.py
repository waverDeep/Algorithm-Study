from collections import deque


def bfs(visited, count, x, y):
    need_visited = deque()
    need_visited.append([x, y])
    while need_visited:
        x, y = need_visited.popleft()
        visited[x][y] = 1
        for i in range(4):
            move_x = x + step_x[i]
            move_y = y + step_y[i]
            if 0 <= move_x < N and 0 <= move_y < M:
                if graph[move_x][move_y] != 0 and visited[move_x][move_y] == 0:
                    visited[move_x][move_y] = 1
                    need_visited.append([move_x, move_y])
                elif graph[move_x][move_y] == 0:
                    count[x][y] += 1


step_x = [-1, 1, 0, 0]
step_y = [0, 0, -1, 1]

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(N)]
day = 0

while True:
    # 방문여부
    visited = [[0] * M for i in range(N)]
    # 개수
    count = [[0] * M for i in range(N)]

    check = 0
    for x in range(N):
        for y in range(M):
            if graph[x][y] != 0 and visited[x][y] == 0:
                bfs(visited, count, x, y)
                check += 1

    for x in range(N):
        for y in range(M):
            graph[x][y] -= count[x][y]
            if graph[x][y] < 0:
                graph[x][y] = 0

    #     for x in range(N):
    #         print(graph[x])

    #     print(check)

    if check == 0:
        print(0)
        break
    if check > 1:
        print(day)
        break
    day += 1



