step_x = [-1, 1, 0, 0]
step_y = [0, 0, -1, 1]


def bfs(red_ball, blue_ball):
    need_visited = []
    visited = []
    count = 0
    need_visited.append([red_ball, blue_ball])
    visited.append([red_ball, blue_ball])

    while need_visited:
        print(need_visited)
        for _ in range(len(need_visited)):
            # 만약 실행 횟수가 10 초과라면...
            if count > 10:
                return -1
            pick_red_ball, pick_blue_ball = need_visited.pop(0)

            # 만약 구멍에 나갔다면
            if maze[pick_red_ball[0]][pick_red_ball[1]] == '0':
                return count

            # 종료시점이 아니라면 4방향 탐색
            for step in range(4):
                red_ball_move_x, red_ball_move_y = pick_red_ball
                # 벽에 부딛칠때까지 굴러가야 한다고 함
                while True:
                    red_ball_move_x += step_x[step]
                    red_ball_move_y += step_y[step]
                    # 만약에 벽이라면
                    if maze[red_ball_move_x][red_ball_move_y] == '#':
                        # 한벅 빽 해야 다음으로 이동할수 있지
                        red_ball_move_x -= step_x[step]
                        red_ball_move_y -= step_y[step]
                        break
                    # 만약 구멍이라면
                    elif maze[red_ball_move_x][red_ball_move_y] == '0':
                        break

                # 파란색도
                blue_ball_move_x, blue_ball_move_y = pick_blue_ball
                # 벽에 부딛칠때까지 굴러가야 한다고 함
                while True:
                    blue_ball_move_x += step_x[step]
                    blue_ball_move_y += step_y[step]
                    # 만약에 벽이라면
                    if maze[blue_ball_move_x][blue_ball_move_y] == '#':
                        # 한벅 빽 해야 다음으로 이동할수 있지
                        blue_ball_move_x -= step_x[step]
                        blue_ball_move_y -= step_y[step]
                        break
                    # 만약 구멍이라면
                    elif maze[blue_ball_move_x][blue_ball_move_y] == '0':
                        break

                if red_ball_move_x == blue_ball_move_x and red_ball_move_y == blue_ball_move_y:
                    if abs(red_ball_move_x - pick_red_ball[0]) + abs(red_ball_move_y - pick_red_ball[1]) > abs(
                            blue_ball_move_x - pick_blue_ball[0]) + abs(blue_ball_move_y - pick_blue_ball[1]):
                        red_ball_move_x -= step_x[step]
                        red_ball_move_y -= step_y[step]
                    else:
                        blue_ball_move_x -= step_x[step]
                        blue_ball_move_y -= step_y[step]

                if [[red_ball_move_x, red_ball_move_y], [blue_ball_move_x, blue_ball_move_y]] not in visited:
                    need_visited.append([[red_ball_move_x, red_ball_move_y], [blue_ball_move_x, blue_ball_move_y]])
                    visited.append([[red_ball_move_x, red_ball_move_y], [blue_ball_move_x, blue_ball_move_y]])
        count += 1
    return -1


N, M = map(int, input().split())
maze = []
red_ball = []
blue_ball = []
for line in range(N):
    maze.append(list(input()))
    for column in range(M):
        if maze[line][column] == 'R':
            red_ball = [line, column]
        elif maze[line][column] == 'B':
            blue_ball = [line, column]

bfs(red_ball, blue_ball)

