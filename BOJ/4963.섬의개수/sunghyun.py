import sys
sys.setrecursionlimit(50000000)

def dfs(x, y):
    if 0 <= x < h and 0 <= y < w:
        if island_map[x][y] == 1:
            island_map[x][y] = 2
            dfs(x-1, y-1)
            dfs(x-1, y)
            dfs(x-1, y+1)
            dfs(x, y-1)
            dfs(x, y+1)
            dfs(x+1, y-1)
            dfs(x+1, y)
            dfs(x+1, y+1)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    # 2차원 리스트 생성
    island_map = []
    for i in range(h):
        island_map.append(list(map(int, input().split())))
    cnt = 0
    for i in range(h):
        for j in range(w):
            if island_map[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)