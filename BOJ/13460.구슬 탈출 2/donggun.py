from collections import deque

n, m = map(int, input().split())

graph = []

redQueue = deque()
blueQueue = deque()

for i in range(n):

    col = input().split()
    newCol = []
    for idx, j in enumerate(col[0]):
        if j == '#':
            newCol.append(1)
        if j == '.':
            newCol.append(0)
        if j == 'O':
            newCol.append(-1)
        if j == 'R':
            newCol.append(3)
            redQueue.append((i, idx))
        if j == 'B':
            newCol.append(4)
            blueQueue.append((i, idx))
    graph.append(newCol)

print(graph)
print(redQueue)
print(blueQueue)

count = 0
while redQueue:
    count += 1
    if count == 11:
        break
    popleft = redQueue.popleft()
    x = popleft[0]
    y = popleft[1]
    print(x)
    print(y)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        while graph[x][y] == 0 or graph[x][y] == 3:
            x = x + dx[i]
            y = x + dx[i]
            print('this is :')
            print(graph[x][y])
            print("x :")
            print(x)
            print("y :")
            print(y)

        print("========")
        print(graph[x][y])


