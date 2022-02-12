from collections import deque

step_x = [-1, 1, 0, 0, 0, 0]
step_y = [0, 0, -1, 1, 0, 0]
step_z = [0, 0, 0, 0, -1, 1]


def bfs(box, already):
    while already:
        #         print(already)
        x, y, z = already.popleft()

        for step in range(6):
            move_x = x + step_x[step]
            move_y = y + step_y[step]
            move_z = z + step_z[step]
            if 0 <= move_x < H and 0 <= move_y < N and 0 <= move_z < M:
                if box[move_x][move_y][move_z] == 0:
                    already.append([move_x, move_y, move_z])
                    box[move_x][move_y][move_z] = box[x][y][z] + 1


M, N, H = map(int, input().split())
# 토마토 박스
box = []
# 초기에 1로 세팅되어있는것들의 위치를 알고 있어야 하지 않나 싶다
already = deque([])

for plane in range(H):
    floor = []
    for line in range(N):
        floor.append(list(map(int, input().split())))
        for tomato_idx in range(len(floor[line])):
            if floor[line][tomato_idx] == 1:
                already.append([plane, line, tomato_idx])
    box.append(floor)

bfs(box, already)

max_day = 0
flag = True
for plane in box:
    for line in plane:
        for tomato in line:
            if tomato == 0:
                flag = False
        max_day = max(max_day, max(line))
#         print(max_day)
if flag:
    print(max_day - 1)
else:
    print(-1)

