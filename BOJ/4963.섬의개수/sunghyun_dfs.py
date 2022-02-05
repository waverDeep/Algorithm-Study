import sys
# 이거를 해줘야 하는지 몰랐었다...
sys.setrecursionlimit(50000000)


def dfs(x, y):
    if 0 <= x < h and 0 <= y < w:
        # 만약 섬이면!
        if island_map[x][y] == 1:
            # 방문한 땅은 2로 바꾸고
            island_map[x][y] = 2
            # 상하좌우 대각선 다 방문하면서어디까지가 섬인지 알아보기!
            dfs(x-1, y-1)
            dfs(x-1, y)
            dfs(x-1, y+1)
            dfs(x, y-1)
            dfs(x, y+1)
            dfs(x+1, y-1)
            dfs(x+1, y)
            dfs(x+1, y+1)


while True:
    # 너비와 높이를 입력받는데,
    w, h = map(int, input().split())

    # 둘다 0이라면 반복을 종료하고 프로그램 종료한다.
    if w == 0 and h == 0:
        break
    # 지도를 생성하기 위한 리스트를 생성한다.
    island_map = []
    # 반복문을 통해서 2차원 형태의 리스트를 입력받는다.
    for i in range(h):
        island_map.append(list(map(int, input().split())))
    # 섬이 몇개있는지 세는 변수
    cnt = 0
    # 2차원 리스트를 탐색하려면 당연히 중첩 반복문...
    for i in range(h):
        for j in range(w):
            # 만약 섬이라면...!
            if island_map[i][j] == 1:
                # 어디까지가 섬인지 알아보자! -> 재귀호출
                dfs(i, j)
                cnt += 1
    print(cnt)