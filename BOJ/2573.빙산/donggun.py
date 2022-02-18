n, m = map(int, input().split())

graph = []
temp = [[0] * m for _ in range(n)]

years = 0

for i in range(n):
    graph.append(list(map(int, input().split())))

# print(graph)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def melt(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx >= 0 and nx < n and ny >= 0 and ny < m):
            if (graph[nx][ny] > 0):
                graph[nx][ny] -= 1

def countYears():
    global years
    ice = []

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                ice.append((i, j))

    # print(ice)

    for i in ice:
        melt(i[0], i[1])

    # print(graph)
    years -= 1


def countIce(x, y, count = 0):
    temp[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx >= 0 and nx < n and ny >= 0 and ny < m):
            if (graph[nx][ny] > 0 and temp[x][y] == 0):
                countIce(nx, ny, count)
                count += 1
                return count

iceCount = 0

countYears()
for i in range(n):
    for j in range(m):
        print(temp)
        print(graph[i][j])
        print(temp[i][j])
        if graph[i][j] > 0 and temp[i][j] == 0:
            countIce(i, j)
            iceCount += 1
print(iceCount)
print(graph)
