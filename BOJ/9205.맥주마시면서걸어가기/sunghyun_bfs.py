def bfs():
    queue = []
    queue.append(0)
    while queue:
        node = queue.pop(0)
        for i in range(n + 2):
            if graph[node][i] == 1 and check[i] == 0:
                check[i] = 1
                queue.append(i)


for _ in range(int(input())):
    n = int(input())
    li = [list(map(int, input().split())) for i in range(n + 2)]
    graph = [[0] * (n + 2) for i in range(n + 2)]
    check = [0] * (n + 2)
    for i in range(n + 2):
        for j in range(n + 2):
            if i == j:
                continue
            if abs(li[i][0] - li[j][0]) + abs(li[i][1] - li[j][1]) <= 1000:
                graph[i][j] = 1
                graph[j][i] = 1
    check[0] = 1
    bfs()
    print("happy" if check[-1] else "sad")