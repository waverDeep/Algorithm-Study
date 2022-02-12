from collections import deque


step_x = [-1, 1, 0, 0]
step_y = [0, 0, -1, 1]


def bfs(red_ball_x, red_ball_y, blue_ball_x, blue_ball_y):
    need_visited= deque()
    need_visited.append((red_ball_x, red_ball_y, blue_ball_x, blue_ball_y))
    visited = []
    visited.append((red_ball_x, red_ball_y, blue_ball_x, blue_ball_y))
    count = 0
    while need_visited:
        for _ in range(len(need_visited)):
            red_ball_x, red_ball_y, blue_ball_x, blue_ball_y = need_visited.popleft()
            if count > 10:
                print(-1)
                return
            if maze[red_ball_x][red_ball_y] == 'O':
                print(count)
                return
            for i in range(4):
                move_red_ball_x, move_red_ball_y = red_ball_x, red_ball_y
                while True:
                    move_red_ball_x += step_x[i]
                    move_red_ball_y += step_y[i]
                    if maze[move_red_ball_x][move_red_ball_y] == '#':
                        move_red_ball_x -= step_x[i]
                        move_red_ball_y -= step_y[i]
                        break
                    if maze[move_red_ball_x][move_red_ball_y] == 'O':
                        break
                move_blue_ball_x, move_blue_ball_y = blue_ball_x, blue_ball_y
                while True:
                    move_blue_ball_x += step_x[i]
                    move_blue_ball_y += step_y[i]
                    if maze[move_blue_ball_x][move_blue_ball_y] == '#':
                        move_blue_ball_x -= step_x[i]
                        move_blue_ball_y -= step_y[i]
                        break
                    if maze[move_blue_ball_x][move_blue_ball_y] == 'O':
                        break
                if maze[move_blue_ball_x][move_blue_ball_y] == 'O':
                    continue
                if move_red_ball_x == move_blue_ball_x and move_red_ball_y == move_blue_ball_y:
                    if abs(move_red_ball_x - red_ball_x) + abs(move_red_ball_y - red_ball_y) > abs(move_blue_ball_x - blue_ball_x) + abs(move_blue_ball_y - blue_ball_y):
                        move_red_ball_x -= step_x[i]
                        move_red_ball_y -= step_y[i]
                    else:
                        move_blue_ball_x -= step_x[i]
                        move_blue_ball_y -= step_y[i]
                if (move_red_ball_x, move_red_ball_y, move_blue_ball_x, move_blue_ball_y) not in visited:  # 방문해본적이 없는 위치라면 새로 큐에 추가 후 방문 처리
                    need_visited.append((move_red_ball_x, move_red_ball_y, move_blue_ball_x, move_blue_ball_y))
                    visited.append((move_red_ball_x, move_red_ball_y, move_blue_ball_x, move_blue_ball_y))
        count += 1
    print(-1)  # 10회가 초과하지 않았지만 10회 내에도 구멍에 들어가지 못하는 경우

N, M = map(int, input().split())
maze = []
for i in range(N):
    maze.append(list(input()))
    for j in range(M):
        if maze[i][j] == 'R':
            red_ball_x, red_ball_y = i, j
        elif maze[i][j] == 'B': 
            blue_ball_x, blue_ball_y = i, j


bfs(red_ball_x, red_ball_y, blue_ball_x, blue_ball_y)