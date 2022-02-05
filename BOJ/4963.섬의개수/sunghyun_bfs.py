def bfs(x, y):
    need_visited = []
    step_x = [1, -1, 0, 0, 1, -1, 1, -1]
    step_y = [0, 0, -1, 1, -1, 1, 1, -1]

    island_map[x][y] = 2
    need_visited.append([x, y])
    while need_visited:
        temp_x, temp_y = need_visited.pop(0)
        for step in range(8):
            position_x = temp_x + step_x[step]
            position_y = temp_y + step_y[step]
            if 0 <= position_x < h and 0 <= position_y < w:
                if island_map[position_x][position_y] == 1:
                    island_map[position_x][position_y] = 2
                    need_visited.append([position_x, position_y])


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
                bfs(i, j)
                cnt += 1
    print(cnt)