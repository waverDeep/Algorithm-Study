from collections import deque

step_x = [-1, 1, 0, 0]
step_y = [0, 0, -1, 1]


def bfs(graph, keep):
    need_visited = deque()
    visited = []
    need_visited.append(keep)
    graph[keep[0]][keep[1]] = 0

    while need_visited:
        x, y = need_visited.popleft()
        for i in range(4):
            move_x = x + step_x[i]
            move_y = y + step_y[i]
            if move_x < 0 or move_x >= M or move_y < 0 or move_y >= N:
                continue
            if graph[move_x][move_y] == 1:
                graph[move_x][move_y] = 0
                need_visited.append([move_x, move_y])


T = int(input())
for i in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * (N) for i in range(M)]
    for i in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1
    count = 0

    for x in range(M):
        for y in range(N):
            if graph[x][y] == 1:
                bfs(graph, [x, y])
                count += 1
    print(count)


