N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x < 0 or x >= N or y < 0  or y >= N:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        visited.append((x,y))
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

# 처음 dfs 시작점에서 단지내 모든 노드들을 graph[x][y] = 1 해주니까 밑에서 단지 내 모든 노드들이 return True 하는게 아니지
result = 0
house = []

for i in range(N):
    for j in range(N):
        visited = []
        if dfs(i, j) == True:
            result += 1
            house.append(len(visited))
            

print(result)

house.sort()
for num in house:
    print(num)

