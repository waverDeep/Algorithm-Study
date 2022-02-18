import copy

n, m = map(int, input().split())

graph = []
count = 0
result = 0

for _ in range(n):
    graph.append(list(map(int, input())))

print(graph)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def shortest(x, y, graph):

    if (x == (n - 1) and y == (m - 1)):
        global result
        result = graph[x][y]

        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (nx >= 0 and nx < n and ny >= 0 and ny < m):
            if (graph[nx][ny] == 0):
                graph[nx][ny] = graph[x][y] - 1
                shortest(nx, ny, graph)
                print(graph)

def breakWall():
    global count
    for i in range(n):
        for j in range(m):
            deepcopy = copy.deepcopy(graph)
            print("####")
            print(deepcopy)
            print("####")
            if deepcopy[i][j] == 1:
                deepcopy[i][j] = 0
                deepcopy[0][0] = -1
                shortest(1, 1, deepcopy)
                print(result)
                # print(deepcopy)
                # count = min(count, )
                # graph[i][j] = 1

breakWall()
print(count)


'''
[-11, 1, -9, -8], 
[1, 1, 1, -7], 
[1, -2, -3, -6], 
[-2, -1, -4, -5], 
[-3, 1, 1, 0], 
[-4, -5, -6, -7]
'''