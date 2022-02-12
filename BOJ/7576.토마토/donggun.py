from collections import deque

m, n = map(int, input().split())
graph = []
global count
count = 0

for i in range(n):
    graph.append(list(map(int, input().split())))

print(graph)

def bfs(graph, x, y, count):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    graph[x][y] = 2
    queue = deque([[x, y]])
    while queue:
        popleft = queue.popleft()
        print(popleft)
        print(queue)
        x = popleft[0]
        y = popleft[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            print(nx)
            print(ny)
            print("==============")

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    queue.append([nx, ny])
                    print('##############')
                    print(graph)
                    print(queue)
                    print('##############')
                    count += 1


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(graph, i, j, count)

print('count : ')
print(count)

